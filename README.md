# Position Size Calculator for Trading

## Project Overview
This is a command-line application that calculates the position size for a trade based on your account size, risk percentage, entry price, and stop-loss price. It helps traders manage risk effectively in their trades.

Key Features:
- Calculates position size and trade value based on user inputs.
- Allows saving results to a file for future reference.
- Provides an option to load previously saved results.

---

## Installation Instructions
To use this tool, ensure you have **Python 3.6+** installed on your system.

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/heydarDehghan/RiskMate.git
   cd RiskMate
   ```

2. Install dependencies (if any):
   ```bash
   pip install argparse
   ```

3. Run the script.

---

## Usage
### Command-Line Arguments
Run the script using the following command:

```bash
python position_size_calculator.py --account_size <account_size> --risk_percentage <risk_percentage> --entry_price <entry_price> --stop_loss_price <stop_loss_price> [--save] [--load]
```

### Arguments:
| Argument             | Description                                    | Required |
|----------------------|------------------------------------------------|----------|
| `--account_size`     | Total trading account size in dollars          | Yes      |
| `--risk_percentage`  | Percentage of account to risk per trade        | Yes      |
| `--entry_price`      | Entry price of the asset                       | Yes      |
| `--stop_loss_price`  | Stop-loss price for the asset                  | Yes      |
| `--save`             | Save the results to a file                     | Optional |
| `--load`             | Load previous results from a saved file        | Optional |

---

### Example Usage
1. **Calculate position size** without saving:
   ```bash
   python position_size_calculator.py --account_size 10000 --risk_percentage 2 --entry_price 50000 --stop_loss_price 49500
   ```

2. **Save results** to a file:
   ```bash
   python position_size_calculator.py --account_size 10000 --risk_percentage 2 --entry_price 50000 --stop_loss_price 49500 --save
   ```

3. **Load previously saved results**:
   ```bash
   python position_size_calculator.py --load
   ```

---

## Output Example
When running the script, you will see an output like this:

```
--- Results ---
Account Risk ($): 200.0
Trade Risk per Coin ($): 500.0
Position Size (Coins): 0.4
Trade Value ($): 20000.0
Results saved to results.json
```

---

## File Management
- Results are saved in a file named `results.json` in the current working directory.
- Use the `--load` flag to view previously saved results.

---

## Contributions
Contributions are welcome! If you'd like to improve this tool, please fork the repository and create a pull request.

---

## License
This project is licensed under the MIT License.

---

## Contact
For questions or feedback, feel free to reach out:
- **Email:** dehghanheydar@gmail.com
- **GitHub:** [heydar-dehghan](https://github.com/heydarDehghan)

---
