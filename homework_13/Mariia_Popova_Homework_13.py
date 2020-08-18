"""
Написать класс, который позволит сохранить список дел, отмечать сделанное и показывать то, что нужно сделать.

Хранить список дел в json файле
При запуске программы должна появится меню с вариантами действий: добавить в список, вывести весь список, вывести
список не сделанных дел, отметить как сделаное
"""

import json
import datetime


class Item:
    def __init__(self, done, info, last_updated):
        self.done = done
        self.info = info
        self.last_updated = datetime.datetime.now().replace(microsecond=0).isoformat()

    def as_dict(self):
        return {
            'done': self.done,
            'info': self.info,
            'last_updated': str(self.last_updated),
        }

    def __repr__(self):
        return self.info


class TodoList:
    def __init__(self, name, owner, dead_line):
        self.name = name
        self.owner = owner
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(f'{self.name}.json', 'r') as file:
                data = json.load(file)
                tasks = []
                for item in data:
                    tasks.append(Item(item['done'], item['info'], item['last_updated']))
                return tasks
        except FileNotFoundError:
            return []

    @property
    def tasks_list(self):
        tasks = ''
        for index, item in enumerate(self.tasks):
            tasks += f'\n {index}\t {item.done}\t {item.info}\t {item.last_updated}'
        return tasks

    @property
    def not_ready_tasks(self):
        tasks = ''
        for item in self.tasks:
            if not item.done:
                tasks += (f'\n {item.done}\t {item.info}\t {item.last_updated}')
        return tasks

    def add_task(self, task):
        self.tasks.append(task)

    def check_done_task(self, index):
        try:
            self.tasks[index].done = True
        except Exception:
            return False

    def to_json(self):
        with open(f'{self.name}.json', 'w') as file:
            tasks = []
            for task in self.tasks:
                tasks.append(task.as_dict())
            json.dump(tasks, file, indent=4)


def init_todo_list():
    list_name = input('list_name ')
    owner = input('owner ')
    return TodoList(list_name, owner, None)


def main():
    todo_list = init_todo_list()
    try:
        while True:
            action = input('Action with list ')
            if action == 'Add_task':
                done = input('1 or 0 ')
                if done not in {'1', '0'}:
                    continue
                done = bool(int(done))
                info = input('Some_info ')
                todo_list.add_task(Item(done, info, None))
            elif action == 'Show_list_of_all_tasks':
                if not todo_list.tasks_list:
                    print("You don't have any tasks")
                    continue
                print(todo_list.tasks_list)
            elif action == 'Show_list_of_not_ready_tasks':
                if not todo_list.not_ready_tasks:
                    print("You have done all tasks")
                    continue
                print(todo_list.not_ready_tasks)
            elif action == 'Check_done_task':
                index = int(input('index '))
                if todo_list.check_done_task(index) == False:
                    print("You don't have task with such index")
                    continue
                todo_list.check_done_task(index)
            elif action == 'exit':
                todo_list.to_json()
                return
    except Exception:
        todo_list.to_json()


if __name__ == '__main__':
    main()
