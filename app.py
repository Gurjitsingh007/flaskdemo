from flask import Flask,render_template,request,redirect,url_for 

app=Flask(__name__)

# app routing or flask routing basically "use to create url routes and pages "
@app.route("/",methods=["GET"])
def welcome():
    button_text="click me"
    print(button_text)
    return "<h1> welcome to home page </h1>"

    

@app.route("/index",methods=["GET"])
def index():
    return "<h2>this is index page </h2>"

#variable rule   m 

@app.route('/success/<int:score>')
def success(score):
    return "the person is passes and score is : "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person is failed and score is : "+ str(score)

@app.route('/form', methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths=float(request.form.get('maths',0))
        science=float(request.form.get('science',0))
        history=float(request.form.get('history',0))

        average_marks=(maths+science+history)/3
        res=""
        if average_marks>=50:
            res="success"
        else:
            res="fail"
        return redirect(url_for(res,score=average_marks)) #this will redirect to the success or fail page based on the average marks



        # return render_template('form.html',score=average_marks)



# redirect:# redirect is used to redirect the user to another page or url
# url_for: # url_for is used to generate the url for the given function name 
# render_template: # render_template is used to render the html template file and return it as a response
# run the app
# debug=True: # debug is used to enable the debug mode which will automatically reload the app
# and show the error messages in the browser
#THIS IS FLASK...










if (__name__=="__main__"):
    app.run(debug=True)


