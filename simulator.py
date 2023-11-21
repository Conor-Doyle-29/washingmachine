import random
import time 
upperLimit= 3533
lowerLimit= 1000
rpmLimit= 3180
rpms = [1400, 1200, 1000, 800,600]  
temp = 0 
speed = rpms[temp]

while True: 
    data= random.randint(lowerLimit,upperLimit)
    time.sleep(700/1000)
    print(data)
    if data > (3180):
        print("WARNING - READING IS TOO HIGH")
  
    
    if data > (3180):
        if speed == 600:
            temp-=1
        temp+=1
        speed= rpms[temp]
        
    print("rpm =", speed)