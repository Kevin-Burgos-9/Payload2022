import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('data.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Acceleration Z")
  
plt.xticks(rotation = 25)
plt.xlabel('TimeStamp')
plt.ylabel('Acceleration')
plt.title('Time vs Acceleration Z', fontsize = 20)
plt.grid()
plt.show()
