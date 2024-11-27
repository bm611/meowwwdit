import reflex as rx
from typing import List


class NavState(rx.State):
    show_mobile_menu: bool = False
    title: str = ""
    description: str = ""
    subreddit: str = ""

    def toggle_menu(self):
        self.show_mobile_menu = not self.show_mobile_menu

    def create_post(self):
        # TODO: Implement post creation logic
        self.title = ""
        self.description = ""
        self.subreddit = ""

    def set_title(self, value):
        self.title = value

    def set_description(self, value):
        self.description = value

    def set_subreddit(self, value):
        self.subreddit = value


def nav_menu_items() -> List[rx.Component]:
    return [
        rx.button(
            rx.hstack(rx.icon("search", size=20), "Search", align="center"),
            class_name="w-full text-left bg-white text-gray-800 px-4 py-2 rounded-md border border-gray-200 hover:bg-gray-100 transition-colors duration-200",
        ),
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    rx.hstack(rx.icon("plus", size=20), "Create", align="center"),
                    class_name="w-full text-left bg-white text-gray-800 px-4 py-2 rounded-md border border-gray-200 hover:bg-gray-100 transition-colors duration-200",
                )
            ),
            rx.dialog.content(
                rx.dialog.title(
                    "New Post",
                    class_name="text-lg font-semibold mb-2",
                ),
                rx.vstack(
                    rx.input(
                        placeholder="Title",
                        on_change=NavState.set_title,
                        value=NavState.title,
                        class_name="w-full p-2 border border-gray-300 rounded-md mb-2",
                    ),
                    rx.text_area(
                        placeholder="Content",
                        on_change=NavState.set_description,
                        value=NavState.description,
                        class_name="w-full p-2 border border-gray-300 rounded-md mb-2",
                    ),
                    rx.input(
                        placeholder="Subreddit",
                        on_change=NavState.set_subreddit,
                        value=NavState.subreddit,
                        class_name="w-full p-2 border border-gray-300 rounded-md mb-2",
                    ),
                    rx.hstack(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                class_name="px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 transition-colors duration-200",
                            ),
                        ),
                        rx.dialog.close(
                            rx.button(
                                "Post",
                                class_name="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition-colors duration-200",
                                on_click=NavState.create_post,
                            ),
                        ),
                        justify="end",
                        spacing="2",
                    ),
                    align_items="stretch",
                ),
                class_name="bg-white p-4 rounded-md shadow-md",
            ),
        ),
        rx.button(
            rx.hstack(rx.icon("user", size=20), "Profile", align="center"),
            class_name="w-full text-left bg-white text-gray-800 px-4 py-2 rounded-md border border-gray-200 hover:bg-gray-100 transition-colors duration-200",
        ),
    ]


