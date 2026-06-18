from datetime import date, timedelta
def add_to_list(tasks,task_words):
    today = date.today()
    new_task = {}
    task_text = " ".join(task_words)
    new_task["task"] = task_text
    new_task["creation_date"] = today.isoformat()
    new_task["completion_date"] = None
    new_task["done"] = False
    tasks.append(new_task)

def show(tasks):
    print("------ TASKS ------\n")
    for i,item in enumerate(tasks,start=1):
            if item["done"]:
                print(f'{i} :[✔ ]: {item["task"]}')
            else:
                print(f'{i} :[  ]: {item["task"]}')

def mark_done(tasks,task_no):
    try:
        z = date.today()
        t = tasks[task_no-1]
        t["completion_date"] = z.isoformat()
        t["done"] = True
    except (IndexError,ValueError):
        print(f"task no {task_no} does not exist")
        
def streak(tasks):
    a=set()
    for i in tasks:
        if i["done"]:
            d=date.fromisoformat(i["completion_date"])
            a.add(d)
    s=0
    z = date.today()
    if z in a:
        s=1
    z = z-timedelta(days=1)
    while z in a:
        s+=1
        z = z-timedelta(days=1)
    return s

def search(tasks,word):
    matches=0
    word = word.lower()
    for i,item in enumerate(tasks,start=1):
        task_str = item["task"].lower()
        if word in task_str:
            matches+=1
            if item["done"]:
                print(f'{i} :[✔ ]: {item["task"]}')
            else:
                print(f'{i} :[  ]: {item["task"]}')
    if matches == 0:
        print("No matching tasks found")

def stats(tasks):
    total = 0
    completed_no = 0
    for i in tasks:
        total+=1
        if i["done"]:
            completed_no+=1
    pending_no = total-completed_no
    rate = round((completed_no/total)*100,2) if total > 0 else 0
    print("----- STATS -----\n")
    print(f"Total tasks      : {total}")
    print(f"Completed        : {completed_no}")
    print(f"Pending          : {pending_no}")
    print(f"Completion rate  : {rate}%")
    print(f"Current streak   : {streak(tasks)}")

def remove(tasks,task_no):
    try:   
        tasks.pop(task_no-1)

    except IndexError:
        print("the typed task no does not exist ")



