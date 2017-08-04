import getNyt
from flask import Flask, url_for, redirect, render_template, request
import getpass
import lxml
import requests
from bs4 import BeautifulSoup
import datetime as dt
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

@app.route('/thehindu')
def thehindu():
    # if request.method == 'POST':
    #    return redirect(url_for("nyt"))
    nyEdt = getNyt.thehindu()
    return render_template("thehindu.html", editorialHeader1=', '.join((nyEdt[0],dt.date.today().strftime("%m/%d/%Y"))), editorialContent1='\n\n'.join(nyEdt[1]),
        editorialHeader2=', '.join((nyEdt[2],dt.date.today().strftime("%m/%d/%Y"))), editorialContent2='\n\n'.join(nyEdt[3]))


@app.route('/nyt')
def nyt():
    nyEdt = getNyt.nyt()
    return render_template("nyt.html", editorialHeader=', '.join((nyEdt[0],dt.date.today().strftime("%m/%d/%Y"))), editorialContent='\n\n'.join(nyEdt[1]))

@app.route('/editorials')
def edit():
    nyEdt = getNyt.nyt()
    return render_template("editorial.html", editorialHeader=', '.join((nyEdt[0],dt.date.today().strftime("%m/%d/%Y"))), editorialContent='\n\n'.join(nyEdt[1]))

if __name__ == "__main__":
    app.run(debug = True)
