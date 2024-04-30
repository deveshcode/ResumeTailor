import React, { useState } from 'react';
import { TextField, Button, Box, LinearProgress, Typography, Container, Paper } from '@mui/material';

function App() {
  const [resume, setResume] = useState('');
  const [jobDescription, setJobDescription] = useState('');
  const [workExperience, setWorkExperience] = useState('');
  const [skills, setSkills] = useState('');
  const [projects, setProjects] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async () => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ resume, jobDescription }),
      });
      const data = await response.json();
      setWorkExperience(data.workExperience);
      setSkills(data.skills);
      setProjects(data.projects);
    } catch (error) {
      console.error('Failed to fetch:', error);
    }
    setIsLoading(false);
  };

  const handleMatchSkills = async () => {
    // This should call an endpoint or logic to match skills with the job description
    console.log('Matching skills...');
    // Simulate an updated skills list
    setSkills('Updated Skills based on job description.');
  };

  const handleMatchWorkExperience = async () => {
    // This should call an endpoint or logic to match work experience with the job description
    console.log('Matching work experience...');
    setWorkExperience('Updated Work Experience based on job description.');
  };

  const handleMatchProjects = async () => {
    // This should call an endpoint or logic to rank projects
    console.log('Matching projects...');
    setProjects('Top 3 Projects: Project A (Score: 95), Project B (Score: 90), Project C (Score: 85). Explanation: These projects are most relevant based on your skills and job description.');
  };

  return (
    <Container component="main" maxWidth="md">
      <Paper elevation={3} style={{ padding: '20px', marginTop: '20px' }}>
        <Typography variant="h4" component="h1" gutterBottom>Resume Tailor</Typography>
        {isLoading && <LinearProgress />}
        <Box sx={{ margin: '20px 0' }}>
          <TextField
            label="Paste your resume here"
            multiline
            fullWidth
            rows={6}
            variant="outlined"
            value={resume}
            onChange={(e) => setResume(e.target.value)}
          />
          <TextField
            label="Paste job description here"
            multiline
            fullWidth
            rows={6}
            variant="outlined"
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            style={{ marginTop: '20px' }}
          />
          <Button onClick={handleSubmit} disabled={isLoading} style={{ marginTop: '20px' }}>Submit</Button>
        </Box>
        <Box sx={{ marginTop: '20px' }}>
          <Typography variant="h6">Work Experience</Typography>
          <TextField
            multiline
            fullWidth
            variant="outlined"
            value={workExperience}
            onChange={(e) => setWorkExperience(e.target.value)}
          />
          <Button onClick={handleMatchWorkExperience} style={{ marginTop: '10px' }}>Match Work Experience</Button>

          <Typography variant="h6" style={{ marginTop: '20px' }}>Skills</Typography>
          <TextField
            multiline
            fullWidth
            variant="outlined"
            value={skills}
            onChange={(e) => setSkills(e.target.value)}
          />
          <Button onClick={handleMatchSkills} style={{ marginTop: '10px' }}>Match Skills</Button>

          <Typography variant="h6" style={{ marginTop: '20px' }}>Projects</Typography>
          <TextField
            multiline
            fullWidth
            variant="outlined"
            value={projects}
            onChange={(e) => setProjects(e.target.value)}
          />
          <Button onClick={handleMatchProjects} style={{ marginTop: '10px' }}>Match Projects</Button>
        </Box>
      </Paper>
    </Container>
  );
}

export default App;
