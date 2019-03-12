from flask import Flask , render_template, request

app = Flask("Test")

def calculate_generation(year_parameter) : 
	gen='Unknow'

	# add logic here to identify generation
	if year_parameter >= 1964 and year_parameter <=1978:
		gen='very OLD'
	if year_parameter > 1979 and year_parameter <= 1995:
	 	gen='Y - Millenials'
	if year_parameter > 1996 and year_parameter <= 2012:
		gen='Z'

	return gen

@app.route("/")
def hello(vistor):
	m = "Welcome to my page" 
	return render_template("home.html", message=m)
	#return "hello"

@app.route("/<vistor>")
def hello(vistor):
	m = "Welcome to my page:" + vistor.title()
	return render_template("home.html", message=m)
	#return "hello"


@app.route("/gen", methods=["POST"])
def handle_generation_query():

	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	year = form_data["dob"]
	print year
	#dateOfBirth =  form_data["dob"] # from the form object getting value of dob field.
	#date = datetime.strptime(dateOfBirth, '%Y-%m-%d').date()
	#month = date.month
	#year = date.year
	generation= calculate_generation(int(year)) #Calling internal method which takes year as a paramter and return text
	
	return render_template ("mygen.html",gen_cohort=generation)

app.run()