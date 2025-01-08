# these small project is Bmi calculator for pythons
# declare varibles that means height and weight
height=float(input("enter your height"))
weight=int(input("enter your weight"))
bmi=weight/height * height
def Bmi_calculator():
    if(bmi<18.5):
        print("you are under weight ::")
    elif bmi>=18.5 and bmi<22.5:
        print("you are normal bmi::")
    elif bmi>=22.5 and bmi<28.7:
        print("your bmi is over")
    else:
        print("you are under obisity ")
        
