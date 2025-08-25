import reflex as rx

from .ui.base import base_page
    
def projectes_destacats()->rx.Component:
    """Creem la secció on es mostren els projectes que vaig fent"""
    imatge = rx.color_mode_cond(
                        dark=rx.image(src = 'Logo_StudyTimer_white.svg', alt='Logo TaskTimer',size='2.5em',decoding="async"),
                        light=rx.image(src= 'Logo_StudyTimer.svg', alt='Logo TaskTimer', width='2.5em',decoding="async"),
                    )# rx.color_mode_cond
    return rx.container(
        rx.heading(
            'Projectes destacats',
            size = '5',
            weight='bold',
            align='left',
            as_='h2',
            aria_label='Projectes destecats',
        ), # rx.heading
        rx.card(
            rx.link(
                rx.flex(
                    # fem que canvii el logo en canviar el color de fons
                    imatge,
                    rx.box(
                        rx.heading('TaskTimer', as_='h2'),
                        rx.text(
                            'Primer projecte personal',
                        ), #rx.text
                    ), #rx.box
                    spacing='2'
                ), # rx.flex
                href='https://task-timer.up.railway.app/',
                aria_label='Link del projecte TastkTimer',
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
            Sóc un estudiant d'enginyeria industrial a punt d’acabar la carrera, amb una ment analítica i gran capacitat de resoldre problemes.
            Tinc experiència en el desenvolupament d’aplicacions web amb Python (Reflex), i estic expandint els meus coneixements cap a Rust i Flutter per tal de crear solucions innovadores i multiplataforma.
            M’apassionen els projectes amb impacte i la combinació de programació amb càlcul.
            Sempre amb ganes d’aprendre, compartir coneixement i seguir evolucionant com a persona i com a professional.
            """,
            text_align = 'justify',
            align='left',
            width='100%',
            margin_top = '1em',
        ), # rx.text
        width = '100%',
    )

@rx.page(route="/", 
        title="Arnau Vidal | Enginyer Industrial i Desenvolupador de Software",
        description="Portafoli d'Arnau Vidal, enginyer industrial i creador de solucions digitals. Projectes en Python, Rust i aplicacions web com StudyTimer.",
        # keyword="Arnau Vidal, portafoli, enginyer industrial, desenvolupador Python, desenvolupador Rust, aplicacions web, TaskTimer, nauvi.dev",
        meta=[
            {"name":"description", "content":"Portafoli d'Arnau Vidal, enginyer industrial i creador de solucions digitals. Projectes en Python, Rust i aplicacions web com TaskTimer."},
            {"name":"keywords", "content":"Arnau Vidal, portafoli, enginyer industrial, desenvolupador Python, desenvolupador Rust, aplicacions web, TaskTimer, nauvi.dev"},
            {"name":"author", "content":"Arnau Vidal"},

            {"property":"og:title", "content":"Arnau Vidal | Desenvolupador i Enginyer Industrial"},
            {"property":"og:description", "content":"Descobreix els meus projectes en enginyeria i programació. Des de Python fins a aplicacions web com TaskTimer."},
            # property="og:image", content="https://nauvi.dev/static/nauvi_logo.png",  # 👉 posa aquí el teu logo o portada
            {"property""og:url", "content""https://nauvi.cat"},
                        # 🐦 Twitter Card
            {"name":"twitter:card", "content":"summary_large_image"},
            {"name":"twitter:title", "content":"Arnau Vidal | Desenvolupador i Enginyer Industrial"},
            {"name":"twitter:description", "content":"Explora els meus projectes i aplicacions com TaskTimer."},
            {"name":"twitter:image", "content":"https://nauvi.dev/static/nauvi_logo.png"},
            ],
        )
def index_portafoli() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.container(
        rx.vstack(
            rx.heading(
                "Arnau Vidal Hernando", 
                size = "8",
            ),
            rx.avatar(
                src = "avatar.jpg",
                alt='Avatar nauvi.cat',
                fallback="nauvi",
                size = "8",
                radius='large',
                aria_label="Avatar de nauvi.cat",
            ),
            rx.link(
                rx.icon("mail"),
                href="mailto:nauvi.dev@gmail.com",
                aria_label="Contacta per correu",
                is_external=True,
            ),
            about_me(),
            rx.divider(),
            projectes_destacats(),
        align_items = "center",
        max_width='80vw',
        min_height="85vh",
        ),        
        align='center',
    )
    return base_page(my_child)


app = rx.App(enable_state=False)
app.add_page(index_portafoli)
