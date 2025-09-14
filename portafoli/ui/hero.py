import reflex as rx

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
            Tinc experiència en el desenvolupament d’aplicacions web amb Python (Reflex), i estic expandint els meus coneixements cap a Rust i el desenvolupament full stack amb dioxus, per tal de crear solucions innovadores i multiplataforma.
            M’apassionen els projectes amb impacte i la combinació de programació amb càlcul i màrketing digital.
            Sempre amb ganes d’aprendre, compartir coneixement i seguir evolucionant com a persona i com a professional.
            """,
            text_align = 'justify',
            align='left',
            width='100%',
            margin_top = '1em',
        ), # rx.text
        width = '100%',
        align='center',
    )