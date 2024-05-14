queue = []
def enqueue():
    item = input("Enter the item : ")
    queue.append(item)
    print(item,"is inserted to queue ")
def dequeue():
    if not queue:
        print("Underflow(empty Queue) ")
    else:
        item = queue.pop(0)
        print("Deleted item = ",item)
def display():
    print(queue)

while True:
    print("Select the operation 1.Insert 2.Delete 3.Display 4.Quit \n")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter Correct Operation ")