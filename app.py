from flask import Flask, render_template, url_for, request, redirect
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		num = request.form.get('number')
		txt = request.form.get('sendText')
		from clockwork import clockwork
		api = clockwork.API('1ddc9fd9717efbc300deb3d1753e182eb296d918')

		message = clockwork.SMS(
		    to = f'{num}',
		    message = f'{txt}',
		    from_name= 'Sent by Mr Akoto\'s web app')

		response = api.send(message)

		return render_template('home.html', num=num, txt=txt)


@app.route('/textMe', methods=['GET', 'POST'])
def textMe():
	if request.method == 'GET':
		return render_template('textMe.html')
	else:
		txt = request.form.get('sendText')
		sender = request.form.get('senderName')
		from clockwork import clockwork
		api = clockwork.API('1ddc9fd9717efbc300deb3d1753e182eb296d918')

		message = clockwork.SMS(
		    to = '447481790498',
		    message = f'{txt}',
		    from_name=f'\n\nMessage sent by: {sender}.')

		response = api.send(message)

		return render_template('textMe.html', txt=txt, sender=sender)