# What is this Project?
### This app accesses news about a particular topic and send them by email.

---

To send emails using Gmail from an app (like a Python script), **you need an App Password** (especially if you have 2-Step Verification enabled). Here's how to generate one:

---

### ✅ Step-by-Step: Create a Gmail App Password

#### 🔐 Prerequisite:

You **must have 2-Step Verification enabled** on your Google Account.

---

### ✅ 1. Enable 2-Step Verification (if not already enabled)

1. Go to: [https://myaccount.google.com/security](https://myaccount.google.com/security)
2. Scroll to **“Signing in to Google”**
3. Click **“2-Step Verification”**
4. Follow the steps to enable it

---

### ✅ 2. Generate App Password

1. After 2-Step Verification is enabled, go back to:
   [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

2. Sign in again if asked.

3. Under **“Select the app”**, choose **Mail** (or select **Other (Custom name)** and type something like `MyPythonApp`)

4. Under **“Select device”**, choose your device (or "Other").

5. Click **Generate**.

6. ✅ Google will show you a **16-character app password** (e.g., `abcd efgh ijkl mnop`) — **copy it**.

> 🔒 This is the password you’ll use in your code **instead of your actual Gmail password**.

---

### 🧪 Example usage in Python with `smtplib`:

```python
import smtplib

sender_email = "your_email@gmail.com"
receiver_email = "recipient@example.com"
app_password = "abcd efgh ijkl mnop"  # Your 16-char App Password (no spaces)

message = "Subject: Hello\n\nThis is a test email from Python."

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender_email, app_password)
    smtp.sendmail(sender_email, receiver_email, message)
```

---

### ⚠️ Important Notes:

* Do **not** use your regular Gmail password in apps — use the **App Password** only.
* Treat App Passwords like your actual password — **keep them secret**.
* You can revoke them anytime from the App Passwords page.

---

