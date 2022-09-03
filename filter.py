file_name=str(input("file name: "))
f=open(file_name+".csv",'r')
arr1=[]
arr2=[]

for t in f.readlines():
    arr1.append(float((t.split(",")[0])))
    arr2.append(float((t.split(",")[1])))
window_size =23

i = 0
moving_averages1 = []
while i < len(arr1) - window_size + 1:


    window = arr1[i : i + window_size]

    window_average1 = round(sum(window) / window_size, 6)

    moving_averages1.append(window_average1)
    i += 1

i = 0
moving_averages2 = []
while i < len(arr2) - window_size + 1:



    window = arr2[i : i + window_size]

    window_average2 = round(sum(window) / window_size, 6)

    moving_averages2.append(window_average2)
    i += 1
f.close()
w=open(file_name+" filter"+".csv","w")
for i in range(0,len(arr1)-1):
    w.write(str(moving_averages1[i])+","+str(moving_averages2[i])+"\n")
w.close()
