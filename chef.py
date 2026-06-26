import base64


def encode_base64(data: str) -> str:
    """Encodes a string into Base64 format."""
    encoded_bytes = base64.b64encode(data.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


def decode_base64(data: str) -> str:
    """Decodes a Base64 string back to text."""
    try:
        decoded_bytes = base64.b64decode(data.encode("utf-8"))
        return decoded_bytes.decode("utf-8")
    except Exception:
        return "Error: Invalid Base64 data."


def encode_hex(data: str) -> str:
    """Encodes a string into Hexadecimal format."""
    return data.encode("utf-8").hex()


def decode_hex(data: str) -> str:
    """Decodes a Hexadecimal string back to text."""
    try:
        return bytes.fromhex(data).decode("utf-8")
    except Exception:
        return "Error: Invalid Hexadecimal data."


def main():
    print("--- kimleb's Chef ---")
    print("Available Formats:")
    print("1. Base64")
    print("2. Hexadecimal")

    # Get format choice
    format_choice = input("\nChoose format (1 or 2): ").strip()
    if format_choice not in ["1", "2"]:
        print("Invalid choice. Exiting.")
        return

    # Get operation choice
    print("\nAvailable Operations:")
    print("1. Encode")
    print("2. Decode")
    operation_choice = input("Choose operation (1 or 2): ").strip()
    if operation_choice not in ["1", "2"]:
        print("Invalid choice. Exiting.")
        return

    # Get user input data
    user_input = input("\nEnter the text to process:\n").strip()

    # Process data based on choices
    if format_choice == "1":  # Base64
        if operation_choice == "1":
            result = encode_base64(user_input)
        else:
            result = decode_base64(user_input)
    else:  # Hexadecimal
        if operation_choice == "2":
            result = encode_hex(user_input)
        else:
            result = decode_hex(user_input)

    # Output the result
    print("\n--- Output ---")
    print(result)


if __name__ == "__main__":
    main()
