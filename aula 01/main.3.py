import flet as ft


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha aplicação flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # Definição de função

    def somar(e):
        num1 = int(input_valor.value)
        num2 = int(input_valor2.value)
        txt_resultado.value = num1 + num2
        page.update()

    def menos(e):
        num1 = int(input_valor.value)
        num2 = int(input_valor2.value)
        txt_resultado.value = num1 - num2
        page.update()

    def divisao(e):
        num1 = int(input_valor.value)
        num2 = int(input_valor2.value)
        txt_resultado.value = num1 / num2
        page.update()

    def multiplicacao(e):
        num1 = int(input_valor.value)
        num2 = int(input_valor2.value)
        txt_resultado.value = num1 * num2
        page.update()

    # Criação de componentes
    input_valor = ft.TextField(label="Digite um numero", hint_text="Ex: 1")
    input_valor2 = ft.TextField(label="Digite um numero", hint_text="Ex: 1")

    btn_somar = ft.FilledButton(text="Adição",width=page.window.width,on_click=somar,)
    btn_menos = ft.FilledButton(text="subtração",width=page.window.width,on_click=menos,)
    btn_divisao = ft.FilledButton(text="divisão",width=page.window.width,on_click=divisao,)
    btn_multiplicacao = ft.FilledButton(text="multiplicação",width=page.window.width,on_click=multiplicacao,)

    txt_resultado = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                ft.ResponsiveRow(
                    [
                        input_valor,
                        input_valor2,
                        btn_somar,
                        btn_menos,
                        btn_divisao,
                        btn_multiplicacao,
                        txt_resultado,
                    ]
                )
            ]
        )
    )

ft.app(main)