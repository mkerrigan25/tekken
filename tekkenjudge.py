import re

class Move:
	command = ""
	count = 1
	damage = 0
	combo = False
	counterHit = False
	tbl = ""


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

def Hit(match):
	fight=match.split('\n')
	p1 = []
	p2 = {}
	x1=0
	x2=0
	for index, line in enumerate(fight):
		print(line)
		if "HIT" in line and "!ROUND" not in line:
			print("found")
			p = fight[index-1].split("|")[0]
			p= p.replace(' ','')
			if "p1:" in p:
				p= p.replace('p1:','')

				for move in p1:
					if move.command == p1:
						move.count += 1
						continue
				
				p1[x1]= Move()
				p1[x1].command=p
				tbl=line
				x1 += 1

				
			else:
				p= p.replace('p2:','')
				if p in p2:
					p2[p] +=1
				else:
					p2[p] =1
	print(p1)
	print(p2)

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
Hit(matches[2])