import boto3

r53 = boto3.client("route53domains", region_name='us-east-1')

# Supply the account number for the account transfering to
# Supply the domain name being transfered.

account_id = ""
domain_name = ""

response = r53.transfer_domain_to_another_aws_account(
    DomainName=domain_name,
    AccountId=account_id
)

print(response)
