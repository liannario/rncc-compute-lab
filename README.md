# Networking and compute lab (module 2)

<p align="center">
</p>

## Objective

Capture files were obtained from: https://wiki.wireshark.org/SampleCaptures

## Initialize your environment

### 1. Create a Cloud9 environment.

From the services menu, choose Cloud9.

![cloud9_0](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/cloud9_create_0.PNG "")

Click on the _Create environment_ button on the right side of the page.

![cloud9_1](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/cloud9_create_1.PNG "")

Now, enter the name of your Cloud9 environment: **MyCloud9Environment** in the _Name_ field, and click on _Next step_.

![cloud9_1](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/cloud9_create_2.PNG "")

Leave the choices as default, since we want:
 * A new instance for the environment running on EC2.
 * The instance to be a **t2.micro** type of instance.
 * To install Amazon Linux on the t2.micro instance.

Then, click on _Next step_.

![cloud9_1](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/cloud9_create_3.PNG "")

Review the information and click on _Create environment_.

![cloud9_1](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/cloud9_create_4.PNG "")

### 2. Within the Cloud9 instance that you just created obtain a copy of this repository.

Make sure you are in your environment directory.
```sh
cd ~/environment
```

Then run the following git command to clone the repository:
```sh
git clone https://github.com/pnpolcher/rncc-compute-lab.git && cd rncc-compute-lab
```

### 3. Run the initialization script to automatically create an S3 bucket and populate it.
```
bash initialize.sh
```
Write down the account ID that the script prints to the terminal. _This is important and will be used in a later step._


## Create DynamoDB table.

<p align="center">
</p>

## Check DynamoDB table

<p align="center">
</p>

## Create SNS topic

<p align="center">
</p>

## Create Lambda layer

<p align="center">
</p>

## Create Lambda function

### Add S3 trigger

### Add event to SNS

## Create EC2 instances

## Create ELB (Elastic Load Balancer)

## Check website

## Create SNS subscription

## Verify SNS subscription

## Upload file

## Check DynamoDB table and website again
