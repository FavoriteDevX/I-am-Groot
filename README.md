# 🌱 I Am Groot (GrootLang)

> *"I am Groot. I am Groot! I AM GROOT? We are Groot."* — **Groot, Lead Language Architect**

<img width="1216" height="864" alt="Untitled-1" src="https://github.com/user-attachments/assets/e20c38e9-0719-4748-a56d-9054745c8e62" />

## 🌳 Manifesto

I am Groot. I am Groot, I am Groot!  
I am Groot... I AM GROOT! I am Groot?  
I am Groot:

```text
I am Groot!
I am Groot!
I am Groot+
I AM GROOT.
WE ARE GROOT!
```

**We are Groot.**

---

<details>
<summary>🦝 <b>Click here for Rocket's Translation (Actual Documentation & Usage)</b></summary>

<br>

*Ugh, fine. Since none of you speak Flora colossus, I'll translate what the twig is trying to say.*

**GrootLang** is a **Turing-complete, stack-and-register-based esoteric programming language** written in pure Python with zero external dependencies. Unlike simple Brainfuck clones, GrootLang features **24 distinct opcodes** controlled entirely by capitalization, punctuation, and intonation—allowing you to perform arithmetic, manipulate ASCII text, manage 32 memory registers, run nested loops, and obfuscate secret messages.

---

### 🚀 Quick Start

#### 1. Clone the repository
```bash
git clone https://github.com/FavoriteDevX/I-am-Groot
cd i-am-groot
```

*(Optional) Make the interpreter directly executable on Linux/macOS:*
```bash
chmod +x groot.py transpiler.py
```

#### 2. Run the demo program
```bash
python groot.py hello.groot
```

**Output:**
```text
GROOT!
5 4 3 2 1
```

#### 3. Debug Mode (Inspect Stack & Memory Registers)
Want to see what's happening inside Groot's wooden brain step-by-step? Pass the `--debug` flag:
```bash
python groot.py hello.groot --debug
```

---

### 🛠️ Text-to-Groot Transpiler (Code Obfuscator)

Don't want to manually count ASCII values using `I am Groot.` and `I am Groot+`? Use the built-in transpiler to convert **any text or secret message** into an executable `.groot` program:

```bash
# Generate a .groot file from any string
python transpiler.py "Guardians of the Galaxy!" > guardians.groot

# Run your newly generated program
python groot.py guardians.groot
```

**Output:**
```text
Guardians of the Galaxy!
```

---

### 📖 Official Instruction Set (24 Opcodes)

Every line in a `.groot` file must be an exact match to one of the commands below. Comments are supported using `//` (Rocket's notes).

#### 📦 Stack & Value Manipulation

| GrootLang Command | Opcode | Description |
| :--- | :--- | :--- |
| `I am Groot.` | `PUSH_1` | Pushes `1` onto the stack. |
| `I am Groot!` | `PUSH_10` | Pushes `10` onto the stack. |
| `I AM GROOT!` | `PUSH_100` | Pushes `100` onto the stack. |
| `i am groot.` | `PUSH_0` | Pushes `0` onto the stack. |
| `I am Groot...` | `DUP` | Duplicates the top value of the stack. |
| `i am groot...` | `POP` | Discards the top value of the stack. |
| `I am Groot?!` | `SWAP` | Swaps the top two values on the stack. |

#### 🧮 Arithmetic & Randomness

| GrootLang Command | Opcode | Description |
| :--- | :--- | :--- |
| `I am Groot+` | `ADD` | Pops `a`, `b` and pushes `b + a`. |
| `I am Groot-` | `SUB` | Pops `a`, `b` and pushes `b - a`. |
| `I am Groot*` | `MUL` | Pops `a`, `b` and pushes `b * a`. |
| `I am Groot/` | `DIV` | Pops `a`, `b` and pushes integer division `b // a`. |
| `I am Groot%` | `MOD` | Pops `a`, `b` and pushes modulo `b % a`. |
| `I am Groot?` | `RAND` | Pushes a random integer between `0` and `100`. |

#### 🧠 Memory & Registers (32 Slots)

| GrootLang Command | Opcode | Description |
| :--- | :--- | :--- |
| `I am GROOT.` | `PTR_RIGHT` | Moves the memory pointer right (`+1`). |
| `GROOT am I.` | `PTR_LEFT` | Moves the memory pointer left (`-1`). |
| `I AM Groot.` | `STORE` | Pops top of stack and stores it in the active register. |
| `I am groot!` | `LOAD` | Loads value from the active register onto the stack. |

#### 🖥️ Input / Output

| GrootLang Command | Opcode | Description |
| :--- | :--- | :--- |
| `I AM GROOT.` | `PRINT_CHAR` | Pops top of stack and prints it as an ASCII character. |
| `I am Groot!!` | `PRINT_NUM` | Pops top of stack and prints it as an integer. |
| `I am Groot???` | `INPUT_CHAR` | Reads 1 character from `stdin` and pushes its ASCII code. |
| `I AM GROOT???` | `INPUT_NUM` | Reads an integer from `stdin` and pushes it onto the stack. |

#### 🔁 Control Flow & System

| GrootLang Command | Opcode | Description |
| :--- | :--- | :--- |
| `I AM GROOT?` | `LOOP_START` | If top of stack is `0`, jumps past matching `We are Groot.`. |
| `We are Groot.` | `LOOP_END` | If top of stack is not `0`, jumps back to `I AM GROOT?`. |
| `WE ARE GROOT!` | `HALT` | Immediately terminates program execution. |

---

### 🧩 Example: Countdown Loop (`countdown.groot`)

```text
// Push 5 onto the stack
I am Groot.
I am Groot.
I am Groot+
I am Groot.
I am Groot+
I am Groot.
I am Groot+
I am Groot.
I am Groot+

// Loop while top of stack != 0
I AM GROOT?
    I am Groot...    // Duplicate counter
    I am Groot!!     // Print number
    I am Groot!      // Push 10 (newline)
    I AM GROOT.      // Print newline
    I am Groot.      // Push 1
    I am Groot-      // Subtract 1 from counter
We are Groot.

WE ARE GROOT!
```

---

### 🤝 Contributing

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingGroot`).
3. Commit your changes (`git commit -m 'I am Groot'`).
4. Push to the branch (`git push origin feature/AmazingGroot`).
5. Open a Pull Request.

---
