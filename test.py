import sys

def print_args(args):
    print("The script is called:", args[0])
    
    if len(args) == 1:
        print("No additional arguments were provided.")
    else:
        print("The following arguments were provided:")
        for i, arg in enumerate(args[1:], start=1):
            print(f"Argument #{i}: {arg}")

if __name__ == "__main__":
    print_args(sys.argv)
