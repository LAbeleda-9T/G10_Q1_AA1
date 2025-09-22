from pyscript import display, document  

def send_message(e):
    name = document.getElementById("name").value
    message = document.getElementById("message").value

    if not name or not message:
        display("⚠️ Please fill out all fields.", target="form-output") #when the fields are empty
    else:
        display(f'✅ Thank you, {name}! We received your message: {message}', target='form-output') #when the fields are filled out
