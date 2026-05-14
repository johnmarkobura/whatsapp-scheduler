import pywhatkit as kit
import time

# ─────────────────────────────────────────────
# WEDDING REMINDER MESSAGES
# ─────────────────────────────────────────────

messages = {
    "Mabel": {
        "phone": "",
        "message": """
paste message here
"""
    },
    "Joshua": {
        "phone": "",
        "message": """
paste message here
"""
    },
    "Faith": {
        "phone": "",
        "message": """
paste message here
"""
    },
    "Mummy": {
        "phone": "",
        "message": """
paste message here
"""
    },
    "Daddy": {
        "phone": "",
        "message": """
paste message here
"""
    },
    "Mercy": {
        "phone": "",
        "message": """
paste message here
"""
    },
}

# ─────────────────────────────────────────────
# SEND MESSAGES
# ─────────────────────────────────────────────

def send_messages():
    print("Starting to send messages...")
    print("Make sure WhatsApp Web is open in your browser!\n")
    time.sleep(3)

    for name, details in messages.items():
        print(f"Sending message to {name}...")
        try:
            kit.sendwhatmsg_instantly(
                phone_no=details["phone"],
                message=details["message"],
                wait_time=15,
                tab_close=True,
                close_time=3
            )
            print(f"✓ Message sent to {name}")
            time.sleep(10)  # Wait between messages
        except Exception as e:
            print(f"✗ Failed to send to {name}: {e}")

    print("\nAll messages sent!")

# ─────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    send_messages()