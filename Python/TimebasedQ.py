import time
t = time.strftime('%H')
hour = int(time.strftime('%H'))
#hour = int(input("Enter hour : "))
print(hour)

if(hour>0 and hour<12):
    print("Good Morning")
elif(hour>=12 and hour<17):
    print("Good Afternoon")
elif(hour>18 and hour<=0):
    print("Good Night")        