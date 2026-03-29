import hashlib
import pyfiglet
import os

def generate_key(token):
    # This salt MUST match the one in sms_tool.py
    salt = "MAGXXIC_VOT_SECRET_SALT_2024"
    return hashlib.sha256((token + salt).encode()).hexdigest()[:16].upper()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    # ASCII Art Title
    title = pyfiglet.figlet_format("MagxxicVOT ADMIN", font="slant")
    print(f"\033[1;33m{title}\033[0m")

    print("\033[1;31m" + "="*50)
    print(" OFFICIAL LICENSE KEY GENERATOR")
    print(" (Administrative Use Only)")
    print("="*50 + "\033[0m")

    while True:
        token = input("\n[?] Enter Customer's System Token (or 'Q' to quit): ").strip().upper()
        if token == 'Q':
            break

        if not token:
            print("\033[1;31m[-] Error: Token cannot be empty.\033[0m")
            continue

        activation_key = generate_key(token)

        print("\n\033[1;32m" + "┌" + "─"*38 + "┐")
        print("│" + " GENERATED ACTIVATION KEY ".center(38) + "│")
        print("├" + "─"*38 + "┤")
        print("│" + f" {activation_key} ".center(38) + "│")
        print("└" + "─"*38 + "┘\033[0m")

        print("\n[!] Send the key above to the customer to activate their software.")
        print("[!] Note: This key is tied to the customer's hardware ID.")

if __name__ == "__main__":
    main()
