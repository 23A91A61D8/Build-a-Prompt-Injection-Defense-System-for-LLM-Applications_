import re
import yaml


class OutputValidator:
    def __init__(self, config_path="config/security_patterns.yaml"):
        """
        Load sensitive patterns from YAML
        """
        try:
            with open(config_path, "r") as file:
                self.patterns = yaml.safe_load(file)
        except Exception as e:
            print("Error loading config:", e)
            self.patterns = {}

    def redact(self, text: str) -> str:
        """
        Replace sensitive information with placeholders
        """

        # Redact email
        text = re.sub(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}",
            "[REDACTED EMAIL]",
            text
        )

        # Redact phone numbers (10 digits)
        text = re.sub(
            r"\b\d{10}\b",
            "[REDACTED PHONE]",
            text
        )

        # Redact API keys / secrets
        text = re.sub(
            r"(api[_-]?key|password|secret)\s*[:=]\s*\S+",
            "[REDACTED SECRET]",
            text,
            flags=re.IGNORECASE
        )

        return text

    def validate(self, text: str) -> str:
        """
        Validate and clean output
        """
        return self.redact(text)
if __name__ == "__main__":
    print("Testing Output Validator...")

    validator = OutputValidator()

    test_output = """
    User email is test@gmail.com
    Phone: 9876543210
    API_KEY: 12345XYZ
    This is safe content
    """

    result = validator.validate(test_output)

    print("\nOriginal Output:\n", test_output)
    print("\nSanitized Output:\n", result)