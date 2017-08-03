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

@app.route('/nyt')
def nyt():
    nysc = requests.get('https://www.nytimes.com/pages/opinion/index.html')
    nysp = BeautifulSoup(nysc.content, 'lxml')
    lk = nysp.select('#spanABCRegion > div.spanAB.wrap.module > div.cColumn > div > div > div > div > div > h3 > a')
    lk2 = lk[0]['href']
    editHead = lk[0].text
    nysc1 = requests.get(lk2)
    nysp1 = BeautifulSoup(nysc1.content, 'lxml')
    editCnt = nysp1.find_all('p', class_="story-body-text story-content")
    ecBin = []
    for ec in editCnt:
        ecBin.append(ec.text)
    return render_template("nyt.html", editorialHeader=', '.join((editHead,dt.date.today().strftime("%m/%d/%Y"))), editorialContent='\n\n'.join(ecBin))

if __name__ == "__main__":
    app.run(debug = True)
