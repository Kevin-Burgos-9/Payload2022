from csv import writer

def record(dataToInsert):
    with open('data.csv', 'a') as dataFile:
        fileObject = writer(dataFile)
        fileObject.writerow(dataToInsert)
        fileObject.close()

