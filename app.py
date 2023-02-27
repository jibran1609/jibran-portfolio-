from logging import exception
from flask import Flask,render_template,url_for,request,redirect,session,send_file
import smtplib

app = Flask(__name__)
app.secret_key = 'many random bytes'
# Python Flask app with two routes rendering index.html template.


@app.route("/")
@app.route('/home',methods = ['POST','GET'])
def home():
    return render_template('index.html')

@app.route("/projects",methods = ["post","get"])
def project():
    return render_template("project.html")


@app.route("/download",methods = ["post","get"])
def download():
    path = "documents\jibran_resume.pdf"
    return send_file(path, as_attachment=True)


@app.route("/contact",methods = ["post","get"])
def contact():
    try:
        name = request.form['name']
        mail_to = request.form['email']
        
        phone = request.form['phone']
        message = request.form['message']
        mail_from = 'jibran1455@gmail.com'
        
        mail_subject = 'Hello '+ name
        
        mail_message_body = f'''
        Hi {name}, 
        Thanks so much for reaching out! This auto-reply is just to let you know… 
        We received your email and will get back to you with a (human) response as soon as possible.'''


        # print(name ,mail_to,phone,message)
        mail_message = f'''
        From: {mail_from}
        To: {mail_to}
        Subject: {mail_subject}

        {mail_message_body}'''
        server = smtplib.SMTP('localhost')
        try:
            server.sendmail(mail_from, mail_to, mail_subject, mail_message)
            server.quit()
        except Exception as e:
            pass
        return render_template("index.html")
    
    except:
        return render_template("404.html")
@app.route("/car",methods = ["post","get"])
def car():
    return render_template("car.html")
    
    
if __name__ == '__main__':
    app.run(debug=True)
    