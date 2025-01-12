+++
date = '2024-12-23T21:25:28Z'
draft = false
title = 'How to Send Emails Using Amazon SES in Laravel'
image = '/images/amazon-ses-laravel.jpeg'
tags = ['Laravel', 'Cloud', 'AWS', 'Amazon SES']
categories = ['Laravel', 'Cloud', 'AWS']
+++
Hey there, Cloud enthusiast! If you’ve ever wanted to send emails through Amazon SES (Simple Email Service) using Laravel, you’re in the right place. Amazon SES is reliable, scalable, and integrates beautifully with Laravel. Let’s dive into the steps to get it up and running in no time! <!--more-->

### Step 1: Install the Required Package

To start, you’ll need to install the `aws/aws-sdk-php-laravel` package. This package provides an easy way to interact with Amazon Web Services (AWS) services, including SES.

```bash
composer require aws/aws-sdk-php-laravel
```

### Step 2: Configure Your AWS Credentials

Next, you’ll need to configure your AWS credentials. Open your `.env` file and add the following lines:

```bash
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_DEFAULT_REGION=your-default-region
```

Replace `your-access-key-id`, `your-secret-access-key`, and `your-default-region` with your actual AWS credentials.

### Step 3: Configure the Mail Driver

While you are in the `.env` file, make sure you have the following lines set up:

```bash
MAIL_MAILER=ses
MAIL_FROM_ADDRESS=[your verified email address]
```

{{% callout warning %}}
Note: The MAIL_FROM_ADDRESS must match an email address verified in your AWS SES console. If it’s not verified, Amazon SES won’t let you send emails.
{{% /callout %}}

No extra setup is required in your config/mail.php file—it’s already set up to read from your .env file.

### Step 4: Send an Email
Now you should get a good handle on how  to send emails using Amazon SES in Laravel. We didn't cover here how to configure Amazon SES itself in AWS Console, but you can find a detailed guide in the [official documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/setting-up-email.html). Although, I will try to put together a guide on that in the future. Stay tuned!