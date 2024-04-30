from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import openai
from openai import OpenAI
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
    OPENAI_API_KEY=""
    
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

    try:
        client = OpenAI(
            api_key= OPENAI_API_KEY,) 
        chat_completion = client.chat.completions.create(
        messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
        response=chat_completion.choices[0].message.content
        print(response)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")
@app.post("/analyze")
async def analyze_resume(data: ResumeData):

    work_experience_prompt = f"Extract experience from this resume from Experience section: {data.jobDescription}\n\n{data.resume}"
    skills_prompt = f"List technical skills from this resume : {data.jobDescription}\n\n{data.resume}"
    projects_prompt = f"Identify Academic Projects section from the resume and extract projects listed there: {data.jobDescription}\n\n{data.resume}"

    work_experience = await call_gpt(work_experience_prompt)
    skills = await call_gpt(skills_prompt)
    projects = await call_gpt(projects_prompt)
  
    return {
        "workExperience": work_experience,
        "skills": skills,
        "projects": projects
    }
