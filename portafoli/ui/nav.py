import reflex as rx

from ..navigation import routes

def navbar_link(text: str, url: str)->rx.Component:
    return rx.link(
        rx.text(text, size='4', weight='medium'),
        href=url,
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            # Configurem per pantalla d'ordinador
            rx.hstack(
                rx.heading("Nauvi.cat", size = "6", weight='bold',), 
                justify='start',
                align_items='center'
            ), # rx.hstack
            id = "my_navbar_hstack-desktop"
        ), # rx.desktop_only
        rx.mobile_and_tablet(
            # Configurem per pantalla de tablet o mobil
            rx.hstack(
                rx.heading(
                    "Nauvi.cat", 
                    size = '6',
                    weight='bold',
                ),#rx.heading
                align_items = "center",
            ),#rx.hstack
            
        ), # rx.mobile_and_tablet
        bg = rx.color("tomato", 3),
        padding = "1em",
        width = "100%",
        id = "my-main-nav"
    )
