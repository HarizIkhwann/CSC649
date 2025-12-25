import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import scrolledtext, messagebox
import google.generativeai as genai
import threading

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

class MusicBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Melody - The AI Music Expert")
        self.root.geometry("500x600")
        
        genai.configure(api_key=API_KEY)

        self.system_prompt = """You are an expert Music Chatbot. Your purpose is to:
        1. Recommend music based on user preferences.
        2. Discuss music genres, artists, and albums.
        3. Only talk about music-related topics.
        4. Keep responses short and helpful."""

        self.model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            system_instruction=self.system_prompt
        )

        self.chat_session = self.model.start_chat(history=[])

        #GUI
        self.chat_display = scrolledtext.ScrolledText(root, state='disabled', wrap='word', font=("Arial", 10))
        self.chat_display.pack(padx=10, pady=10, fill='both', expand=True)
        self.chat_display.tag_config('user', foreground='blue')
        self.chat_display.tag_config('bot', foreground='green')
        self.chat_display.tag_config('error', foreground='red')

        input_frame = tk.Frame(root)
        input_frame.pack(padx=10, pady=5, fill='x')

        self.user_input = tk.Entry(input_frame, font=("Arial", 12))
        self.user_input.pack(side='left', fill='x', expand=True, padx=(0, 5))
        self.user_input.bind("<Return>", self.send_message)

        self.send_btn = tk.Button(input_frame, text="Send 🎵", command=self.send_message, bg="#ddd")
        self.send_btn.pack(side='right')

        self.append_to_chat("Bot: Yo! I'm Melody. Ask me for a playlist or artist facts!", 'bot')

    def append_to_chat(self, message, tag):
        """Helper to add text to the scrolling window"""
        self.chat_display.configure(state='normal') # Unlock to write
        self.chat_display.insert(tk.END, message + "\n\n", tag)
        self.chat_display.configure(state='disabled') # Lock again
        self.chat_display.see(tk.END) # Auto-scroll to bottom

    def send_message(self, event=None):
        """Handles sending the message"""
        user_text = self.user_input.get()
        
        if not user_text.strip():
            return

        # Clear input field
        self.user_input.delete(0, tk.END)
        
        # Show user message
        self.append_to_chat(f"You: {user_text}", 'user')

        # Run API call in a separate thread to keep GUI responsive
        threading.Thread(target=self.get_bot_response, args=(user_text,)).start()

    def get_bot_response(self, user_text):
        """Fetches response from Gemini"""
        try:
            # Send message to Gemini 
            response = self.chat_session.send_message(user_text)
            
            # Update GUI with response
            self.root.after(0, self.append_to_chat, f"Melody: {response.text}", 'bot')
            
        except Exception as e:
            # Error Handling 
            error_msg = "Error: Could not connect to the music studio. Try again."
            self.root.after(0, self.append_to_chat, error_msg, 'error')
            print(f"Technical Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicBotApp(root)
    root.mainloop()