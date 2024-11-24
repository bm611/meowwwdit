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
            rx.text("Purrdit Stats", class_name="font-bold text-center text-2xl mb-4"),
            *[
                rx.hstack(
                    rx.icon(icon, size=32),
                    rx.vstack(
                        rx.text(label, class_name="text-lg font-medium"),
                        rx.text(value, class_name="text-lg font-bold"),
                        align_items="start",
                    ),
                    class_name="flex bg-[#FFD93D] p-4 rounded-lg border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transition-all duration-300 hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:translate-x-0.5 hover:translate-y-0.5",
                )
                for label, value, icon in stats
            ],
            align_items="stretch",
        ),
        class_name="hidden md:block ml-4 mt-4 mr-4",
        width="250px",
    )
