def parse_message(message: str) -> dict:
    # figure out: does this message look like a booking request?
    # hint: check if certain words appear in message.lower(), e.g. "book", "table", "reservation"

    text = message.lower()
    booking_keywords = ["book", "table", "reservation"]
    if any(keyword in text for keyword in booking_keywords):
        return {
            "type": "booking",
            "message": message,
        }
    else:
        return {
            "type": "other",
            "message": message,
        }


def main():
    print(parse_message("Can I book a table for 4 tomorrow at 7pm?"))
    print(parse_message("What are your opening hours?"))

if __name__ == "__main__":
    main()
    