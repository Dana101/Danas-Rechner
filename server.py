#encoding=utf-8

from flask import Flask
from flask import request
from flask import render_template
import os
app = Flask(__name__)

if os.getenv("VCAP_APP_PORT"):
	port = int(os.getenv("VCAP_APP_PORT"))
else:
	port = 8080

@app.route("/")
def rechner():
	return render_template("Prozent.html")
	
@app.route("/hallo")
def hello():
	name = request.args.get('name', 'Dana')
	return "Hallo " + name

@app.route("/berechnen")
def berechnen(ergebnis=None, typ=None, rechnung=None, fehler=None):
	gw = request.args.get('gw', '')
	pw = request.args.get('pw', '')
	ps = request.args.get('ps', '')
	
	if pw and gw and not ps:
		ps = float(pw) / 100 * float(gw) 
		ergebnis = str(ps)
		rechnung = pw + " : 100 * " + gw
		 # return render_template('Prozent.html', typ="ps", ergebnis = ergebnis, rechnung=rechnung, fehler=fehler)
	elif pw and ps and not gw:
		gw = float(pw) / float(ps)
		ergebnis = str(gw)
		rechnung = pw + " : " + ps
		 #return render_template('Prozent.html', typ="ps", ergebnis = ergebnis, rechnung=rechnung, fehler=fehler)
	elif gw and ps and not pw:
		pw = float(gw) * float(ps)
		ergebnis = str(pw)
		rechnung = gw + " * " + ps
	else:
		fehler= "Du musst genau 2 Felder ausfuellen, das dritte wird berechnet"
		#return render_template('Prozent.html', fehler=fehler)
	return render_template('Prozent.html', typ="ps", ergebnis = ergebnis, rechnung=rechnung, fehler=fehler)
		
		
	# if not ps and not pw and not gw:
		# fehler= "Du musst mindestens 2 Felder ausfuellen"
		# return render_template('Prozent.html', fehler=fehler)
		# if pw and gw: 
			# ps = float(pw) / 100 * float(gw) 
			# # ergebnis = "Der Prozentsatz betraegt " + str(ps) + "%"  + " <a href=\"/\">Zurück</a>"
			# ergebnis = str(ps)
			# rechnung = pw + " : 100 * " + gw
		# else: 
			# fehler="Bitte gib Prozentwert und grundwert ein"
		# return render_template('Prozent.html', typ="ps", ergebnis = ergebnis, rechnung=rechnung, fehler=fehler)
	# elif not gw:
		# if pw and ps:
			# gw = float(pw) / float(ps)
			# # ergebnis =  "Der Grundwert betraegt " + str(gw)  + " <a href=\"/\">Zurück</a>"
			# ergebnis = str(gw)
			# rechnung = pw + " : " + ps 
		# else: 
			# fehler="Bitte gib Prozentwert und Prozentsatz ein"
		# return render_template('Prozent.html', typ="gw", ergebnis = ergebnis, rechnung=rechnung, fehler=fehler)
	# else:
		# if gw and ps: 
			# pw = float(gw) * float(ps)
			# # ergebnis = "Der Prozentwert betraegt " + str(pw) + " <a href=\"/\">Zurück</a>" 
			# ergebnis = str(pw)
			# rechnung = gw + " * " + ps
		# else: 
			# fehler="Bitte gib Grundwert und prozentsatz ein"
		# return render_template('Prozent.html', typ="pw", ergebnis = ergebnis, rechnung=rechnung, fehler=fehler)
	
		
		

	
if __name__ == "__main__":
	PORT = int(os.getenv('port', '8080'))
	HOST = str(os.getenv('VCAP_APP_HOST', '0.0.0.0'))
	app.run(host=HOST,port=PORT)
