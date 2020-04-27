weight = float(input ("Enter Weight (kg):"))
bf = float(input("Enter Estimated body-fat percentage:"))
height = float(input ("Enter Height (cm):"))
age = float(input ("Enter Age:"))
weightlbs = float (weight * 2.20462)
ffmi = float (weightlbs * (1 - (bf / 100)))


BMR = float((10*weight)+(6.25*height)-(5*age)+5)
print ("Your BMR is:" + " " + str(BMR) + " " +  "calories")
print ('Now we need an activity multiplier.')
print ('1.2-1.5 - Gym/Sedentary')
print ('1.5-1.8 - Gym/Lightly Active')
print ('1.8-2.0 - Gym/Moderatley Active')
print ('2.0-2.2 - Gym/Highly Active')
print()

activity = float(input ("Enter Activity Multiplier:"))

nM = int(BMR * activity)

print ("Your Maintenance Calories are:" + " " + str(nM) + " " + "calories")
print ('If cutting, press 1. Calories will be 80% of maintenance')
print ('If bulking, press 2. Calories will be 115% of maintenance')

boc = input()


if boc == '1' :
    print('You will require' + ' ' + (str(int(nM * 0.8))) +' ' + 'calories')
    # print ('Make sure to eat this much protein:', str(int(ffmi * 1.4 ))+'g') #added protein (general recommendation of 1.4g/lbm. Next step - add sliding model of protein, select range of 1.2-1.6 (check body recomp for details))
elif boc == '2' :
    print('You will require' + ' ' + (str(int(nM * 1.15))) +' ' + 'calories')
    # print ('Make sure to eat this much protein:', str(int(ffmi * 1.4 ))+ 'g')

print ('Using the sliding protein model, decide if your protein should range between 1.2 - 1.6g /lbm')
slidingProtein = float(input ()) #try adding units at end of input?? for sake of completness
print('Make sure to eat this much protein:', str(int(ffmi * slidingProtein ))+ 'g')


    







