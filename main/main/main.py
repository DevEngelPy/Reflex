import reflex as rx
from main.components.navbar import navbar
from main.views.header.header import header
class State(rx.State):
    pass

#pag index
def index()->rx.Component:
    return rx.vstack(
        navbar(),
        header()
    )


#ibtegracion del index
app = rx.App() #crear obj
app.add_page(index) #ionteggar funcion (`pag)
app.compile() #compilacion