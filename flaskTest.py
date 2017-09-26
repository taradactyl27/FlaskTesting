from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return Hello!

@my_app.route('/one')
def one():
    return Hello World!!

@my_app.route('/two')
def two():
    return Hi Everybody!

if __name__ == '__main__':
        my_app.debug = True
        my_app.run()
