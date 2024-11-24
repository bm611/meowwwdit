import reflex as rx
from .components.nav import nav_section
from .components.feed import feed_section
from .components.sidebar import sidebar
from .components.right_sidebar import r_sidebar
from .components.post_right_sidebar import post_right_sidebar

from .pages.post import post_page
from app.state import State


@rx.page(route="/", title="Meowwwdit")
def index():
    return rx.box(
        nav_section(),
        rx.hstack(
            sidebar(),
            rx.center(
                feed_section(),
            ),
            r_sidebar(),
            class_name="flex justify-between",
        ),
    )


@rx.page(route="/post/[post_id]", title="Post", on_load=State.set_current_post)
def post():
    return rx.box(
        nav_section(),
        rx.hstack(
            sidebar(),
            rx.center(
                post_page(),
            ),
            post_right_sidebar(),
            class_name="flex justify-between",
        ),
    )


style = {
    "font_family": "Funnel",
    "background_color": "#FFECEC",
}

app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css"],
)
