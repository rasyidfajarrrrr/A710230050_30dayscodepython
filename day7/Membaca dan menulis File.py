fileku = open("buah.txt","w")
fileku.write('Apel\n')
fileku.write('Mangga\n')
fileku.write('Jambu')
fileku.close()

bacafileku = open("buah.txt","r")
print(bacafileku.read())