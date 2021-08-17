import pymongo
import project
from bson import ObjectId

class DBInterface:
    def __init__(self, db_connection_string):
        self.client = pymongo.MongoClient(db_connection_string, tls=True, tlsAllowInvalidCertificates=True)
        self.projects_coll = self.client.db["projects"]

    def insert_project(self, project):
        self.projects_coll.insert_one(project.get_json())
    
    def remove_project(self, project_id):
        self.projects_coll.delete_one({"_id" : project_id})

    def update_project(self, project):
        self.projects_coll.replace_one({"_id" : project.id}, project.get_json())
        
    def get_projects(self):

        projects = []
        for document in self.projects_coll.find():
            projects.append(project.Project.from_json(document))

        return projects
    
    def get_project(self, id):
        project_data = self.projects_coll.find_one({"_id" : ObjectId(id)})

        retrieved = project.Project.from_json(project_data)
        return retrieved