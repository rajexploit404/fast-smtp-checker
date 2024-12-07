# Fast SMTP Checker Coded By Rajexploit404

A simple, fast, and efficient Python-based SMTP checker to test multiple SMTP servers for connectivity and functionality. Coded by **RajExploit404**.

## Features

- Checks the ability to send email through multiple SMTP servers.
- Displays clear success and failure messages in color.
- Supports threaded connections to speed up the process.
- Displays the result in a clean format.

## Requirements

This project requires Python 3 and the following Python libraries:

- `colorama`: For colored output in the terminal.
  
To install the required libraries, create a `requirements.txt` file by following the instructions below.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/rajexploit404/fast-smtp-checker.git
   cd fast-smtp-checker
   ```

2. Install dependencies using `pip`:

   ```bash
   pip3 install -r requirements.txt
   ```

### Requirements File (`requirements.txt`)

```
colorama
```

## Usage

### Running the SMTP Checker

To run the SMTP checker, simply execute the `main.py` file. Make sure you have your SMTP list file (`smtp.txt`) ready.

```bash
python3 main.py
```

You will be prompted to enter the following:

1. **SMTP list file** (e.g., `smtp.txt`)
2. **Recipient email address**

### Example `smtp.txt` format

The `smtp.txt` file should contain a list of SMTP server details in the following format:

```
example.com|port|example@example.com|examplepass
smtp.example.org|587|user@example.com|password123
mail.example.net|25|someone@domain.com|securepass
```

### Example Output

```bash
     ███████╗████████╗██╗██████╗ ██╗  ██╗███████╗██╗██╗██████╗                                                                                                         
     ╚══███╔╝╚══██╔╝██║██╔══██╗██║  ██║██╔════╝██║██║██╔══██╗                                                                                                          
        ██╔╝    ██║   ██║██████╔╝███████║███████╗██║██║██████╔╝                                                                                                        
       ██╔╝     ██║   ██║██╔═══╝ ██╔══██║╚════██║██║██║██╔══██╗                                                                                                        
     ███████╗   ██║   ██║██║     ██║  ██║███████║██║██║██████╔╝                                                                                                        
     ╚══════╝   ╚═╝   ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝╚═╝╚═════╝                                                                                                         
                                                                                                                                                                       
SMTP CHECKER
Coded by RajExploit404
                                                                                                                                                                       
Enter the SMTP list file name (e.g., smtp_list.txt): smtp.txt
Enter the recipient email: receive@gmail.com
[-] Failed to send from example.com
[+] Successfully sent from test@gmail.com to receive@gmail.com
[+] Successfully sent from test@yahoo.com to receive@gmail.com
[+] Successfully sent from victim@gmail.com to receive@gmail.com
```

### Output Explanation

- **[+] Successfully sent from...**: Indicates the email was successfully sent from the specified SMTP server.
- **[-] Failed to send from...**: Indicates a failure in sending the email from the SMTP server.
