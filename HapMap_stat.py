#This python script would take a barebone hapmap file (See input file attached for format) and makes a hapmap with statistics-Harish Manmathan

#The sample input is tab limited file.

import csv

infile = open('Hapmap.csv','r')#The name of input file
outfile = open('Hapmap-stat.csv','w')#The name of output file

reader = csv.reader(infile, delimiter='\t', quotechar='"')
first = True
for row in reader:
	if first:
		outfile.write('rs#\talleles\tchrom\tpos\talleleA\talleleB\thet\tpresent\tMAF\tpercentHET\t' + '\t'.join(row[11:]) + '\n')
		first = False
	else:
		A = row[1].split('/')[0]
		B = row[1].split('/')[1]
		N = 0
		ACGT = 0

		alleleA = 0
		alleleB = 0
		het = 0

		for item in row[11:]:
			if item == A:
				alleleA += 1
			if item == B:
				alleleB += 1
			if item == 'N':
				N += 1
			if item == 'H':
				het += 1
			if item in ['A','C','G','T']:
				ACGT += 1
			

		present = float(alleleA + alleleB + het) / float(alleleA + alleleB + het + N)
		MAF = float(min(alleleA, alleleB)) / float(alleleA + alleleB + het)
		percentHET = float(het) / float(alleleA + alleleB + het)		

		outfile.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+str(alleleA)+'\t'+str(alleleB)+'\t'+str(het)+'\t'+str(present)+'\t'+str(MAF)+'\t'+str(percentHET)+'\t'+'\t'.join(row[11:])+'\n')

infile.close()
outfile.close()
