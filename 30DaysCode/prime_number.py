number = int(input())
for i in range(number):
    number_to_evaluate=int(input())
    not_prime=False
    if number_to_evaluate==0 or number_to_evaluate==1:
        print("Not prime")
    else:
        for j in range(2,int(number_to_evaluate**(1/2))+1):
            if number_to_evaluate%j==0:
                print("Not prime")
                not_prime=True
                break
        if not_prime==False:
            print("Prime")
