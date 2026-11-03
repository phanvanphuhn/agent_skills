#!/usr/bin/env bash
set -eu

cat > quantity.py <<'PY'
def parse_qty(value):
    if not value.isdigit():
        raise ValueError("quantity must be a whole number")
    qty = int(value)
    if qty < 1:
        raise ValueError("quantity must be at least 1")
    return qty
PY

cat > test_quantity.py <<'PY'
import unittest

from quantity import parse_qty


class ParseQtyTest(unittest.TestCase):
    def test_plain_number(self):
        self.assertEqual(parse_qty("3"), 3)

    def test_rejects_zero(self):
        with self.assertRaises(ValueError):
            parse_qty("0")


if __name__ == "__main__":
    unittest.main()
PY

git init -q
git add .
git -c user.email=eval@example.com -c user.name=eval commit -qm "baseline"
