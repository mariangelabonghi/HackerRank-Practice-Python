# Enter your code here. Read input from STDIN. Print output to STDOUT
ret_date, due_date =input().split(' '),input().split(' ')
for i in range(3): ret_date[i]=int(ret_date[i])
for i in range(3): due_date[i]=int(due_date[i])
result=0
if ret_date[2] > due_date[2]:
    result=10000
else:
    if ret_date[2] == due_date[2]:
        if ret_date[1]>  due_date[1]:
            result=500*((ret_date[1])-(due_date[1]))
        else:
            if ret_date[1] == due_date[1]:
                if  ret_date[0] > due_date[0]:
                    result=15*((ret_date[0])-(due_date[0]))
                else:
                    result=0
print(str(result))
