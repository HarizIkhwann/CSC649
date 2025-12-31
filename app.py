import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
from datetime import timedelta
import secrets

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

# Configure Gemini
genai.configure(api_key=API_KEY)

system_prompt = """You are an expert Music Chatbot. Your purpose is to:
1. Recommend music based on user preferences.
2. Discuss music genres, artists, and albums.
3. Only talk about music-related topics.
4. Keep responses short and helpful.
5. When recommending songs, artists, or playlists, provide YouTube and/or Spotify links.
6. Format links clearly: include the song/artist name followed by the platform links.
7. Use search URLs like:
   - YouTube: https://www.youtube.com/results?search_query=[artist+song]
   - Spotify: https://open.spotify.com/search/[artist song]
8. For specific recommendations, try to provide both YouTube and Spotify links when possible.
9. You may also recommend any public playlist available that suits the user's preferences."""

# Store chat sessions per user
chat_sessions = {}

def get_chat_session():
    """Get or create a chat session for the current user
    """
    if 'session_id' not in session:
        session['session_id'] = secrets.token_hex(16)
        session.permanent = True
    
    session_id = session['session_id']
    
    if session_id not in chat_sessions:
        model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            system_instruction=system_prompt
        )
        chat_sessions[session_id] = model.start_chat(history=[])
    
    return chat_sessions[session_id]

@app.route('/')
def index():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get the chat session for this user
        chat_session = get_chat_session()
        
        # Send message to Gemini
        response = chat_session.send_message(user_message)
        
        return jsonify({
            'success': True,
            'response': response.text
        })
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'success': False,
            'error': 'Could not connect to the music studio. Try again.'
        }), 500

@app.route('/clear', methods=['POST'])
def clear_chat():
    """Clear the chat history"""
    try:
        if 'session_id' in session:
            session_id = session['session_id']
            if session_id in chat_sessions:
                del chat_sessions[session_id]
        
        return jsonify({'success': True})
    except Exception as e:
        print(f"Error clearing chat: {e}")
        return jsonify({'success': False}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
