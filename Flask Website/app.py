from flask import Flask, render_template

posts = [{
    'author': 'Hammad',
    'title': 'My first Blog',
    'contenet': 'My first content',
    'date': 'September 17, 2024'
},
    {
    'author': 'Arham',
    'title': 'Blog post',
    'content': 'My tech content',
    'date': 'September 18, 2024'

}



]

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


'''
@app.route('/')
def home():
    return render_template('home.html')

'''


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
