import sys
import time
import datetime

def vraag23():
    print("de politie bied jou een verblijfsverguning aan.")
    print("ze geven je ook gelijk een plekje om te verblijven met je vrienden")
    time.sleep(1)
    print("neem je het aan of niet")
    print("A : ja je neemt het aan!")
    print("B : nee je neemt niet aan")
    antwoord23 = input() 
    if antwoord23.lower() == "a":
        print("ja natuurlijk je woont nu veilig met je vrienden in Nederland!")
        sys.exit()
    elif antwoord23.lower() == "b":
        print("dit is niet zo slim van je!")
        print(vraag1())
    else:
        print("kies a,b") 

def vraag22():
    print("de politie bied jou een verblijfsverguning aan.")
    print("ze geven je ook gelijk een plekje om te verblijven met je famillie")
    time.sleep(1)
    print("neem je het aan of niet")
    print("A : ja je neemt het aan!")
    print("B : nee je neemt niet aan")
    antwoord22 = input() 
    if antwoord22.lower() == "a":
        print("ja natuurlijk je woont nu veilig met je famillie in Nederland!")
        sys.exit()
    elif antwoord22.lower() == "b":
        print("dit is niet zo slim van je!")
        print(vraag1())
    else:
        print("kies a,b")    
        print(vraag20())

def vraag21():
    print("je bent aangekomen in Nederland met je familie.")
    print("je ziet de politie en je vraagt hun wat je moet doen")
    time.sleep(1)
    print("ze vragen jou of je met je famillie mee wil naar het asiel")
    print("A : ga je mee?")
    print("B : ga je niet mee?")
    antwoord21 = input() 
    if antwoord21.lower() == "a":
        print("ja natuurlijk !")
        print(vraag22())
    elif antwoord21.lower() == "b":
        print("je gaat niet mee dat is niet slim!")
        print(vraag1())
    else:
        print("kies a,b")    
        print(vraag21()) 

def vraag20():
    print("je bent aangekomen in Nederland met je vrienden.")
    print("je ziet de politie en je vraagt hun wat je moet doen")
    time.sleep(1)
    print("ze vragen jou of je met vrienden mee wil naar het asiel")
    print("A : ga je mee?")
    print("B : ga je niet mee?")
    antwoord20 = input() 
    if antwoord20.lower() == "a":
        print("ja natuurlijk !")
        print(vraag23())
    elif antwoord20.lower() == "b":
        print("je gaat niet mee dat is niet slim!")
        print(vraag1())
    else:
        print("kies a,b")    
        print(vraag20())

def vraag19():
    print("je rent met je familie uit het land en je ziet een smokelaar.")
    print("hij vraagt jullie 100 euro om jullie naar nederland te brengen")
    time.sleep(1)
    print("je hebt in totaal 100 euro bij je met je famillie ga je mee of niet?")
    print("A : ja natuurlijk")
    print("B : je gaat niet mee")
    antwoord19 = input() 
    if antwoord19.lower() == "a":
        print("je gaat mee met de smokelaar!")
        print(vraag21())
    elif antwoord19.lower() == "b":
        print("je gaat niet mee dat is niet slim!")
        print(vraag1())
    else:
        print("kies a,b")    
        print(vraag19()) 

def vraag18():
    print("je rent met je vrienden uit het land en je ziet een smokelaar.")
    print("hij vraagt jullie 100 euro om jullie naar nederland te brengen")
    time.sleep(1)
    print("je hebt in totaal 100 euro bij je met je vrienden ga je mee of niet?")
    print("A : ja natuurlijk")
    print("B : je gaat niet mee")
    antwoord18 = input() 
    if antwoord18.lower() == "a":
        print("je gaat mee met de smokelaar!")
        print(vraag20())
    elif antwoord18.lower() == "b":
        print("je gaat niet mee dat is niet slim!")
        print(vraag1())
    else:
        print("kies a,b")    
        print(vraag18())        

def vraag17():
    print("je bent aangekomen bij de grens.")
    print("je wil over de grens")
    time.sleep(1)
    print("hoe ga je er langs ?")
    print("A : rustig aan de politie vragen of jij en je vrienden er langs mogen")
    print("B : je gaat mee met de andere vluchtelingen")
    antwoord17 = input() 
    if antwoord17.lower() == "a":
        print("de politie neemt je mee naar een gevangenis vanwege die vraag die je hem stelt!")
        print(vraag1())
    elif antwoord17.lower() == "b":
        print("je rent zo snel mogelijk met je vrienden mee met de andere!")
        print(vraag18())
    else:
        print("kies a,b")    
        print(vraag17())

def vraag16():
    print("je bent aangekomen bij de grens.")
    print("je wil over de grens")
    time.sleep(1)
    print("hoe ga je er langs ?")
    print("A : rustig aan de politie vragen of jij en je familie er langs mogen")
    print("B : je gaat mee met de andere vluchtelingen")
    antwoord16 = input() 
    if antwoord16.lower() == "a":
        print("de politie neemt je mee naar een gevangenis vanwege die vraag die je hem stelt!")
        print(vraag1())
    elif antwoord16.lower() == "b":
        print("je rent zo snel mogelijk met je familie mee met de andere!")
        print(vraag19())
    else:
        print("kies a,b")    
        print(vraag16())

