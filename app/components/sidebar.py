import reflex as rx


def sidebar() -> rx.Component:
    subreddits = [
        ("r/CatMemes", "laugh"),
        ("r/PurrProgramming", "code"),
        ("r/WhiskerWisdom", "lightbulb"),
        ("r/FelinePhilosophy", "book"),
        ("r/NipNaps", "moon"),
        ("r/CatConspiracy", "eye"),
        ("r/LazyCats", "coffee"),
        ("r/CatPranks", "sparkles"),
        ("r/MeowMusic", "music"),
        ("r/CatFortress", "castle"),
        ("r/PawsomePics", "camera"),
        ("r/CatastrophicFails", "zap"),
        ("r/WhiskerWatchers", "eye"),
        ("r/CatnipAddicts", "leaf"),
        ("r/MidnightZoomies", "zap"),
        ("r/BoxLiving", "package"),
        ("r/PurrfectFashion", "shirt"),
        ("r/CatScience", "flask-conical"),
        ("r/LitterBoxThoughts", "brain"),
        ("r/NineLivesClub", "heart"),
    ]
    return rx.box(
        rx.vstack(
            rx.text("Subreddits", class_name="font-bold text-2xl mb-4"),
            *[
                rx.hstack(
                    rx.icon(icon, size=16),
                    rx.text(sub, class_name="text-sm"),
                    class_name="mb-2 flex items-center justify-left",
                )
                for sub, icon in subreddits
            ],
            spacing="3",
            align_items="stretch",
        ),
        class_name="hidden lg:block ml-4 mt-4 bg-[#FFD93D] p-6 rounded-lg border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] transition-all duration-300 hover:shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:translate-x-0.5 hover:translate-y-0.5",
        width="250px",
    )
