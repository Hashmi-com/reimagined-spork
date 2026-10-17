daily_task = 4
origanal_task = daily_task
print(f"You have:{daily_task} tasks to finish today")
completed = 0
current = 1
while current <= daily_task:
    if current == 1:
        Next = "Make your bed"
    elif current == 2:
        Next = "Feed the pet"
    elif current == 3:
        Next = "Brush your teeth"
    else:
        Next = "Do your homework"
    answer = input(f"Have you completed {Next}?")
    if answer == "Yes":
        completed = completed + 1
        current = current + 1
        print("Good job task completed")
    else:
        print("Okay, finish and check again")
    print(f"Tasks remaining {daily_task - completed}")
print("All Tasks completed\nGreat work finishing your entire checklist today")