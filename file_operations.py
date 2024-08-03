# file_operations.py
import base64
import binascii
import gzip
import os

def read_file(file_path):
    """Read the content of a file."""
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path, data):
    """Write data to a file."""
    with open(file_path, 'wb') as file:
        file.write(data)

def encode_url(data):
    """Encode data using URL encoding."""
    return base64.urlsafe_b64encode(data)

def encode_html(data):
    """Encode data for HTML."""
    return base64.b64encode(data).decode('ascii')

def encode_base64(data):
    """Encode data using Base64."""
    return base64.b64encode(data)

def encode_ascii_hex(data):
    """Encode data using ASCII Hex."""
    return binascii.hexlify(data).decode('ascii')

def encode_hex(data):
    """Encode data using Hex."""
    return binascii.hexlify(data).decode('ascii')

def encode_octal(data):
    """Encode data using Octal."""
    return ''.join(format(byte, 'o') for byte in data)

def encode_binary(data):
    """Encode data using Binary."""
    return ''.join(format(byte, '08b') for byte in data)


def decode_url(data):
    """Decode URL encoded data."""
    return base64.urlsafe_b64decode(data)

def decode_html(data):
    """Decode HTML encoded data."""
    return base64.b64decode(data)

def decode_base64(data):
    """Decode Base64 encoded data."""
    return base64.b64decode(data)

def decode_ascii_hex(data):
    """Decode ASCII Hex encoded data."""
    return binascii.unhexlify(data.encode('ascii'))

def decode_hex(data):
    """Decode Hex encoded data."""
    return binascii.unhexlify(data.encode('ascii'))

def decode_octal(data):
    """Decode Octal encoded data."""
    return bytes(int(data[i:i+3], 8) for i in range(0, len(data), 3))

def decode_binary(data):
    """Decode Binary encoded data."""
    return bytes(int(data[i:i+8], 2) for i in range(0, len(data), 8))



def string_to_bytes(key_str):
    """Convert a string key to bytes."""
    return key_str.encode('utf-8')

def encrypt_data(data, key_str, encoding_format):
    """Encrypt data based on the selected encoding format."""
    key = string_to_bytes(key_str)
    if encoding_format == 'url':
        return encode_url(data)
    elif encoding_format == 'html':
        return encode_html(data)
    elif encoding_format == 'base64':
        return encode_base64(data)
    elif encoding_format == 'ascii_hex':
        return encode_ascii_hex(data)
    elif encoding_format == 'hex':
        return encode_hex(data)
    elif encoding_format == 'octal':
        return encode_octal(data).encode('ascii')
    elif encoding_format == 'binary':
        return encode_binary(data).encode('ascii')
    else:
        raise ValueError("Unsupported encoding format")

def decrypt_data(data, key_str, encoding_format):
    """Decrypt data based on the selected encoding format."""
    key = string_to_bytes(key_str)
    if encoding_format == 'url':
        return decode_url(data)
    elif encoding_format == 'html':
        return decode_html(data)
    elif encoding_format == 'base64':
        return decode_base64(data)
    elif encoding_format == 'ascii_hex':
        return decode_ascii_hex(data)
    elif encoding_format == 'hex':
        return decode_hex(data)
    elif encoding_format == 'octal':
        return decode_octal(data.decode('ascii'))
    elif encoding_format == 'binary':
        return decode_binary(data.decode('ascii'))
    else:
        raise ValueError("Unsupported encoding format")

def get_key(file_path):
    """Retrieve the secret key associated with the file."""
    key_path = f"{file_path}.key"
    if os.path.exists(key_path):
        with open(key_path, 'r') as file:
            return file.read().strip()
    return None

def set_key(file_path, key):
    """Store the secret key associated with the file."""
    key_path = f"{file_path}.key"
    with open(key_path, 'w') as file:
        file.write(key)
