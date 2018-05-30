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
		
		if "Closing" in str(line):
			
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
	for index, line in enumerate(fight):
		a=line.split("|")
		if len(a)==14:
			a[3]=a[3].replace(' ','')
			if a[3] == "HIGH" or a[3] == "MID" or a[3] == "LOW" or a[3] == "THROW":

				if "p1:" in a[0]:
					a[0]= a[0].replace('p1:','')
					a[0]= a[0].replace(' ','')
					x = Move()
					x.command=a[0]
					x.tbl=line
					x.st=a[4]
					x.block=a[5]
					x.hit=a[6]
					p1.append(x)

				elif "p2:" in a[0]:
					a[0]= a[0].replace('p2:','')
					a[0]= a[0].replace(' ','')
					x = Move()
					x.command=a[0]
					x.st=a[4]
					x.block=a[5]
					x.hit=a[6]
					p2.append(x)
		elif len(a)==6:
			if "p1:" in a[0]:
					a[0]= a[0].replace('p1:','')
					a[0]= a[0].replace(' ','')
					x = Hit()
					x.hitType=a[0]
					x.damage=a[1]
					x.hits=a[2]
					p2.append(x)

			elif "p2:" in a[0]:
					a[0]= a[0].replace('p2:','')
					a[0]= a[0].replace(' ','')
					x = Hit()
					x.hitType=a[0]
					x.damage=a[1]
					x.hits=a[2]
					p1.append(x)
		elif len(a)==1 and "NO_PUNISH" in a[0]:
			if "p1" in fight[index-1]:
				x = Hit()
				x.hitType="Block_NO_PUNISH"
				x.damage=0
				x.hits=1
				p1.append(x)
			elif "p1" in fight[index-1]:
				x = Hit()
				x.hitType="Block_NO_PUNISH"
				x.damage=0
				x.hits=1
				p1.append(x)

	player1 = {}
	player2 = {}
	st = ""
	for obj in p1:
		try:
			if st == "":
				st = obj.hitType
			if st in player1:
				player1[st+obj.hitType][0] += 1
				player1[st+obj.hitType][2] += int(obj.damage)
				st =""
			else:
				
				player1[st+obj.hitType] = [1, int(obj.damage), int(obj.damage)]
				st = ""


		except AttributeError:
			st += obj.command + " "

	for obj in p2:
		try:
			if st == "":
				st = obj.hitType
			if st in player1:
				player2[st+obj.hitType][0] += 1
				player2[st+obj.hitType][2] += int(obj.damage)
				st =""
			else:
				
				player2[st+obj.hitType] = [1, int(obj.damage), int(obj.damage)]
				st = ""


		except AttributeError:
			st += obj.command + " "
	print("player 1")
	for x in player1:
		print(x)
		for y in player1[x]:
			print(y)
		print("\n")

	print("player 2")
	for x in player2:
		print(x)
		for y in player2[x]:
			print(y)
		print("\n")




matches =Viewfile("testdata.txt")
matchData(matches[2])