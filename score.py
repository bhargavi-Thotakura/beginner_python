
#print(type(score))
try:
  score = float(input("Enter Score: "))
   #score = float(score_pt)
   #print("Calculationg Grade")
  if 0.0 < score < 1.0 :
       if score >= 0.9 :
         print(score,'A')
       elif 0.8 <=score:
         print('B')
       elif 0.7 <=score:
           print(score,'C')
       elif 0.6 <=score:
           print(score,'D')
       else:print(score,'F')


except:
    print("Please enter valid entry!!")
    quit()
#convert to floating
#score.ft = float (score)
