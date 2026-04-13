from flask import Flask, render_template

app = Flask(__name__)

books = [
    {
        "title": "Python Basics",
        "author": "John Doe",
        "image": "book1.jpg"
    },
    {
        "title": "Web Development",
        "author": "Jane Smith",
        "image": "book2.jpg"
    },
    {
        "title": "AI Guide",
        "author": "Ali Khan",
        "image": "book3.jpg"
    }
]

@app.route('/')
def home():
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)