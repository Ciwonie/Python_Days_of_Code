# Create a py file that encodes and decodes every line in bits.txt
import sys

script, input_encoding, error = sys.argv


def main(text_file, encoding, errors):
    line = text_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(text_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    byte_string = next_lang.encode(encoding, errors=errors)
    utf_string = byte_string.decode(encoding, errors=errors)
    print(f"{byte_string} <====> {utf_string}")


languages = open("bits.txt", encoding="utf-8")
main(languages, input_encoding, error)

arr = bytes([
    # Offset 0x00000000 to 0x00000015
    0x73, 0x74, 0x72, 0x65, 0x61, 0x6D, 0x74, 0x79, 0x70, 0x65, 0x64, 0x20,
    0xC3, 0xA8, 0x20, 0xE2
])
