import reflex as rx
from .components.nav import nav_section
from .components.feed import feed_section
from app.state import State


@rx.page(route="/", title="Meowwwdit")
def index():
    return rx.box(
        nav_section(),
        rx.center(
            feed_section(),
        ),
    )


@rx.page(route="/post/[post_id]", title="Post")
def post():
    return rx.box(
        nav_section(),
        rx.text(State.get_post_id),
    )


style = {
    "font_family": "Funnel",
    "background_color": "#F5F5F5",
}

app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css"],
)
