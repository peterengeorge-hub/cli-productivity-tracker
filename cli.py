import argparse

from storage import load_tasks,save_tasks
from logic import (add_to_list,
                   show,
                   mark_done,
                   streak,
                   search,
                   stats,
                   remove)

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command")
add_parser = subparser.add_parser("add")
add_parser.add_argument("task",nargs="+")
list_parser = subparser.add_parser("list")
mark_parser = subparser.add_parser("mark_done")
mark_parser.add_argument("index",type=int)
streak_parser = subparser.add_parser("streak")
search_parser = subparser.add_parser("search")
search_parser.add_argument("keyword")
stat_parser = subparser.add_parser("stats")
delete_parser = subparser.add_parser("delete")
delete_parser.add_argument("task_no",type=int)
args=parser.parse_args()
if args.command is None:
    parser.print_help()
    exit()

tasks = load_tasks()
if args.command == "add":
    add_to_list(tasks,args.task)
    save_tasks(tasks)

elif args.command == "list":
    show(tasks)

elif args.command == "mark_done":
    mark_done(tasks,args.index)
    save_tasks(tasks)

elif args.command == "streak":
    print(f"the current streak is {streak(tasks)}")

elif args.command == "search":
    search(tasks,args.keyword)

elif args.command == "stats":
    stats(tasks)

elif args.command == "delete":
    remove(tasks,args.task_no)
    save_tasks(tasks)
    print("deleted")