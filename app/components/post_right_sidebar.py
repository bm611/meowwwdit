import reflex as rx


def post_right_sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon("cat", size=24, class_name="text-gray-700"),
                rx.heading(
                    "r/CatMemes", size="lg", class_name="text-gray-800 font-bold"
                ),
                spacing="4",
                class_name="flex items-center",
            ),
            rx.text(
                "A place for all your feline humor needs.",
                class_name="text-gray-600 text-sm",
            ),
            rx.divider(class_name="border-gray-200"),
            rx.hstack(
                rx.vstack(
                    rx.text("123k", class_name="text-gray-800 font-bold text-2xl"),
                    rx.text("Members", class_name="text-gray-600 text-xs uppercase"),
                    align_items="center",
                ),
                rx.vstack(
                    rx.text("1.5k", class_name="text-gray-800 font-bold text-2xl"),
                    rx.text("Online", class_name="text-gray-600 text-xs uppercase"),
                    align_items="center",
                ),
                justify_content="space-around",
                width="100%",
            ),
            rx.divider(class_name="border-gray-200"),
            rx.text("Created: January 1, 2020", class_name="text-gray-600 text-sm"),
            rx.button(
                "Join",
                class_name="bg-gray-600 text-white px-6 py-2 rounded-lg font-medium hover:bg-blue-700 transition-colors",
            ),
            spacing="4",
            align_items="stretch",
            class_name="w-full",
        ),
        class_name="hidden md:block ml-4 mt-4 mr-4 w-full p-6 bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300",
        width="300px",
    )
