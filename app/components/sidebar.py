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
            rx.text("Subreddits", class_name="text-gray-800 font-bold text-2xl"),
            *[
                rx.link(
                    rx.hstack(
                        rx.icon(icon, size=16, class_name="text-gray-600"),
                        rx.text(sub, class_name="text-gray-700 font-medium hover:text-blue-600 transition-colors"),
                        class_name="flex items-center gap-2",
                    ),
                    href="#",
                    class_name="no-underline",
                )
                for sub, icon in subreddits
            ],
            spacing="4",
            align_items="stretch",
            class_name="w-full",
        ),
        class_name="hidden lg:block ml-4 mt-4 w-full p-6 bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300",
        width="250px",
    )
