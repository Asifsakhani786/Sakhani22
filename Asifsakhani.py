# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))