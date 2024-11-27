import reflex as rx
from app.state import State
from app.components.post import post
from app.components.feed import sample_posts


def comment_box(author: str, content: str, time_posted: str):
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.avatar(name=author, size="sm"),
                rx.text(author, class_name="font-medium text-gray-900"),
                rx.text(time_posted, class_name="text-sm text-gray-500"),
                spacing="3",
                align_items="center",
            ),
            rx.text(content, class_name="text-gray-600 mt-2"),
            rx.hstack(
                rx.button(
                    rx.icon("arrow-up", size=16),
                    variant="ghost",
                    class_name="text-gray-400 hover:text-blue-500",
                ),
                rx.text("0", class_name="text-sm text-gray-500"),
                rx.button(
                    rx.icon("arrow-down", size=16),
                    variant="ghost",
                    class_name="text-gray-400 hover:text-red-500",
                ),
                rx.spacer(),
                rx.button(
                    rx.icon("message-circle", size=16),
                    rx.text("Reply", class_name="ml-1 text-sm"),
                    variant="ghost",
                    class_name="text-gray-500 hover:bg-gray-50",
                ),
                width="100%",
                class_name="mt-2",
            ),
            align_items="start",
            class_name="p-4 bg-white hover:bg-gray-50 transition-colors duration-200",
        ),
        width="100%",
        class_name="border-b border-gray-100",
    )


def comment_section():
    return rx.box(
        rx.vstack(
            rx.text("Comments", class_name="text-xl font-medium text-gray-900 mb-6"),
            rx.hstack(
                rx.input(
                    placeholder="Add a comment...",
                    class_name="w-full p-2 ml-4 rounded-full h-12",
                ),
                rx.button(
                    "Post",
                    class_name="rounded-full h-12 px-6 bg-gray-600",
                ),
                width="100%",
                spacing="3",
                class_name="mb-8",
            ),
            comment_box(
                author="JohnDoe",
                content="This is a great post! Thanks for sharing.",
                time_posted="2h ago",
            ),
            comment_box(
                author="JaneSmith",
                content="I have a different perspective on this...",
                time_posted="1h ago",
            ),
            width="100%",
            spacing="0",
            class_name="p-4 bg-white rounded-lg border border-gray-200 divide-gray-100 w-full overflow-hidden",
        ),
        width="100%",
        class_name="w-full",
    )


def post_page():
    return rx.container(
        rx.vstack(
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
            comment_section(),
            width="100%",
            spacing="6",
        ),
        class_name="mt-6 w-full max-w-4xl mx-auto px-2 sm:px-0",
    )
