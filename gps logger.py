import serial
import numpy
filen=str(input("input file name: "))
f=open(filen+".csv","w")
mf=open("m"+filen,'w')
val=0
x=str(input("input COM port number"))
gps=serial.Serial("COM"+x,baudrate=9600)
def tra(t):
	return str(numpy.floor(float(t.split(",")[0].replace("\n",""))/100)+((float(t.split(",")[0])%100)/60))+","+str(numpy.floor(float(t.split(",")[1])/100)+((float(t.split(",")[1].replace(",",""))%100)/60))
def fix(data):
	return str(float("{:.6f}".format(float(data.split(",")[0]))))+","+str(float("{:.6f}".format(float(data.split(",")[1]))))
while True:
	mdata=gps.readline().decode()
	if val !=0:
		mf.write(mdata+"\n")
		print(".")
	data=mdata.split(",")
	if "$GNRMC" in data and data[3] != "":
		val=1
		print(fix(tra(str(data[3])+","+str(data[5])+"\n")))
		f.write(fix(tra(str(data[3])+","+str(data[5])))+"\n")
	if "$GNGGA" in data and data[2] != "":
		val=1
		print(fix(tra(str(data[2])+","+str(data[4])+"\n")))
		f.write(fix(tra(str(data[2])+","+str(data[4])))+"\n")
f.close()
mf.close()
