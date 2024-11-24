import reflex as rx


def post_right_sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon("cat", size=24, color="#1F1F1F"),
                rx.heading("r/CatMemes", size="lg", class_name="font-bold"),
                spacing="4",
                class_name="flex items-center justify-left",
            ),
            rx.text(
                "A place for all your feline humor needs.",
                class_name="text-sm text-gray-600 italic",
            ),
            rx.divider(class_name="border-black"),
            rx.hstack(
                rx.vstack(
                    rx.text("123k", class_name="font-bold text-2xl"),
                    rx.text("Members", class_name="text-xs uppercase"),
                    align_items="center",
                ),
                rx.vstack(
                    rx.text("1.5k", class_name="font-bold text-2xl"),
                    rx.text("Online", class_name="text-xs uppercase"),
                    align_items="center",
                ),
                justify_content="space-around",
                width="100%",
            ),
            rx.divider(class_name="border-black"),
            rx.text("Created: January 1, 2020", class_name="text-sm"),
            rx.button(
                "Join",
                class_name="bg-black text-white px-4 py-2 rounded-full hover:bg-gray-800 transition-colors duration-200",
            ),
            spacing="4",
            align_items="stretch",
        ),
        class_name="hidden md:block ml-4 mt-4 mr-4 bg-[#FFD93D] p-6 rounded-lg border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] transition-all duration-300 hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-0.5 hover:translate-y-0.5",
        width="300px",
    )
