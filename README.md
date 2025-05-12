🛡️ Garuda HMAC Verifier
This project is a part of the Garuda Sentinel cybersecurity series inspired by the book Serious Cryptography. It demonstrates the use of HMAC (Hash-based Message Authentication Code) with SHA3-256 for ensuring message authenticity and integrity.

📌 Features
✅ Generate HMAC for any plaintext message using a secret key.

✅ Verify if a received message was altered using HMAC comparison.

✅ Uses hmac and sha3 modules for secure hashing.

✅ Simple, interactive CLI interface.

🧠 Concepts Covered
HMAC (Hash-based Message Authentication Code)

Message Integrity

SHA3-256 Cryptographic Hashing

Secure Comparison for Authentication

📦 Libraries Used
hmac – For generating and verifying HMACs

sha3 – For SHA3-256 hashing (can use hashlib.sha3_256 in Python 3.6+)

os – For general operations

🧪 How It Works
1. Generate HMAC
User enters a plaintext message and a secret key.

The tool outputs the generated HMAC (SHA3-256) in hexadecimal form.

2. Verify Message Integrity
User provides a received message, the shared secret key, and the received HMAC.

The tool regenerates the HMAC and securely compares it with the received one.

✅ If they match → Message is authentic.

❌ If not → Message was altered.

▶️ Usage
bash
Copy
Edit
$ python garuda_hmac_verifier.py
✅ Example
bash
Copy
Edit
Select an option:
1. Create HMAC
2. Verify message integrity
> 1

Enter message: hello world
Enter secret key: supersecret

Generated HMAC (SHA3-256):
1a7b8d...cfe1
🔐 Future Work
Add file-based integrity checks using HMAC.

Support for binary data and larger payloads.

Enhanced CLI with argument parsing.

📁 Part of Garuda Sentinel
This is Project 9 in the Garuda Sentinel cybersecurity portfolio.
