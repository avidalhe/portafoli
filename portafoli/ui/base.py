import reflex as rx

from .nav import navbar
from .foot import footer

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    """Aquesta funció serà la bàsica de la nostra pàgina"""
    return rx.fragment(
        rx.box(
            navbar(),
            child,
            footer(),
            max_width = "100%",
            id = 'my-content-area-el',
        ),

        rx.color_mode.button(position="bottom-left"),
        id = "my-base-container"
    )
