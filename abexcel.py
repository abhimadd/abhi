import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('sample1.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        infile = open('sample1.csv')
    while file_to_read != ("sample1.csv"):
        file_to_write = raw_input("Enter output file name (sample1.csv will be appended to it):")
        file_to_write = file_to_write + "sample1.csv"
        outfile = open(file_to_write, "w")
        readings = (infile.readline())
        print (readings)
        while readings != 0:
            global count
            readings = int(readings)
            minimum = (infile.readline())
            maximum = (infile.readline())

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()