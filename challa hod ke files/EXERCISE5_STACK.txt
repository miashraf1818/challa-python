stack = []
def push():
    if len(stack) == n:
        print("Overflow(stack is full) ")
    else:
        item = int(input('Enter Item to Push '))
        stack.append(item)
        print(stack)
def pop():
    if not stack:
        print("Underflow(empty stack) ")
    else:
        item = stack.pop()
        print("Popped element = ",item)
        print(stack)
n = int(input("Enter Stack Limit "))
while True:
    print(" Select the operation 1.Push 2.Pop 3.Quit ")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Enter Correct Operation ")
