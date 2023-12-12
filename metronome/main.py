from conductor.model import Conductor
from auditor.model import Auditor
from critic.model import Critic
import random
import json

class Metronome:
    def __init__(self, openai_api_key, model_name="gpt-4-32k", temperature=0.9, verbose=True) -> None:
        self.openai_api_key = openai_api_key
        self.model_name = model_name
        self.temperature = temperature
        self.verbose = verbose
    
    def reformat_task_lists(self,candidate_task_lists):
        reformatted_task_lists = "\n"
        counter = 1
        for task_list in candidate_task_lists:
            reformatted_task_lists = reformatted_task_lists + "Candidate "+ str(counter) + " TaskList : \n" + json.dumps(task_list) +" \n\n"
            counter +=1
        
        return reformatted_task_lists


    def setTempo(self, objective, candidate_task_lists,mode="empirical"):
        reformatted_task_lists = self.reformat_task_lists(candidate_task_lists)
        critic = Critic(openai_api_key=self.openai_api_key)
        assessment = critic.score(objective,reformatted_task_lists,mode=mode)
        top_score_task = assessment['Critic_Scores'].index(max(assessment['Critic_Scores']))
        selected_tasklist = candidate_task_lists[top_score_task]
        return selected_tasklist

        

    def start(self, objective, examples, mode="empirical"):
        auditor = Auditor(self.openai_api_key)
        candidate_task_lists = []
        while len(candidate_task_lists)<3:
            conductor_temperature = random.uniform(0.3,1.3)
            conductor = Conductor(openai_api_key=self.openai_api_key, temperature= conductor_temperature)
            temp_task_list = conductor.run(objective,examples)
            report = auditor.audit(objective,temp_task_list)
            if report['verdict']=='Pass':
                candidate_task_lists.append(temp_task_list)
        
        return self.setTempo(objective=objective, candidate_task_lists=candidate_task_lists, mode=mode)

