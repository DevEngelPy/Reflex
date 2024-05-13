import reflex as rx

def navbar()->rx.Component:
    return rx.hstack(
        rx.text(
            "DevEngel",
            heigth="40px"
        ),
        position="sticky",
        bg="blue",
        paddimg_x = "16px",
        padding_y= "16px",
        index_z = "5"
    )