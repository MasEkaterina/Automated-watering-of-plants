from flask import Flask, render_template, url_for
from classes import PolivHub
import time

app = Flask(__name__)
hub = PolivHub.Hub()

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/poliv/<id>', methods=['POST'])
def poliv(id):
	res = hub.water_plant(id, 10)
	return ("OK" if res else "NOT FOUND")

@app.route('/history/<id>', methods=['POST'])
def history(id):
	return hub.readHistory(id)
