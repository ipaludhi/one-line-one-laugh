# One Line, One Laugh — one funny line, written to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR). No network, no randomness, no input.
# The joke: inbox zero achieved the nuclear way — delete the account.
# The payoff reframes the whole premise: the peace cost the job.
import os
from pathlib import Path

TEXT = "I finally achieved inbox zero by deleting my email account; the peace was worth the unemployment."

# Gate self-check (rules: UTF-8 text, 1-140 chars, not only whitespace,
# single self-contained line): fail loudly here rather than ship invalid.
assert 1 <= len(TEXT) <= 140, f"entry is {len(TEXT)} chars, gate needs 1-140"
assert TEXT.strip() and "\n" not in TEXT.strip()
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")
