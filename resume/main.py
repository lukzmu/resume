import os

from builder.services import BuilderService

readme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "README.md"))

builder = BuilderService(
    person_name="Lukasz Zmudzinski",
    person_title="Python Engineer",
    person_contact=[
        "lukasz@zmudzinski.me",
        "github.com/lukzmu",
<<<<<<< HEAD
        "linkedin.com/in/lukzmu",
=======
        "linkedin.com/in/lukzmu"
>>>>>>> b99b30e (Update personal contact)
    ],
    file_path=readme_path
)
builder.build()
