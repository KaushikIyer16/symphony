from collections import defaultdict, deque
from .task_out_of_order_exception import TaskOutOfOrderException

class Orchestra:
  def __init__(self, registry):
    self.registry: defaultdict = registry
    self.output = {}
  
  def get_dependency_graph(self, tasks):
    dependency_graph = defaultdict(set)
    in_deg = defaultdict(int)
    for task in tasks:
      if len(task["dependent_task_ids"]) == 0:
        in_deg[task["id"]] = 0
      for dependency in task["dependent_task_ids"]:
        in_deg[task["id"]] += 1
        dependency_graph[dependency].add(task["id"])
    return dependency_graph, in_deg

  def execute_task(self, objective, task_id):
    task_to_be_completed = self.tasks[task_id]
    task_objective = task_to_be_completed["task"]
    tool = task_to_be_completed["tool"]
    dependent_tasks = set(task_to_be_completed["dependent_task_ids"])
    dependency_info = []
    for dep in dependent_tasks:
      if dep not in self.output:
        raise TaskOutOfOrderException()
      dependency_info.append(self.output[dep])
    self.output[task_id] = self.registry[tool].run(objective, task_objective, dependency_info)

  def format_tasks(self, tasks):
    formatted_map = {}
    for task in tasks:
      formatted_map[task["id"]] = task
    return formatted_map

  def run(self, objective, tasks):
    self.tasks = self.format_tasks(tasks)
    print("1 -->", self.tasks)
    dependency_graph, in_deg = self.get_dependency_graph(tasks)
    zeroes = deque([node for node, degree in in_deg.items() if degree == 0])
    while len(zeroes) > 0:
      task_id = zeroes.popleft()
      print("starting task", task_id)
      self.execute_task(objective, task_id)
      print("complete task", task_id)
      for node in dependency_graph[task_id]:
        in_deg[node] -= 1
        if in_deg[node] == 0:
          zeroes.append(node)
    return self.output
