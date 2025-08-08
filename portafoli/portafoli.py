"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .ui.base import base_page
    
def projectes_destacats()->rx.Component:
    """Creem la secció on es mostren els projectes que vaig fent"""
    imatge = rx.color_mode_cond(
                        dark=rx.avatar(src = 'Logo_StudyTimer_white.svg'),
                        light=rx.avatar(src= 'Logo_StudyTimer.svg'),
                    )# rx.color_mode_cond
    return rx.container(
        rx.heading(
            'Projectes destacats',
            size = '5',
            weight='bold',
            align='left',
        ), # rx.heading
        rx.card(
            rx.link(
                rx.flex(
                    # fem que canvii el logo en canviar el color de fons
                    imatge,
                    rx.box(
                        rx.heading('TaskTimer'),
                        rx.text(
                            'Primer projecte personal',
                        ), #rx.text
                    ), #rx.box
                    spacing='2'
                ), # rx.flex
                href='https://task-timer.up.railway.app/',
                # Fem que s'obri una pastanya nova
                is_external=True,
            ), #rx.link
            align_items='center',
            margin_top='1em',
            width='100%',
        ), # rx.card
        width='100%',
    )


def about_me () -> rx.Component:
    """Aquí pintem les coses sobre mi"""
    return rx.container(
        rx.heading(
            "Qui sóc?",
            size = '5', 
            weight='bold',
            align="left",
        ), # rx.heading
        rx.text(
            """
            Sóc un estudiant d'enginyeria industrial a punt d’acabar la carrera, amb una ment analítica i orientada a la resolució de problemes.
            Tinc experiència en el desenvolupament d’aplicacions web amb Python (Reflex), i estic expandint els meus coneixements cap a Rust i Flutter per crear solucions multiplataforma.
            M’apassionen els projectes amb impacte, la combinació de programació i càlcul, i estic construint un portafoli que reflecteixi el meu creixement i visió.
            Sempre amb ganes d’aprendre, compartir coneixement i seguir evolucionant com a persona i com a professional.
            """,
            align='left',
            width='100%',
            margin_top = '1em',
        ), # rx.text
        width = '100%',
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
                src = "avatar.jpeg",
                fallback="nauvi",
                size = "8",
                radius='large',
            ),
            about_me(),
            rx.divider(),
            projectes_destacats(),
            
        align_items = "center",
        max_width='80vw',
        min_height="85vh",
        ),
    )
    return base_page(my_child)


app = rx.App()
app.add_page(index)
