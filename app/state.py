import reflex as rx


class State(rx.State):
    @rx.var
    def get_post_id(self) -> str:
        return self.router.page.params.get("post_id", "")
