import boto3

#AWS_SHARED_CREDENTIALS_FILE = 'C:/Users/fallo/.aws/credentials'
#AWS_CONFIG_FILE = 'C:/Users/fallo/.aws/config'

def list_ec2():
    ec2 = boto3.resource('ec2')
    counter = 0
    instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        counter = counter + 1
        print(instance.id, instance.instance_type)
    print(f'You have {counter} instances running!')
    main()

def create_ec2():
    ec2 = boto3.resource('ec2')
    ec2.create_instances(ImageId='ami-051dfed8f67f095f5', MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName='ellenszenves')
    main()

def create_s3():
    buck_name = input(f'Write a name for your bucket: ')
    with open('C:\\Users\\fallo\\.aws\\config', 'r') as config_file:
        for row in config_file:
            if row.startswith('region'):
                cutted = row.split('=')
                region = cutted[1].strip()
    print(region)
    s3_client = boto3.client('s3', region_name=region)
    location = {'LocationConstraint': region}
    s3_client.create_bucket(Bucket=buck_name, CreateBucketConfiguration=location)
    print(f'Bucket {buck_name} created!')
    main()

def list_s3():
    s3 = boto3.resource('s3')
    counter = 0
    buck_list = []
    for bucket in s3.buckets.all():
        #print(bucket.name)
        buck_list.append(bucket.name)
        counter = counter + 1
    print(f'You have {counter} bucket!')
    print(buck_list)
    main()

def del_s3():
    imp = input(f'Write the name of the bucket: ')
    with open('C:\\Users\\fallo\\.aws\\config', 'r') as config_file:
        for row in config_file:
            if row.startswith('region'):
                cutted = row.split('=')
                region = cutted[1].strip()
    client = boto3.client('s3', region_name=region)
    client.delete_bucket(Bucket=imp)
    print(f'Bucket {imp} deleted!')
    main()

def main():
    stringem = """
    Select a number from the menu:
    1. Create EC2 instance
    2. List EC2 instances
    3. S3 bucket
    4. List buckets
    5. Delete buckets
    """
    print(stringem)
    imp = input(f'Choose:  ')
    if imp == '1':
        create_ec2()
    elif imp == '2':
        list_ec2()
    elif imp == '3':
        create_s3()
    elif imp == '4':
        list_s3()
    elif imp == '5':
        del_s3()
    else:
        print(f'Invalid option!')
        main()
    
start_str = """
    boto3 teszt from Ellenszenves!
    If you want to use aws in another region, modify it in your config file!"""
print(start_str)
main()