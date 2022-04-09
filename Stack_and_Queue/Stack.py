class stackImpl:
    def __init__(self,size):
        self.__capacity = size
        self.__list = []

    def isFull(self):
        if len(self.__list) < self.__capacity:
            return True
        return False

    def isEmpty(self):
        if len(self.__list) == 0:
            return True
        return False

    def push(self,value):
        if self.isFull():
            self.__list.append(value)
            print(value," is inserted successfully..")
        else:
            print("stack is Full..")

    def pop(self):
       if self.isEmpty():
           print("Stack is Empty..")
       else:
           print(self.__list.pop()," is poped successfully..") 

    def get_stack(self):
        return self.__list

print("-------------------Welcome to Stack Implemetation-------------------------------")

size = int(input("Enter the size of the stack "))
stack = stackImpl(size)
while True:
    n = int(input("Which operation you want to perform..?\n1. Push\n2. Pop\n3. Print Stack\n4. Exit\n"))
    if n == 1:
        stack.push(int(input("Enter element: ")))
    elif n == 2:
        stack.pop()
    elif n == 3:
        print("Your stack --> ",stack.get_stack())
    elif n == 4:
        print("Implementation Ended..")
        break
    else:
        print("Invalid Input")
        
'''
-------------------- Output ---------------------------

-------------------Welcome to Stack Implemetation-------------------------------
Enter the size of the stack 4
Which operation you want to perform..?
1. Push
2. Pop
3. Print Stack
4. Exit
1
Enter element: 12
12  is inserted successfully..        
Which operation you want to perform..?
1. Push
2. Pop
3. Print Stack
4. Exit
1
Enter element: 23
23  is inserted successfully..
Which operation you want to perform..?
1. Push
2. Pop
3. Print Stack
4. Exit
1
Enter element: 56
56  is inserted successfully..
Which operation you want to perform..?
1. Push
2. Pop
3. Print Stack
4. Exit
1
Enter element: 78
78  is inserted successfully..
Which operation you want to perform..?
1. Push
2. Pop
3. Print Stack
4. Exit
1
Enter element: 56
stack is Full..
Which operation you want to perform..?
1. Push
2. Pop
3. Print Stack
4. Exit
2
78  is poped successfully..
Which operation you want to perform..?
1. Push
2. Pop
3. Print Stack
4. Exit
2
56  is poped successfully..
Which operation you want to perform..?
1. Push
2. Pop
3. Print Stack
4. Exit
3
Your stack -->  [12, 23]
Which operation you want to perform..?
1. Push
2. Pop
3. Print Stack
4. Exit
4
Implementation Ended..

G:\Advance_python>

'''
