from typing import Any
import satelite
from gitlab import Gitlab as gitlab

class gitlabsat(satelite):

	

	def __init__(self) -> None:
		super().__init__()

	def init_con(self,url:str) -> Any:
		self.conection = gitlab(url)
		pass