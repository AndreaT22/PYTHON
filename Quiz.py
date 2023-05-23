print("Hello! Welcome!")
score=0
bank={
    "What's the biggest animal? a)shrew, b)cheetah c)whale": "whale", 
    "What's the smallest animal? a)cheetah, b)shrew c)whale": "shrew",
    "What's the fastest animal? a)shrew b)whale c)cheetah": "cheetah"
      }
for (question,answer) in bank.items():
    print(question)
    useranswer=input()
    if answer==useranswer: #double= compares two things
        score=score+2
        print("Great!")
    else:
        score=score-1
        print ("I'm sorry, it's not correct.")
print("Your score is:"+ str(score))

#HWK - create - design a flow chart, and use it to create a program
