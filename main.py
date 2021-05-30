from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
	Date = datetime.date.today()
	daysrem = str(datetime.date(2021,7,31) - Date)
	return render_template('index.html', data=daysrem)


if __name__ == "__main__":
	app.run(debug=True)


