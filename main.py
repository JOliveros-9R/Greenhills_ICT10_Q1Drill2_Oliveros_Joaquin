from pyscript import display, document

def generate_message(e):
    output_div = document.getElementById("output")
    output_div.innerText = ""

    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    profile = f"""\
Student Profile
Name : {name}
Age : {age}
School : {school}
"""

    notes = f"""\
Notes:
{name} is currently {age} years old and studies at {school}.
This information was gathered through input fields and displayed using a multiline string in Python via PyScript."""


    display(full_message = profile + "\n" + notes())

