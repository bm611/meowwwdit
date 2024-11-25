import reflex as rx
from app.state import State
from app.components.post import post
from app.components.feed import sample_posts


def comment_section():
    comments = []
    for i in range(1, 4):
        comments.append(
            sample_comment(
                username="User" + str(i),
                content=f"This is sample comment {i}",
                upvotes=i * 5,
            )
        )
        if i < 3:  # Don't add divider after the last comment
            comments.append(rx.divider(border_color="black", border_width="0.5px"))

    return rx.vstack(
        # Comment input box
        rx.grid(
            rx.input(
                placeholder="Add a comment...",
                width="100%",
                class_name="bg-transparent h-12 border-4 border-[#1F1F1F] rounded-lg p-2 text-[#1F1F1F] shadow-[4px_4px_0px_0px_rgba(31,31,31,1)]",
            ),
            rx.button(
                "Post",
                class_name="bg-[#B0C4DE] h-12 text-[#1F1F1F] px-6 py-4 rounded-lg border-4 border-[#1F1F1F] shadow-[4px_4px_0px_0px_rgba(31,31,31,1)] hover:shadow-[2px_2px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300 font-bold",
            ),
            template_columns="1fr auto",
            class_name="grid-cols-1 sm:grid-cols-[1fr_auto] gap-4 w-full",
        ),
        # Comments container
        rx.box(
            rx.vstack(
                *comments,
                width="100%",
                spacing="4",
                align_items="stretch",
                padding=["2", "3", "4"],
            ),
            class_name="w-full bg-[#FFE5E5] border-4 border-[#1F1F1F] rounded-xl shadow-[4px_4px_0px_0px_rgba(31,31,31,1)]",
            width="100%",
        ),
        class_name="w-full space-y-6 items-stretch px-2 sm:px-4",
    )


def sample_comment(username: str, content: str, upvotes: int):
    return rx.vstack(
        # User info and voting section
        rx.vstack(
            # User info
            rx.hstack(
                rx.avatar(
                    name=username,
                    size="sm",
                    class_name="border-2 border-[#1F1F1F] rounded-full min-w-[32px]",
                ),
                rx.text(
                    username,
                    class_name="font-bold text-[#1F1F1F] text-sm sm:text-base truncate",
                ),
                spacing="2",
                width="100%",
                align_items="center",
            ),
            # Comment content
            rx.text(
                content,
                class_name="text-[#1F1F1F]/80 text-sm sm:text-base break-words",
            ),
            # Voting buttons
            rx.hstack(
                rx.button(
                    rx.icon("arrow-big-up", size=20),
                    variant="ghost",
                    class_name="hover:text-[#B4A69B] p-2",
                ),
                rx.text(
                    str(upvotes),
                    class_name="font-bold text-[#1F1F1F] text-sm min-w-[2rem] text-center",
                ),
                rx.button(
                    rx.icon("arrow-big-down", size=20),
                    variant="ghost",
                    class_name="hover:text-[#B4A69B] p-2",
                ),
                spacing="0",
                class_name="px-2 flex items-center bg-white/50 rounded-full border-2 border-[#1F1F1F] shadow-[2px_2px_0px_0px_rgba(31,31,31,1)]",
            ),
            spacing="2",
            align_items="start",
            width="100%",
        ),
        spacing="3",
        align_items="start",
        width="100%",
        class_name="p-2 sm:p-3",
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
        class_name="mt-6 w-full max-w-4xl mx-auto px-2 sm:px-4",
    )
