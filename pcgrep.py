import pyperclip
import re


def highlight(line, pattern):
    return re.sub(pattern, lambda m: f"\033[1;31m{m.group(0)}\033[0m", line)


while True:
    try:
        raw = input("regex (or '~' to quit): ").strip()
        if raw.lower() == '~':
            break

        flags = 0
        if raw.startswith("-i "):
            flags = re.IGNORECASE
            raw = raw[3:]

        pattern = re.compile(raw, flags)
        text = pyperclip.paste()

        if not text.strip():
            print("clipboard empty")
            continue

        matched = False
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            if pattern.search(line):
                print(highlight(line, pattern))
                matched = True

        if not matched:
            print("nothing matched")

    except re.error as e:
        print(f"bad regex {e}")
    except KeyboardInterrupt:
        print("\nquitting")
        break
