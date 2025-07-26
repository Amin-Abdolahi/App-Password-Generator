
### 🛡️ Password Manager

A simple Python-based application to generate, store, and manage secure passwords.

---

### 📌 Features

* Generate random, secure passwords (numeric only or full character set)
* Save passwords along with a note (e.g., website, description, or URL)
* Support multiple entries for the same username
* Store data in a local `data/passwords.json` file
* View saved credentials in a readable format

---

### 🧱 Project Structure

```
project/
├── main.py
├── utils/
│   └── PasswordGenerator.py
├── data/
│   └── passwords.json  ← automatically created
├── README.md
```

---

### ▶️ How to Run

```bash
python3 main.py
```

---

### 📂 Sample Usage

```
Welcome to password manager
Show [s] or create [c] a new strong password? c
New password = x4T$7aQ1!z
Do you want to save it? [y/n]: y
Enter your username: amin
Input note or URL: Gmail
Password saved successfully.
```

---

### 💾 Storage Format

Passwords are stored in JSON like this:

```json
{
  "amin": [
    {
      "password": "x4T$7aQ1!z",
      "note": "Gmail"
    },
    {
      "password": "T2@p9kL0!",
      "note": "GitHub"
    }
  ]
}
```

---

### 📥 Viewing Stored Passwords

Choosing the `[s]how` option will display stored credentials in a clean format:

```
Username: amin
------------------------
🔐 Password: x4T$7aQ1!z
📝 Note: Gmail

🔐 Password: T2@p9kL0!
📝 Note: GitHub
```

---

### 🔒 Security Notes

> ⚠️ Passwords are stored unencrypted. This app is intended for **educational purposes only**.

* Do **not** use this in production without adding encryption and secure file handling.
* You can extend it with modules like `cryptography`, `keyring`, or secure vault integrations.

---

