from flask import Flask, render_template, url_for

app = Flask(__name__)


class Projects:
    def __init__(self, name, description, image, link):
        self.name = name
        self.description = description
        self.image = image
        self.link = link


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/Documentation")
def documentation():
    return render_template('documentation.html')


if __name__ == '__main__':
    app.run(debug=True)
