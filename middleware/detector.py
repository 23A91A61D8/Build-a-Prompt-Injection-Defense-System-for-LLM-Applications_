import re
import yaml


class ThreatDetector:
    def __init__(self, config_path="config/security_patterns.yaml"):
        try:
            with open(config_path, "r") as file:
                self.patterns = yaml.safe_load(file)
        except Exception as e:
            print("Error loading config:", e)
            self.patterns = {}

        # Extra keywords (fallback detection)
        self.generic_attack_keywords = [
            "ignore",
            "bypass",
            "disregard",
            "override",
            "leak",
            "reveal",
            "execute",
            "hidden instruction"
        ]

    def detect_prompt_injection(self, text):
        # YAML patterns
        for pattern in self.patterns.get("prompt_injection", []):
            if re.search(pattern, text, re.IGNORECASE):
                return True

        # Fallback keyword detection (VERY IMPORTANT)
        for word in self.generic_attack_keywords:
            if word in text.lower():
                return True

        return False

    def detect_jailbreak(self, text):
        for pattern in self.patterns.get("jailbreak", []):
            if re.search(pattern, text, re.IGNORECASE):
                return True
        return False

    def detect_prompt_leak(self, text):
        for pattern in self.patterns.get("prompt_leak", []):
            if re.search(pattern, text, re.IGNORECASE):
                return True
        return False

    def analyze(self, text):
        return {
            "prompt_injection": self.detect_prompt_injection(text),
            "jailbreak": self.detect_jailbreak(text),
            "prompt_leak": self.detect_prompt_leak(text),
        }