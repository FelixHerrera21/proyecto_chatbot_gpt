from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola mundo, proyecto chatbot!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/FelixHerrera21/proyecto_chatbot_gpt.git
git push -u origin main