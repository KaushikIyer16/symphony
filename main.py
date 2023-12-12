from conductor.model import Conductor
from orchestra.main import Orchestra
from sheet_music.main import get_examples
from registry import get_registry

#conductor = Conductor(openai_api_key="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")
#objective = "I have 2 cauliflowers and 1 onion left, what can I cook?"
#tasks = conductor.run(objective)
objective = "I want a list of 35 CPOs from USA in software industry"


static_objectives, static_task_lists, static_examples = get_examples(objective,mode="static",top_k=2)
print("static no. of examples = ", len(static_task_lists))
conductor = Conductor(openai_api_key="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")
static_tasks = conductor.run(objective,static_examples)
print(static_tasks)


dynamic_objectives, dynamic_task_lists, dynamic_examples = get_examples(objective,mode="dynamic",top_k=2)

print("dynamic = ", len(dynamic_task_lists))
dynamic_tasks = conductor.run(objective,dynamic_examples)
print(dynamic_tasks)




#print(tasks)
#orchestra = Orchestra(registry=get_registry())
#print(orchestra.run(objective, tasks))
