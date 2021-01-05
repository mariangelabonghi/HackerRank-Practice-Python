#!/bin/python3
n= int(input())
rubric ={}
for i in range(n*2):
    try:
        name=str(input()).split()
        if i<((n*2)/2):
            rubric[name[0]]=name[1]
        else:
            if str(rubric.get(name[0]))=="None":
                print("Not found")
            else:
                print('{}={}'.format(name[0],str(rubric.get(name[0]))))
    except EOFError as error:
        break
