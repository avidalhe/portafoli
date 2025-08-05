import reflex as rx

from ..navigation import routes

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            # Configurem per pantalla d'ordinador
            rx.hstack(
                rx.heading("Nauvi.dev", size = "7", weight='bold',),
                aling_items = 'center',
                spacing="4",
            ), # rx.hastck
            justify = "between",
            aling_items = "center",
            id = "my_navbar_hstack-desktop"
        ), # rx.desktop_only
        rx.mobile_and_tablet(
            # Configurem per pantalla de tablet o mobil
            
        ), # rx.mobile_and_tablet
        bg = rx.color("tomato", 3),
        padding = "1em",
        width = "100%",
        id = "my-main-nav"
    )
