from flask import Flask, render_template, url_for

app = Flask(__name__)

class Projects:
    def __init__(self,name,description,image,link):
        self.name = name
        self.description = description
        self.image = image
        self.link = link
        
listofprojects = [Projects("Attention Evaluation System", "AI Attention Evaluation System using Tensorflow and Keras", "img/about-bg.jpg", 'about'),
                  Projects("ChartIT Statistics Software", "JavaScript", "img/post-sample-image.jpg", 'about'),
                  Projects("Web Services with Docker", "Implemented a project using a mix of web technologies such as Docker, K8, MongoDB, MySQL and RabbitMQ. ","img/home-bg.jpg", 'webproject'),
                  Projects("Symfony Backend Project", "Used Symfony PHP Framework to create a full ecommerce page, Twig Template for front end and other interesting features","img/home-bg.jpg", 'about')]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/projects")
def projects():
    print(projects)
    return render_template('projects.html', title='my_projects', project=listofprojects)

@app.route("/webproject")
def webproject():
    return render_template('web.html')

# @app.route("/about")
# def about():
#     return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)