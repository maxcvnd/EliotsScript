file = open("Output.txt", "r")
string = file.read().replace('\n','').replace('-', ' ')
jump = ")"
symbols = "][(,' "
for char in jump:
	string = string.replace(char,"\n")
for char in symbols:
	string = string.replace(char,"")
#print (string)
def changeFile():
	f = open("Output.txt", "w")
	f.write (string)
	f.close()

changeFile()
print("Proces Finished!!")
print('Check the file "Output.txt"')
