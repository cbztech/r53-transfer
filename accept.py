import boto3

# Provide the domain name being accepted.
# Supply the password that was sent in the transfer response.

domain_name = ""
password = ""

r53 = boto3.client("route53domains", region_name='us-east-1')

response = r53.accept_domain_transfer_from_another_aws_account(
    DomainName=domain_name,
    Password=password
)

print(response)
