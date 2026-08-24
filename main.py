from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print(os.getenv("MY_VAR"))


if __name__ == "__main__":
    main()
