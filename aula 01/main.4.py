import flet as ft


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha aplicação flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # Definição de função
    def idade(e):
        num1 = int(input_valor.value)
        idade = 2025 - num1
        if idade >= 18:
            txt_resultado.value = "Ja é adulto"
            page.update()
        elif idade < 18:
            txt_resultado.value = "Ainda é criança"
            page.update()


    # Criação de componentes
    input_valor = ft.TextField(label="Digite uma data", hint_text="Ex: 13/05/2007")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=idade,
    )
    txt_resultado = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                ft.ResponsiveRow(
                    [
                        input_valor,
                        btn_enviar,
                        txt_resultado,
                    ]
                )
            ]
        )
    )

ft.app(main)