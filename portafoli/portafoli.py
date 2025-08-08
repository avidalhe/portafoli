"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .ui.base import base_page


class State(rx.State):
    """The app state."""


def about_me () -> rx.Component:
    """Aquí pintem les coses sobre mi"""
    return rx.container(
        rx.heading(
            "About me",
            size = '5', 
            weight='bold',
            justify='stard'
        ), # rx.heading

        id = 'aboutme'
    )

def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.container(
        rx.vstack(
            rx.heading(
                "Arnau Vidal", 
                size = "8",
            ),
            rx.avatar(
                src = "avatar_a_substituir.png",
                fallback="nauvi",
                size = "8",
                radius='large',
            ),
            about_me(),
            
        align_items = "center",
        min_height="85vh",
        ),
    )
    return base_page(my_child)


app = rx.App()
app.add_page(index)
