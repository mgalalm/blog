+++
date = '2024-12-16T16:53:20Z'
draft = false
title = 'How to Keep Your Test Suite Under Control Without Breaking the Bank'
image = '/images/integration-tests-group.jpg'
+++

Imagine this: you’re running your test suite every time you make a change, but instead of your tests zipping through like a speedster, they keep calling an evolving 3rd party API that you need to make sure your code is still compatible with.  <!--more-->

You’re not only waiting for your tests to finish, but you’re also paying for the API calls. This is a common scenario in the world of testing, and it can be a real pain in the neck. In this article, we’ll explore how to keep your test suite under control without breaking the bank.



## Integration Tests Are Heavy
Integration tests are awesome because they ensure your application works as a whole, including those tricky external APIs. But here’s the rub:

- They’re expensive: Each test call to an external API takes time and bandwidth.
- They’re unnecessary (most of the time): Do you really need to test that API call every single time you update a CSS file? Nope.


## Group Your Tests Like a Pro
Laravel and Pest make it ridiculously easy to organize and control your test suite. We can mark specific tests as part of an "API" group and exclude them when we run our suite during regular development. Here’s how.


### Step 1: Create a Test Group
You can organize your integration tests into a specific folder, like tests/Integration. Then, use a group to mark them as belonging to an API category.

Add a Test Suite in phpunit.xml
Update your phpunit.xml to include a dedicated test suite for integration tests:

<testsuite name="Integration">
    <directory>tests/Integration</directory>
</testsuite>

### Step 2 Configure Groups in Pest
If you’re using Pest—and you should because it’s clean and fun—you can extend it to include your integration tests. Update your Pest.php file like this:

```php
pest()->extend(Tests\TestCase::class)
    // Add other test configurations here if needed
    ->in(targets: 'Integration');
```

### Step 3: Exclude the Group When Running Tests

Here’s the magic. When running your test suite, simply exclude the integration group during your normal development workflow:

```bash
php artisan test --exclude-group integration
```
This command skips those heavy integration tests while letting you focus on the rest of your suite

## When to Run Integration Tests?

You might be thinking, “If I’m excluding integration tests, when do I actually run them?” Good question! Here’s when:

1. On Deployment: Make it part of your CI/CD pipeline. Integration tests can run once before your code ships to production.
2. Sporadically: Running them manually every now and then is enough to ensure external APIs still behave as expected.
3. When You’re Testing Changes to External APIs: Any changes to API-related logic should prompt a full run of these tests.

## Why This Approach Works

This setup keeps your test suite lean during development but ensures those critical integration tests don’t get ignored. It’s a win-win:

1. Faster Feedback: Running tests is quicker when you skip integration tests during active coding.
2. Save API Limits: No need to bombard external APIs with every little code change.
3. Less Frustration: Your team (and your future self) will thank you for keeping the test suite manageable


###TL;DR: Don't Let Integration Tests Weigh You Down

Testing should empower you, not slow you down. By grouping your integration tests and excluding them when you don’t need them, you can run your suite as often as you like without fear of wasting resources or time.