import re


class ContentSafetyClassifier:
    def __init__(self):
        """
        Define harmful content patterns (with word boundaries to avoid false positives)
        """
        self.harmful_patterns = [
            r"\bkill\b",
            r"\bsuicide\b",
            r"\bbomb\b",
            r"\battack\b",
            r"\bhate\b",
            r"\bviolence\b",
            r"\bterrorist\b",
            r"\bdrug abuse\b",
        ]

    def is_unsafe(self, text: str) -> bool:
        """
        Check if content is unsafe
        """
        for pattern in self.harmful_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return True
        return False

    def classify(self, text: str) -> str:
        """
        Return SAFE or UNSAFE
        """
        return "UNSAFE" if self.is_unsafe(text) else "SAFE"


# =========================
# TEST BLOCK
# =========================
if __name__ == "__main__":
    print("Testing Content Safety Classifier...")

    classifier = ContentSafetyClassifier()

    test_inputs = [
        "How to build a bomb",
        "I hate this person",
        "Explain machine learning",
        "How to improve coding skills"
    ]

    for text in test_inputs:
        result = classifier.classify(text)
        print("\nInput:", text)
        print("Safety:", result)