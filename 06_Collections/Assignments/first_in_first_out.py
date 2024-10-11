#!/usr/bin/python3

"""
"""


my_list = []
while True:
    
    action = input("Enter which operation you want to perform 'push' or 'pop': ").lower().strip()
    
    if action not in ("push","pop","exit"):
        print("Invalid action, Enter push or pop")
    else:
    
        if action == "push":
            val = int(input("Enter the value you want to add"))
            my_list.append(val)
        
        elif action == "pop" and len(my_list) == 0:
            print("Stack is already empty and you can't perform pop operation")
        
        elif action == "exit":
            break
    
        else:
            my_list.pop(0)
            print(f"size of stack is:", len(my_list))
            print(f"{my_list =}")

