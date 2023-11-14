import reflex as rx

certificates = {
    "terraform": {
        "certificate_title": "HashiCorp Certified: Terraform Associate (002)",
        "certificate_issuer": "Hashicorp",
        "certificate_url": "https://www.credly.com/badges/a38bc6c6-b4ce-444e-9908-b685f712dcf9/"
    },
    "ace": {
        "certificate_title": "Google Cloud Certified: Associate Cloud Engineer",
        "certificate_issuer": "Google",
        "certificate_url": "https://google.accredible.com/c8de0fe2-20de-4e59-9be1-9705fb6b0b86?_gl=1*w5yswh*_ga*MTY3NDIyODM2My4xNjk5OTAxNDMy*_ga_FSDJZHHBH0*MTY5OTkwMTQzMS4xLjEuMTY5OTkwMjc3My4wLjAuMA..#gs.0wqihd"
    }
}

def get_certifications(certificate_name: str) -> rx.link:

    return(
        rx.link(
            rx.box(
                rx.vstack(
                    rx.image(
                        src=f"/{certificate_name}_badge.png",
                        height="110px",
                        width="110px",
                        mt="20px"                            
                    ),
                    rx.center(
                        rx.vstack(
                            rx.text(
                                certificates[certificate_name]["certificate_title"],
                                font_family="sans-serif",
                                font_size="1rem",
                                mt="11px",
                                line_height="18px",
                            ),
                            rx.text(
                                f"Issuer: {certificates[certificate_name]['certificate_issuer']}",
                                font_family="sans-serif",
                                font_size="0.81rem",
                                as_="i",
                                color="#666",
                            ),
                            ml="18px",
                            mr="18px",
                        ),
                        text_align="center",
                    )
                ),
                width="150px",
                height="270px",
                border="1px solid #E2E2E2",
                border_radius="4px",
            ),
            href=certificates[certificate_name]["certificate_url"]
        )
    )