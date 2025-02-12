# Flask GenAI Chatbot
# Anirban Sarkar : Instagram -> bong_ani_007
This guide will help you set up a Flask project with a virtual environment, install dependencies, generate a Gemini API key, and run your GenAI chatbot.

---

## 1. Setup Virtual Environment

### Create a Virtual Environment
Run the following command to create a virtual environment named `env`:
```bash
python -m venv env
```

### Activate the Virtual Environment
- **Windows**:
  ```bash
  env\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source env/bin/activate
  ```

Once activated, you should see `(env)` in your terminal prompt.

---

## 2. Install Dependencies
After activating the virtual environment, install the required packages using:
```bash
pip install -r requirements.txt
```
This will install Flask, Google Generative AI SDK, Markdown, and dotenv.

---

## 3. Generate a Gemini API Key

To use Google's Gemini AI model, follow these steps to get an API key:
1. Go to the [Google AI Studio](https://aistudio.google.com/) website.
2. Sign in with your Google account.
3. Navigate to the API key section.
4. Generate a new API key and copy it.
5. Create a `.env` file in your project root and add:
   ```ini
   API_KEY=your_generated_api_key_here
   ```

---

## 4. Run the Flask Project

Once everything is set up, start your Flask app by running:
```bash
python app.py
```
By default, it will run on `http://127.0.0.1:5000/`.

---

## 5. Deactivate the Virtual Environment
When you're done, deactivate the virtual environment by running:
```bash
deactivate
```

Enjoy building your GenAI chatbot with Flask! 🚀

