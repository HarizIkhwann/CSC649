# 🚀 Deployment Guide - Render

This guide will help you deploy your Music Chatbot to Render.

## Prerequisites

- GitHub account
- Render account (sign up at [render.com](https://render.com))
- Google Gemini API key

## Step 1: Prepare Your Repository

1. **Initialize Git** (if not already done)
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Create a GitHub repository**
   - Go to [github.com](https://github.com) and create a new repository
   - Follow the instructions to push your code:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Deploy on Render

1. **Sign up/Login to Render**
   - Go to [render.com](https://render.com)
   - Sign up or log in (can use GitHub account)

2. **Create a New Web Service**
   - Click "New +" button
   - Select "Web Service"

3. **Connect Your Repository**
   - Connect your GitHub account if not already connected
   - Select your music chatbot repository

4. **Configure the Service**
   - **Name**: Choose a name (e.g., `music-chatbot`)
   - **Region**: Choose closest to your location
   - **Branch**: `main`
   - **Root Directory**: Leave blank
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

5. **Add Environment Variable**
   - Scroll down to "Environment Variables"
   - Click "Add Environment Variable"
   - **Key**: `GEMINI_API_KEY`
   - **Value**: Your Gemini API key
   - Click "Add"

6. **Select Plan**
   - Choose the **Free** plan
   - Click "Create Web Service"

## Step 3: Wait for Deployment

- Render will now build and deploy your app
- This usually takes 2-5 minutes
- You can watch the logs in real-time

## Step 4: Access Your App

Once deployed, you'll get a URL like:
```
https://your-app-name.onrender.com
```

Your app is now live! 🎉

## Important Notes

### Free Tier Limitations
- The free tier "spins down" after 15 minutes of inactivity
- First request after spin-down may take 30-60 seconds to wake up
- 750 hours/month of free usage

### Updating Your App
When you push changes to GitHub:
```bash
git add .
git commit -m "Your update message"
git push
```
Render will automatically redeploy your app.

### Environment Variables
- NEVER commit your `.env` file or API keys to GitHub
- Always add sensitive data through Render's Environment Variables panel

### Custom Domain (Optional)
- You can add a custom domain in Render's settings
- Free tier includes SSL certificate

## Troubleshooting

### App won't start?
- Check the logs in Render dashboard
- Verify environment variables are set correctly
- Ensure requirements.txt includes all dependencies

### Build failed?
- Check Python version compatibility
- Verify requirements.txt syntax

### API errors?
- Verify GEMINI_API_KEY is correctly set
- Check API key is valid in Google AI Studio

## Support

For Render-specific issues, visit:
- [Render Documentation](https://render.com/docs)
- [Render Community](https://community.render.com)
