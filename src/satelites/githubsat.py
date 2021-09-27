from typing import Any, AsyncContextManager
import satelite
from github import Github as github

class githubsat(satelite):
	repo : str = None
	acces_token : str = None

	def __init__(self) -> None:
		super().__init__()

	def init_con(self, *args:list):
		if args.count != 0:
			token = args[0]
			repo = args[1]
		if token is None:
			self.acces_token = self.get_acces_token()
		self.conection = github(self.acces_token)
		if repo is not None:
			self.set_repo(repo)
		return self

	def set_repo(self, repo:str):
		try:
			self.repo = self.conection.get_repo(repo)
			self.issues = self.repo.get_issues(state='open')
		except:
			self.repo = None
			raise Exception("No se ha podido acceder al respositorio.", repo)
		return self
	
	def get_acces_token(self, token:str = None):
		if token is None:
			toke = "DEFAULT_TOKEN"
		if token is not None:
			self.acces_token = token
		return self.acces_token

	