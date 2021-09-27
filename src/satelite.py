from _typeshed import Self
from abc import abstractmethod
from typing import Any

class satelite:
	_conection: Any = None
	_type: str = "BASE"
	_issue_list: list = None

	# no me acuerdo si los valores base se ponian en el constructor o en la definicion de la clase... mucho .net
	def __init__(self) -> None:
		self._conection = None
		self._type = "BASE"
		pass

	@property
	def type(self) -> str:
		return self._type
		pass

	@type.setter
	def type(self,type:str) -> None:
		self._type = type
		return self

	@property.getter
	def conection(self) -> str:
		return self._conection
		pass

	@property
	def issues(self) -> list:
		return self._issue_list
	
	@issues.setter
	def issues(self, issues: list):
		self._issue_list = issues
		return self

	@abstractmethod
	def init_con(self,*args:list) -> Any:
		pass

	@classmethod
	def cerate_sat(type: str, *args:list) -> satelite:
		sat : satelite = None
		try:
			sat = eval(f"satelites.{type}.__init__(None)")
			sat._conection = sat.init_con(args)
		except Exception as e:
			raise Exception("No se ha podido invocar al satélite.",type)
		return sat
	pass