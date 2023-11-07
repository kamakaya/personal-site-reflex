from typing import List, Dict, Any, TypedDict
# import ast
import reflex as rx
import csv


PROJECTS_ICON_MAP = {
    "github": "/github.svg",
}

TECHNOLOGY_COLOR_MAP = {
    "Python": "blue",
    "Next.js": "green",
    "Docker": "orange",
}

class ProjectsState(rx.State):

    projects: list[dict[str, list]] = [
        {
            "project_name": "Discord Clone",
            "project_url": "https://github.com/kamakaya/discord-clone",
            "technologies": ["Next.js", "Prisma", "Tailwind", "Google Cloud", "Docker", "MySQL"]
        },
        {
            "project_name": "Personal Website",
            "project_url": "https://github.com/kamakaya/discord-clone",
            "technologies": ["Python", "Reflex"]
        },
        {
            "project_name": "OTP API",
            "project_url": "https://github.com/kamakaya/otp-api",
            "technologies": ["Python", "Flask", "Google Cloud", "Docker"]
        },
        {
            "project_name": "User Management REST API",
            "project_url": "https://github.com/kamakaya/authorized-users-api",
            "technologies": ["Python", "Flask", "Google Cloud", "MySQL"]
        }
    ]

def get_badge(technology: str) -> rx.Component:
    return rx.badge(technology, variant="subtle", color_scheme="gray")

def project_item(project: dict):

    return rx.box(
        rx.hstack(            
            rx.link(
                rx.button(
                    rx.image(src=PROJECTS_ICON_MAP["github"], height="20px", width="20px", mr="10px"),
                    rx.text(project["project_name"]),
                    variant="ghost",
                    justify_content="flex-start",
                    width="275px",

                ),
                href=project["project_url"].to_string(json=False),
                is_external=True
            ),
            rx.foreach(project["technologies"], get_badge)

        ),
        ml=40,
        padding_top="0.5%",
    )
