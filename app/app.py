import reflex as rx
from .components.nav import nav_section
from .components.feed import feed_section


class State(rx.State):
    pass


@rx.page(route="/", title="Meowwwdit")
def index():
    return rx.box(
        nav_section(),
        rx.center(
            feed_section(),
        ),
    )


style = {
    "font_family": "Funnel",
}

app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css"],
)
