from locust import HttpUser, task, between

class ReqResUser(HttpUser):
    # 每個使用者的等待時間 (隨機 1~3 秒)
    wait_time = between(1, 3)

    @task(2)
    def get_users(self):
        """模擬 GET 請求：取得使用者列表"""
        self.client.get("/api/users?page=2")

    @task(1)
    def create_user(self):
        """模擬 POST 請求：建立新使用者"""
        self.client.post("/api/users", json={
            "name": "晨亮",
            "job": "QA Engineer"
        })
