class TaskOutOfOrderException(Exception):
  def __init__(self, message="Current task to be executed has dependencies not yet executed"):
    super().__init__(self.message)