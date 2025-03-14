from flet import *

def login(page: Page):
    def conf_func(e):
        usuario=Item.controls[0].content.controls[1].controls[0].value
        senha=Item.controls[0].content.controls[1].controls[1].value
        if usuario=='Pedro' and senha=='123':
            page.go("/pag_inicial")


    def desb_conf_func(e):
        cod1=Item.controls[0].content.controls[1].controls[0].value
        cod2=Item.controls[0].content.controls[1].controls[1].value
        if cod1 and cod2:
            Item.controls[0].content.controls[1].controls[2].controls[1].disabled=False
        else:
            Item.controls[0].content.controls[1].controls[2].controls[1].disabled=True
        page.update()
        pass

    Item=Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            width=page.window.width,
            height=page.window.height, 
            controls=[
                    Container(
                            width=page.window.width-150,
                            height=page.window.height-540,
                            bgcolor=colors.WHITE30,
                            padding=20, 
                            border_radius=border_radius.all(5),
                            content=Column(
                                        alignment=MainAxisAlignment.START,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        spacing=50,
                                        controls=[
                                                Container(
                                                        width=page.window.width-200,
                                                        height=100,
                                                        bgcolor=colors.WHITE30,
                                                        content=Text(
                                                                    value='PROGRAMA DE GESTÃO DE ITENS E PEDIDOS',
                                                                    text_align=TextAlign.CENTER,
                                                                    color=colors.BLACK,
                                                                    weight=FontWeight.BOLD,
                                                                    size=20,
                                                        ),
                                                        border_radius=border_radius.all(5),
                                                        alignment=alignment.center
                                                ),
                                                Column(
                                                    controls=[
                                                        TextField(
                                                            label='Usuário',
                                                            width=page.window.width-250,
                                                            on_change=desb_conf_func
                                                        ),
                                                        TextField(
                                                            label='Senha',
                                                            width=page.window.width-250,
                                                            on_change=desb_conf_func,
                                                        ),
                                                        Row(
                                                            width=page.window.width-250,
                                                            alignment=MainAxisAlignment.END,
                                                            controls=[
                                                                    ElevatedButton(
                                                                        text='Esqueci a senha.',
                                                                        style=ButtonStyle(
                                                                                        shape=RoundedRectangleBorder(radius=4),
                                                                        )
                                                                    ),
                                                                    ElevatedButton(
                                                                        text='Confirmar',
                                                                        style=ButtonStyle(
                                                                                        shape=RoundedRectangleBorder(radius=4)
                                                                        ),
                                                                        disabled=True,
                                                                        on_click=conf_func
                                                                    )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                ]
                            )
                    )
        ]
    )

    pag1=Container(
        width=page.window.width-33,
        height=page.window.height,
        content=Item,
        bgcolor=colors.BLACK,
    )


    return pag1

