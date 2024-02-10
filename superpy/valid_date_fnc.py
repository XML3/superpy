from datetime import datetime
import argparse

def valid_date(string):
    try: 
        return datetime.strptime(string, "%Y-%m-%d")
    except ValueError:
        msg = f"Not a valid date: '{string}'."
        raise argparse.ArgumentTypeError(msg)