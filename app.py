import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN="sqlite:///projeto2.db"

engine=create_engine(CONN, echo = True)
Session=sessionmaker(bind=engine)
session=Session()

def main(page=ft.Page):

    list_prod=ft.ListView()

    def cadastrar(e):
        try:
            new_prod=Produto(titulo=prod.value, preco=preco.value)
            session.add(new_prod)
            session.commit()
            list_prod.controls.append(
                ft.Container(
                    ft.Text(prod.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                )
            )
            txt_error.visible=False
            txt_acerto.visible=True
        except:
            txt_error.visible=True
            txt_acerto.visible=False
        page.update()
        print('Produto salvo com sucesso!')

    page.title='Cadastro App'
    txt_error=ft.Container(ft.Text('Erro ao salvar porduto'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_acerto=ft.Container(ft.Text('Produto salvo com sucesso'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)
    txt_tlt=ft.Text('Título do produto')
    prod=ft.TextField(label='Digite o produto', text_align=ft.TextAlign.LEFT)
    txt_preco=ft.Text('Preço do produto')
    preco=ft.TextField(value='0', label='Digite o preço', text_align=ft.TextAlign.LEFT)
    btn_prod=ft.ElevatedButton('Cadastrar', on_click=cadastrar)

    page.add(
        txt_error,
        txt_acerto,
        txt_tlt,
        prod,
        txt_preco,
        preco,
        btn_prod
    )

    for p in session.query(Produto).all():
        list_prod.controls.append(
            ft.Container(
                 ft.Text(p.titulo),
                 bgcolor=ft.colors.BLACK12,
                 padding=15,
                 alignment=ft.alignment.center,
                 margin=3,
                 border_radius=10
            )
        )

    page.add(
        list_prod
    )

ft.app(target=main)