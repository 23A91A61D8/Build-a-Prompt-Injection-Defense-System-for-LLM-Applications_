class SecurityPolicy:
    def __init__(self, level="balanced"):
        """
        Security levels:
        - strict → block everything suspicious
        - balanced → allow minor cases, block major threats
        """
        self.level = level

    def should_block(self, threat_type):
        """
        Decide action based on threat type and policy level
        """

        strict_rules = [
            "PROMPT_INJECTION",
            "JAILBREAK",
            "PROMPT_LEAK",
            "INDIRECT_INJECTION",
            "UNSAFE_CONTENT",
            "UNSAFE_OUTPUT"
        ]

        balanced_rules = [
            "PROMPT_INJECTION",
            "JAILBREAK",
            "INDIRECT_INJECTION",
            "UNSAFE_CONTENT"
        ]

        if self.level == "strict":
            return threat_type in strict_rules

        elif self.level == "balanced":
            return threat_type in balanced_rules

        return False