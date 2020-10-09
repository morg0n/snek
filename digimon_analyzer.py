digimon=[]
temp=[]
for i in range(0,3):
  temp.append(input("Enter Digimon For Analysis"))
  temp.append(int(input("Enter stats of digital monster 1:")))
  temp.append(int(input("Enter stats of digital monster 2:")))
  temp.append(int(input("Enter stats of digital monster 3:")))
  digimon.insert(i,temp[0:4])
  temp.clear()
print(digimon)