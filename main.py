from pyscript import display, document

def generate_message():
    output_div = document.querySelector("#output")
    output_div.innerText = ""

    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value

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


    full_message = profile + "\n" + notes
    output_div.innerText = full_message
