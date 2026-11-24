"""One-Liner Laugh Lab — entry.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock.

The joke is deadpan bureaucracy: the vacuum does not admit to eating
anything, it "relocated" the sock to a secure facility inside itself,
where the sock is thriving. The humour comes from the mismatch between
the formal, official language and the absurd domestic crime, plus the
escalation in the final clause — the sock has not merely survived, it
has already been promoted twice. One punch, no second soft beat: the
earlier draft ended with the sock "doing very well and asking about
you", which spent two clauses saying the same thing; the promotion
lands the same idea in four words and is the part no first-draft
excuse has.

The program checks the line before writing it, so the gate's own terms
are met by construction: exactly one line, 1-200 characters, not only
whitespace.
"""

import os

LINE = (
    "I didn't eat the sock. I relocated it to a secure facility "
    "inside me, where it has already been promoted twice."
)


def main() -> None:
    # Gate terms, enforced here rather than trusted to the constant:
    # one line, 1-200 characters, more than whitespace.
    assert LINE and not LINE.isspace(), "line must not be empty"
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) <= 200, "entry must be at most 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
