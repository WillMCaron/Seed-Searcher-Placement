from random import randint, seed

def seed_search(goal = 72727, iteration = 1, num = 100):
  found_count = 0
  file = open("ones.txt","r")
  seed_num = int(file.readlines()[-1])+1
  file.close()

  while (found_count < num):
      seed(seed_num)

      for i in range(iteration):
        randNum = randint(0,100000)
    
      if randNum == goal:
        file = open("ones.txt","a")
        file.write(str(seed_num)+"\n")
        file.close()
        print(randNum, seed_num)
        found_count += 1
      seed_num +=1

def rep_search(goal = 72727, iteration = 10, num = 1):
  found_count = 0
  file = open("tensC.txt","r")
  seed_num = int(file.readlines()[-1])+1
  file.close()

  while (found_count < num):
      seed(seed_num)
      rep_count = 1
      for i in range(iteration):
        randNum = randint(0,100000)
        if randNum != goal:
          rep_count = 0
          break
      if seed_num %100000 == 0:
        print(seed_num, "searched")
    
      if rep_count == 1:
        file = open("ones.txt","a")
        file.write(str(seed_num)+"\n")
        file.close()
        print(randNum, seed_num)
        found_count += 1
      seed_num +=1

#seed(138377)
#print(randint(0,100000))
seed_search(num = 1000)
#rep_search(iteration = 2)
