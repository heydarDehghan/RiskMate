import argparse
import json
import os


def calculate_position_size(account_size, risk_percentage, entry_price, stop_loss_price):
    account_risk = account_size * (risk_percentage / 100)
    trade_risk = entry_price - stop_loss_price

    if trade_risk <= 0:
        return "Invalid input: Stop-loss price must be below the entry price."

    position_size = account_risk / trade_risk
    trade_value = position_size * entry_price

    return {
        "Account Risk ($)": round(account_risk, 2),
        "Trade Risk per Coin ($)": round(trade_risk, 2),
        "Position Size (Coins)": round(position_size, 4),
        "Trade Value ($)": round(trade_value, 2)
    }


def save_results_to_file(results, filename="results.json"):
    try:
        with open(filename, "w") as file:
            json.dump(results, file, indent=4)
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error saving results: {e}")


def load_previous_results(filename="results.json"):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                data = json.load(file)
                print("\n--- Previous Results ---")
                for key, value in data.items():
                    print(f"{key}: {value}")
        else:
            print("No previous results found.")
    except Exception as e:
        print(f"Error loading results: {e}")


def main():
    parser = argparse.ArgumentParser(description="Position Size Calculator for Trading")
    parser.add_argument("--account_size", type=float, required=True, help="Your account size in dollars.")
    parser.add_argument("--risk_percentage", type=float, required=True,
                        help="Percentage of account to risk per trade (e.g., 2 for 2%).")
    parser.add_argument("--entry_price", type=float, required=True, help="Entry price of the asset.")
    parser.add_argument("--stop_loss_price", type=float, required=True, help="Stop-loss price of the asset.")
    parser.add_argument("--save", action="store_true", help="Save the results to a file.")
    parser.add_argument("--load", action="store_true", help="Load previous results from a file.")

    args = parser.parse_args()

    if args.load:
        load_previous_results()

    result = calculate_position_size(args.account_size, args.risk_percentage, args.entry_price, args.stop_loss_price)

    print("\n--- Results ---")
    if isinstance(result, str):
        print(result)
    else:
        for key, value in result.items():
            print(f"{key}: {value}")

        if args.save:
            save_results_to_file(result)


if __name__ == "__main__":
    main()
