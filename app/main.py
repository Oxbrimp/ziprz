def file_to_binary_string(filepath):
    with open(filepath, "rb") as f:  # Reads file in binary mode
        byte_data = f.read() # Loads entire file into memory as raw bytes
 
    binary_string = ''.join(format(byte,'08b') for byte in byte_data) # Turns each byte into an 8-bit binary string and concatenates them all together
    return binary_string

