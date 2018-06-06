# coding=<utf-8>

from urllib import parse
import base64
import binascii


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
        try:
            protocol = string[:string.index("//")]+"//"
        except ValueError:
            protocol = "http://"
        string = string.replace("http://", "", 1)
        string = string.replace("https://", "", 1)
        if "/" in string:
            string = parse.quote(string.replace(string[:string.index("/")], string[:string.index("/")].encode("idna").decode("utf-8"), 1), safe="%/:=&?~#+!$,;'@()*[]")
        else:
            string = string.encode("idna").decode("utf-8")
        string = protocol+string
        return string

    @staticmethod
    def url_decode(string):
        try:
            protocol = string[:string.index("//")]+"//"
        except ValueError:
            protocol = "http://"
        string = string.replace("http://", "", 1)
        string = string.replace("https://", "", 1)
        if "/" in string:
            string = parse.unquote(string.replace(string[:string.index("/")], bytearray(string[:string.index("/")], "idna").decode("idna"), 1), encoding='utf-8')
        else:
            string = bytearray(string, "idna").decode("idna")
        string = protocol+string
        return string

    @staticmethod
    def image_base64_encode(filename, dataurl=False):
        with open(filename, "rb") as image_file:
            data = image_file.read()
            if dataurl:
                filetype = binascii.hexlify(data[:2])
                if filetype == b'8950':
                    string = base64.b64encode(data)
                    string = string.decode('ascii')
                    result = '<img src="data:{};base64,{}" >'.format(
                        'image/png', string)
                elif filetype == b'ffd8':
                    string = base64.b64encode(data)
                    string = string.decode('ascii')
                    result = '<img src="data:{};base64,{}" >'.format(
                        'image/jpeg', string)
                elif filetype == b'4749':
                    string = base64.b64encode(data)
                    string = string.decode('ascii')
                    result = '<img src="data:{};base64,{}" >'.format(
                        'image/gif', string)
            else:
                string = base64.b64encode(data)
                result = string.decode('ascii')
        return result
