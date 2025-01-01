"""
def abc():
    for i in range(6):
        for j in range(i):
            print(j, end=" ")
        print("\n")
abc() 


def abc():
    for i in range(6):
        for j in range(6-i,0,-1):
            print(j,end=" ")
        print("\n")
abc()

def compute():  #Write a python program that compute the number divisible by 5 and even from 10-100.
    for i in range(10,101):
        if i%5==0:
           if i%2==0:
               print(i)
compute() 

def vowels():
    list = ['a','i','o','u','e']
    string = "Wondeetesfa "
    count=0
    for i in string: 
        if i in list:
            count +=1
    print(count)
vowels()        

def display():
    number =int(input("Enter a number : ")) 
    even_sum=0
    od_sum=0
    for i in range(number+1):
        if i%2==0:
            even_sum +=i
        else:
            od_sum +=i
    if even_sum > od_sum:
        print("Even is larger")
    else:
        print("Odd is larger")
    
display()    

def abc():
    count =0
    num =int(input("Enter the number : "))
    while num !=0:
         num=num//10
         count +=1
    print(f"The number of digit is {count}.")
abc() """
    

 

