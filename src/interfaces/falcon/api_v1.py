from uuid import UUID
import falcon
import falcon.asgi

from src.domain.adapters.dto import DtoTask
from src.interactors.task.interface import IFactoryTask


class TaskAPI:
   
   def __init__(self, task: IFactoryTask) -> None:
        self._task = task
   
   async def on_get(self, req:falcon.Request, resp:falcon.Response) -> None:
        try: 
            id = UUID(req.get_param("id"))
            task = self._task.get_task(id)
            resp.media = {
                 "id": task.id,
                "title": task.title,
                "description": task.description,
                "created_at": task.created_at,
                "due_date": task.due_date,
                "completed_at": task.completed_at,
                "status": task.status,
                "priority": task.priority,
                "tags": task.tags,
            }
            resp.status = falcon.HTTP_OK
        except ValueError as e:
           raise falcon.HTTPBadRequest(description="{}".format(e))
            

   async def on_patch(self, req:falcon.Request, resp:falcon.Response) -> None:
        try:
             id = UUID(req.get_param("id"))
             body = await req.get_media()
             dto = DtoTask(
                id=id, 
                title=body.get("title"),
                description=body.get("description"),
                due_date=body.get("due_date"),
                completed_at= body.get("complete_at"),
                status=body.get("status"),
                priority=body.get("priority"),
                tags=body.get("tags"),
                created_at= body.get("created_at")
             )
             self._task.update_task(dto)
             resp.status = falcon.HTTP_NO_CONTENT
        except ValueError as e:
            raise falcon.HTTPBadRequest(description="{}".format(e))


   async def on_post(self, req:falcon.Request, resp:falcon.Response) -> None:
        try:
            body = await req.get_media()
            dto = DtoTask(
                id=None, 
                title=body.get("title"),
                description=body.get("description"),
                due_date=body.get("due_date"),
                completed_at= body.get("completed_at"),
                status=body.get("status"),
                priority=body.get("priority"),
                tags=body.get("tags"),
                created_at=None
             )
            self._task.create_task(dto)
            resp.status = falcon.HTTP_NO_CONTENT
        except ValueError as e:
            raise falcon.HTTPBadRequest(description="{}".format(e))
        
   
   async def on_get_all(self, req:falcon.Request, resp:falcon.Response) ->  None:
        try:
            resp.media = self._task.get_tasks()
            resp.status = falcon.HTTP_OK
        except ValueError as e:
            raise falcon.HTTPBadRequest(description="{}".format(e))
   
   async def on_delete(self, req:falcon.Request, resp:falcon.Response) -> None:
        try:
            id = UUID(req.get_param("id"))
            self._task.delete_task(id)
        except ValueError as e:
            raise falcon.HTTPBadRequest(description="{}".format(e))
   
        




def NewTaskAPI(router: falcon.asgi.App, task:IFactoryTask) -> falcon.asgi.App:
     t = TaskAPI(task)
     router.add_route("/tasks", t, suffix="all")
     router.add_route("/task", t)
     router.add_route("/task/{id}", t)
     return router