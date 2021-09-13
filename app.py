from werkzeug.exceptions import NotFound, Forbidden, Unauthorized
from pyrebase import initialize_app
from flask import *

###############################################################################################

app = Flask(__name__)

config = {
    "apiKey":"AIzaSyAY3VyJDM6PBMFRwWx4frQHqO_mfJb61G8",
    "authDomain":"epictools-4ac97.firebaseapp.com",
    "projectId":"epictools-4ac97",
    "storageBucket":"epictools-4ac97.appspot.com",
    "messagingSenderId":"524489150559",
    "appId":"1:524489150559:web:580bc45f3bfc407e6ccbea",
    "measurementId":"G-L4RQ73R6TJ",
    "databaseURL":"https://epictools-4ac97.firebaseio.com"
}

firebase = initialize_app(config)

auth = firebase.auth()

US = "Please check your credentials."
S = "Login successful"

###############################################################################################
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title="Login | Epictools")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template("login.html", s=S, title="Login | Epictools")
        except:
            return render_template('login.html', us=US, title="Login | Epictools")
    return render_template('login.html', title="Login | Epictools")
    
@app.route('/tools', methods=['GET', 'POST'])
def tools():
    return render_template('tools.html', title="Tools | Epictools")

@app.route('/workshop', methods=['GET', 'POST'])
def workshop():
    return render_template('workshop.html', title="Workshop | Epictools")

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html', title="Register")

@app.errorhandler(NotFound)
def notfound(e):
    return render_template('notfound.html'), 404

###############################################################################################


#email = input('Enter your email: ')
#password = input('Enter your password: ')

#user = auth.create_user_with_email_and_password(email, password)
#user = auth.sign_in_with_email_and_password(email, password)
#auth.send_email_verification(user['idToken'])
#auth.send_password_reset_email(email)
#print(auth.get_account_info(user['idToken']))


###############################################################################################
if __name__ == '__main__':
    app.run(debug=True)