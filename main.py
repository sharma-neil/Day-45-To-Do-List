import time, os

print("🌟Life Organizer🌟")

#function to add tasks to the list
def add_tasks():
  task = input("What is the task? > ")
  due_date = input("When is it due by? > ")
  priority = input("What is the priority? > ")
  return [task, due_date, priority]

#function that lets you view the list
def view_tasks(tasks):
  view_choice = input("Do you want to view all or view by priority? > ")
  if view_choice == "all":
    for row in tasks:
      print(row)
  elif view_choice == "priority":
    priority_choice = input("What priority do you want to view? > ")
    for row in tasks:
      if priority_choice in row:
        print(row)

#functions that removes a task and creates a new one
def edit_tasks(tasks):
  task = input("Name of task trying to edit? > ")
  for row in tasks:
    if task in row:
      tasks.remove(row)
      new_task = add_tasks()
      tasks.append(new_task)
      print("Task edited successfully.")
      return tasks
    else:
      print("Tasks not found in the list.")
      return tasks

#function to remove tasks
def remove_tasks(tasks):
  task = input("Which task are you trying to remove? > ")
  for row in tasks:
    if task in row:
      tasks.remove(row)
      print(f"{task} has been removed from the list.")
      return tasks
    else:
      print(f"{task} not found in the list.")


#Main Menu prompts which calls the functions listed above
task_list = []

while True:
  menu_choice = input("Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > ")
  if menu_choice == "add":
    task_list.append(add_tasks())
  elif menu_choice == "view":
    view_tasks(task_list)
  elif menu_choice == "edit":
    task_list = edit_tasks(task_list)
  elif menu_choice == "remove":
    task_list = remove_tasks(task_list)
  else:
    print("Invalid choice. Please try again.")

  time.sleep(1)
  os.system("clear")