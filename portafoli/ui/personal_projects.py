import reflex as rx
from ..navigation import routes
# Aquest document és per crear un estànder de tots el projectes que faig.

def projectes_destacats()->rx.Component:
    """Creem la secció on es mostren els projectes que vaig fent"""
    imatge_task_timer = rx.color_mode_cond(
                        dark=rx.image(src = 'Logo_StudyTimer_white.svg', alt='Logo TaskTimer',width='2.5em',decoding="async", aria_label="Logo TaskTimer mode blanc"),
                        light=rx.image(src= 'Logo_StudyTimer.svg', alt='Logo TaskTimer', width='2.5em',decoding="async", aria_label='Logo TaskTimer mode fosc'),
                    )# rx.color_mode_cond
    image_YEYE = rx.color_mode_cond(
        dark=rx.image(src='YEYE_favico_dark.svg', alt='Logo YEYE', width='2em', decoding='async'),
        light=rx.image(src='YEYE_favico_white.svg', alt='Logo YEYE', width='2em', decoding='async'),
    )
    return rx.container(
        rx.heading(
            'Projectes destacats',
            size = '5',
            weight='bold',
            align='left',
            as_='h2',
            aria_label='Projectes destecats',
        ), # rx.heading
        # PROJECTE TASKTIMER
        rx.card(
            rx.hover_card.root(
                rx.hover_card.trigger(
                    rx.link(
                        rx.flex(
                            # fem que canvii el logo en canviar el color de fons
                            imatge_task_timer,
                            rx.box(
                                rx.heading('TaskTimer', as_='h2'),
                                rx.text(
                                    'Primer projecte personal',
                                ), #rx.text
                            ), #rx.box
                            spacing='2'
                        ), # rx.flex
                        href= routes.TASK_TIMER,
                        aria_label='Link del projecte TastkTimer',
                        # Fem que s'obri una pastanya nova
                        is_external=True,
                    ), #rx.link
                ), #rx.hover_card.trigger
                rx.hover_card.content(
                        rx.text('Aquesta és la meva primera aplicació, encara està en fase de desenvolupant, disculpeu les molèsties :/'),
                ), # rx.hover_card.content
            ), #rx.hover_card.root     
            align_items='center',
            margin_top='1em',
            width='100%',
        ), # rx.card
        # PROJECTE PERRUQUERIA YEYE
        rx.card(
            rx.hover_card.root(
                rx.hover_card.trigger(
                    rx.link(
                        rx.flex(
                            # fem que canvii el logo en canviar el color de fons
                            image_YEYE,
                            rx.box(
                                rx.heading('Perruqueria yeye', as_='h2'),
                                rx.text(
                                    'Primer projecte real',
                                ), #rx.text
                            ), #rx.box
                            align='center',
                            spacing='2'
                        ), # rx.flex
                        href= routes.YEYE_HAIR_STYLE_CA,
                        aria_label='Link del la pàgian web de la perruqueria YEYE',
                        # Fem que s'obri una pastanya nova
                        is_external=True,
                    ), #rx.link
                ), #rx.hover_card.trigger
                rx.hover_card.content(
                        rx.text('Aquesta és el meu projecte per a una empresa real, espero que ús agradi :)'),
                ), # rx.hover_card.content
            ), #rx.hover_card.root     
            align_items='center',
            margin_top='1em',
            width='100%',
        ), # rx.card
        width='100%',
        align='center',
    )



