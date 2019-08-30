import os

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
		api = clockwork.API(os.getenv("TEXTAPI"),)

		message = clockwork.SMS(
		    to = f'{num}',
		    message = f'{txt}',
		    from_name='MrAkotoApps')

		response = api.send(message)

		if response.success:
			return render_template('home.html', num=num, txt=txt)
		else:
			return redirect(url_for('home'))


@app.route('/textMe', methods=['GET', 'POST'])
def textMe():
	if request.method == 'GET':
		return render_template('textMe.html')
	else:
		txt = request.form.get('sendText')
		from clockwork import clockwork
		api = clockwork.API(os.getenv("TEXTAPI"),)

		message = clockwork.SMS(
		    to = '447481790498',
		    message = f'{txt.lower()}',
		    from_name='MrAkotoApps')

		response = api.send(message)

		if response.success:
			return render_template('textMe.html', txt=txt)
		else:
			return redirect(url_for('textMe'))