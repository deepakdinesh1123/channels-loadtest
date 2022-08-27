from locust import HttpUser, TaskSet, between, events, task
from websocket import create_connection
import time
import random
import json

class UserBehavior(TaskSet):

    def on_start(self):
        time.sleep(10)
        self.uri = "ws://localhost:80/ws/test/" + str(random.randint(10, 20))
        self.ws = create_connection(self.uri)

    def on_stop(self):
        self.ws.close()
    
    @task(1)
    def say_hello(self):
        start_at = time.time()
        body = {"message": "hello"}
        self.ws.send(json.dumps(body))
        events.request_success.fire(
            request_type="WebSocket Sent",
            name=f"ws/test/{self.uri}",
            response_time=int((time.time()-start_at) * 1000000),
            response_length=len(body)
        )

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(5, 15)

