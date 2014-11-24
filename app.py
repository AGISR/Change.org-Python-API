from flask import Flask
import changeorgscraper

app = Flask(__name__)

@app.route('/')
def helloWorld():
	return "hello world"

sp = changeorgscraper.Scraper()

if __name__ == "__main__":
	app.run()