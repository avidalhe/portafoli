import reflex as rx

def footer () -> rx.Component:
    """Peu de pàgina"""
    return rx.center(
        rx.text(
            "Web creada per ",
            rx.link("nauvi", href="/"),
        ),
        bg="slate.900",
        # color="white",
        padding="1.5em",
    )
