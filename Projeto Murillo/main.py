import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = "#2d2d2d"
    page.window.width = 290 #largura
    page.window.height = 475 #Altura

    resultado_texto = ft.Text(value="0", size=28, color="white", text_align="right")

    def atualizar_display(valor):
        if resultado_texto.value == "0":
            resultado_texto.value = valor
        else:
            resultado_texto.value += valor
        page.update()

    def calcular():
        try:
            resultado_texto.value = str(eval(resultado_texto.value))
        except Exception:
            resultado_texto.value = "Erro"
        page.update()

    def limpar():
        resultado_texto.value = "0"
        page.update()

    def apagar_ultimo():
        resultado_texto.value = resultado_texto.value[:-1] or "0"
        page.update()

    tela = ft.Container(
        content=resultado_texto,
        bgcolor="#37474F",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right
    )

    Estilo_numeros = {
        "height": 60,
        "bgcolor": "#FF0000",
        "color": "white",
        "expand": 1,
    }

    grelha_de_botoes = [
        ["C", "(", ")", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "⌫", "="],
    ]

    botoes = []

    for linha in grelha_de_botoes:
        linha_control = []
        for texto in linha:
            btn = ft.ElevatedButton(
                text=texto,
                width=60,
                height=Estilo_numeros["height"],
                bgcolor=Estilo_numeros["bgcolor"],
                color=Estilo_numeros["color"],
                expand=Estilo_numeros["expand"],
                on_click=lambda e, t=texto: (
                    atualizar_display(t) if t not in ["C", "=", "⌫"] else
                    limpar() if t == "C" else
                    calcular() if t == "=" else
                    apagar_ultimo()
                )
            )
            linha_control.append(btn)
        botoes.append(ft.Row(linha_control, spacing=5))

    page.add(
        ft.Column(
            [
                tela,
                *botoes
            ],
            spacing=10,
            horizontal_alignment=ft.alignment.center,
        )
    )

ft.app(target=main)
