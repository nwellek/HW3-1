## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application 
#code below so that the routes described in the 
#README exist and render the templates they are 
#supposed to (all templates provided inside the HW3Part1/templates directory).

from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/user/<name>')
def hello_user():
	return '<h1>Hello {0}<h1>'.format(name)

@app.route('/artistform')
def artist():
	return render_template('artistform.html')

@app.route('/artistinfo', methods = ['GET', 'POST'])
def itunes_data():
	if request.method =='GET':
		result = request.args
		term=result.get('artist')
		url = requests.get('https://itunes.apple.com/search?term='+term)
		data = json.loads(url.text)
	return render_template('artist_info.html', objects=data['results'])

@app.route('/artistlinks')
def b():
	return render_template('artist_links.html')

@app.route('/specific/song/<artist_name>', methods= ['GET', 'POST'])
def d(artist_name):
	d = {'term' : artist_name, 'media' : 'music', 'format':'json'}
	resp = requests.get("https://itunes.apple.com/search?", params=d)
	d_info = json.loads(resp.text)
	return render_template('specific_artist.html', results=d_info['results'])	