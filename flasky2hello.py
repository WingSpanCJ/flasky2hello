from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test/<int:num>')
def numReceive(num:int):
    import datetime
    time = datetime.datetime.now()
    return "{}: Number is {}.".format(time.strftime("%Y-%m-%d %H:%M:%S"), num)

if __name__ == '__main__':
    app.run()
