import random

#def sample(data):
 #   newlist=[]
  #  for val in range(0,len(data)):
   #     newlist.append(random.choice(data))
    #return newlist

def sample(data):
    sample =data[random.randint(0,len(data))]*len(data)
    return sample

    #sample=[]
    #for val in range(0,len(data)):
        #sample.append(data[random.randint(0,len(data))])

prices = []
f = open("prices.txt")
for line in f:
    v=float(line.strip())
    prices.append(v)
#TRIALS=20
#for trial in range(0, TRIALS)
print sample(prices)
