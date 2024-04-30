from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import openai

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Specifies the origins that are allowed to make requests.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods.
    allow_headers=["*"],  # Allows all headers.
)

class ResumeData(BaseModel):
    resume: str
    jobDescription: str

async def call_gpt(prompt: str) -> str:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a coding and system design expert."},
                {"role": "user", "content": prompt}
            ]
        )
        formatted_response = response['choices'][0]['message']['content'].strip()
        return formatted_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")

@app.post("/analyze")
async def analyze_resume(data: ResumeData):
    work_experience_prompt = f"Extract work experience relevant to the job description: {data.jobDescription}\n\n{data.resume}"
    skills_prompt = f"List technical skills that match the job description: {data.jobDescription}\n\n{data.resume}"
    projects_prompt = f"Identify projects in the resume that align with the job description: {data.jobDescription}\n\n{data.resume}"

    work_experience = await call_gpt(work_experience_prompt)
    skills = await call_gpt(skills_prompt)
    projects = await call_gpt(projects_prompt)

    return {
        "workExperience": work_experience,
        "skills": skills,
        "projects": projects
    }
