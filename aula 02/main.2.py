import flet as ft
from flet import AppBar, Text, ElevatedButton, Page, View
from flet.core.colors import Colors

def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha aplicação flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # Definição de função

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ElevatedButton(text="Navegar",width=page.window.width, on_click=lambda _: page.go("/segunda")),
                ],
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(value= f"Titulo: {input_titulo.value}"),
                        Text(value= f"Descrição: {input_descricao.value}"),
                        Text(value= f"Categoria: {input_categoria.value}"),
                        Text(value= f"Autor: {input_autor.value}"),
                    ],
                )
            )
        page.update()


    input_titulo = ft.TextField(label="Digite um titulo")
    input_descricao = ft.TextField(label="Digite uma descricao")
    input_categoria = ft.TextField(label="Digite uma categoria")
    input_autor = ft.TextField(label="Digite um autor")

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

    # Criação de componentes

    # Construir o layout

ft.app(main)