def vraag15():
    print("je hebt ervoor gekozen om door te lopen met je vrienden .")
    print("jullie zijn heel moe en willen uitrusten")
    time.sleep(1)
    print("ga je zitten of blijven lopen?")
    print("A : je gaat zitten met je vrienden")
    print("B : je gaat doorlopen ")
    antwoord15 = input() 
    if antwoord15.lower() == "a":
        print("je zit en de kans die je hebt om dood te gaan is te groot om te gaan rusten!!")
        print(vraag1())
    elif antwoord15.lower() == "b":
        print("je gaat lopen want je kan niet stoppen goeie keus!")
        print(vraag17())
    else:
        print("kies a,b")    
        print(vraag15())

def vraag14():
    print("je bent aangekomen bij de grens.")
    print("je wil over de grens")
    time.sleep(1)
    print("hoe ga je er langs ?")
    print("A : rustig aan de politie vragen of jij en je vrienden er langs mogen")
    print("B : je gaat mee met de andere vluchtelingen")
    antwoord14 = input() 
    if antwoord14.lower() == "a":
        print("de politie neemt je mee naar een gevangenis vanwege die vraag die je hem stelt!")
        print(vraag1())
    elif antwoord14.lower() == "b":
        print("je rent zo snel mogelijk met je vrienden mee met de andere!")
        print(vraag18())
    else:
        print("kies a,b")    
        print(vraag14())

def vraag13():
    print("je koos ervoor doortelopen.")
    print("je begint heel moe te raken met je familie  ")
    time.sleep(1)
    print("je ziet verderop een plekje waar je kan zitten ga je eventjes rusten met je famillie of blijf je lopen ?")
    print("A : je blijft lopen")
    print("B : je gaat ziiten")
    antwoord13 = input() 
    if antwoord13.lower() == "a":
        print("je gaat lopen want je kan niet stoppen goeie keus!")
        print(vraag16())
    elif antwoord13.lower() == "b":
        print("je zit en de kans die je hebt om dood te gaan is te groot om te gaan rusten!")
        print(vraag1())
    else:
        print("kies a,b")    
        print(vraag13())

def vraag12():
    print("je koos ervoor om een rit te zoeken.")
    print("je ziet een man en hij zegt 30 euro om jullie allemaal naar de grens te brengen van syrie")
    time.sleep(1)
    print("ga je mee of blijf je zoeken ?")
    print("A : je gaat mee")
    print("B : je gaat door met zoeken")
    antwoord12 = input() 
    if antwoord12.lower() == "a":
        print("je stapt in met je famillie dat is een hele goeie keus!")
        print(vraag16())
    elif antwoord12.lower() == "b":
        print("je gaat door met zoeken dat is niet een goede keus!")
        print(vraag1())
    else:
        print("kies a,b")    
        print(vraag12())

def vraag11():
    print("je koos ervoor doortelopen.")
    print("je begint heel moe te raken met je vrienden  ")
    time.sleep(1)
    print("je ziet verderop een plekje waar je kan zitten ga je eventjes rusten met je vrienden of blijf je lopen ?")
    print("A : je gaat blijft lopen")
    print("B : je gaat ziiten")
    antwoord11 = input() 
    if antwoord11.lower() == "a":
        print("je gaat lopen en je stopt niet goeie keus!")
        print(vraag15())
    elif antwoord11.lower() == "b":
        print("je zit en de kans die je hebt om dood te gaan is te groot om te gaan rusten!")
        print(vraag1())
    else:
        print("kies a,b")    
        print(vraag11())

def vraag10():
    print("je koos ervoor om een rit te zoeken.")
    print("je ziet een man en hij zegt 30 euro om jullie allemaal naar de grens te brengen van syrie")
    time.sleep(1)
    print("ga je mee of blijf je zoeken ?")
    print("A : je gaat mee")
    print("B : je gaat door met zoeken")
    antwoord10 = input() 
    if antwoord10.lower() == "b":
        print("je blijft zoeken dat is niet goed!")
        print(vraag1())
    elif antwoord10.lower() == "a":
        print("je stapt in met je vrienden dat is een hele goeie keus!")
        print(vraag14())
    else:
        print("kies a,b")    
        print(vraag10())

def vraag9():
    print("je koos ervoor om het eten van de man aantenemen.")
    print("jullie zijn helemaal klaar voor jullie reis hoe gaan jullie verder")
    time.sleep(1)
    print(" lopend of ga je zoeken naar een rit?")
    print("A : lopend")
    print("B : je gaat iemand zoeken")
    antwoord9 = input() 
    if antwoord9.lower() == "a":
        print("je blijft doorlopen!")
        print(vraag13())
    elif antwoord9.lower() == "b":
        print("je gaat op zoek naar een rit!")
        print(vraag12())
    else:
        print("kies a,b")    
        print(vraag9())

