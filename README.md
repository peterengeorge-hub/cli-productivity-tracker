# CLI PRODUCTIVITY TRACKER
A simple command-line productivity tracker written in Python.
I built this to practice working with files, CLI arguments (argparse), and basic data handling.

## What it does
- Add tasks
- List tasks
- Mark tasks as done
- Delete tasks
- Search tasks
- Show stats (completion rate, pending, etc.)
- Track daily streak

Tasks are stored locally in a tasks.json file.

## Commands

Run everything using:

python cli.py <command>
### Available commands
- add "task name" → Adds a new task
- list → Shows all tasks
- mark_done <task_no> → Marks a task as completed
- delete <task_no> → Deletes a task
- search <keyword> → Finds tasks containing a word
- stats → Shows task statistics
- streak → Shows current completion streak


## Setup

Clone the repo:

git clone https://github.com/peterengeorge-hub/cli-productivity-tracker.git

cd cli-productivity-tracker

No extra dependencies needed — just Python.