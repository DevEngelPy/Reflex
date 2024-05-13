import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Dev Engel", size="5"),
        rx.text("@DEvEngel"),
        rx.text("Hola Mi nombre es engel"),
        rx.text("jbferiubferbfiub")
    )