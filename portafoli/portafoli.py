import reflex as rx

from .ui.base import base_page
from .ui.hero import about_me
from .ui.personal_projects import projectes_destacats

@rx.page(route="/", 
        title="Arnau Vidal | Enginyer Industrial i Desenvolupador de Software",
        description="Portafoli d'Arnau Vidal, enginyer industrial i creador de solucions digitals. Projectes en Python, Rust i aplicacions web com TaskTimer.",
        meta=[
            # Etiquetes rellevans pels motors de cerca de google
            {"name":"viewport", "content":"width=device-width", "initial-scale":"1.0"},
            {"tag_name":"link", "rel":"canonical", "href":"https://nauvi.cat"},
            {"tag_name": "link", "rel": "alternate", "hreflang": "ca-ES", "href": "https://nauvi.cat"},
            {"tag_name":"link", "rel":"icon", "href":"/favicon.ico", "type":"image/x-icon"},
            {"char_set": "UTF-8"},
            # Open Graph bàsic
            {"property":"og:type", "content":"profile"},
            {"property":"og:title", "content":"Arnau Vidal | Desenvolupador i Enginyer Industrial"},
            {"property":"og:description", "content":"Portafoli d'Arnau Vidal, enginyer industrial i creador de solucions digitals. Projectes en Python, Rust i aplicacions web com TaskTimer."},
            {"property":"og:url", "content":"https://nauvi.cat"},
            {"property":"og:image", "content":"/og-nauvi.jpg"},
            {"property":"og:site_name", "content":"Arnau Vidal Portfolio"},
            {"property":"og:locale", "content":"ca_ES"},
            {"property":"profile:first_name", "content":"Arnau"},
            {"property":"profile:last_name", "content": "Vidal"},
            {"property":"profile:username", "content":"nauvi"},
            {"property":"profile:gender", "content":"male"},            
            
            
            # # 🐦 Twitter Card
            # {"name":"twitter:card", "content":"summary_large_image"},
            # {"name":"twitter:title", "content":"Arnau Vidal | Desenvolupador i Enginyer Industrial"},
            # {"name":"twitter:description", "content":"Explora els meus projectes i aplicacions com TaskTimer."},
            # {"name":"twitter:image", "content":"https://nauvi.dev/static/nauvi_logo.png"},
        ],
    )
def index_portafoli() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.center(
        rx.vstack(
            rx.heading(
                "Arnau Vidal Hernando", 
                font_size="clamp(16px, 3.2vw, 36px)",
                as_='h2'
            ),
            rx.avatar(
                src = "avatar.jpg",
                alt='Avatar nauvi.cat',
                fallback="nauvi",
                size = "8",
                radius='large',
                aria_label="Avatar de nauvi.cat",
            ),
            rx.hstack(
                rx.link(
                    rx.icon("mail", size=3),
                    href="mailto:nauvi.dev@gmail.com",
                    aria_label="Contacta per correu",
                    is_external=True,
                ),
                rx.link(
                    rx.icon("phone", size=3,),
                    href="tel:+34661139326",
                    aria_label="Truca al 661 13 93 23",
                    is_external=True,   
                ),
            ),
            about_me(),
            rx.divider(),
            projectes_destacats(),
        align_items = "center",
        max_width='80vw',
        min_height="85vh",
        ),     
        margin_top='0.75em',   
        width='100%',
    )
    return base_page(my_child)


app = rx.App(enable_state=False)
app.add_page(index_portafoli)



