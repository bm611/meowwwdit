import reflex as rx
from app.components.feed import sample_posts


class State(rx.State):
    @rx.var
    def get_post_id(self) -> str:
        return self.router.page.params.get("post_id", "")

    current_post: dict[str, str | int] = {}

    def set_current_post(self):
        get_post = next(
            (post for post in sample_posts if post["post_id"] == self.get_post_id), {}
        )
        self.current_post = {
            "post_id": get_post["post_id"],
            "title": get_post["title"],
            "content": get_post["content"],
            "author": get_post["author"],
            "subreddit": get_post["subreddit"],
            "upvotes": get_post["upvotes"],
            "comments": get_post["comments"],
            "time_posted": get_post["time_posted"],
        }
