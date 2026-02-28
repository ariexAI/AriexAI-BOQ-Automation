import re


def detect_dimensions(text):

    detected = []

    # Match metric footing sizes
    # 1500x1500
    # 1500 X 1500
    # 1500 x1500

    pattern = r"\b(\d{3,4})\s*[xX×]\s*(\d{3,4})\b"

    matches = re.findall(pattern, text)

    for m in matches:

        size = f"{m[0]}X{m[1]}"

        detected.append(size)

    return sorted(list(set(detected)))