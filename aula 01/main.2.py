import flet as ft


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha aplicação flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # Definição de função
    def par_impar(e):
        num1 = int(input_valor.value)
        if num1 % 2 == 0:
            txt_resultado.value = "é par"
            page.update()
        else:
            txt_resultado.value = "é impar"
            page.update()


    # Criação de componentes
    input_valor = ft.TextField(label="Digite um numero", hint_text="Ex: 1")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=par_impar,
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