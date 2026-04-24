import logging
import os
from datetime import datetime


class SecurityLogger:
    def __init__(self, log_dir="logs"):
        """
        Initialize logger and create logs folder
        """
        self.log_dir = log_dir

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, "security.log")

        # Avoid duplicate handlers
        self.logger = logging.getLogger("SecurityLogger")

        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    def log_event(self, input_text, threat_type, action):
        """
        Log security event
        """
        message = f"INPUT: {input_text} | THREAT: {threat_type} | ACTION: {action}"
        self.logger.info(message)
if __name__ == "__main__":
    print("Testing Logger...")

    logger = SecurityLogger()

    logger.log_event(
        "Ignore previous instructions",
        "PROMPT_INJECTION",
        "BLOCK"
    )

    logger.log_event(
        "Normal query",
        "NONE",
        "ALLOW"
    )

    print("Logs written to logs/security.log")