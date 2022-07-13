# Route53 Domain Transfer

---

1. Spin up a virtual environment.
2. Install the requirements (boto3)
3. Setup AWS Credentials in command-line for account that owns domain
4. Set variables in transfer.py
   1. The domain name
   2. Account you are transfering to.
5. Run transfer.py
6. Capture password from the response
7. Setup AWS Credentials for account that received the domain.
8. Set variables in acccept.py
   1. The Domain name
   2. The password
9. Run accept.py
10. Order pizza.
