from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail

mail = Mail()

app = Flask(__name__)

app.secret_key = ''

app.config['MAIL_SERVER'] = ''
app.config['MAIL_PORT'] = 
app.config['MAIL_USE_SSL'] = 
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''

mail.init_app(app)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/expertise')
def expertise():
	return render_template('expertise.html')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/cv')
def cv():
	return render_template('cv.html')

@app.route('/code')
def code():
	return render_template('code.html')

@app.route('/research')
def research():
	return render_template('research.html')

@app.route('/email', methods=['GET', 'POST'])
def email():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('email.html', form=form)
        else:
            msg = Message(form.subject.data, sender='sender@domain.com', recipients=['recipient@domain.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('email.html', success=True)

    elif request.method == 'GET':
        return render_template('email.html', form=form)  

if __name__ == '__main__':
	app.run(debug=True)