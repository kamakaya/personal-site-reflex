from rxconfig import config
import reflex as rx
import os

from .helpers.projects import project_item, ProjectsState
from .helpers.certifications import get_certifications

resume_url = "RESUME_URL"

def index() -> rx.Component:

    RESUME_URL = os.environ[resume_url] if resume_url in os.environ else "https://drive.google.com/file/d/1EiMvYfULcOgO7esFHOcfvuBCgZsPfMIs/view?usp=sharing"

    return rx.fragment(
        rx.box(
            rx.image(
                src="/header_background.jpg",
                html_width="100%"
            ),
            rx.hstack(
                rx.image(
                    src="/rommel_headshot.png",
                    height="12em",
                    width="12em",
                    # padding_top="-10%",
                    ml=40,
                    mt="-115px",
                ),
                rx.link(
                    rx.button(
                        rx.icon(
                            tag="download",
                            height="1em",
                            width="1em",
                            mr=2
                        ),
                        "Resume", 
                        variant="outline", 
                        size="lg",
                        position="absolute",
                        right=40,
                    ),
                    href=RESUME_URL
                ),
            ),
        ),
        rx.box(
            rx.heading(
                "Rommel Silva", 
                font_size="3em",
                align="left",
                ml=40,
                padding_top="2%",
            ),
            rx.box(
                "I'm a technology consultant with a background in application development and cloud-based infrastructure. I'm currently based in Denver, CO ⛰, originally from Angola 🇦🇴 , but at heart I'm a citizen of the world.",
                ml=40,
                mr=40,
                font_size="1em"
            ),
            rx.hstack(
                rx.icon(
                    tag="phone",
                    height="1em",
                    width="1em",
                ),
                rx.text("(561)221-7088", font_size="1em", ml=5),
                ml=40,
                padding_top="0.8%"
            ),
            rx.hstack(
                rx.icon(
                    tag="email",
                    height="1em",
                    width="1em",
                ),
                rx.link("kamakayasilva@gmail.com", font_size="1em", ml=5, href="mailto:kamakayasilva@gmail.com"),
                ml=40,
                padding_top="0.5%"
            ),
            rx.hstack(
                rx.icon(
                    tag="link",
                    height="1em",
                    width="1em",
                ),
                rx.link(
                    "linkedin.com/in/kamakaya", 
                    font_size="1em", 
                    ml=5, 
                    href="https://www.linkedin.com/in/kamakaya/",
                    is_external=True
                ),
                ml=40,
                padding_top="0.5%"
            ),
        ),
        rx.box(
            rx.heading(
                "Latest Projects", 
                font_size="2em",
                align="left",
                ml=40,
                padding_top="3%",
            ),
            rx.list(                
                rx.foreach(ProjectsState.projects, project_item) 
            ),
            # padding_bottom="3em"
        ),
        rx.box(
            rx.heading(
                "Certifications", 
                font_size="2em",
                align="left",
                ml=40,
                padding_top="3%",
            ),
            rx.container(
                rx.hstack(
                    get_certifications("terraform"),
                    get_certifications("ace")
                ),
                center_content=True,
            )
        ),
        rx.box(
            padding_bottom="3em"
        )
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
