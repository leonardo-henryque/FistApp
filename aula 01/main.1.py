import flet as ft


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha aplicação flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # Definição de função
    def mostrar_nome(e):
        txt_resultado.value = f"{input_nome.value} {input_sobrenome.value}"
        page.update()

    # Criação de componentes
    input_nome = ft.TextField(label="Digite seu nome", hint_text="Ex: Leonardo")
    input_sobrenome = ft.TextField(label="Digite seu sobrenome", hint_text="Ex: Henrique")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=mostrar_nome,
    )
    txt_resultado = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                ft.ResponsiveRow(
                    [
                        input_nome,
                        input_sobrenome,
                        btn_enviar,
                        txt_resultado,
                    ]
                )
            ]
        )
    )

ft.app(main)