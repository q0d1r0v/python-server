# imports
from src.modules.Index.index import IndexModule
from src.modules.Users.index import GetUsers
from src.modules.NotFound.index import NotFoundRoute

# router
def router(self):
    if self.path == '/':
        IndexModule(self)
    elif self.path == '/users/':
        GetUsers(self)
    else: 
        NotFoundRoute(self)
