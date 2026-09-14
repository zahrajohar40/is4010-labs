# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed and authenticated the GitHub Copilot CLI on my system. Verified version detail: `gh copilot --version 1.0.5`.

### Antigravity CLI

I installed and authenticated the Antigravity CLI on my system. Verified version detail: `antigravity --version 0.4.2`.

## Shared task

### Shared prompt

Paste the exact prompt you submitted to both CLI tools.

```text
Write a Python function count_vowels(text: str) -> int that counts a, e, i, o, u case-insensitively and does not count y.
```

### Copilot CLI observations

GitHub Copilot CLI suggested writing straightforward helper functions using built-in string methods like strip() and title() for names, simple modulo operations for evenness checks, and a set membership lookup combined with lower() for vowel counting. I questioned whether the vowel count approach handled uppercase characters and empty strings without extra dependencies. I verified that using set operations alongside a generator expression provided high readability while maintaining full coverage for boundary conditions like empty inputs.

### Antigravity CLI observations

Antigravity CLI recommended using regular expressions with the re module to count vowels via re.findall with re.IGNORECASE, while offering standard conditional checks for greeting strings and even numbers. I questioned whether introducing the re module for basic vowel checking added unnecessary overhead compared to built-in string iteration. I would verify performance, memory usage, and code legibility against the lab test suite to see if regex offers any real advantage over standard Python iterations.

### Comparison

Comparing the two CLI tools, GitHub Copilot CLI prioritized clean, standard Python idioms that align naturally with built-in data structures and methods. In contrast, Antigravity CLI leaned heavily on functional utilities and regex patterns. Copilot's output was immediately clearer and easier to adapt directly into the lab functions without introducing external or unnecessary top-level module imports into the codebase. Antigravity's regex suggested alternative pattern-matching ideas, but introducing regex felt over-engineered for simple string checks. Ultimately, I selected Copilot's set-based lookup and generator pattern because it keeps the overall codebase concise, readable, performant, and perfectly suited to satisfy the provided lab test constraints and edge cases. Furthermore, Copilot provided explanation steps that made it easier to verify before writing any code.
## Test-guided implementation
unning the initial pytest suite revealed specific expectations regarding case insensitivity, empty strings, zero, and negative values across all functions. Inspecting test even zero and negative values confirmed that negative even numbers must accurately evaluate as even, which reinforced using the simple modulo logic without adding arbitrary lower-bound checks or extra logic. For vowel counting, running test vowels are case insensitive and test empty text highlighted the importance of converting strings to lowercase before checking set membership. These test outcomes directly guided my code revisions, ensuring every helper function handles edge inputs gracefully and strictly satisfies all function contracts defined by the automated test suite. Visualizing test outputs helped isolate boundary bugs early during development.

## Preferred tool combination

Different AI assistance formats fit distinct stages of my software development workflow. Browser chat tools are ideal for broad conceptual learning and debugging high-level design decisions. GitHub Copilot in VS Code provides seamless inline code completion during continuous typing. CLI tools like Copilot CLI and Antigravity CLI excel at quick command-line assistance when operating directly in terminal environments. My currently preferred combination is GitHub Copilot in VS Code paired with local terminal execution using pytest, which provides instant visual context alongside fast test verification. However, working on remote servers via SSH without a graphical editor would shift my preference toward CLI tools.