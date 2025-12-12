#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Yamato Okada
# SPDX-License-Identifier: BSD-3-Clause

import unittest
import subprocess

class TestLangSplit(unittest.TestCase):
    def test_split(self):
        input_text = (
            "Hello World\n"
            "こんにちは\n"
            "!!!???\n"
            "1234567890\n"
            "Python 3.10\n"
            "テストです。\n"
        )
        
        result = subprocess.run(
            ['./langsplit'],
            input=input_text.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout_output = result.stdout.decode().strip()
        stderr_output = result.stderr.decode().strip()

        self.assertIn("Hello World", stdout_output)
        self.assertIn("!!!???", stdout_output)
        self.assertIn("1234567890", stdout_output)
        self.assertIn("Python 3.10", stdout_output)

        self.assertIn("こんにちは", stderr_output)
        self.assertIn("テストです。", stderr_output)

        self.assertNotIn("こんにちは", stdout_output)
        self.assertNotIn("Hello World", stderr_output)

if __name__ == '__main__':
    unittest.main()
