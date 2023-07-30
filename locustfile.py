from locust import FastHttpUser, task, between

class IndexPageUser(FastHttpUser):
    wait_time = between(1, 2.5)

    @task
    def index_page(self):
        self.client.get("/")

class AboutPageUser(FastHttpUser):
    @task
    def about_page(self):
        self.client.get("/about-us")