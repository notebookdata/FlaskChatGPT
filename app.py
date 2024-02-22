from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    if request.method == 'POST':
        query = request.form['query']
        response = generate_response(query)
        return render_template('index.html', query=query, response=response)

def generate_response(query):
    # Send the query to ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