def nav_section():
    return rx.box(
        # Desktop Navigation
        rx.hstack(
            rx.hstack(
                rx.icon("paw-print", size=28),
                rx.text(
                    "Purrdit",
                    class_name="font-extrabold text-2xl md:text-4xl",
                ),
                class_name="flex items-center justify-center cursor-pointer",
                on_click=rx.redirect("/"),
            ),
            rx.input(
                placeholder="Search...",
                class_name="w-1/3 h-12 mx-4 border-4 border-black rounded-lg focus:outline-none focus:ring-0 focus:border-blue-500 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] transition-all duration-300 hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-0.5 hover:translate-y-0.5 hidden md:block text-xl",
            ),
            rx.hstack(
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(
                            rx.icon("plus"),
                            "Create",
                            size="4",
                            class_name="bg-white text-[#1F1F1F] px-4 py-2 rounded-lg border-4 border-[#1F1F1F] shadow-[4px_4px_0px_0px_rgba(31,31,31,1)] hover:shadow-[2px_2px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300 hidden md:flex items-center gap-2",
                        )
                    ),
                    rx.dialog.content(
                        rx.dialog.title(
                            "Create a New Post",
                            class_name="text-xl font-bold mb-4",
                        ),
                        rx.dialog.description(
                            "Share your thoughts with the community.",
                            class_name="text-sm text-gray-500 mb-4",
                        ),
                        rx.flex(
                            rx.text(
                                "Title",
                                as_="div",
                                class_name="font-bold mb-2",
                            ),
                            rx.input(
                                placeholder="Enter your post title",
                                on_change=NavState.set_title,
                                value=NavState.title,
                                class_name="w-full h-12 p-3 border-4 border-[#1F1F1F] rounded-xl bg-white shadow-[4px_4px_0px_0px_rgba(31,31,31,1)] hover:shadow-[2px_2px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300 focus:outline-none focus:ring-0 focus:border-[#4A90E2] mb-4",
                            ),
                            rx.text(
                                "Description",
                                as_="div",
                                class_name="font-bold mb-2",
                            ),
                            rx.text_area(
                                placeholder="Enter your post content",
                                on_change=NavState.set_description,
                                value=NavState.description,
                                class_name="w-full p-3 border-4 border-[#1F1F1F] rounded-xl bg-white shadow-[4px_4px_0px_0px_rgba(31,31,31,1)] hover:shadow-[2px_2px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300 focus:outline-none focus:ring-0 focus:border-[#4A90E2] mb-4",
                            ),
                            rx.text(
                                "Subreddit",
                                as_="div",
                                class_name="font-bold mb-2",
                            ),
                            rx.input(
                                placeholder="Enter subreddit name",
                                on_change=NavState.set_subreddit,
                                value=NavState.subreddit,
                                class_name="w-full h-12 p-3 border-4 border-[#1F1F1F] rounded-xl bg-white shadow-[4px_4px_0px_0px_rgba(31,31,31,1)] hover:shadow-[2px_2px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300 focus:outline-none focus:ring-0 focus:border-[#4A90E2] mb-4",
                            ),
                            direction="column",
                        ),
                        rx.flex(
                            rx.dialog.close(
                                rx.button(
                                    "Cancel",
                                    class_name="bg-gray-200 text-[#1F1F1F] px-6 py-3 rounded-xl border-4 border-[#1F1F1F] shadow-[4px_4px_0px_0px_rgba(31,31,31,1)] hover:shadow-[2px_2px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300",
                                ),
                            ),
                            rx.dialog.close(
                                rx.button(
                                    "Post",
                                    class_name="bg-[#FFA5A5] text-[#1F1F1F] px-6 py-3 rounded-xl border-4 border-[#1F1F1F] shadow-[4px_4px_0px_0px_rgba(31,31,31,1)] hover:shadow-[2px_2px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300",
                                    on_click=NavState.create_post,
                                ),
                            ),
                            justify="end",
                            spacing="3",
                            margin_top="4",
                        ),
                        class_name="bg-white p-8 rounded-xl border-4 border-[#1F1F1F] shadow-[8px_8px_0px_0px_rgba(31,31,31,1)]",
                    ),
                ),
                rx.button(
                    rx.icon("user"),
                    "Ringo",
                    size="4",
                    class_name="bg-white border-4 border-black text-gray-800 px-4 py-2 rounded-lg hidden md:flex shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300",
                ),
                # Mobile Menu
                rx.box(
                    rx.button(
                        rx.icon("menu"),
                        class_name="md:hidden bg-black text-white p-2 rounded-lg border-4 border-[#1F1F1F] shadow-[6px_6px_0px_0px_rgba(31,31,31,1)] hover:shadow-[4px_4px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300",
                        on_click=NavState.toggle_menu,
                    ),
                    rx.cond(
                        NavState.show_mobile_menu,
                        rx.vstack(
                            *nav_menu_items(),
                            align_items="center",
                            class_name="absolute right-0 top-full p-4 mt-2 w-52 bg-white border-4 border-black rounded-lg shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] z-50",
                        ),
                    ),
                    position="relative",
                ),
                spacing="4",
                class_name="flex items-center justify-center",
            ),
            class_name="w-full justify-between md:justify-around items-center bg-[#F0F0F0] p-4 border-4 border-black rounded-lg shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]",
        ),
    )
