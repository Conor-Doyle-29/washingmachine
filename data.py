import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM14'
ser.open()
rpms = [1400, 1200, 1000, 800,600]  
temp = 0 
speed = rpms[temp]
while True:
    data = str(ser.readline())
    data= data.replace("b","")
    data= data.replace("'","")
    data= data.replace(" ","")
    data= data.replace("\\r\\n","")
    data = int(data)

    if data > (3180):
        print("WARNING - READING IS TOO HIGH")
    print(data)
    
    if data > (3180):
        temp+=1
        speed= rpms[temp]
    print("rpm =", speed)


"""
    if len(data) > 0:
        print(data)
        file = open("accelerometer.csv",'a')
        file.write(data+",")
        file.close()
"""     

  
