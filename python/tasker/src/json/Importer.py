import json


class Importer:

    def __init__(self):
        self.tasks = []

    def read_tasks(self):
        with open('taski.json', encoding='utf-8') as f:
            self.tasks = json.load(f)

    def get_tasks(self):
        return self.tasks
