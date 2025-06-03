1. OVERVIEW
    This lab demosntrates NO RATE LIMITING bug. This lab consists of a vunarable php code that simulates a backend server for checking 
    username and passowrd, and a python script to exploit the server.

2. ROOT CAUSE
    This usually happens when developers forgets to limit the amount of tries for a perticular field. This allows the attacker to send inputs 
    multiple times without any restriction.

3. VULNARABLE SERVER
    index.php is a vulnarable server that requests username and passeword through POST based input. It then checks whether the username and 
    password match the data.

3. EXPLOIT
    The exploit takes the advantage of no rate limit and sends a POST based request to the server containing a username and password.

4. IMPACT 
    This allows a powerfull brute-force attack on the password field which made up of 4 digits. Through certain crafted payloads, these POST
    requests can be sent in a large number and crash the server.

5. CVSS SCROE ESTIMATE

- **Base Score**: 7.1 (High)
- **Attack Vector**: Network
- **Attack Complexity**: Low
- **Privileges Required**: None
- **User Interaction**: None
- **Confidentiality**: High
- **Integrity**: High

6. HOW TO RUN
    Open 2 terminals. In one run the index.php script in the vuln_code directory using the command: "sudo php -S localhost:8080"
    In another terminal run the exploit.py script in the vuln_code directory using the command: "python3 exploit.py"
