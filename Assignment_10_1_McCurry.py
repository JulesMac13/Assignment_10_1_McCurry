#import os library
import os


def main():
    directory = input("Enter the directory that you want to save the file: ")

    name = input("Enter the file name: ")

    address = input("Enter your address: ")

    phoneNumber = input("Enter your phone Number: ")

    #checking to see if the directory exists
    if os.path.isdir(directory):

        #Creating and opening the file to write
        writeFile = open(os.path.join(directory, filename), 'w')

        #Writing the data separated by comma
        writeFile.write(name+ ', ' +address+ ', ' +phoneNumber+ '\n')

        #close file
        writeFile.close()

        print("File contents: ")

        #reading the file for proof of storing
        readFile = open(os.path.join(directory, filename), 'r')

        for line in readFile:
            print(line)

        readFile.close()
        
    else:
        print("Sorry that directory does not exist...")

main()
