def berechnen(gw=None,pw=None,ps=None):	
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
		ergebnis=None
		rechnung= None
		
		#return render_template('Prozent.html', fehler=fehler)
	
	return  ps,ergebnis,rechnung,fehler
	#return render_template('Prozent.html', typ="ps", ergebnis = ergebnis, rechnung=rechnung, fehler=fehler)
	

	
print "Test: 1"	
er = berechnen(gw=10,pw=6,ps=7)
print er

print "Test: 2"
er = berechnen(gw="hgg",pw="sd")
print er