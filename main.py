import os

LINE = "Going up. Please hold all existential questions until we reach the ground floor."

LIMIT = 120
if len(LINE) != 80 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 80 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# The elevator is polite, patient, and done with your questions.
