try:
    find(Pattern("1497873092909.png").similar(0.81))
    print ("[INFO] explorer item gefunden")
    sleep(5)
    doubleClick(Pattern("1497873376310.png").similar(0.73))
    print ("[INFO] explorer item angeklickt")
    sleep(5)
    find("1497873588420.png")
    print ("[INFO] Sucheiste gefunden")
    sleep(2)
    click(Pattern("1497873629012.png").targetOffset(32,0))
    print ("[INFO] Suchleiste angeklickt")
    sleep(2)
    paste("danas-rechner.mybluemix.net")
    print ("[INFO] Webadresse eingefügt")
    sleep(2)
    type(Key.ENTER)
    print("[INFO] Enter gedrueckt")
    sleep(2)
    find("1497958538149.png")
    print ("[INFO] Browser starten und auf die Website verbinden erfolgreich")
except FindFailed:
    print ("[ERROR] Browser starten und auf die Website verbinden fehlgeschlagen")
    sys.exit(1)
    
try:
    find("1497874606170.png")  
    print ("[INFO] Grundwrt gefunden") 
    sleep(2)
    click(Pattern("1497958889687.png").similar(0.90).targetOffset(-17,11))
    print ("[INFO] Grundwert angeklickt")
    sleep (2)
    paste ("698")
    print ("[INFO] Grundwert Zahl eingegeben")
    type (Key.ENTER)
    print ("[INFO] Grundwert Zahl angeklickt")
    sleep (2)
    find(Pattern("1497966381967.png").similar(0.90))
    print ("[INFO] Prozentsatz gefunden")
    sleep (2)
    click(Pattern("1497966403155.png").similar(0.90).targetOffset(-21,16))
    print ("[INFO] Prozentsatz angeklickt")
    sleep(2)
    paste ("23")
    print ("[INFO] Prozentsatz Zahl eingegeben")
    sleep(2)
    type(Key.ENTER)
    sleep(2)
    click(Pattern("1497959296514.png").similar(0.90))
    print ("[INFO] Erfogreich auf Berechnen Geklickt")
    sleep (2)
    find("1497966492042.png")
    print ("[INFO] Ergebnis erfolgreich gefunden")
except FindFailed:
    print ("[ERROR] Ergebnis nicht gefunden")
    sys.exit(1)
    
    
    
    
    
    
    
    









