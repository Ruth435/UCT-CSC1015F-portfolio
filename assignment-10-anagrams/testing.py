result=[]
infile = open("M10P.txt",'r') #[1] mark for opening file correctly
num=0
for line in infile: #[1] mark for reading in file contents
 full = line.split() #[1] mark for split
 result.append(full) #[1] mark for adding content to list or dictionary
 total=0.0
 max=0.0
 min=10.0
 for i in range(2,8):
  score=eval(result[num][i])
 total=total+score
 if score>max: #[3] mark for calculating correct final score
  max=score
 if score<min:
  min=score
 finalScore=total-max-min
 average=finalScore/(4)
 result[num].insert(0,average)
 num+=1
result.sort()
result.reverse() #[2] mark for getting correct positions 
print("Place\tSURNAME\tName\tFinal Score")
x=1
for i in result:
 print(str(x)+"\t"+i[1]+"\t"+i[2]+"\t"+str(i[0])) #[1] mark for correct output
 x+=1