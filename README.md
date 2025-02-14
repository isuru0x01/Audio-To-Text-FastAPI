# 🎙️ Audio Transcription API

This project provides an API for transcribing audio files using Groq's API.

## 🚀 Getting Started

Follow these steps to set up and run the project:

### 📋 Prerequisites

- Python 3.8 or higher
- Conda package manager
- Groq API key
- Audio file for transcription (e.g., sample.mp3)
- Postman (for API testing)

### ⚙️ Environment Setup

1. Configure environment file:
   ```bash
   # Rename the example environment file
   mv .env.test .env
   ```

2. 🔑 Add your Groq API key:
   - Get your free API key from [Groq Console](https://console.groq.com/)
   - Open the `.env` file and add your API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

3. 🐍 Create and activate Conda environment:
   ```bash
   # Create new environment
   conda create -n transcription-api python=3.8

   # Activate environment
   conda activate transcription-api
   ```

4. 📦 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 🎯 Running the Application

5. Start the FastAPI server:
   ```bash
   python -m uvicorn main:app --reload
   ```

6. 🌐 Using the API:
   - Open your browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Look for the `/transcribe` endpoint
   - Upload your `sample.mp3` file to test the transcription

### 🧪 Testing with Postman

7. Configure Postman:
   - 📬 Create a new POST request to `http://localhost:8000/transcribe`
   - 📝 In the "Body" tab:
     - Select "form-data"
     - Add a key named `file`
     - Click the dropdown next to the key field and change type to "File"
     - Upload your audio file (supported formats: .mp3, .m4a)
   - 🚀 Click "Send" to submit the request
   - ✅ You should receive a JSON response containing the transcribed text

Example Response:
```json
{
    "transcription": "Your transcribed text will appear here..."
}
```

## 📝 API Documentation

The API documentation is automatically generated and can be accessed at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.