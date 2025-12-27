// DOM Elements
const chatContainer = document.getElementById('chatContainer');
const chatForm = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const clearBtn = document.getElementById('clearBtn');
const typingIndicator = document.getElementById('typingIndicator');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    userInput.focus();
});

// Handle form submission
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const message = userInput.value.trim();
    if (!message) return;
    
    // Add user message to chat
    addMessage(message, 'user');
    
    // Clear input
    userInput.value = '';
    
    // Disable send button and show typing indicator
    setLoading(true);
    
    try {
        // Send message to server
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Add bot response to chat
            addMessage(data.response, 'bot');
        } else {
            // Show error message
            addMessage(data.error || 'An error occurred. Please try again.', 'error');
        }
        
    } catch (error) {
        console.error('Error:', error);
        addMessage('Could not connect to the music studio. Please check your connection.', 'error');
    } finally {
        setLoading(false);
        userInput.focus();
    }
});

// Handle clear chat button
clearBtn.addEventListener('click', async () => {
    if (!confirm('Are you sure you want to clear the chat history?')) {
        return;
    }
    
    try {
        const response = await fetch('/clear', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        
        if (response.ok) {
            // Clear chat display
            chatContainer.innerHTML = '';
            
            // Add welcome message
            addMessage("Yo! I'm Melody. Ask me for a playlist or artist facts! 🎶", 'bot');
        }
    } catch (error) {
        console.error('Error clearing chat:', error);
        alert('Failed to clear chat. Please try again.');
    }
});

// Add message to chat display
function addMessage(text, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}-message`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    // Format the message with appropriate prefix
    let prefix = '';
    let content = '';
    
    if (type === 'user') {
        prefix = '<strong>You:</strong> ';
        content = escapeHtml(text);
    } else if (type === 'bot') {
        prefix = '<strong>Melody:</strong> ';
        // Parse markdown for bot messages
        content = marked.parse(text, { breaks: true });
    } else if (type === 'error') {
        prefix = '<strong>Error:</strong> ';
        content = escapeHtml(text);
    }
    
    contentDiv.innerHTML = prefix + content;
    messageDiv.appendChild(contentDiv);
    chatContainer.appendChild(messageDiv);
    
    // Scroll to bottom
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Set loading state
function setLoading(isLoading) {
    sendBtn.disabled = isLoading;
    userInput.disabled = isLoading;
    
    if (isLoading) {
        typingIndicator.style.display = 'flex';
        sendBtn.textContent = 'Sending...';
    } else {
        typingIndicator.style.display = 'none';
        sendBtn.textContent = 'Send 🎵';
    }
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Auto-resize input on mobile
userInput.addEventListener('input', () => {
    userInput.style.height = 'auto';
    userInput.style.height = userInput.scrollHeight + 'px';
});
