from urllib.parse import quote as urlquote
from mathematics import add,sub,mul
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def render_html():
    return render_template("index.html")
@app.route('/add',methods=["POST"])
def sum_route():
    number1=float(request.form['num1'])
    number2=float(request.form['num2'])
    res=add(number1,number2)
    return render_template("index.html",result=res)
@app.route('/sub',methods=["POST"])
def diff_route():
    number1=float(request.form['num1'])
    number2=float(request.form['num2'])
    res=sub(number1,number2)
    return render_template("index.html",result=res)
@app.route('/mul',methods=["POST"])
def mul_route():
    number1=float(request.form['num1'])
    number2=float(request.form['num2'])
    res=mul(number1,number2)
    return render_template("index.html",result=res)
    
if __name__=="__main__":
    app.run(debug=True,port=5001)