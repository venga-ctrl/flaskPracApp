from flask import Flask, url_for, redirect, render_template, request
import getpass
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World!"

@app.route('/welcome/<user>')
def welcomeUser(user):
#	return render_template("welcome.html")   
	return render_template("welcome.html", thisUser=user)   
#	return render_template("welcome.html", thisUser=getpass.getuser())   
	#return redirect(url_for("hello"))
    
@app.route('/welcome')
def welcome():
#	return render_template("welcome.html")   
#	return render_template("welcome.html", thisUser=user)   
	return render_template("welcome.html", thisUser=getpass.getuser())   
	#return redirect(url_for("hello"))

@app.route('/e2e', methods = ['GET', 'POST'])
def e2e():
    if request.method == 'POST':
#        return "The name of this test is " , request.form['testName'] , " The EDM running is"
        return "The name of this test is %s" % request.form['testName']
    return render_template("e2eUserInputs.html")

    
if __name__ == "__main__":
    app.run(debug = True)
