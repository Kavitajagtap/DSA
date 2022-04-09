class QueueImp:
    def __init__(self,size):
        self.__capacity = size
        self.__list = []
        self.__front = -1
        self.__rear = -1

    def isfull(self):
        return self.__rear ==self.__capacity-1 and self.__front == 0

    def isEmpty(self):
        return  self.__rear ==-1 and self.__front == -1

    def enqueue(self):
        if self.isfull():
            print("Queue is Full..")
        else:
            data = int(input("Enter an element: "))
            if len(self.__list) == 0:
                self.__list.append(data)
                self.__front  += 1
            else:
                self.__list.append(data)
            self.__rear +=1
            print(str(data) + " is Enqueued successfully..")

    def dequeue(self):
      if self.isEmpty():
          print("Queue is Empty..")

      elif self.__front == self.__rear:
          print(self.__list.pop(), " is Dequeued successfully..")
          self.__front = -1
          self.__rear = -1
      else:
          print(self.__list.pop(0)," is Dequeued successfully..")
          self.__front += 1
    
    def get_queue(self):
        return self.__list

print("-------------------------------Welcome to Queue--------------------------")
size = int(input("Give size of the queue: "))    
queue = QueueImp(size)

while True:
    n = int(input("Which operation you want to perform..?\n1. Enqueue\n2. Dequeue\n3. isFull?\n4. isEmpty?\n5. Print Queue\n"))
    if n == 1:
        queue.enqueue()
    elif n == 2:
        queue.dequeue()
    elif n == 3:
        print(queue.isfull())
    elif n == 4:
        print(queue.isEmpty())
    elif n == 5:
        print(f"Your queue is --> {queue.get_queue()}")
    else:
        print("Invalid Input")
'''
---------------------- OUtput ------------------------------------

-------------------------------Welcome to Queue--------------------------
Give size of the queue: 4
Which operation you want to perform..?
1. Enqueue
2. Dequeue
3. isFull?
4. isEmpty?
5. Print Queue
6. Exit
1
Enter an element: 12
12 is Enqueued successfully..
Which operation you want to perform..?
1. Enqueue
2. Dequeue
3. isFull?
4. isEmpty?
5. Print Queue
6. Exit
1
Enter an element: 34
34 is Enqueued successfully..
Which operation you want to perform..?
1. Enqueue
2. Dequeue
3. isFull?
4. isEmpty?
5. Print Queue
6. Exit
1
Enter an element: 56
56 is Enqueued successfully..
Which operation you want to perform..?
1. Enqueue
2. Dequeue
3. isFull?
4. isEmpty?
5. Print Queue
6. Exit
1
Enter an element: 78
78 is Enqueued successfully..
Which operation you want to perform..?
1. Enqueue
2. Dequeue
3. isFull?
4. isEmpty?
5. Print Queue
6. Exit
1
Queue is Full..
Which operation you want to perform..?
1. Enqueue
2. Dequeue
3. isFull?
4. isEmpty?
5. Print Queue
6. Exit
2
12  is Dequeued successfully..
Which operation you want to perform..?
1. Enqueue
2. Dequeue
3. isFull?
4. isEmpty?
5. Print Queue
6. Exit
2
34  is Dequeued successfully..
Which operation you want to perform..?
1. Enqueue
2. Dequeue
3. isFull?
4. isEmpty?
5. Print Queue
6. Exit
3
False
Which operation you want to perform..?
1. Enqueue
2. Dequeue
3. isFull?
4. isEmpty?
5. Print Queue
6. Exit
4
False
Which operation you want to perform..?
1. Enqueue
2. Dequeue
3. isFull?
4. isEmpty?
5. Print Queue
6. Exit
5
Your queue is --> [56, 78]
Which operation you want to perform..?
1. Enqueue
2. Dequeue
3. isFull?
4. isEmpty?
5. Print Queue
6. Exit
6
Queue Implementation Ended

G:\Advance_python>

'''
