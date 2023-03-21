
Gen= input("Your Gender -  ")

if (Gen=="male"):
    print (input("Your age - "))
elif( Gen=="female"):
    print(input("your age - "))
elif (Gen=="others"):
    print(input("your age - "))
else:
    print("Wrong input please enter m(male) , f(female) or  others ")
wt = float(input("Enter your weight =     "))
ht_met= float (input("Enter your height in feet =  "))
ht = (ht_met/3.281)**2
bmi= (wt/ht)
print( "Your BMI is ->"    , bmi , "kg/m2")

if (bmi <18.5):
    print ("You are underweight")
elif(18.5>bmi>24.9):
    print("You have a healthy body weight")
elif(25>bmi>29.9):
    print("You are Overweight")
else:
    print("You need to work on your body")

        



 
