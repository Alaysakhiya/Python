# 🏦 Bank Management System

> *What actually happens when you hit "withdraw"?*
> This is that logic — written from scratch in Python.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![OOP](https://img.shields.io/badge/Concept-OOP-purple) ![CLI](https://img.shields.io/badge/Interface-Console-orange) ![Status](https://img.shields.io/badge/Status-Learning%20Project-success)

A console-based banking system built with core OOP principles — Abstraction, Inheritance, Encapsulation, and Polymorphism — instead of a database or framework. Every deposit, withdrawal, and transfer runs through real class logic, not a spreadsheet pretending to be one.

---

## 📖 Overview

This project simulates the core operations of a bank through a simple menu-driven command-line interface:

- Customers can be registered
- Two types of accounts can be opened — Saving or Current
- Money can be deposited, withdrawn, or transferred between accounts
- Every account keeps its own timestamped transaction history

It's a learning project built to actually **use** OOP concepts in a working system, rather than just define them in isolation.

---

## 🧩 The Blueprint

```
Person ──▶ Customer

Account (Abstract) ──▶ SavingAccount   (earns interest)
                  └──▶ CurrentAccount  (allows overdraft)

Bank ──▶ manages all Accounts & Customers
```

Every account *must* define its own `withdraw()` — the abstract class won't let it skip that. Saving accounts refuse to go negative. Current accounts dip into an overdraft instead of failing outright.

### Why the design works

- `Account` is an **abstract base class** — you can never accidentally create a "generic" account with undefined withdrawal behavior
- `balance` is **encapsulated** behind a `@property`, not a public attribute anyone can overwrite carelessly
- `withdraw()` is **polymorphic** — the same method call behaves differently depending on whether it's a Saving or Current account
- `Bank` acts as the **orchestrator**, holding the full list of customers and accounts and handling cross-account operations like transfers

---

## ⚙️ What It Can Do

| Action | Behind the Scenes |
|---|---|
| 👤 Create Customer & Account | Registers a `Customer` and opens a `SavingAccount` or `CurrentAccount` |
| 💵 Deposit | Adds to balance, logs a timestamped entry |
| 💸 Withdraw | Saving blocks overdrafts · Current uses the overdraft limit smartly |
| 🔁 Transfer | Bank moves funds between two accounts, logging both sides |
| 📊 Balance Check | Reads the private `__balance` safely through a property |
| 🧾 Print Statement | Displays account details + full transaction history |
| 📈 Interest | Saving accounts can grow their balance on demand |
| 🔢 Total Accounts | A `staticmethod` tracks every account ever created |

---

## 🖥️ Menu Preview

```
====== Bank Management System ======
1. Create New Account
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Check Balance
6. Print Statement
7. View Total Accounts (classmethod)
8. Exit
```

---

## 🔮 What's Next

- [ ] Fix the transfer bug above
- [ ] Add proper input validation and custom exceptions
- [ ] Persist data with SQLite or JSON instead of in-memory lists
- [ ] Add PIN or password-based authentication
- [ ] Wrap the logic in a GUI (Tkinter) or a web API (Flask)
- [ ] Add unit tests with `pytest`

---

## 🧠 What I Learned

Building this helped me actually apply:

- Abstract classes and enforced method contracts
- Property-based encapsulation instead of raw public attributes
- Designing a "manager" class (`Bank`) that coordinates other objects
- Keeping a clean, timestamped audit trail per object

---

<div align="center">

**Made by Alay Sakhiya** — built to actually understand OOP, not just define it.

⭐ If this helped you learn something too, consider starring the repo.

</div>