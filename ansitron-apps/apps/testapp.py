#! usr/bin/python3
import subprocess, os, flask
from ansitron.loader import dotatronenv
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

os.environ['MY_PROJECT_ROOT'] = os.path.dirname(os.path.abspath(__file__))

@app.route('/about')
def about():
    return render_template('layout.html')

# @app.route('/about/<string:vary>/')
# def about(vary):
#     return '<h3>{}</h3>'.format(vary)

#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    def inner():
        os.chdir(os.environ['MY_PROJECT_ROOT'])
        subprocess.run(['python','-m','ansitron']) 
    return flask.Response(inner(), mimetype='text/html')

@app.route('/yieldresults')
def yieldresults():
    def inner():
        os.chdir(os.environ['MY_PROJECT_ROOT'])
        proc = subprocess.Popen(
            'python -m ansitron',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        while proc.poll() is None:
            #redirect(url_for('yieldresults'))
            yield proc.stdout.readline() + b'<br/>\n'
        
    return flask.Response(inner(), mimetype='text/html')


@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    # if dotatronenv.load_dotatronenv(dotatronenv.find_dotatronenv()):
    #     return "good"
    users = ['Bob', 'Jane', 'Adam']
    return '<h2>Hi {}</h2>'.format(users[user_id])

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=False)
