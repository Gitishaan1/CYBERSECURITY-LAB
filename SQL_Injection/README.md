Sql Injection - Login bypass

1. SUMMARY:
This project demonstrates sql injection vulnarability using a PHP and python code both simulating a 
login page. The source code accepts user input and enters it into the database query without
sanitization. This leads to login authentication bypass and potential data leak from the database.

2. ROOT CAUSE:
Processing user input into database query without proper sanitization.

3. HOW TO RUN:
i) Run the PHP server over localhost:
php -S localhost:8080
ii) Go to any browser and type:
http://localhost:8080/index.php?username=anything' or '1' = '1' -- &password=anything

4. EXPLOIT:
Run the exploit file in the directory vuln_lab 'exploit.py':
pyhton3 exploit.py

5. DISCLAIMER:
This project if for your basic understanding of sql injection. It is made only for educational
purposes and does not intend to harm anyone. Advanced sql injection projects are coming soon !!
