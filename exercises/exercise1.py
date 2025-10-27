questions=["1. what is the speed of light\n","2. what is the correct form of relativity theory equation\n","3. who invented AC ? \n"]
options=[['a. 2x10^8','b. 3x10^8','c. 5x10^6','d. 1x10^3'],['a. e=mc','b. e=mc^2','c. e=(mc)^2','d. none of these'],['a. Edison','b. Tesla','c. Einstein','d. Marconi']]
answers=['b','b','b']
no=0
score=0
user_input=[]
for q in questions:
    print(q)
    for o in options[no]:
        print(o)
    inp=input("\n enter ")
    user_input.append(inp)
    print("-----------------------------------")
    if inp == answers[no]:
        print("correct")
        score+=1
    else:
        print("wrong")
    print("----------------------------------")   
    no+=1
print("\nfinal score: ",score)
