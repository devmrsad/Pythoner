headers = [
    {"name": "PNG", "header": b"\x89PNG\r\n\x1a\n"},
    {"name": "JPEG", "header": b"\xff\xd8\xff"},
    {"name": "BMP", "header": b"\x42\x4d"},
    {"name": "TIFF", "header": b"\x49\x49\x2a\x00"},
    {"name": "GIF", "header": b"\x47\x49\x46\x38"},
    {"name": "ZIP", "header": b"\x50\x4b\x03\x04"},
    {"name": "ELF", "header": b"\x7fELF"},
    {"name": "PDF", "header": b"\x25\x50\x44\x46"},
    {"name": "MP3", "header": b"\x49\x44\x33"},
    {"name": "MPEG", "header": b"\xff\xfb"},
    {"name": "PDDF", "header": b"\x00\x00\x01\x00"},
    {"name": "ICO", "header": b"\x00\x01\x00\x00"},
]

def data_recovery(data):
    formats = []
    for header in headers:
        while True:
            index = data.find(header["header"])
            if index == -1:
                break
            data = data[:index] + data[index + len(header["header"]):]
            formats.append(header["name"])
    return formats


formats = data_recovery(b'\x89PNG\r\n\x1a\nBMII*\x00\xff\xd8\xff\xff\xd8\xff\x00\x00\x01\x00\x00')
print(formats)