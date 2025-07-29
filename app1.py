from flask import Flask,render_template,request,url_for
app=Flask(__name__)

@app.route("/")
def home():
    return"welcome to home page"

@app.route('/login',methods=["GET","POST"])
def form1():
    if request.method=="GET":
        return render_template('ap.html')
    else:
        username=(request.form.get('username',0))
        password=(request.form.get('password',1))

        if username=='admin' and password=='1234':
            return "login succesfull"
        else:
            return "please try again"









if (__name__=="__main__"):
    app.run(debug=True)


