import reflex as rx

config = rx.Config(
    app_name="portafoli",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],

    # Treiem que es vegi que s'ha creat amb el framework de reflex
    show_built_with_reflex=False,
    
)