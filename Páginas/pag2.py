from flet import *

def page_inicial(page: Page):

    def def_view(e):
        pass

    Itens=Column(
            controls=[
                    Row(
                        width=page.window.width,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Container(
                                width=page.window.width/1.3,
                                height=70,
                                bgcolor=colors.WHITE30,
                                border_radius=border_radius.all(5),
                                content=NavigationBar(
                                                    destinations=[
                                                        NavigationBarDestination(
                                                            icon=Icons.PLUS_ONE_ROUNDED,
                                                            label="Adicionar Item"
                                                        ),
                                                        NavigationBarDestination(
                                                            icon=Icons.REMOVE_CIRCLE_OUTLINE_ROUNDED,
                                                            label="Remover Item"
                                                        ),
                                                        NavigationBarDestination(
                                                            icon=Icons.LIST_ALT_ROUNDED,
                                                            label='Listar itens'
                                                        ),
                                                        NavigationBarDestination(
                                                            icon=Icons.TASK_ALT_ROUNDED,
                                                            label='Quadro de avisos'
                                                        )
                                                    ],
                                                    on_change=def_view
                                                )
                            )
                        ]
                    )
        ]
    )

    page2=Container(
                width=page.window.width,
                height=page.window.height,
                bgcolor=colors.BLACK,
                content=Itens
    )

    return page2