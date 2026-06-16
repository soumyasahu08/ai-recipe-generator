from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Replace with your actual API key or use an environment variable
openai.api_key = "your_api_key_here"

@app.route('/', methods=['GET', 'POST'])
def index():
    recipe = ""
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        prompt = f"Create a recipe using these ingredients: {ingredients}"
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            recipe = response.choices[0].text.strip()
        except Exception as e:
            recipe = f"Error: {str(e)}"
    return render_template('index.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)
