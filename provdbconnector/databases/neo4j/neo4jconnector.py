from provdbconnector.databases.baseconnector import BaseConnector

class Neo4jConnector(BaseConnector):
    def __init__(self,*args):
        super(Neo4jConnector, self).__init__()
        pass

    def connect(self):
        raise NotImplementedError