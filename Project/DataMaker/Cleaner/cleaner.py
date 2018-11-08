f = open('sp-biogrid.v3.4.157-sls-std.tsv', 'r')
clean = open('clean.txt','w')
allData = f.readlines()

for i in range (len (allData)):
	line = allData[i].split()
	#print (line[0] + " " + line[1] )
	clean.write(line[0] + " " + line[1]+ "\n")
