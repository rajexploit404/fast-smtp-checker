import smtplib
from email.message import EmailMessage
import threading
import time
from colorama import Fore, init

init(autoreset=True)

HTML_MESSAGE = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SMTP Checker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #2C3E50;
            color: white;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .container {
            background-color: #34495E;
            padding: 30px;
            margin-top: 50px;
            border-radius: 8px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }
        h1 {
            font-size: 3em;
            color: #1ABC9C;
        }
        p {
            font-size: 1.2em;
            color: #BDC3C7;
        }
        footer {
            position: absolute;
            bottom: 10px;
            font-size: 0.9em;
            color: #BDC3C7;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>SMTP CHECKER</h1>
        <p>MADE BY RAJEXPLOIT404</p>
    </div>
    <footer>&copy; 2024 RAJEXPLOIT404. All rights reserved.</footer>
</body>
</html>
"""

def smtp_check(server, port, email, passwd, recipient):
    try:
        msg = EmailMessage()
        msg["From"] = email
        msg["To"] = recipient
        msg["Subject"] = "SMTP Checker Test Email"
        msg["Reply-To"] = email
        msg["Message-ID"] = f"<{time.time()}@{server}>"
        msg["Return-Path"] = email
        msg.add_alternative(HTML_MESSAGE, subtype="html")

        with smtplib.SMTP(server, port, timeout=10) as smtp:
            smtp.ehlo()
            if port == 587:
                smtp.starttls()
            smtp.login(email, passwd)
            smtp.send_message(msg)

            print(Fore.GREEN + f"[+] Successfully sent from {email} to {recipient}")
            with open("alive.txt", "a") as f:
                f.write(f"{server}|{port}|{email}|{passwd}\n")

    except (smtplib.SMTPAuthenticationError, smtplib.SMTPRecipientsRefused):
        print(Fore.RED + f"[-] Failed to send from {email} (Authentication error)")
    except smtplib.SMTPException:
        print(Fore.RED + f"[-] Failed to send from {email}")
    except Exception:
        print(Fore.RED + f"[-] Failed to send from {email} (General error)")

def load_smtp_list(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip().split('|') for line in file if '|' in line]
    except FileNotFoundError:
        print(Fore.RED + f"File '{file_path}' not found.")
        return []

def worker(smtp_list, recipient):
    while smtp_list:
        server, port, email, passwd = smtp_list.pop(0)
        smtp_check(server, int(port), email, passwd, recipient)
        time.sleep(0.1)

def print_banner():
    banner = """
     ███████╗████████╗██╗██████╗ ██╗  ██╗███████╗██╗██╗██████╗ 
     ╚══███╔╝╚══██╔╝██║██╔══██╗██║  ██║██╔════╝██║██║██╔══██╗
        ██╔╝    ██║   ██║██████╔╝███████║███████╗██║██║██████╔╝
       ██╔╝     ██║   ██║██╔═══╝ ██╔══██║╚════██║██║██║██╔══██╗
     ███████╗   ██║   ██║██║     ██║  ██║███████║██║██║██████╔╝
     ╚══════╝   ╚═╝   ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝╚═╝╚═════╝ 
    """
    print(Fore.CYAN + banner)
    print(Fore.GREEN + "SMTP CHECKER")
    print(Fore.YELLOW + "Coded by RajExploit404\n")

if __name__ == "__main__":
    print_banner()

    smtp_file = input("Enter the SMTP list file name (e.g., smtp_list.txt): ").strip()
    recipient = input("Enter the recipient email: ").strip()

    smtp_list = load_smtp_list(smtp_file)

    if smtp_list:
        threads = []
        thread_count = 30

        for _ in range(thread_count):
            t = threading.Thread(target=worker, args=(smtp_list, recipient))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
    else:
        print(Fore.RED + "SMTP list is empty or file not found.")
