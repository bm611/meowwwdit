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
            rx.hstack(
                rx.vstack(
                    rx.icon_button(
                        rx.icon("chevron-up", size=20),
                        class_name="hover:text-[#B4A69B]",
                        variant="ghost",
                    ),
                    rx.text(
                        upvotes,
                        class_name="font-bold text-sm md:text-base text-[#1F1F1F]",
                    ),
                    rx.icon_button(
                        rx.icon("chevron-down", size=20),
                        class_name="hover:text-[#B4A69B]",
                        variant="ghost",
                    ),
                    spacing="2",
                    class_name="flex items-center justify-center",
                ),
                rx.link(
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                f"r/{subreddit}",
                                class_name="text-xs md:text-sm font-medium text-[#1F1F1F]",
                            ),
                            rx.text("•", class_name="text-xs md:text-sm text-[#B4A69B]"),
                            rx.text(
                                f"Posted by {author}",
                                class_name="text-xs md:text-sm hidden md:inline",
                            ),
                            rx.text(
                                "•",
                                class_name="text-xs md:text-sm text-[#B4A69B] hidden md:inline",
                            ),
                            rx.text(
                                time_posted,
                                class_name="text-xs md:text-sm",
                            ),
                            class_name="flex flex-wrap items-center gap-2",
                        ),
                        rx.text(
                            title, class_name="font-bold text-lg md:text-xl text-[#1F1F1F]"
                        ),
                        rx.text(
                            content,
                            class_name="text-sm md:text-base text-[#1F1F1F]/80 line-clamp-3 overflow-hidden",
                        ),
                        rx.button(
                            rx.hstack(
                                rx.icon("message-circle", size=16),
                                rx.text(
                                    f"{comments} comments", class_name="text-md font-bold"
                                ),
                                spacing="2",
                                align="center",
                            ),
                            class_name="mt-2 bg-[#B0C4DE] text-[#1F1F1F] px-4 py-5 rounded-full border-2 border-[#1F1F1F] shadow-[6px_6px_0px_0px_rgba(31,31,31,1)] hover:shadow-[3px_3px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300",
                        ),
                        align_items="start",
                        spacing="2",
                        class_name="cursor-pointer",
                    ),
                    href=f"/post/{post_id}",
                    class_name="no-underline",
                ),
                align_items="start",
                spacing="4",
            ),
            width="100%",
        ),
        class_name="w-full p-4 bg-[#FFE5E5] border-4 border-[#1F1F1F] rounded-xl shadow-[4px_4px_0px_0px_rgba(31,31,31,1)] hover:shadow-[2px_2px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300",
    )
