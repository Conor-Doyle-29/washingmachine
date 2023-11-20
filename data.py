import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM14'
ser.open()
while True:
    data = str(ser.readline())
    data= data.replace("b","")
    data= data.replace("'","")
    data= data.replace(" ","")
    data= data.replace("\\r\\n","")
    if data > str(3180):
        print("WARNING - READING IS TOO HIGH")
    print(data)
    rpms = [1400, 1000, 800,600]  
    temp = 0 
    speed = rpms[temp]
    if data > str(3180):
        speed= rpms[temp+1]
    print("rpm =", speed)


"""
    if len(data) > 0:
        print(data)
        file = open("accelerometer.csv",'a')
        file.write(data+",")
        file.close()
"""     

  
