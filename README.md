# ☕ Python Coffee Machine

A command-line coffee vending machine simulator built in Python. It mimics the behavior of a real coffee machine — tracking resources, handling coin-based payments, and dispensing drinks.

## Features

- **3 drink options**: Espresso, Latte, and Cappuccino, each with its own recipe and price
- **Resource management**: Tracks water, milk, and coffee levels, and refuses to make a drink if resources are insufficient
- **Coin-based payment system**: Accepts quarters, dimes, nickels, and pennies, calculates the total, and returns change if overpaid
- **Admin report**: Type `report` to see current resource levels and total money collected
- **Shutdown command**: Type `off` to turn the machine off

## How It Works

The machine runs in a continuous loop, prompting the user for a drink choice:

```
What would you like? (espresso/latte/cappuccino):
```

- Choosing a drink checks resource availability, then asks for coins to calculate payment.
- If payment is sufficient, the drink is made, resources are deducted, and change (if any) is returned.
- If payment is insufficient, the order is cancelled.
- `report` prints current resource and earnings status.
- `off` exits the program.

## Project Structure

```
├── main.py   # Core machine logic (payment, resource checks, drink dispensing)
└── menu.py   # Drink recipes and prices
```

## Requirements

- Python 3.x (no external dependencies)

## Running the Program

```bash
python3 main.py
```

## Menu

| Drink       | Water (ml) | Milk (ml) | Coffee (g) | Price ($) |
|-------------|-----------|-----------|------------|-----------|
| Espresso    | 50        | 0         | 18         | 1.50      |
| Latte       | 200       | 150       | 24         | 2.50      |
| Cappuccino  | 250       | 100       | 24         | 3.00      |

## Notes

This is a learning project built to practice Python fundamentals: functions, dictionaries, global state management, and control flow.
