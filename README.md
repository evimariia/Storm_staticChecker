# Static Checker for Storm2024-2

## Overview

This repository contains the **Static Checker** project for the **Storm2024-2 programming language**, developed as part of the *Compilers* course at Senai Cimatec. The Static Checker implements **lexical and partial syntactic analysis** to validate source code written in Storm2024-2, a language inspired by C but simplified for educational purposes.

The Static Checker performs the following tasks:
- Reads and validates Storm2024-2 source files (`.242`).
- Conducts lexical analysis to identify tokens and reserved keywords.
- Partially analyzes syntax to build a symbol table and syntax reports.
- Generates detailed reports for debugging and verification purposes.

## Features

- **Lexical Analysis:** Tokenizes the source code, identifies reserved words, and filters invalid characters.
- **Symbol Table:** Maintains and updates a table of identifiers with attributes like type, scope, and occurrence.
- **Syntax Reporting:** Produces `.LEX` and `.TAB` files with analysis results.
- **Support for Comments:** Handles both block and inline comments.
- **Case Insensitivity:** Treats identifiers with different letter cases as identical.
- **Error Reporting:** Provides detailed feedback for invalid constructs (future expansion includes graphical interface options).

## File Structure

- **`source/`**: Contains the implementation code for the Static Checker.
- **`examples/`**: Includes example Storm2024-2 `.242` files.
- **`docs/`**: Documentation, including project specifications and example outputs.
- **`reports/`**: Generated `.LEX` and `.TAB` files from sample analyses.
- **`tests/`**: Unit and integration tests for each module.

## How It Works

### Input and Output

1. The Static Checker takes a `.242` source file as input.
2. It outputs:
   - A `.LEX` file containing a detailed lexical analysis report.
   - A `.TAB` file with the symbol table details.

### Modules

1. **Lexical Analyzer:**
   - Reads the source file character by character.
   - Forms tokens (atoms) based on language rules.
   - Handles reserved words, comments, and whitespace.

2. **Symbol Table Manager:**
   - Stores identifiers and their attributes.
   - Updates scope and type information dynamically.
   - Generates the `.TAB` report.

3. **Partial Syntax Analyzer:**
   - Constructs a syntax tree (future expansion).
   - Integrates lexical tokens into structured output.

## Requirements

- Programming Language: Defined by the team and approved by the instructor.
- Dependencies: Detailed in the `requirements.txt` (or similar file) for easy setup.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Storm2024-2-Static-Checker.git
   cd Storm2024-2-Static-Checker

2. Compile the project (adjust based on the language used)::
   ```bash
   make

3. Run the Static Checker:
   ```bash
   ./static_checker <source_file_name>
   
4. View the output reports in the same directory as the input file:
   ```
   <source_file_name>.LEX
   <source_file_name>.TAB

## Contributors
Bruno da Costa Sales
Évila Maria de Souza Carneiro
Gabriel Batista Reis
João Victor Borges Lima

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
This project was guided by Professor Osvaldo Requião Melo as part of the Compilers course at Senai Cimatec. The specifications were collaboratively developed to support the discipline's goals.
