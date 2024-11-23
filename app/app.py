import reflex as rx
from .components.nav import nav_section
from .components.feed import feed_section

from .pages.post import post_page
from app.state import State


@rx.page(route="/", title="Meowwwdit")
def index():
    return rx.box(
        nav_section(),
        rx.center(
            feed_section(),
        ),
    )


@rx.page(route="/post/[post_id]", title="Post", on_load=State.set_current_post)
def post():
    return rx.box(
        nav_section(),
        post_page(),
    )


style = {
    "font_family": "Funnel",
    "background_color": "#F5F5F5",
}

app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css"],
)
