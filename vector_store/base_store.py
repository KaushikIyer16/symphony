from abc import ABC, abstractmethod

class BaseStore(ABC):
  def __init__(self, credentials) -> None:
    self.credentials = credentials
  
  @abstractmethod
  def find_top_x(self, vector, x, **kwargs):
    pass