"""Command-line interface for the calculator."""
import sys
from calculator.operations import add, subtract, multiply, divide


OPERATIONS = {
    "add": add,
    "sub": subtract,
    "mul": multiply,
    "div": divide,
}


def main() -> int:
    if len(sys.argv) != 4:
        print("Usage: python -m calculator.cli <add|sub|mul|div> <a> <b>")
        return 1

    op_name, a_str, b_str = sys.argv[1], sys.argv[2], sys.argv[3]

    if op_name not in OPERATIONS:
        print(f"Unknown operation: {op_name}")
        return 1

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print("Operands must be numbers")
        return 1

    try:
        result = OPERATIONS[op_name](a, b)
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
