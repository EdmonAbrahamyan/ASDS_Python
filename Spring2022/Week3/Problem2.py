class Server:
    __shared_state = dict()  

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.resource = "free"
        
class API:
    
    def __init__(self):
        self.server = Server()
    
    def request_server(self, client):
        if self.server.resource == 'free':
            self.server.resource = 'busy'
            client.server = self.server
        else:
            client.server = 'server is busy'
        
    def free_server(self, user):
        self.server.resource = 'free'
        user.server = 'server is free'

class Client:
    
    def __init__(self):
        self.server = 'server is free'


client = Client()
api = API()
api.request_server(client)

print(client.server.resource)


other_client = Client()
api.request_server(other_client)
print(other_client.server)

