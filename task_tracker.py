# CLI task tracker
# Commands: add, list, done <n>, filter <priority>, stats, quit

tasks =[]

def add(tasks, priority, task, deadline):
    if priority == 1:
        priority = "низкий"
    elif priority == 2:
        priority = "средний"
    elif priority == 3:
        priority = "высокий"
    tasks.append([task, priority, deadline, False])
    return tasks

def show_tasks(tasks):
    for i in range(len(tasks)):
        is_ready = "○"
        if tasks[i][3] == True:
            is_ready = "✓"
        task = tasks[i]
        print(f"{i+1}. задача: {task[0]} приоритет: {task[1]} дата: {task[2]} {is_ready}")

def done(tasks, number):
    n = 0
    for task in tasks:
        n +=1
        if n == number:
            task[3] = True
            print(task)

def filter_tasks(tasks, priority):
    for task in tasks:
        if task[1] == priority:
            print(task)

def stats(tasks):
    n = 0
    left=0
    finished = 0
    for task in tasks:
        if task[3] == True:
            finished += 1
        else:
            left += 1
        n += 1
    if n == 0:
        print("Задач нет.")
        return
    sum = finished / n * 100
    print(f"всего задач:{n}, выполнено:{finished}, осталось:{left}, % выполнения:{sum}")


while True:
    command  = input("Введите команду: 1.add 2.list 3.stats 4.filter 5.done 6.quit").split()
    tap = command[0]
    if tap == "add":
        task = input("Введите название: ")
        priority = int(input("приоритет 1–3:"))
        deadline = input("Введите дату этой задачи:")
        add(tasks=tasks, task=task, priority=priority, deadline=deadline)
    elif tap == "list":
        show_tasks(tasks=tasks)
    elif tap == "stats":
        stats(tasks=tasks)
    elif tap == "filter":
        filter_tasks(tasks =tasks, priority = command[1])
    elif tap == "done":
        done(tasks=tasks, number=int(command[1]))
    elif tap == "quit":
        break



