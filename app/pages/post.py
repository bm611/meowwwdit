import reflex as rx
from app.state import State
from app.components.post import post
from app.components.feed import sample_posts


def post_page():
    return rx.container(
        post(
            title=State.current_post["title"],
            content=State.current_post["content"],
            author=State.current_post["author"],
            subreddit=State.current_post["subreddit"],
            upvotes=State.current_post["upvotes"],
            comments=State.current_post["comments"],
            time_posted=State.current_post["time_posted"],
            post_id=State.current_post["post_id"],
        ),
        class_name="mt-6",
    )
