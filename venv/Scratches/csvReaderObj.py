# Opens a .csv file as a list of lists and prints each list on a new line
import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(*exampleData, sep='\n')

# Accessing the cells we want in the list using exampleData[row][col]
print('\n' + exampleData[0][0])
print(exampleData[0][1])
print(exampleData[0][2])
print(exampleData[1][1])
print(exampleData[6][1])
