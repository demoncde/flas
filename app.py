from flask import Flask, make_response, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/a1')
def a1():
    print(request.headers)
    rp = make_response()
    rp.set_cookie('a1', '123')
    return rp


@app.route('/a2')
def a2():
    print(request.headers)
    rp = make_response()
    # rp.set_cookie('a2', '234')
    return rp


@app.route('/a3')
def a3():
    print(request.headers)
    rp = make_response()
    rp.set_cookie('a3', '345')
    return rp


@app.route('/index/')
def index():
    print(request.headers)
    return render_template('index.html')

@app.route('/search/')
def search():
    # arguments
    condition = request.args.get('q')
    return '用户提交的查询参数是: {}'.format(condition)

# 默认的试图函数， 只能采用get请求
# 如果你想采用post请求，那么要写明
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print(request.headers)
        return render_template('login.html')
    else:
        print(request.headers)
        username = request.form.get('username')
        password = request.form.get('password')
        print('username: {}, password: {}'.format(username, password))
        return 'name = {}, password = {}'.format(username, password)



if __name__ == '__main__':
    app.run()
