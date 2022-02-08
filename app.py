#Configuración de correo con GMAIL
from flask import Flask, render_template,request
from flask_mail import Mail,Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="miguel.leon4@gmail.com"
app.config['MAIL_PASSWORD']="Carpediem10!"
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/send_message',methods=['GET','POST'])
def send_message():
    if request.method=="POST":
        email=request.form['email']
        subject = request.form['subject']
        msg=request.form['message']
        
        message = Message(subject,sender="miguel.leon4@gmail.com",recipients=[email])
        
        message.body = msg

        mail.send(message)
        success = "message sent"
        return render_template("result.html",success=success)

if __name__ == "__main__":
    app.run(host="172.24.41.200", port=5001,debug=True)

