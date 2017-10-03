from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 


@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/year')
def age():
	return render_template('template1.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
	if request.method == 'GET':
		result = request.args
		num2 = 2017 - int(result['num'])
		return "You were born in " + str(num2)	

@app.route('/name')
def name():
	return render_template('names.html')

@app.route('/result2', methods = ['GET', 'POST'])
def result_two():
	names = "Nate Sammy Bari Mat Jonny"
	if request.method == 'GET':
		result = request.args
		num2 = str(result['num'])
		if num2 in names:
			return str(num2) + ", you passed the test."
		else:
			return str(num2) + ", you did NOT passed the test."	