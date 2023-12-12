from storage.vector_db import initialize_and_search
from conductor.model import Conductor
from auditor.model import Auditor
import json

def get_examples(input_query,top_k = 5, mode="dynamic"):
    
    conductor, auditor = initialize_system()
    results = initialize_and_search(input_query,top_k=top_k)

    return process_results(results,conductor,auditor,mode)

def process_results(results,conductor,auditor,mode):
    objectives = []
    task_lists = []
    reformatted_examples= "\n Examples: "
    for closest_objective, task_list in results:
        if mode == "static":
            objectives.append(closest_objective)
            task_lists.append(task_list)
            reformatted_examples = reformatted_examples + "\n Objective: "+closest_objective+"\n TaskList: "+task_list+"\n"
        elif mode == "dynamic":
            try:
                task_list, report  = dynamic_processing(closest_objective,conductor,auditor)
            except Exception as e:
                print("Exception, skipping this example")
                continue
            if (report['verdict']=='Pass'):
                objectives.append(closest_objective)
                task_lists.append(task_list)
                reformatted_examples = reformatted_examples + "\n Objective: "+closest_objective+"\n TaskList: "+task_list+"\n"
    return objectives, task_lists, reformatted_examples


def dynamic_processing(objective,conductor,auditor):
    task_list = json.dumps(conductor.run(objective=objective))
    report = auditor.audit(objective = objective, task_list= task_list)
    return task_list, report

def initialize_system(openai_api_key="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"):
    conductor = Conductor(openai_api_key,verbose=False)
    auditor = Auditor(openai_api_key)
    return conductor, auditor

