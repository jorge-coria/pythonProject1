import csv

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

# Number of characters written to file for each row
print(outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']))
print(outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']))
print(outputWriter.writerow([1, 2, 3.141592, 4]))

outputFile.close()
