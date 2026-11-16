#!/usr/bin/env python3
"""
GrootLang Interpreter v1.0
A Turing-complete, stack-and-register-based esoteric programming language.
Usage: python groot.py <file.groot> [--debug]
"""

import sys
import random
import os

class GrootRuntimeError(Exception):
    pass

class GrootInterpreter:
    def __init__(self, debug=False):
        self.stack = []
        self.registers = [0] * 32  # 32 memory slots (0-31)
        self.pointer = 0           # Current active memory register
        self.debug = debug
        self.pc = 0                # Program Counter
        self.jump_map = {}

        # The Official GrootLang Instruction Set (24 Opcodes)
        self.OPCODES = {
            # --- Stack & Value Manipulation ---
            "I am Groot.":          "PUSH_1",      # Push 1 onto stack
            "I am Groot!":          "PUSH_10",     # Push 10 onto stack
            "I AM GROOT!":          "PUSH_100",    # Push 100 onto stack
            "i am groot.":          "PUSH_0",      # Push 0 onto stack
            "I am Groot...":        "DUP",         # Duplicate top of stack
            "i am groot...":        "POP",         # Discard top of stack
            "I am Groot?!":         "SWAP",        # Swap top two stack items

            # --- Arithmetic & Logic ---
            "I am Groot+":          "ADD",         # Pop a, b -> Push b + a
            "I am Groot-":          "SUB",         # Pop a, b -> Push b - a
            "I am Groot*":          "MUL",         # Pop a, b -> Push b * a
            "I am Groot/":          "DIV",         # Pop a, b -> Push b // a
            "I am Groot%":          "MOD",         # Pop a, b -> Push b % a
            "I am Groot?":          "RAND",        # Push random int (0-100)

            # --- Memory & Pointers ---
            "I am GROOT.":          "PTR_RIGHT",   # Move memory pointer right (+1)
            "GROOT am I.":          "PTR_LEFT",    # Move memory pointer left (-1)
            "I AM Groot.":          "STORE",       # Pop stack -> save in current register
            "I am groot!":          "LOAD",        # Push value from current register to stack

            # --- Input / Output ---
            "I AM GROOT.":          "PRINT_CHAR",  # Pop stack -> print as ASCII character
            "I am Groot!!":         "PRINT_NUM",   # Pop stack -> print as integer
            "I am Groot???":        "INPUT_CHAR",  # Read 1 char from stdin -> push ASCII
            "I AM GROOT???":        "INPUT_NUM",   # Read integer from stdin -> push int

            # --- Control Flow & System ---
            "I AM GROOT?":          "LOOP_START",  # If top of stack == 0, jump to matching LOOP_END
            "We are Groot.":        "LOOP_END",    # If top of stack != 0, jump back to LOOP_START
            "WE ARE GROOT!":        "HALT",        # Terminate program execution
        }

    def tokenize(self, source_code):
        tokens = []
        for line_num, raw_line in enumerate(source_code.splitlines(), 1):
            # Strip comments starting with // (Rocket's notes)
            line = raw_line.split("//")[0].strip()
            if not line:
                continue
            if line not in self.OPCODES:
                raise GrootRuntimeError(
                    f"[Line {line_num}] Syntax Error: Groot doesn't understand '{line}'"
                )
            tokens.append((self.OPCODES[line], line_num, line))
        return tokens

    def build_jump_map(self, tokens):
        loop_stack = []
        for idx, (op, line_num, _) in enumerate(tokens):
            if op == "LOOP_START":
                loop_stack.append(idx)
            elif op == "LOOP_END":
                if not loop_stack:
                    raise GrootRuntimeError(f"[Line {line_num}] Unmatched 'We are Groot.'")
                start_idx = loop_stack.pop()
                self.jump_map[start_idx] = idx
                self.jump_map[idx] = start_idx
        if loop_stack:
            _, line_num, _ = tokens[loop_stack[-1]]
            raise GrootRuntimeError(f"[Line {line_num}] Unclosed 'I AM GROOT?'")

    def pop(self, line_num):
        if not self.stack:
            raise GrootRuntimeError(f"[Line {line_num}] Stack Underflow! Groot has nothing to give.")
        return self.stack.pop()

    def run(self, source_code):
        tokens = self.tokenize(source_code)
        self.build_jump_map(tokens)
        self.pc = 0

        while self.pc < len(tokens):
            op, line_num, raw = tokens[self.pc]

            if self.debug:
                print(f"[DEBUG L{line_num}] {raw:<16} -> {op:<12} | Stack: {self.stack} | Reg[{self.pointer}]: {self.registers[self.pointer]}", file=sys.stderr)

            if op == "PUSH_1":
                self.stack.append(1)
            elif op == "PUSH_10":
                self.stack.append(10)
            elif op == "PUSH_100":
                self.stack.append(100)
            elif op == "PUSH_0":
                self.stack.append(0)
            elif op == "DUP":
                if not self.stack:
                    raise GrootRuntimeError(f"[Line {line_num}] Nothing to duplicate.")
                self.stack.append(self.stack[-1])
            elif op == "POP":
                self.pop(line_num)
            elif op == "SWAP":
                a = self.pop(line_num)
                b = self.pop(line_num)
                self.stack.extend([a, b])
            elif op == "ADD":
                a = self.pop(line_num)
                b = self.pop(line_num)
                self.stack.append(b + a)
            elif op == "SUB":
                a = self.pop(line_num)
                b = self.pop(line_num)
                self.stack.append(b - a)
            elif op == "MUL":
                a = self.pop(line_num)
                b = self.pop(line_num)
                self.stack.append(b * a)
            elif op == "DIV":
                a = self.pop(line_num)
                b = self.pop(line_num)
                if a == 0:
                    raise GrootRuntimeError(f"[Line {line_num}] Division by zero! Even Groot can't do that.")
                self.stack.append(b // a)
            elif op == "MOD":
                a = self.pop(line_num)
                b = self.pop(line_num)
                if a == 0:
                    raise GrootRuntimeError(f"[Line {line_num}] Modulo by zero!")
                self.stack.append(b % a)
            elif op == "RAND":
                self.stack.append(random.randint(0, 100))
            elif op == "PTR_RIGHT":
                self.pointer = (self.pointer + 1) % len(self.registers)
            elif op == "PTR_LEFT":
                self.pointer = (self.pointer - 1) % len(self.registers)
            elif op == "STORE":
                self.registers[self.pointer] = self.pop(line_num)
            elif op == "LOAD":
                self.stack.append(self.registers[self.pointer])
            elif op == "PRINT_CHAR":
                val = self.pop(line_num)
                print(chr(val % 1114112), end="", flush=True)
            elif op == "PRINT_NUM":
                val = self.pop(line_num)
                print(val, end="", flush=True)
            elif op == "INPUT_CHAR":
                ch = sys.stdin.read(1)
                self.stack.append(ord(ch) if ch else 0)
            elif op == "INPUT_NUM":
                try:
                    val = int(input())
                    self.stack.append(val)
                except ValueError:
                    raise GrootRuntimeError(f"[Line {line_num}] Invalid integer input.")
            elif op == "LOOP_START":
                if not self.stack or self.stack[-1] == 0:
                    self.pc = self.jump_map[self.pc]
            elif op == "LOOP_END":
                if self.stack and self.stack[-1] != 0:
                    self.pc = self.jump_map[self.pc]
            elif op == "HALT":
                break

            self.pc += 1

def main():
    if len(sys.argv) < 2:
        print("Usage: python groot.py <file.groot> [--debug]")
        sys.exit(1)

    filepath = sys.argv[1]
    debug_mode = "--debug" in sys.argv

    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    interpreter = GrootInterpreter(debug=debug_mode)
    try:
        interpreter.run(code)
    except GrootRuntimeError as e:
        print(f"\n[GROOT CRASH] {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
