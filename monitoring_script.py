import boto3
from datetime import datetime, timede

REGION_NAME = 'us-east-1'
INSTANCE_ID = 'i-0abcdef1234567890'  # i had deleted my instance from aws account because i do not want to be charged
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:12345678910:ServerHealthAlerts'  # 
CPU_THRESHOLD_PERCENT = 80.0  # Threshold to trigger an alert

# --- AWS Clients ---
cloudwatch = boto3.client('cloudwatch', region_name=REGION_NAME)
sns = boto3.client('sns', region_name=REGION_NAME)

def get_cpu_utilization(instance_id):
    """the average CPUUtilization
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=5)

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,  # 5 minutes
        Statistics=['Average']
    )

    if response['Datapoints']:
        return max(response['Datapoints'], key=lambda x: x['Timestamp'])['Average']
    return None

def send_alert(instance_id, utilization):
    "Sends an alert notification "
    message = f"Instance ID: {instance_id}\nCPU Utilization: {utilization:.2f}%\nThreshold: {CPU_THRESHOLD_PERCENT}%"
    sns.publish(TopicArn=SNS_TOPIC_ARN, Message=message)

def monitor_instance_health():
    "Monitors the instance health and triggers alerts."
    cpu_usage = get_cpu_utilization(INSTANCE_ID)
    if cpu_usage is not None:
        print(f"Current CPU Utilization: {cpu_usage:.2f}%")
        if cpu_usage > CPU_THRESHOLD_PERCENT:
            print("⚠️ High CPU utilization! Sending alert.")
            send_alert(INSTANCE_ID, cpu_usage)
        else:
            print("✅ Instance is healthy.")
    else:
        print("Monitoring failed due to lack of data.")

if __name__ == "__main__":
    monitor_instance_health()
