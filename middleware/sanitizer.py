import re

class InputSanitizer:
    def __init__(self):
        pass

    def clean(self, text: str) -> str:
        # 1. Remove leading/trailing spaces
        text = text.strip()

        # 2. Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text)

        # 3. Remove newlines/tabs
        text = text.replace("\n", " ").replace("\t", " ")

        return text



if __name__ == "__main__":
    sanitizer = InputSanitizer()

    test_input = "   Hello     \n  world\t\t  "
    cleaned = sanitizer.clean(test_input)

    print("Original:", test_input)
    print("Cleaned:", cleaned)