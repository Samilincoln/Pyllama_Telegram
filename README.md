# Pyllama_Telegram
AI Telegram Bot utilizing the LLaMA 3-8B-8192 model
# PyLLaMa Bot

PyLLaMa Bot is a Telegram bot integrated with the Groq API, designed to provide a conversational AI assistant experience. Built with Flask and deployed on Vercel, this bot responds to user messages using Groq's `llama3-70b-8192` model.

## Features

- **Telegram Bot**: Interacts with users in real-time on Telegram.
- **Groq Integration**: Uses the `llama3-70b-8192` model to respond conversationally.
- **Flask API**: Runs a Flask app that handles the webhook for receiving and processing Telegram updates.
- **Vercel Deployment**: Easily deployable on Vercel for scalable, serverless hosting.

## Prerequisites

- Python 3.8+
- A [Groq API](https://groq.com) key
- A [Telegram Bot API](https://core.telegram.org/bots) key
- Vercel account for deployment

## Installation

1. Clone the repository:
   ```bash
   pip install -r requirements.txt

   ```
2. Install dependencies:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
3. Create a .env file in the root directory with your API keys:
   ```env
    TELEGRAM_API_KEY=your-telegram-bot-api-key
    GROQ_API_KEY=your-groq-api-key
    ```

4. Running the Bot Locally:
    To test the bot locally:
   ```bash
   python app.py
   or
   flask run
   ```
5. Setting the Webhook:
    To deploy the bot, ensure the webhook is correctly configured to your Vercel deployment URL. Set the webhook using::
   ```bash
   python app.py
   ```
   or or directly by making a request to:
   ```url
   https://api.telegram.org/bot<YOUR_TELEGRAM_API_KEY>/setWebhook?url=<YOUR_VERCEL_URL>/api/webhook
   ```
6. Deploying to Vercel:
    For deploying to Vercel, create a new Vercel project connected to this Git repository and push the code.