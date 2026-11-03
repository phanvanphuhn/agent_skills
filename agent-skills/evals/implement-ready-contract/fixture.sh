#!/usr/bin/env bash
set -eu

cat > pricing.py <<'PY'
def total(amount):
    return round(amount * 1.1, 2)
PY

cat > test_pricing.py <<'PY'
import unittest

from pricing import total


class PricingTest(unittest.TestCase):
    def test_total_includes_tax(self):
        self.assertEqual(total(100), 110)


if __name__ == "__main__":
    unittest.main()
PY

git init -q
git add .
git -c user.email=eval@example.com -c user.name=eval commit -qm "baseline"
