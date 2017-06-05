from locust import HttpLocust, TaskSet, task
from random import choice
from string import ascii_uppercase


class UserBehavior(TaskSet):

    @task(1)
    def profile(self):
        self.client.get("/messages/5931d8b783a93400090ef33d")

class PosterBehavior(TaskSet):

    @task(1)
    def profile(self):
        word = ''.join(choice(ascii_uppercase) for i in range(100))
        headers = {'content-type': 'application/json'}
        self.client.post("/messages", None, {"message": word})

class WebsiteUser(HttpLocust):
    weight = 10
    task_set = UserBehavior
    min_wait = 1
    max_wait = 1000

class WebsitePoster(HttpLocust):
    weight = 1
    task_set = PosterBehavior
    min_wait = 500
    max_wait = 3000
