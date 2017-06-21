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
    find(Pattern("1497966540715.png").similar(0.90))  
    print ("[INFO] Prozentsatz gefunden") 
    sleep(2)
    click(Pattern("1497966571003.png").similar(0.90).targetOffset(-27,17))
    print ("[INFO] Prozentsatz angeklickt")
    sleep (2)
    paste ("52")
    print ("[INFO] Prozentsatz Zahl eingegeben")
    type (Key.ENTER)
    sleep (2)
    find(Pattern("1497959100825.png").similar(0.90))
    print ("[INFO] Prozentwert gefunden")
    sleep (2)
    click(Pattern("1497959180299.png").similar(0.90).targetOffset(-11,15))
    print ("[INFO] Prozentwert angeklickt")
    sleep(2)
    paste ("68")
    print ("[INFO] Prozentwert Zahl eingegeben")
    sleep(2)
    click(Pattern("1497959296514.png").similar(0.90))
    print ("[INFO] Erfogreich auf Berechnen Geklickt")
    sleep (2)
    find("1497966734475.png")
    print ("[INFO] Ergebnis erfolgreich gefunden")
except FindFailed:
    print ("[ERROR] Ergebnis nicht gefunden")
    sys.exit(1)
    
    
    
    
    
    
    
    









