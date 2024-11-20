import reflex as rx
from datetime import datetime


def post(
    title: str,
    content: str,
    author: str,
    subreddit: str,
    upvotes: int,
    comments: int,
    time_posted: datetime,
) -> rx.Component:
    return rx.box(
        rx.vstack(
            # Vote buttons and count
            rx.hstack(
                rx.vstack(
                    rx.icon_button(
                        rx.icon("chevron-up", size=20),
                        class_name="hover:text-green-500",
                        variant="ghost",
                    ),
                    rx.text(str(upvotes), class_name="font-bold text-sm md:text-base"),
                    rx.icon_button(
                        rx.icon("chevron-down", size=20),
                        class_name="hover:text-red-500",
                        variant="ghost",
                    ),
                    spacing="2",
                    class_name="flex items-center justify-center",
                ),
                # Post content
                rx.vstack(
                    # Header with subreddit, author, and timestamp
                    rx.hstack(
                        rx.text(f"r/{subreddit}", class_name="text-xs md:text-sm font-medium"),
                        rx.text("•", class_name="text-xs md:text-sm text-gray-500"),
                        rx.text(
                            f"Posted by {author}",
                            class_name="text-xs md:text-sm text-gray-500 hidden md:inline",
                        ),
                        rx.text("•", class_name="text-xs md:text-sm text-gray-500 hidden md:inline"),
                        rx.text(
                            time_posted.strftime("%b %d, %Y"),
                            class_name="text-xs md:text-sm text-gray-500",
                        ),
                        class_name="flex flex-wrap items-center gap-2",
                    ),
                    rx.text(title, class_name="font-bold text-lg md:text-xl"),
                    rx.text(content, class_name="text-sm md:text-base text-gray-600"),
                    # Comment button at the bottom
                    rx.button(
                        rx.hstack(
                            rx.icon("message-circle", size=16),
                            rx.text(f"{comments} comments", class_name="text-sm"),
                            spacing="2",
                            align="center",
                        ),
                        class_name="bg-black text-white px-4 py-2 rounded-none shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:shadow-[1px_1px_0px_0px_rgba(0,0,0,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300",
                    ),
                    align_items="start",
                    spacing="2",
                ),
                align_items="start",
                spacing="4",
            ),
            width="100%",
        ),
        class_name="w-full p-4 bg-white border-4 border-black rounded-none shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300",
    )
