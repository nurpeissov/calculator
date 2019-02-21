from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
	result = None
	log = None
	if request.method == 'POST':
		if request.form['number1'] and request.form['number2'] is not None  :
			number1 = float(request.form['number1'])
			number2 = float(request.form['number2'])
			operator = request.form['operator']
			if operator=='Add':
				result=number1+number2
			if operator=='Substract':
				result=number1-number2
			if operator=='Multiply':
				result=number1*number2
			if operator=='Divide':
				if number2==0:
					result="Division by Zero is not possible"
				else:	
					result=number1/number2
		else :
			result="Plese input numbers"
	return render_template('calculate.html', result=result)

if __name__ == '__main__':
    app.debug = True
    app.run()