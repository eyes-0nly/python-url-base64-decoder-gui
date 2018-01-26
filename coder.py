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
        string = parse.quote(string, safe="%/:=&?~#+!$,;'@()*[]")
        return string

    @staticmethod
    def url_decode(string):
        string = parse.unquote(string, encoding='utf-8')
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
