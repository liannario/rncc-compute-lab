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

![cloud9_accountid](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/cloud9_account_id.PNG "")

## Create DynamoDB table.

From the _Services_ menu, choose _DynamoDB_ and click it.

![dynamo_0](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/dynamo_create_0.PNG "")

At the main DynamoDB screen, click on the _Create table_ button at the center.

![dynamo_1](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/dynamo_create_1.PNG "")

Now you need to give the table a name and configure its settings.
 * Enter **PacketCaptures** into the _Table name_ field.
 * For the partition key, enter **s3Id** into the _Primary key_ field and leave _String_ as the type of the field.

We will use the default settings for this demo, so go ahead and click on the _Create_ button at the bottom right corner of the screen.

![dynamo_2](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/dynamo_create_2.PNG "")

You will be taken to the main table screen, where you will be presented with an overview of the table and a series of tabs to access the different features in a table. For now, we are just interested in making sure the table is empty.

Click on the _Items_ tab at the center top portion of the screen.

![dynamo_3](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/dynamo_create_3.PNG "")

You will now be presented with a screen like the one below. Note that the number of total items is zero, and that there are no items whatsoever listed below.

![dynamo_4](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/dynamo_create_4.PNG "")

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