def vraag8():
    print("je koos ervoor om het broodje aannemen.")
    print("jullie zijn helemaal klaar voor jullie reis hoe gaan jullie verder")
    time.sleep(1)
    print("lopend of iemand vragen voor een rit?")
    print("A : door lopen")
    print("B : iemand vragen")
    antwoord8 = input() 
    if antwoord8.lower() == "a":
        print("je gaat doorlopen!")
        print(vraag11())
    elif antwoord8.lower() == "b":
        print("je gaat zoeken naar een rit !")
        print(vraag10())
    else:
        print("kies a,b")    
        print(vraag8())

def vraag7():
    print("je koos voor om door te lopen.")
    print("er komt nu een man naar je toe en hij vraagt of jullie eten nodig hebben")
    time.sleep(1)
    print("wat doe je ?")
    print("A : je zegt ja")
    print("B : je zegt nee")
    antwoord7 = input() 
    if antwoord7.lower() == "a":
        print("ja natuurlijk moet je het aanemen !")
        print(vraag9())
    elif antwoord7.lower() == "b":
        print("je zegt nee en je verhongerd uiteindelijk!")
        print(vraag1())
    else:
        print("kies a,b")    
        print(vraag7())

def vraag6():
    print("je koos voor om lopend te gaan na paar uur komt er een man naar jullie en vraagt of je een broodje.")
    time.sleep(1)
    print("wat doe je ?")
    print("A : broodje aanemen")
    print("B : je blijft doorlopen")
    antwoord6 = input() 
    if antwoord6.lower() == "a":
        print("ja natuurlijk moet het aanemen !")
        print(vraag8())
    elif antwoord6.lower() == "b":
        print("je blijft doorlopen dat is niet goed je moet altijd eten aanemen!")
        print(vraag1())
    else:
        print("kies a,b")    
        print(vraag6())

def vraag5():
    print("je loopt al paar uren lang en jullie hebben honger.")
    print("wat doe je?")
    print("A : jullie gaan opzoek naar eten")
    print("B : je blijft doorlopen")
    antwoord5 = input() 
    if antwoord5.lower() == "a":
        print("jullie gaan samen opzoek naar eten dat is niet goed want anders verhongeren jullie terwijl je de hele tijd zit te zoeken !")
        print(vraag1())
    elif antwoord5.lower() == "b":
        print("je blijft doorlopen want je vind dat je zo snel mogelijk moet vluchten uit het land!")
        print(vraag7())
    else:
        print("kies a,b")    
        print(vraag5())

def vraag4():
    print("je zoekt naar je vrienden en je komt ze tegen in de hoofstad jullie zijn van plan om te gaan vluchten.")
    time.sleep(1)
    print("hoe ga je?")
    print("A : met de auto van een vriend")
    print("B : lopend")
    antwoord4 = input() 
    if antwoord4.lower() == "a":
        print("je gaat met de auto niet zo verstandig want er komen alleen maar bommen uit de lucht vallen!")
        print(vraag1())
    elif antwoord4.lower() == "b":
        print("je gaat lopend goeie keus want je kan dan zien of er een bom op jullie valt!")
        print(vraag6())
    else:
        print("kies a,b")    
        print(vraag4())

def vraag3():
    print("je ziet je familie tijdens de oorlog en bent van plan om met hun het land uit te gaan.")
    time.sleep(1)
    print("hoe ga je?")
    print("A : lopend  ")
    print("B : je vraagt de politie om hulp")
    antwoord3 = input() 
    if antwoord3.lower() == "a":
        print("Je gaat lopend dat is een goeie keuze, want de politie zou jou en je familie gelijk meenemen naar de cel.")
        print(vraag5())
    elif antwoord3.lower() == "b":
        print("je bent niet slim bezig ze nemen jou en je familie mee naar de cel waar je mischien ook wel dood kan gaan  !")
        print(vraag1())
    else:
        print("kies a,b")    
        print(vraag3())

def vraag2():
    print ("ik moet het land uit voor mijn eigen veiligheid, omdat er een grote burgeroorlog is..")
    time.sleep(1)
    print ("met wie moet ik het land proberen uit te gaan met mijn familie of vrienden?")
    print("A : familie")
    print("B : vrienden")
    antwoord2 = input() 
    if antwoord2.lower() == "a":
        print("je gaat met je famillie de land uit goeie keus!")
        print(vraag3())
    elif antwoord2.lower() == "b":
        print("je gaat met vrienden het land uit!")
        print(vraag4())
    else:
        print("kies a,b")    
        print(vraag2())

def vraag1():
    print ("waarom vlucht ik uit syrië ?")
    print("a : voor mijn eigen veiligheid")
    print("b : omdat ik het zelf wou")
    antwoord1 = input()
    if antwoord1.lower() == "a":
        print("ja dat klopt!")
        print(vraag2()) 
    elif antwoord1.lower() == "b":
        print("nee dat klopt niet")
        print(vraag1())
    else:
         print("kies a,b")
         print(vraag1())     

print(vraag1())
