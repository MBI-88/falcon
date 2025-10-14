from src.domain.entities.task import Task
import os

from falcon import MEDIA_JSON 
import config.config 
import falcon.asgi

from src.interactors.task.factory import NewFactoryTask
from src.interfaces.falcon.api_v1 import NewTaskAPI
from src.interfaces.repository.connections import NewDbConnection
from src.interfaces.repository.db_config import DbConfig


app = falcon.asgi.App(
        cors_enable=True,
        media_type=falcon.MEDIA_JSON,
)

db = DbConfig()
conn = db.get_connection()
   
if not os.path.exists(config.config.DATABASE):
     print("Database not found. Creating...")
     try:
          db.create_table(Task)
     except ValueError as e:
          print(e)
          exit()
           
     print("Database created successfult")

   

repo = NewDbConnection(conn)
task = NewFactoryTask(repo)
app = NewTaskAPI(app, task)