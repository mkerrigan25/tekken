import re

class Move:
	command = ""
	st=0
	hit=0
	block=0

class Hit:
	hitType = ""
	damage  = 0
	hits = 0


def Viewfile(file):
    with open(file,'r') as viewFileOpen:
        data = viewFileOpen.read()
        matches = Matchsort(data)
    return matches

def Matchsort(data):
	matches = re.findall(r'(?xs)Fight\ detected(.*?)No\ fight', data, )

	return matches

def Punish(match):
	fight=match.split('\n')
	p1 = {}
	p2 = {}
	for index, line in enumerate(fight):
		print(line)
		if "Closing" in str(line):
			print("found")
			if "p1:" in fight[index-1]:
				if fight[index-1] in p1:
					p1[fight[index-1]] +=1
				else:
					p1[fight[index-1]] =1
			else:
				if fight[index-1] in p2:
					p2[fight[index-1]] +=1
				else:
					p2[fight[index-1]] =1

def matchData(match):
	fight=match.split('\n')
	p1 = []
	p2 = []
	x1=0
	x2=0
	for line in fight:
		a=line.split("|")
		if len(a)==14:
			a[3]=a[3].replace(' ','')
			print(a[3])
			if a[3] == "HIGH" or a[3] == "MID" or a[3] == "LOW" or a[3] == "THROW":
				print(a[3])
				print(line)
				if "p1:" in a[0]:
					a[0]= a[0].replace('p1:','')
					x = Move()
					x.command=a[0]
					x.tbl=line
					x.st=a[4]
					x.block=a[5]
					x.hit=a[6]
					p1.append(x)

				elif "p2:" in a[0]:
					a[0]= a[0].replace('p2:','')
					x = Move()
					x.command=a[0]
					x.st=a[4]
					x.block=a[5]
					x.hit=a[6]
					p2.append(x)
		elif len(a)==6:
			if "p1:" in a[0]:
					a[0]= a[0].replace('p1:','')
					x = Hit()
					x.type=a[0]
					x.damage=a[1]
					x.hits=a[2]
					p2.append(x)

			elif "p2:" in a[0]:
					a[0]= a[0].replace('p2:','')
					x = Hit()
					x.type=a[0]
					x.damage=a[1]
					x.hits=a[2]
					p1.append(x)

			
	for obj in p1:
		print(obj)
	print("\n")
	for obj in p2:
		print(obj)

#def Hit(match):
#	fight=match.split('\n')
#	p1 = {}
#	p2 = {}
#	for index, line in enumerate(fight):
#		print(line)
#		if "HIT" in line and "!ROUND" not in line:
#			print("found")
#			p = fight[index-1].split("|")[0]
#			p= p.replace(' ','')
#			if "p1:" in p:
#				p= p.replace('p1:','')
#				if p in p1:
#					p1[p] +=1
#				else:
#					p1[p] =1
#			else:
#				p= p.replace('p1:','')
#				if p in p2:
#					p2[p] +=1
#				else:
#					p2[p] =1
#	print(p1)
#	print(p2)


matches =Viewfile("testdata.txt")
matchData(matches[2])