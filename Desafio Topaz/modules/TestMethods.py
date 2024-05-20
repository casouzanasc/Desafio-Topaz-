import re
import unittest
import uuid 
from github_user import User, get_user, get_user_repos, user_report 
import os
import codecs

  

class TestMethods(unittest.TestCase):

    def test_user_class_has_minimal_parameters(self):
         parameters = [
            'name', 'url', 'public_repos', 'followers', 'following'
        ]
         user = User("githubuser", "https://api.github.com/users/githubuser", 4, 11, 0)
         for param in parameters:
          self.assertTrue(hasattr(user, param))

    
    def test_user_report_with_user_without_repos(self):
         
         user = get_user("githubuser")                                   
         repos = get_user_repos("githubuser")   

            
         if repos is None or len(repos) == 0:
             with open("githubuser.txt", "w", encoding="utf-8") as f:
              
              f.write(f"Usuário não publicou nenhum repositório público.")
         else:  
             with open("githubuser.txt", "w", encoding="utf-8") as f:
              f.write(str(user))  
              f.write("\nRepositórios:\n")                
              for repo_name, repo_info in repos.items():      
               f.write(f"\t- {repo_name} ({repo_info['html_url']})\n")             
 
            
if __name__ == "__main__":
   # unittest.main()  

    username =  "maria"
    nomearquivo = f"{username}.txt"
    user = get_user(username)
    print(user)    
    
    username =  "roberto"
    nomearquivo = f"{username}.txt"
    user = get_user(username)
    print(user)    
    
    username =  "camia"
    nomearquivo = f"{username}.txt"
    user = get_user(username)
    print(user)    
