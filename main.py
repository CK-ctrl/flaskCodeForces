from flask import Flask, render_template
import forces
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
	Date = datetime.date.today()
	daysrem = str(datetime.date(2021,7,31) - Date)
	temp = daysrem.split(',')[0]
	return render_template('index.html', days=temp, user=forces.my_data)


if __name__ == "__main__":
	app.run(debug=True)
