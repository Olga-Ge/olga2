while True:
    try:
        prompt1=("what is your gross income?")
        gross=input(prompt1)
        gross = int(gross)

        if gross <1000:
            tax=0.1
        elif gross < 2000:
            tax = 0.11
        elif gross < 4000:
            tax = 0.12
        else:
            tax=0.14
        break
    except:
        print ("that is not a number")
while True:
    try:
        kids = input ("how many kids?")
        kids = int(kids)
        if gross < 2000:
            tax = tax - kids*0.01
        else:
            tax = tax - kids*0.005
        if tax<0:
            print ("stop making kids")
            tax = 1
        net=gross*(1-tax)
        print("you take home", net, "pounds")
        break
    except:
        print("that is not a number")
