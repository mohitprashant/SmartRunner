import hashlib


def hash_string_sha256(plaintext):
    if type(plaintext) is not str:
        raise Exception("Given arguments is not of type str")

    return hashlib.sha256(plaintext.encode()).hexdigest()
