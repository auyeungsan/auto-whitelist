import boto3
import fun

aws_client = boto3.client('wafv2')
ip_set_name = 'api-client-ip'
ip_set_id = '1b707298-0e00-463c-bf0e-f0404574818c'

# get current ip set 'lock token' and 'ip list'
response_get_ip_set = aws_client.get_ip_set(
    Name=ip_set_name,
    Scope='CLOUDFRONT',
    Id=ip_set_id
)
ip_set_lock_token = response_get_ip_set['LockToken']

aws_ip_set = response_get_ip_set['IPSet']['Addresses']
# print("current ip list :", array_sort(ip_a))
fun.write_file("aws_ip.txt", fun.array_sort(aws_ip_set))

# curl api to get update ip here
api_response = fun.api_request('http://api.open-notify.org/astros.json').json()
print('api request: ', api_response)
print('api request: ', api_response["people"])
for api_re in api_response["people"]:
    print('name : ', api_re['name'])
    print('craft : ', api_re['craft'])
update_ip = ['172.16.0.1/32', '172.16.0.2/32', '192.168.0.1/32', '192.168.0.2/32', '192.168.0.3/32', '192.168.0.4/32', '192.168.0.5/32']
# print("current ip list :", array_sort(ip_b))
fun.write_file("update_ip.txt", fun.array_sort(update_ip))


digest_aws = fun.hash_file(fun.read_file("aws_ip.txt"))
# print(digest_aws)

digest_update = fun.hash_file(fun.read_file("update_ip.txt"))
# print(digest_update)


if digest_update != digest_aws:
    print("不相等")

    response_update_ip_Set = aws_client.update_ip_set(
        Name=ip_set_name,
        Scope='CLOUDFRONT',
        Id=ip_set_id,
        Addresses=update_ip,
        LockToken=ip_set_lock_token
    )

    print('info after run : ', response_update_ip_Set)

else:
    print("相等")
