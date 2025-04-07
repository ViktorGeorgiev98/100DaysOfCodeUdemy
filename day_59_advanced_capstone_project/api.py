import requests


class API:
    def __init__(self):
        self.base_url = "https://api.npoint.io/674f5423f73deab1e9a7"
        self.post_url = ""

    def get_posts(self):
        response = requests.get(self.base_url)
        response.raise_for_status()
        return response.json()

    def get_post_by_id(self, post_id):
        posts = self.get_posts()
        for post in posts:
            if int(post["id"]) == int(post_id):
                return post
        return None
