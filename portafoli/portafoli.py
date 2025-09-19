import reflex as rx

from .ui.base import base_page
from .ui.hero import about_me
from .ui.personal_projects import projectes_destacats
from .ui.services import my_services
from .navigation import routes

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
                    rx.icon("mail"),
                    href="mailto:nauvi.dev@gmail.com",
                    aria_label="Contacta per correu",
                    is_external=True,
                ),
                rx.link(
                    rx.icon("phone"),
                    href="tel:+34661139326",
                    aria_label="Truca al 661 13 93 23",
                    is_external=True,   
                ),
            ),
            rx.flex(
                rx.text("| "),
                rx.link(
                    rx.color_mode_cond(
                        dark=rx.text("Qui sóc |", color="white", font_size="clamp(10px, 2.1vw, 16px)",),
                        # segon si dark mode
                        light=rx.text("Qui sóc |", color='black', font_size="clamp(10px, 2.1vw, 16px)",)
                    ), # rx.color_mode_cond
                    href="#qui-soc",
                    aria_label = "Link que et porta a la descripció de qui soc",
                    outline_color="transparent",
                    text_decoration='None'  
                ),
                rx.link(
                    rx.color_mode_cond(
                        dark=rx.text("Els meus serveis |", color='white', font_size="clamp(10px, 2.1vw, 16px)",),
                        light=rx.text("Els meus serveis |", color='black', font_size="clamp(10px, 2.1vw, 16px)",),
                    ), #rx.color_mode_cond
                    aria_label='Redirecció als meus serveis',
                    outline_color="transparent",
                    text_decoration='None',
                    href=routes.ELS_MEUS_SERVEIS, # Aquí he de posar el link de la meva pàgina de serveis que he de crear més tard.
                    is_external=True,
                ), #rx.link
                rx.link(
                    rx.color_mode_cond(
                        dark=rx.text("Els meus Projectes |", color="white", font_size="clamp(10px, 2.1vw, 16px)",),
                        # segon si dark mode
                        light=rx.text("Els meus Projectes |", color='black',font_size="clamp(10px, 2.1vw, 16px)",)
                    ), # rx.color_mode_cond
                    href="#projectes",
                    aria_label = "Link que et porta a els meus projectes",
                    outline_color="transparent",
                    text_decoration='None',
                ),
                space='5',
                direction="row",
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

def my_service() -> rx.Component:
    my_child = rx.fragment(
        my_services(), # Cridem el component 'my_service'
    )
    return base_page(my_child)

app = rx.App(enable_state=False)
app.add_page(index_portafoli)
app.add_page(my_service, route='/my_services')



