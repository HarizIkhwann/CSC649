# 🎵 Melody - The AI Music Expert

A music chatbot powered by Google's Gemini AI that provides music recommendations, discusses genres, artists, and albums through an intuitive GUI interface.

## Features

- 🎼 AI-powered music recommendations
- 🎤 Discuss artists, genres, and albums
- 💬 Interactive chat interface
- 🎨 User-friendly GUI built with Tkinter
- ⚡ Real-time responses using Gemini 2.5 Flash

## Prerequisites

- Python 3.12 or higher
- Google AI Studio API Key

## Installation

1. **Clone or download this project**

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   ```bash
   .venv\Scripts\Activate
   ```

4. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Get your API Key from Google AI Studio**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy your API key

2. **Create a `.env` file** in the project root directory

3. **Add your API key to the `.env` file**
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the application:
```bash
python musicBot.py
```

Once the GUI opens:
1. Type your music-related question or request in the input field
2. Press Enter or click the "Send 🎵" button
3. Melody will respond with music recommendations and information

## Example Queries

- "Recommend some jazz artists"
- "What are the best albums of 2023?"
- "Tell me about classical music"
- "Suggest a playlist for studying"

## Project Structure

```
CSC649/
├── musicBot.py          # Main application file
├── requirements.txt     # Python dependencies
├── .env                 # API key configuration (create this)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Notes

- The bot only discusses music-related topics
- Responses are kept concise and helpful
- The chat history is maintained during the session

## License

This project is for educational purposes.
