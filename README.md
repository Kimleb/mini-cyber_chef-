# Mini CyberChef #

A lightweight, terminal-based clone of CyberChef written in Python. This tool allows you to quickly encode and decode text using Base64 and Hexadecimal formats without relying on any external dependencies.

Features

*   **Base64**: Standard data encoding and decoding.
*   **Hexadecimal**: Native byte-to-hex string translation.
*   **Zero Dependencies**: Uses only standard built-in Python libraries.

Prerequisites

*   Python 3.x installed on your system.

Installation & Setup

1.  Clone this repository or download the source code:
    
    bash
    
        git clone https://github.com
        cd mini-cyberchef
        
    
    Use code with caution.
    
2.  Run the script directly from your terminal:
    
    bash
    
        python chef.py
        
    
    Use code with caution.
    
    *(Note: Use `python3 chef.py` if you are on Mac or Linux).*

Usage Example

Encoding "hello world" to Base64

text

    --- Mini CyberChef ---
    Available Formats:
    1. Base64
    2. Hexadecimal
    
    Choose format (1 or 2): 1
    
    Available Operations:
    1. Encode
    2. Decode
    Choose operation (1 or 2): 1
    
    Enter the text to process:
    hello world
    
    --- Output ---
    aGVsbG8gd29ybGQ=
    

Use code with caution.

Future Roadmap

*   Add an interactive continuous loop.
*   Implement recipe chaining (pipelines).
*   Add URL and ROT13 encoding.
*   Create a graphical user interface (GUI).

License

This project is open-source and available under the MIT License.
