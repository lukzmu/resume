import os

from builder.services import BuilderService

readme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "README.md"))

builder = BuilderService(
    person_name="Lukasz Zmudzinski",
    person_title="Python Engineer",
    person_contact=[
        "lukasz@zmudzinski.sh",
        "github.com/lukzmu",
    ],
    file_path=readme_path
)
builder.build()
