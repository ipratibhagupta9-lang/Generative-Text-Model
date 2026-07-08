# Generative Text Model using Groq API

## About the Project

This project was developed as part of my **CODTECH Internship Task-4**. It is a desktop application built using **Python**, **Tkinter**, and the **Groq API** that generates high-quality text based on user prompts.

The goal of this project is to provide a simple and interactive interface where users can enter any topic and instantly receive well-structured AI-generated content. The application is easy to use and includes several useful features to improve the overall experience.

## Features

- Generate AI-powered text from user prompts
- Clean and easy-to-use Tkinter interface
- Light and Dark mode
- Adjustable temperature and token settings
- Save generated text as a `.txt` file
- Copy generated text to the clipboard
- Clear input and output with one click
- Word and character counter
- Progress bar during text generation
- Responsive interface using multithreading

## Technologies Used

- Python
- Tkinter
- Groq API
- Threading
- python-dotenv

## Installation

Clone this repository:

```bash
git clone https://github.com/your-username/Generative-Text-Model-using-Groq-API.git
```

Move to the project folder:

```bash
cd Generative-Text-Model-using-Groq-API
```

Install the required packages:


## API Setup

Create a `.env` file in the project folder and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

## Run the Project

```bash
python Generative_text_model.py
```

## Sample Prompt

```
Write a detailed article about Artificial Intelligence in Healthcare.
```

## Future Improvements

- Support for multiple AI models
- Export generated text as PDF or DOCX
- Chat history
- Voice input support
- Streaming responses
- Better UI design
