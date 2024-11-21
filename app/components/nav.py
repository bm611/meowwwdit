import reflex as rx
from typing import List


class NavState(rx.State):
    show_mobile_menu: bool = False

    def toggle_menu(self):
        self.show_mobile_menu = not self.show_mobile_menu


def nav_menu_items() -> List[rx.Component]:
    return [
        rx.button(
            rx.hstack(rx.icon("search", size=20), "Search", align="center"),
            class_name="w-full text-left bg-white hover:bg-gray-100 px-4 py-2 text-black rounded-lg border-4 border-black shadow-[6px_6px_0px_0px_rgba(0,0,0,1)]",
        ),
        rx.button(
            rx.hstack(rx.icon("plus", size=20), "Create", align="center"),
            class_name="w-full text-left bg-[#4A90E2] hover:bg-[#4682B4] px-4 py-2 text-white rounded-lg border-4 border-[#1F1F1F] shadow-[6px_6px_0px_0px_rgba(31,31,31,1)]",
        ),
        rx.button(
            rx.hstack(rx.icon("user", size=20), "Profile", align="center"),
            class_name="w-full text-left bg-[#E67E22] hover:bg-[#FF9900] px-4 py-2 text-white rounded-lg border-4 border-[#1F1F1F] shadow-[6px_6px_0px_0px_rgba(31,31,31,1)]",
        ),
    ]


def nav_section():
    return rx.box(
        # Desktop Navigation
        rx.hstack(
            rx.hstack(
                rx.icon("paw-print", size=28),
                rx.text(
                    "Meowwwdit",
                    class_name="font-extrabold text-2xl md:text-4xl",
                ),
                class_name="flex items-center justify-center cursor-pointer",
                on_click=rx.redirect("/"),
            ),
            rx.input(
                placeholder="Search...",
                class_name="w-1/3 h-12 mx-4 border-4 border-black rounded-lg focus:outline-none focus:ring-0 focus:border-blue-500 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] transition-all duration-300 hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-0.5 hover:translate-y-0.5 hidden md:block",
            ),
            rx.hstack(
                rx.button(
                    rx.icon("plus"),
                    "Create",
                    size="4",
                    class_name="bg-[#4A90E2] text-white px-4 py-2 rounded-lg border-4 border-[#1F1F1F] shadow-[6px_6px_0px_0px_rgba(31,31,31,1)] hover:shadow-[4px_4px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300 hidden md:flex",
                ),
                rx.button(
                    rx.icon("user"),
                    "Ringo",
                    size="4",
                    class_name="bg-[#E67E22] text-white px-4 py-2 rounded-lg border-4 border-[#1F1F1F] shadow-[6px_6px_0px_0px_rgba(31,31,31,1)] hover:shadow-[4px_4px_0px_0px_rgba(31,31,31,1)] hover:translate-x-0.5 hover:translate-y-0.5 transition-all duration-300 hidden md:flex",
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
                            class_name="absolute right-0 top-full py-2 mt-2 w-40 bg-white border-4 border-black rounded-lg shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] z-50",
                        ),
                    ),
                    position="relative",
                ),
                spacing="4",
                class_name="flex items-center justify-center",
            ),
            class_name="w-full justify-between md:justify-around items-center bg-white p-4 border-4 border-black rounded-lg shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]",
        ),
    )
