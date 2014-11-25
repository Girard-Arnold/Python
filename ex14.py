#from sys import argv #tell the script that we want to take a command called argv from the feature(module) set "sys"

#script, filename = argv #arguments required for the script to run

filename = raw_input("Please enter the script's name\n >")
txt = open(filename) #tell the script to open a file (determined by argv aka the user here)

print "Here's your file %r:" % filename #prints the filename
print txt.read() #this reads, and prints whatever characters are contained in the file, until it hits the end
txt.close()

print "Type the filename again:"
file_again = raw_input("> ") 

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
