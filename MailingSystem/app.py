from flask import Flask, render_template, request, redirect, url_for
import smtplib
import os
from email.message import EmailMessage


app = Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/sending', methods=['POST'])
def sending():
    if request.method == 'POST':
        sending.username = request.form['email']
        sending.password = request.form['password']
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        if mail.login(sending.username,sending.password)==(235, b'2.7.0 Accepted'):
            return redirect(url_for('mailing'))
        else:
            sending.message="Cannot Log In "
            return render_template('index.html',message=sending.message)
    else:
        return "Something went wrong"
        
# Content Page
@app.route('/mail',methods=['GET'])
def mailing():
    mailing.username=sending.username
    mailing.password=sending.password
    return render_template('sendmail.html',From_value=mailing.username)

   ### To send information 
@app.route('/content',methods=['POST'])
def content_sending() :
    if request.method=='POST':
        to=request.form['to']
        subjects=request.form['subject']
        message_box=request.form['message']
        username_from=mailing.username
        msg=EmailMessage()
        msg['Subject']=subjects
        msg['From']=username_from
        msg['To']=to
        msg.set_content(message_box)
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(mailing.username,mailing.password)
        mail.send_message(msg)
        return render_template('sendmail.html')
    else:
        return "Something Went Wrong"


if __name__ == "__main__":
    app.run(debug=True)
