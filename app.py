from flask import Flask,render_template,request

app=Flask(__name__)

# app routing or flask routing basically "use to create url routes and pages "
@app.route("/",methods=["GET"])
def welcome():
    return "<h1> welcome to home page </h1>"
    

@app.route("/index",methods=["GET"])
def index():
    return "<h2>this is index page </h2>"

#variable rule 

@app.route('/success/<int:score>')
def success(score):
    return "the person is passes and score is : "+ str(score) +"b "

@app.route('/form', methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths=float(request.form.get('maths',0))
        science=float(request.form.get('science',0))
        history=float(request.form.get('history',0))

        average_marks=(maths+science+history)/3
        return render_template('form.html',score=average_marks)











if (__name__=="__main__"):
    app.run(debug=True)


