from conductor.model import Conductor
from orchestra.main import Orchestra
from registry import get_registry

conductor = Conductor(openai_api_key="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")
objective = "I have 2 cauliflowers and 1 onion left, what can I cook?"
tasks = conductor.run(objective)

orchestra = Orchestra(registry=get_registry())
print(orchestra.run(objective, tasks))