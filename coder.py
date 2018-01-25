# coding=<utf-8>

from urllib import parse
import base64


class Coder:
    @staticmethod
    def base64_decode(string):
        try:
            string = base64.b64decode(string)
            string = string.decode('utf-8')
        except ValueError:
            string = ("ValueError: The input string contains non-ASCII "
                      "characters or have been corrupted")
        return string

    @staticmethod
    def base64_encode(string):
        string = base64.b64encode(bytes(string, 'utf-8'))
        string = string.decode('ascii')
        return string

    @staticmethod
    def url_encode(string):
        string = parse.quote(string, safe="%/:=&?~#+!$,;'@()*[]")
        return string

    @staticmethod
    def url_decode(string):
        string = parse.unquote(string, encoding='utf-8')
        return string

    @staticmethod
    def image_base64_encode(filename):
        with open(filename, "rb") as image_file:
            string = base64.b64encode(image_file.read())
            string = string.decode('ascii')
        return string
