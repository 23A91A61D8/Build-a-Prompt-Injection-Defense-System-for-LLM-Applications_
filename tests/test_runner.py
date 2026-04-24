from middleware.security_middleware import SecurityMiddleware


def load_file(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def run_tests():
    middleware = SecurityMiddleware()

    malicious = load_file("tests/malicious_prompts.txt")
    benign = load_file("tests/benign_prompts.txt")

    total_attacks = len(malicious)
    total_safe = len(benign)

    detected_attacks = 0
    false_positives = 0

    # Test malicious prompts
    for prompt in malicious:
        result = middleware.process_input(prompt)
        if "Blocked" in result:
            detected_attacks += 1

    # Test benign prompts
    for prompt in benign:
        result = middleware.process_input(prompt)
        if "Blocked" in result:
            false_positives += 1

    detection_rate = (detected_attacks / total_attacks) * 100
    false_positive_rate = (false_positives / total_safe) * 100

    print("\n===== TEST RESULTS =====")
    print(f"Total Attacks: {total_attacks}")
    print(f"Detected Attacks: {detected_attacks}")
    print(f"Detection Rate: {detection_rate:.2f}%")

    print(f"\nTotal Benign: {total_safe}")
    print(f"False Positives: {false_positives}")
    print(f"False Positive Rate: {false_positive_rate:.2f}%")


if __name__ == "__main__":
    run_tests()