#要激活虚拟目录才能够正常运行。
#如果使用pycharm运行此文件，需要选择正确的“Project Interpreter”


from flask import Flask, render_template


from flask_bootstrap import Bootstrap
#bootstrap提供用户界面组件用于创建整洁美观的网页

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.errorhandler(404)
#定义404错误页面
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
#定义500错误页面
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
#定义网站主页
def index():
    return render_template('index.html')


@app.route('/user/<name>')
#定义localhost/user/name页面
def user(name):
    return render_template('user.html', name=name)

#启动flask服务	
if __name__=='__main__':
    app.run()