import vonage
import os

V_KEY = os.getenv("V_KEY")
V_SECRET = os.getenv("V_SECRET")

def send_sms(phone, msg):
    client = vonage.Client(key=V_KEY, secret=V_SECRET)
    sms = vonage.Sms(client)
    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": phone,
            "text": msg,
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

if __name__ == "__main__" :
    phone = 15159665573
    msg = "deip ec2 is Normal"
    send_sms(phone, msg)