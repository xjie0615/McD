from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    data = {
        'name': 'zinin',
        'age': 20,
        'city': 'New York'
        'Zinin say' :'I am a gay'
    }


    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()



    
