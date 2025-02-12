from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import markdown
import markdown.extensions.fenced_code  
import os 
app = Flask(__name__)

API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = model.generate_content(user_message)

        if response and hasattr(response, 'text'):
            markdown_text = response.text
            html_response = markdown.markdown(markdown_text, extensions=['fenced_code'])  # Convert Markdown to HTML
            return jsonify({'response': html_response})
        else:
            return jsonify({'error': 'Invalid response from AI'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
