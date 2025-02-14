import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=groq_api_key)

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": (
            "Welcome to the Audio Transcription API powered by FastAPI! "
            "This service enables users to upload audio files and receive accurate "
            "text transcriptions using advanced machine learning models. "
            "Explore the interactive documentation at /docs to learn more about available endpoints "
            "and how to integrate audio-to-text conversion into your applications."
        )
    }


@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Ensure the file has a supported audio extension (optional validation)
    if not file.filename.lower().endswith((".m4a", ".wav", ".mp3")):
        raise HTTPException(status_code=400, detail="Unsupported file type.")

    # Save the uploaded file temporarily
    temp_filename = f"temp_{file.filename}"
    with open(temp_filename, "wb") as temp_file:
        content = await file.read()
        temp_file.write(content)

    try:
        with open(temp_filename, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=(temp_filename, audio_file.read()),
                model="whisper-large-v3",
                response_format="verbose_json",
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transcription failed: {str(e)}")
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

    return {"transcription": transcription.text}
