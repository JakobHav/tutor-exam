# Ex3: Strings (20P)

def encode(msg, key):
    ...


def validate_email(email):
    ...


if __name__ == "__main__":
    assert encode("abc", 3) == "def"
    assert encode("Hallo Welt!", 5) == "Mfqqt%\\jqy&"

    assert validate_email("user@example.com")
    assert validate_email("test.user_123@domain.co.uk") is False
    assert validate_email("invalid@@email.com") is False
