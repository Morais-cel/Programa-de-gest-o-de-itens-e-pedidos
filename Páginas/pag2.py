from flet import *

def page_inicial(page: Page):

    def list_suj_func(e):
        suj=["Disco de freio", "Discos diagrama para tacógrafo (24 hr, 125 Km/h)", "Discos diagrama para tacógrafo (7 dias, 125 Km/h)", "Elemento de combustível", "Elemento filtrante", "Filtro bi-combustível", "Filtro blindado para óleo hidráulico",
            "Filtro carburente", "Filtro de ar", "Filtro de ar condicionado", "Filtro de ar de cabine", "Filtro de cabine", "Filtro de carburante", "Filtro de combustível", "Filtro de óleo", "Filtro de óleo de motor", "Filtro de óleo lubrificante",
            "Filtro hidráulico", "Filtro para cabine", "Filtro para óleo/combustível", "Filtro secador do ar", "Filtro separador água/combustível", "Óleo", "Pastilha de freio", "Secador de ar", "Separador de água"]
        #input=Itens.controls[1].content.controls[1].content.controls[0].value
        for item in suj:
            if input in item:
                print(item)

    def def_view(e):
        mod=e.control.data
        if len(Itens.controls)==2:
            Itens.controls.pop()
        match mod:
            case 'Add_item':
                Itens.controls.append(
                    Container(
                        width=page.window.width-30,
                        height=page.window.height-135,
                        content=Column(
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Container(
                                            content=Text(
                                                        value='Adição de itens ao estoque',
                                                        weight=FontWeight.BOLD,
                                                        color=colors.BLACK,
                                                        size=19
                                                ),
                                            height=70,
                                            width=page.window.width-250,
                                            bgcolor=colors.WHITE12,
                                            alignment=alignment.center,
                                            border_radius=border_radius.all(5)
                                        ),
                                        Container(
                                            content=Column(
                                                        spacing=5,
                                                        controls=[
                                                            TextField(
                                                                label='Produto',
                                                                on_change=list_suj_func,
                                                            ),
                                                            Row(
                                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                                controls=[
                                                                    TextField(
                                                                        label='Marca',
                                                                        on_change=list_suj_func
                                                                    ),
                                                                    Icon(
                                                                        name=Icons.ARROW_FORWARD_ROUNDED,
                                                                    ),
                                                                    TextField(
                                                                        label='Modelo',
                                                                        on_change=list_suj_func
                                                                    ),
                                                                ]
                                                            ),
                                                            Row(
                                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                                controls=[
                                                                    TextField(
                                                                        label='Tipo de veículo',
                                                                        on_change=list_suj_func
                                                                    ),
                                                                    Icon(
                                                                        name=Icons.ARROW_FORWARD_ROUNDED,
                                                                    ),
                                                                    TextField(
                                                                        label='Placa',
                                                                        on_change=list_suj_func
                                                                    ),
                                                                ]
                                                            ),
                                                        ]
                                            ),
                                            height=page.window.height-400,
                                            width=page.window.width-60,
                                            bgcolor=colors.WHITE12,
                                            border_radius=border_radius.all(5),
                                            padding=5
                                        )
                                    ]
                        ),
                        bgcolor=colors.WHITE12,
                        border_radius=border_radius.all(5),
                        padding=5
                    )
                )
                page.update()
                pass
            case 'Rem_item':
                Itens.controls.append(
                    Container(
                        width=100,
                        height=100,
                        content=Column(
                                    controls=[
                                        Container(
                                            
                                        )
                                    ]
                        ),
                        bgcolor=colors.BLUE
                    )
                )
                page.update()
                pass
            case 'List':
                pass
            case 'Tasks':
                pass
        pass


    Itens=Column(
            width=page.window.width,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                    Container(
                        width=page.window.width/1.3,
                        border_radius=border_radius.all(5),
                        height=70,
                        bgcolor=colors.WHITE10,
                        content=Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                ElevatedButton(
                                            content=Column(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        spacing=2,
                                                        controls=[
                                                                Icon(
                                                                    name=Icons.ADD,
                                                                    size=22
                                                                ),
                                                                Text(
                                                                    value='Adicionar item',
                                                                    text_align=TextAlign.CENTER,
                                                                    size=12
                                                                )
                                                        ]
                                                    ),
                                            width=110,
                                            height=90,
                                            style=ButtonStyle(
                                                        shape=ContinuousRectangleBorder(radius=1)
                                                    ),
                                            bgcolor=colors.TRANSPARENT,
                                            elevation=0,
                                            data='Add_item',
                                            on_click=def_view
                                    ),
                                ElevatedButton(
                                            content=Column(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        spacing=2,
                                                        controls=[
                                                                Icon(
                                                                    name=Icons.REMOVE_CIRCLE_OUTLINE_ROUNDED,
                                                                    size=22
                                                                ),
                                                                Text(
                                                                    value='Remover item',
                                                                    text_align=TextAlign.CENTER,
                                                                    size=12
                                                                )
                                                        ]
                                                    ),
                                            width=110,
                                            height=90,
                                            style=ButtonStyle(
                                                        shape=ContinuousRectangleBorder(radius=1)
                                                    ),
                                            bgcolor=colors.TRANSPARENT,
                                            elevation=0,
                                            data='Rem_item',
                                            on_click=def_view
                                    ),
                                ElevatedButton(
                                            content=Column(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        spacing=2,
                                                        controls=[
                                                                Icon(
                                                                    name=Icons.LIST_ALT_ROUNDED,
                                                                    size=22
                                                                ),
                                                                Text(
                                                                    value='Listar itens',
                                                                    text_align=TextAlign.CENTER,
                                                                    size=12
                                                                )
                                                        ]
                                                    ),
                                            width=110,
                                            height=90,
                                            style=ButtonStyle(
                                                        shape=ContinuousRectangleBorder(radius=1)
                                                    ),
                                            bgcolor=colors.TRANSPARENT,
                                            elevation=0,
                                            data='List',
                                            on_click=def_view
                                    ),
                                ElevatedButton(
                                            content=Column(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        spacing=2,
                                                        controls=[
                                                                Icon(
                                                                    name=Icons.TASK_ALT_OUTLINED,
                                                                    size=22
                                                                ),
                                                                Text(
                                                                    value='Quadro de avisos',
                                                                    text_align=TextAlign.CENTER,
                                                                    size=12
                                                                )
                                                        ]
                                                    ),
                                            width=130,
                                            height=90,
                                            style=ButtonStyle(
                                                        shape=ContinuousRectangleBorder(radius=1)
                                                    ),
                                            bgcolor=colors.TRANSPARENT,
                                            elevation=0,
                                            data='Tasks',
                                            on_click=def_view
                                    ),
                            ]
                        )
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