import base64

def base64_encoder_decoder(data, operation):
    """
    Encode or decode a string using base64.

    Args:
        data (str): The string to encode or decode.
        operation (str): The operation to perform. Either "encode" or "decode".

    Returns:
        str: The result of the encoding or decoding operation.
    """
    if operation == "encode":
        # Encode the input string using base64.
        encoded_bytes = base64.b64encode(data.encode("utf-8"))
        return encoded_bytes.decode("utf-8")
    elif operation == "decode":
        # Decode the input string from base64.
        decoded_bytes = base64.b64decode(data.encode("utf-8"))
        return decoded_bytes.decode("utf-8")
    else:
        raise ValueError("Invalid operation. Must be 'encode' or 'decode'.")

# Example usage
input_string = "This is a test string."
encoded_string = base64_encoder_decoder(input_string, "encode")
print("Encoded string:", encoded_string)
decoded_string = base64_encoder_decoder(encoded_string, "decode")
print("Decoded string:", decoded_string)
