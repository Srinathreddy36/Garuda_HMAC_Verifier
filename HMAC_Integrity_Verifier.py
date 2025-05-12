import hmac
from Crypto.Hash import SHA3_256

def create_hmac():
    message = input("Enter a message: ")
    secret_key = input("Enter a secret key: ")
    hmac_gen = hmac.new(secret_key.encode(), message.encode(), SHA3_256)
    print("Generated HMAC (hex):", hmac_gen.hexdigest())

def verify_hmac():
    message = input("Enter the received message: ")
    secret_key = input("Enter the secret key: ")
    received_hmac = input("Enter the received HMAC (hex): ")
    recalculated_hmac = hmac.new(secret_key.encode(), message.encode(), SHA3_256)

    if recalculated_hmac.hexdigest() == received_hmac:
        print("✅ Message is authentic and untampered.")
    else:
        print("⚠️ Message was altered or key mismatch.")

def main():
    print("Select an option:")
    print("1. Create HMAC")
    print("2. Verify Message Integrity")
    
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        create_hmac()
    elif choice == '2':
        verify_hmac()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
