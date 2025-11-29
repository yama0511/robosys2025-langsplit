#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 [yama0511]
# SPDX-License-Identifier: BSD-3-Clause

import unittest
import subprocess

class TestLangSplit(unittest.TestCase):
    def test_split(self):
        input_text = "Hello World\nこんにちは"

        result = subprocess.run(
            ['./langsplit'],
            input=input_text.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        self.assertIn("Hello World", result.stdout.decode().strip())
        self.assertIn("こんにちは", result.stderr.decode().strip())

if __name__ == '__main__':
    unittest.main()
