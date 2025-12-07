# 1. Automated Server Provisioning and Monitoring

## Description

This project involved the design and implementation of a fully automated process to provision a secure and scalable web server environment on Amazon Web Services (AWS). Following the initial provisioning, a comprehensive monitoring script was developed to continuously check and report on the system's health.

## 🛠️ Technologies Used

* **AWS Services:** EC2, VPC, IAM, S3, CloudWatch
* **Programming/Scripting:** Python (Boto3)

## ✨ Key Accomplishments

The automation and monitoring solution achieved the following:

* **Programmatic Infrastructure Management:** Utilized the **Boto3** library to programmatically manage AWS resources, specifically:
    * Creation and termination of **EC2 instances**.
    * Configuration of network **security groups**.
    * Attachment of **S3 buckets** for highly available static content hosting.
* **Automated Health Monitoring:** Developed a **Python script** that leveraged **CloudWatch metrics** to:
    * Continuously check the health status of provisioned instances.
    * Send real-time alerts via **SNS (Simple Notification Service)** in case of issues.
* **Security & Compliance:** Applied industry-standard **security best practices** throughout the deployment, including:
    * Configuring highly **restrictive IAM roles**.
    * Implementing **least-privilege access** for all AWS resources to minimize the security footprint.

1.  **Prerequisites:**
    * [pip install Python3]
    * [pip install Boto3]
    * Configured AWS CLI with necessary access credentials.
2.  **Provisioning:**
    ```bash
    # command to run the provisioning script
    python provision_server.py
    ```
3.  **Monitoring:**
    ```bash
    # Excute 
    python monitoring_script.py --start
    ```

---
