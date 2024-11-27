import reflex as rx


def post(
    title: str,
    content: str,
    author: str,
    subreddit: str,
    upvotes: int,
    comments: int,
    time_posted: str,
    post_id: str,
) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.link(
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            subreddit,
                            class_name="text-sm font-medium text-blue-600",
                        ),
                        rx.spacer(),
                        rx.text(
                            author,
                            class_name="text-sm font-medium text-orange-500",
                        ),
                        rx.text(
                            f"• {time_posted}",
                            class_name="text-sm text-gray-500",
                        ),
                        class_name="flex items-center justify-between w-full",
                    ),
                    rx.heading(title, size="lg", class_name="text-gray-800 font-bold"),
                    rx.text(
                        content,
                        class_name="text-gray-600 line-clamp-3 overflow-hidden",
                    ),
                    rx.hstack(
                        rx.hstack(
                            rx.button(
                                rx.icon("arrow-up", size=20),
                                variant="ghost",
                                class_name="text-gray-500 hover:text-blue-500 transition-colors",
                            ),
                            rx.text(
                                upvotes,
                                class_name="font-bold text-gray-700",
                            ),
                            rx.button(
                                rx.icon("arrow-down", size=20),
                                variant="ghost",
                                class_name="text-gray-500 hover:text-red-500 transition-colors",
                            ),
                            spacing="1",
                            class_name="flex items-center",
                        ),
                        rx.button(
                            rx.icon("message-square", size=18),
                            rx.text(f"{comments} comments", class_name="ml-2"),
                            variant="ghost",
                            class_name="text-gray-500 hover:text-gray-700 transition-colors",
                        ),
                        width="100%",
                        class_name="mt-2 flex items-center gap-8",
                    ),
                    align_items="start",
                    spacing="3",
                    class_name="cursor-pointer w-full",
                ),
                href=f"/post/{post_id}",
                class_name="no-underline w-full",
            ),
            width="100%",
        ),
        class_name="w-full md:min-w-[600px] p-6 bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 min-h-[200px]",
    )
