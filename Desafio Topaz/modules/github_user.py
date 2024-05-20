import codecs
import requests
import os
from User import User

     
def get_user(username: str) -> User: # Dados do usuário do Github
    url = f"https://api.github.com/users/{username}"
    try:
          response = requests.get(url)
          response.raise_for_status()  
          data = response.json()
          return User(data["name"], data["url"], data["public_repos"], data["followers"], data["following"])
    except OSError as e:
          error_message = f"Erro na requisição para o usuário '{username}': {e}"

def get_user_repos(username: str) -> dict: #repositórios do usuário como chave e a URL do repositório como valor 
    user_repos_url = f"https://api.github.com/users/{username}/repos"
    try:
      response = requests.get(user_repos_url)    
      response.raise_for_status()  
      data = response.json()
      repos = {}
      
      for repo in data:
        repo_info = {"name": repo["name"], "html_url": repo["html_url"]}
        repos[repo["name"]] = repo_info
      return repos    
    except OSError as e:
          error_message = f"Erro : {e}"     

 
def user_report(user: User, repos: dict, encoding="utf-8") -> None:  # gerar o relatorio  receba os dados do usuário e seus repositórios 
    
    user = get_user(user)

    repos = {}  
    repos = get_user_repos(user)
           
    nomearquivo = f"{user}.txt" 
    try:
      if repos is None or len(repos) == 0:
       with open(nomearquivo, "w", encoding="utf-8") as f:
        f.write(f"Usuário não publicou nenhum repositório público.")
      else:  
       with open(nomearquivo, "w", encoding="utf-8") as f:
        f.write(str(user))  
        f.write("\nRepositórios:\n")                
        for repo_name, repo_info in repos.items():      
         f.write(f"\t- {repo_name} ({repo_info['html_url']})\n")            
    except OSError as e:
        error_message = f"Erro : {e}"

              
 
      
     


