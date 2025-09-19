
import reflex as rx


def my_services() -> rx.Component:
    """This component will show all of my services"""
    return rx.center(
        rx.vstack(
            rx.fragment(
                rx.heading(
                    "TRANSFORMA LA TEVA PRESENCIA DIGITAL",
                    font_size="clamp(16px, 3.8vw, 42px)",
                    color_scheme='indigo',
                    text_align='center',
                    high_contrast=True,
                    as_='h2',
                    max_width='70vw'   
                ), 
                rx.text(
                    "Augmenta la teva presencia a un nivell superior!",
                    font_size="clamp(10px, 2.1vw, 16px)",
                    font_weight='700', #Estilitzem el text en negreta.
                ),# rx.text
                margin_bottom = '1erm'
            ), #rx.box
            rx.section(),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Característica"),
                        rx.table.column_header_cell("Pack Simple (100€)"),
                        rx.table.column_header_cell("Pack Plus (200€)"),
                    ),
                ),
                rx.table.body(
                    rx.table.row(
                        rx.table.row_header_cell("Pàgina web"),
                        rx.table.cell("Web essencial: serveis, horaris i contacte en un sol lloc"),
                        rx.table.cell("Tot el del Pack Simple amb més velocitat i optimització"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("SEO bàsic"),
                        rx.table.cell("Opcional +50€ (millor visibilitat a Google)"),
                        rx.table.cell("Inclòs (textos i estructura optimitzats)"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Domini personalitzat *"),
                        rx.table.cell("Subdomini gratuït: www.elteunegoci.nauvi.cat*"),
                        rx.table.cell("Subdomini gratuït: www.elteunegoci.nauvi.cat*"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Allotjament Servidor *"),
                        rx.table.cell("1r any gratuït amb Nauvi.cat. Després 5 €/mes *"),
                        rx.table.cell("1r any gratuït amb Nauvi.cat. Després 5 €/mes *"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Modificacions inicials"),
                        rx.table.cell("1 mes gratuït després de l’entrega oficial"),
                        rx.table.cell("1 mes gratuït després de l’entrega oficial"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Modificacions posteriors"),
                        rx.table.cell("Pàgina nova: 100 €. Altres canvis: a pressupostar"),
                        rx.table.cell("Pàgina nova: 100 €. Altres canvis: a pressupostar"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Optimització d'imatges"),
                        rx.table.cell("No s'inclou"),
                        rx.table.cell("Inclosa (compressió i adaptació per velocitat)"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Valor afegit"),
                        rx.table.cell("Preu competitiu, ideal per començar."),
                        rx.table.cell("Web més ràpida i millor posicionada a Google."),
                    ),
                ),
                variant='surface',
                size='3',
            ), # rx.table.root()
            rx.section(),
            rx.container(
                rx.heading("- Condicions de domini i allotjament", size="5", margin_bottom="0.5em", as_='h3'),
                rx.unordered_list(
                    rx.list_item(
                        "Subdomini gratuït: tots els packs inclouen un subdomini de la forma ",
                        rx.text("www.elteunegoci.nauvi.cat", as_="span", font_weight="bold"),
                        ", amb allotjament gratuït durant el primer any."
                    ),
                    rx.list_item(
                        "Domini propi: si prefereixes un domini personalitzat (.com, .cat, .es…), la compra del domini és responsabilitat teva. Nauvi s’encarrega de connectar-lo al servidor sense cost extra."
                    ),
                    rx.list_item(
                        "En aquest cas, l’allotjament és gratuït el primer mes, i posteriorment té un cost de ",
                        rx.text("5 €/mes (60 €/any)", as_="span", font_weight="bold"),
                        "."
                    ),
                    rx.list_item(
                        "En qualsevol moment pots traslladar la teva web a un altre proveïdor sense cap cost afegit."
                    ),
                ),
                size='3',
            ), # rx.container
            rx.link(
                rx.button(
                    "Contacta'm per WhatsApp",
                    color_scheme='green',
                    size='4',
                    variant='solid',
                    border_radius='full',
                ),
                href="https://wa.me/34661139326",
                is_external=True,
            ), 
            margin_top='1.5em', 
            align = "center",
            max_width='80vw',
        ), #rx.vstack
        height='100%',
        width='100%',
    )
