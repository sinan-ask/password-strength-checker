# 🔐 Password Strength Checker

A lightweight desktop application built with Python that evaluates password security in real-time. This tool uses regular expressions to analyze password complexity and provides instant, actionable feedback through a clean graphical user interface (GUI).

## ✨ Features

*   **GUI Interface:** Simple and intuitive desktop window built with Tkinter.
*   **Regex Validation:** Evaluates passwords against standard security criteria:
    *   Minimum of 8 characters.
    *   At least one uppercase letter.
    *   At least one lowercase letter.
    *   At least one numerical digit.
    *   At least one special character (`@$!%*?&#`).
*   **Dynamic Feedback:** Instantly rates passwords as **Weak**, **Medium**, or **Strong** with color-coded visual indicators.
*   **Actionable Tips:** Provides specific suggestions on how the user can improve their password if it fails to meet the criteria.

## 🛠️ Technology Stack

*   **Language:** Python 3.x
*   **Libraries:** 
    *   `tkinter` (Standard GUI library for Python)
    *   `re` (Regular expression operations)

## 🚀 How to Run Locally

### Prerequisites
Make sure you have [Python](https://www.python.org/downloads/) installed on your system. 

### Installation
1. Clone the repository to your local machine:
```bash
   git clone [https://github.com/sinan-ask/password-strength-checker.git](https://github.com/sinan-ask/password-strength-checker.git)
