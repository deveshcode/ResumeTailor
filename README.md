# ResumeTailor

## Project Overview
ResumeTailor is a web application designed to dynamically tailor your resume based on a specific job description. It uses advanced natural language processing (NLP) techniques to analyze your resume and the job description, identify the most relevant experiences and projects, and even suggest new projects if necessary.

## Features
- **Resume Analysis:** Automatically segments your resume into different sections such as Work Experience, Projects, and Skills.
- **Job Description Matching:** Analyzes job descriptions to identify key skills and requirements and matches them with your resume.
- **Dynamic Project Suggestions:** Generates project ideas when existing entries do not align well with job descriptions.
- **User-Friendly Interface:** Provides a simple and intuitive web interface for users to input their resume and job description.
- **Modular Design:** Allows for easy updates and changes to the NLP model and analysis algorithms.

## Technologies Used
- **Frontend:** ReactJS
- **Backend:** FastAPI
- **NLP Library:** OpenAI's GPT-3.5
- **Database:** MongoDB (for storing user data and processing results)

## Getting Started
### Prerequisites
- Node.js
- Python 3.x
- MongoDB

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ResumeTailor.git
    ```
   
2. Install the necessary frontend dependencies:
```bash
cd ResumeTailor/frontend
npm install
```

3. Install the necessary backend dependencies:
```bash
```

4. Start the development servers:
```bash
# In the frontend directory
npm start

# In the backend directory
uvicorn main:app --reload
```

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
Devesh Surve - deveshssurve@gmail.com
