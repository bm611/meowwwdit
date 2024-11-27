import reflex as rx


def r_sidebar() -> rx.Component:
    stats = [
        ("Total Users", "1,234,567", "users"),
        ("Total Subreddits", "5,678", "hash"),
        ("Total Posts", "9,876,543", "pencil"),
        ("Total Comments", "87,654,321", "message-circle"),
    ]
    return rx.box(
        rx.vstack(
            *[
                rx.hstack(
                    rx.icon(icon, size=24, class_name="text-gray-600"),
                    rx.vstack(
                        rx.text(label, class_name="text-gray-700 font-medium"),
                        rx.text(value, class_name="text-gray-800 font-bold"),
                        align_items="start",
                        spacing="1",
                    ),
                    class_name="flex items-center p-4 bg-white rounded-lg shadow hover:shadow-md transition-shadow duration-300 gap-4",
                )
                for label, value, icon in stats
            ],
            spacing="4",
            align_items="stretch",
            class_name="w-full",
        ),
        class_name="hidden md:block ml-4 mt-4 mr-4",
        width="250px",
    )
