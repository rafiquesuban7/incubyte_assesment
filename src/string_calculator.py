
from __future__ import annotations

import re
from typing import Iterable, List


class StringCalculator:
    """
    String Calculator implementing the Incubyte TDD kata.

    Supports:
    - Empty string -> 0
    - Comma and newline delimiters
    - Custom delimiters via //;<newline> or //[***]<newline>
    - Multiple delimiters via //[x][y]<newline>
    - Ignores numbers > 1000
    - Raises ValueError on negative numbers with all negatives listed
    """

    DEFAULT_DELIMITERS = [",", "\n"]

    def add(self, text: str) -> int:
        if text is None or text == "":
            return 0

        numbers = self._parse_numbers(text)
        negatives = [n for n in numbers if n < 0]
        if negatives:
            msg = f"negative numbers not allowed: {', '.join(map(str, negatives))}"
            raise ValueError(msg)

        return sum(n for n in numbers if n <= 1000)

    # ---------------- internal helpers ---------------- #

    def _parse_numbers(self, text: str) -> List[int]:
        delimiters, body = self._extract_delimiters_and_body(text)
        # Build a regex that splits on any of the delimiters
        # Escape each delimiter for regex; join via alternation
        pattern = "|".join(map(re.escape, delimiters))
        tokens = re.split(pattern, body) if body else []
        # Filter out empty tokens (in case of adjacent delimiters)
        return [int(tok) for tok in tokens if tok != ""]

    def _extract_delimiters_and_body(self, text: str) -> tuple[list[str], str]:
        """
        Parse custom delimiter header if present.
        Forms supported:
          //;<newline>numbers
          //[***]<newline>numbers
          //[*][%]<newline>numbers
          //[***][%%]<newline>numbers
        """
        if text.startswith("//"):
            header, _, body = text.partition("\n")
            delim_spec = header[2:]  # strip leading //
            # Bracketed multiple (or long) delimiters
            if delim_spec.startswith("["):
                # Extract content inside each [ ... ]
                parts = re.findall(r"\[([^\]]+)\]", delim_spec)
                if not parts:
                    raise ValueError("Invalid delimiter specification")
                delimiters = parts + self.DEFAULT_DELIMITERS
                return delimiters, body
            else:
                # Single-char delimiter like //; or multi-char without brackets (optional)
                delimiter = delim_spec
                return [delimiter] + self.DEFAULT_DELIMITERS, body
        else:
            return self.DEFAULT_DELIMITERS, text
