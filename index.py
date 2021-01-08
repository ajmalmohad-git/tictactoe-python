import array as arr

mark=0
options=['A','B','C','D']

quiz = {
        'How many days do we have in a week?':['A: Seven','B: Six','C: Eight','D: Ten','A'],
        'How many primary colors are there?':['A: Five','B: Three','C: Six','D: One','B'],
        ' Which is the principal source of energy for earth?':['A: Sun','B: Moon','C: Jupiter','D: Mercury','A'],
        'Which animal is known as the ‘Ship of the Desert?’':['A: Dog','B: Cat','C: Eagle','D: Camel','D'],
        'Which month of the year has the least number of days?':['A: January','B: July','C: February','D: June','C'],
    }

def answercheck(y):
    ans=''
    print('Enter the answer option:')
    ans=input(ans)
    ans=ans.capitalize()
    if ans==y[4]:
        print('Correct')
        global mark
        mark+=1
    elif ans not in options:
        print('Incorrect input format . Enter options A,B,C or D')
        answercheck(y)
    else:
        print('Wrong')


for x,y in quiz.items():
    print('\n',x,'\n',y[0],'\n',y[1],'\n',y[2],'\n',y[3])  #y[0:-1]
    answercheck(y)
    

print('\n',"You got ",mark," marks.","\n\n")

input()