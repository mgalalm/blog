+++
date = '2024-12-07T21:30:02Z'
draft = false
title = 'Stubs Mocks Double and Spies When to Use One Over the Other?'
image = '/images/mock-stub-spy.jpg'
tags = ['Laravel', 'Testing', 'Mockery', 'Unit Testing']
categories = ['Laravel', 'Testing']
description = 'Learn about the differences between Stubs, Mocks, Doubles, and Spies in Laravel testing scenarios and when to use each one.'
+++

In software development, especially when working with frameworks like Laravel, unit testing is crucial for ensuring code reliability and maintainability. Laravel integrates well with Mockery, a mocking framework for PHP, to help developers create test doubles. Let's delve into the concepts of Stubs, Mocks, Doubles, and Spies, and how they're used in Laravel testing scenarios.
<!--more-->


### What are Test Doubles?
Test doubles are objects that stand in for real objects during testing. They simulate the behavior of complex, real objects to isolate the code being tested. The term "test double" was coined by Gerard Meszaros to describe these stand-ins, which include stubs, mocks, dummies, fakes, and spies.


### Stubs
A stub is an object that provides predefined answers to calls made during a test, focusing on controlling the output of the dependency.

When to use Stubs: Use stubs when you want to replace a method's behavior with a fixed response. For example, when testing a method that interacts with a database, you can use a stub to return a predefined dataset instead of querying the database. Stubs are useful when you need to control the output of a method to test different scenarios. 

```php
$stub = Mockery::mock('MyClass');
$stub->shouldReceive('method')->andReturn('foo');
```
This stub will return 'foo' whenever the method is called. Example of usage would be:
When you want to stub API call to return a specific response without actually making the network request.

### Mocks

Mocks are similar to stubs but they also verify interactions with the system under test. They expect certain methods to be called with specific parameters.

When to use Mocks: Mocks are used when you need to assert that certain methods were called with the right parameters:

```php
$mock = Mockery::mock('MyClass');
$mock->shouldReceive('method')->with('foo')->once();
```
This mock will expect the method to be called with 'foo' as a parameter exactly once. Example of usage would be:
When you want to ensure that a method is called with specific parameters. For example, when testing a method that sends an email, you can use a mock to verify that the email was sent with the correct subject and body.

### Spies

Spies are test doubles that record calls made during the test, allowing assertions after the fact rather than setting expectations beforehand. Spies are useful for verifying that methods get called without prescribing how they should be called:

```php
$spy = Mockery::spy('MyService');
// Perform some action that should call 'method' on 'MyService'
$spy->shouldHaveReceived('method');
```
 Example would be, If you're testing event broadcasting in Laravel, you might use a spy to ensure an event was dispatched without caring about the specific details of the event data. 


 ### Final Thoughts
Choosing between stubs, mocks, doubles, and spies depends on the specific requirements of your test. Stubs are useful when you want to control the output of a method, mocks are used to verify interactions, and spies are helpful for verifying calls after the fact. By understanding the differences between these test doubles, you can write more effective and maintainable tests in your Laravel applications. 