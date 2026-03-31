import sys
from typing import Optional


def get_greeting(name: Optional[str] = None) -> str:
    """
    Generate a greeting message.

    Args:
        name (Optional[str]): The name to greet. Defaults to None.

    Returns:
        str: A formatted greeting message.
    """
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"


def main() -> None:
    """
    Main entry point of the program.

    Prints a greeting message and exits with status code 0.
    """
    # Generate and print a greeting
    greeting = get_greeting()
    print(greeting)

    # Exit with success status
    sys.exit(0)


if __name__ == "__main__":
    main()
