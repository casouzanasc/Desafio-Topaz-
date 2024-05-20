class User:
    def __init__(self, name: str, url: str, public_repos: int, followers: int, following: int):
        self.name = name
        self.url = url
        self.public_repos = public_repos
        self.followers = followers
        self.following = following

    def __str__(self):
        return f"""
        Nome: {self.name}
        Perfil: {self.url}
        Número de repositórios publicos: {self.public_repos}
        Número de seguidores: {self.followers}
        Número de usuários seguidos: {self.following}
        """   
