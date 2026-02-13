def encode(msg: str, key: int) -> str:
    return "".join([chr(ord(ch) + key) for ch in msg])


def validate_email(email: str) -> bool:
    if email.count("@") != 1 or email.count(".") != 1:
        return False

    local, second = email.split("@")
    site, dom = second.split(".")

    if not local.isalnum() or not site.isalnum() or not dom.isalnum():
        return False

    if len(dom) < 2:
        return False

    return True


if __name__ == "__main__":
    assert encode("abc", 3) == "def"
    assert encode("Hallo Welt!", 5) == "Mfqqt%\\jqy&"

    assert validate_email("user@example.com")
    assert validate_email("test.user_123@domain.co.uk") is False
    assert validate_email("invalid@@email.com") is False
