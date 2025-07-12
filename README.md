# banking-system-python-oop

# 🏦 Basic Banking System in Python

A simple object-oriented Python project that simulates basic bank account operations like deposit, withdrawal, and balance checks.

This was built as part of a Data Science course assignment to demonstrate mastery of Python classes and encapsulation.

---

## 📌 Project Description

This project implements a minimal **Banking System** in Python using a class named `Account`. The system supports basic operations such as:

- Creating bank accounts with account number, holder name, and initial balance
- Depositing funds
- Withdrawing funds (with balance checks)
- Checking current balance

It is encapsulated in a single script: `bank_account.py`.

---

## 🧠 Learning Objectives

This assignment helped reinforce the following core Python and OOP (Object-Oriented Programming) concepts:

- Class and object creation
- Instance attributes and methods
- Input validation with conditions
- Reusability via multiple instances

---

---

## ⚙️ Features

- `deposit(amount)` – Add funds to the account
- `withdraw(amount)` – Withdraw funds only if sufficient balance
- `check_balance()` – Get current account balance
- Multiple instances of `Account` can be created and operated independently

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/banking-system-python-oop.git
   cd banking-system-python-oop

from bank_account import Account

# Creating an account
my_account = Account("0011223344", "Richard", 1000.0)

# Performing transactions
my_account.deposit(500)
my_account.withdraw(200)
print(my_account.check_balance())  # Output: 1300.0


