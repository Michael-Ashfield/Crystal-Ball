#Made by Michael Ashfield on 09/12/2016 Last Updated 09/12/2016
import random
print("Ask the magic crystal ball a question to discover your future!")
name = str(input("Give me your name: "))
print(name, "you are now bound to my powers, I can see your future!")
ans = ["Yes",
       "No",
       "Maybe",
       "I dont think so",
       "Try asking again",
       "It looks unlikley",
       "Probably",
       "Your future is foggy, ask again",
       "It looks likley",
       "Don't count on it",
       "I think so"]
while True:
    a = str(input("Ask me a question: "))
    print(random.choice(ans))
