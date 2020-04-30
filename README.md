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

![cloud9_2](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/cloud9_create_2.PNG "")

Leave the choices as default, since we want:
 * A new instance for the environment running on EC2.
 * The instance to be a **t2.micro** type of instance.
 * To install Amazon Linux on the t2.micro instance.

Then, click on _Next step_.

![cloud9_3](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/cloud9_create_3.PNG "")

Review the information and click on _Create environment_.

![cloud9_4](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/cloud9_create_4.PNG "")

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

On the _Services menu_, type in **SNS** in the search bar, and click on the _Simple Notification Service_ service link.

![sns_0](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/sns_topic_0.PNG "")

Enter the **PacketCaptureProcessorTopic** in the _Topic name_ field, and click on the _Next step_ button below.

![sns_1](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/sns_topic_1.PNG "")

We will not be filling in any optional data, so you can safely click on the _Create topic_ button at the lower right corner of the screen.

![sns_2](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/sns_topic_2.PNG "")

You have created an SNS topic, which we will be using later on in this tutorial. Let's move on to creating our Lambda function.

## Create Lambda layer

On the _Services menu_, type in **Lambda** in the search bar, and click on the _Lambda_ service link.

![lambda_0](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_0.PNG "")

On the sidebar on your left, click on the _Layers_ menu item.

![lambda_layers_1](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_layers_1.PNG "")

Then, click on the _Create layer_ at the top right corner of the screen.

![lambda_layers_2](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_layers_2.PNG "")

You will be taken to the Create layer screen. Since we're creating a layer for Scapy to be available to a number of Lambda functions, we will name it accordingly:

 * Type **ScapyLayer** into the _Name_ field.
 * Select _Upload a file from Amazon S3_.
 * In the _Amazon S3 link URL_ text field, enter the URL to the file within the bucket that was created for you. It is **s3://ripe-ncc-compute-lab-012345678901/scapy_layer.zip**, where 012345678901 is the account ID that you wrote down during the first steps.
 * From the _Compatible runtimes - optional_ dropdown, choose **Python 3.8**.

Once you are done, click on the _Create_ button at the bottom right corner.

![lambda_layers_3](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_layers_3.PNG "")

## Create Lambda function

Now we will move on to creating the actual Lambda function that will process the cap/pcap files uploaded into the S3 bucket.

From the sidebar on your left, click on _Functions_.

![lambda_functions_1](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_functions_1.PNG "")

Then, click on the _Create function_ button at the top right corner.

![lambda_functions_2](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_functions_2.PNG "")

Leaving the _Author from scratch_ option that is selected by default, enter the lambda function settings:

 * Into the _Function name_ text field, enter **PacketCaptureProcessorFunction**. This will be the name of our Lambda function.
 * From the _Runtime_ dropdown, choose **Python 3.8**.
 * Click on _Choose or create an execution role_ to reveal more options.
 * From the _Execution role_ radio button set, choose _Use an existing role_.
 * From the _Existing role_ dropdown, choose **Cloud9-myLambdaRole**.
 
Now you are ready to create the function. Click on the _Create function_ button at the bottom right corner of the screen.

![lambda_functions_3](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_functions_3.PNG "")

Now, click on the _Layers_ block in the _Designer_ section.

![lambda_functions_4](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_functions_4.PNG "")

Click on _Add a layer_ button in the _Layers_ section below.

![lambda_functions_5](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_functions_5.PNG "")

From the _Name_ dropdown, choose **ScapyLayer**. And from the _Version_ dropdown, choose **1**.

Click on the _Add_ button to continue.

![lambda_functions_6](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_functions_6.PNG "")

### Add S3 trigger

Now we will be adding an S3 trigger, so that every time a **.cap** file is uploaded to our bucket, the lambda function is invoked.

Click on the _Add trigger_ button in the _Designer_ section.

![lambda_functions_7](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_functions_7.PNG "")

From the _Trigger configuration_ dropdown, select _S3_. Then, from the _Bucket_ dropdown, select your bucket. _Remember your bucket starts with_ **ripe-ncc-compute-lab-** _followed by your account ID_.

Leave **All object create events** in the _Event type_ dropdown, and enter **.cap** into the _Suffix_ text field.

Then, click on the _Add_ button at the bottom right corner of the screen.

![lambda_functions_8a](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_functions_8a.PNG "")

### Add code to Lambda

Go back to your Cloud9 editor, open the **lambda.py** file and copy the contents to the clipboard.

![lambda_functions_8b](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_functions_8b.PNG "")

Now, go back to your Lambda tab. Click on the _PacketCaptureProcessorFunction_ block in the _Designer_ section, and paste the code into the _lambda_function.py_ tab in the _Function code_ section.

Then, click on the _Save_ button at the top right corner of the screen.

![lambda_functions_9](https://github.com/pnpolcher/rncc-compute-lab/raw/master/img/lambda_functions_9.PNG "")

### Add event to SNS

## Create EC2 instances

## Create ELB (Elastic Load Balancer)

## Check website

## Create SNS subscription

## Verify SNS subscription

## Upload file

## Check DynamoDB table and website again
