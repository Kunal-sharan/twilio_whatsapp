
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# load_dotenv()

app = Flask(__name__)
# run_with_lt(app)
account_sid = "AC073967f980dd387f56e1235ec5cc56b8"
auth_token = "8b89472feab24f8e587b6ebc2c935915"
client = Client(account_sid, auth_token)

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route('/message', methods=['POST'])
def reply():
    message = request.form.get('Body').lower()
    if message:
        return respond(f'Thank you for your message! A member of our team will be in touch with you soon.')

if __name__ == "__main__": 
  app.run()
