+++
date = '2024-12-07T16:06:15Z'
draft = false
title = 'Mocking Classes With Real Time Facades'
tags = ["Laravel", "Testing", "Facades", "Mocking"]
categories = ["Programming", "Laravel"]
image = "/images/mocking-with-facade.jpg"
+++

In PHP, particularly within frameworks like Laravel, facades provide a static-like interface to classes available in the service container. Here, we delve into the concept of real-time facades, which allow you to treat any class in your application as if it were a facade, enhancing your ability to mock dependencies for testing. 

<!--more-->

### Understanding Real-Time Facades for Mocking

When employing real-time facades, you essentially use the Facades namespace before the path of the class you intend to mock or interact with. This approach dynamically creates facade access for any class without needing to define a specific facade class.

Let's start by looking at how we might use a class without real-time facades:

```php
use App\Clients\ClientFactory;
```

Here, `ClientFactory` is used directly. However, when you apply the real-time facade concept, you alter the usage like this:

```php
use Facades\App\Clients\ClientFactory;
```

By using Facades before App\Clients\ClientFactory, you're instructing PHP to resolve the ClientFactory from the service container as if it were a facade. This is powerful for mocking because:

- Dependency Injection: The actual implementation is resolved from the container, adhering to the principles of dependency injection.
- Mocking: You can easily mock this facade for testing purposes. For example:

```php
 ClientFactory::shouldReceive('make')->andReturn(new class implements Client {
        public function checkAvailability(Stock $stock): StockStatus
        {
            return new StockStatus($available = true, $price = 9900);
        }
    });
```

This line mocks the make method of ClientFactory to return a FakeClient instance, which is particularly useful in unit testing where you want to control what the make method does.

### Implementation in Your Code for Mocking

To use this real-time facade approach in your testing environment, you need to adjust the class usage in your code as well. Here's how you might implement it:
  
```diff
- use App\Clients\ClientFactory;
+ use Facades\App\Clients\ClientFactory;
```
  
  This change allows you to mock the ClientFactory class in your tests, providing a more controlled environment for testing.


### Conclusion
Real-time facades simplify the interaction with classes in your application, making them behave like facades with minimal setup. This technique enhances both development and testing by allowing more flexible and mockable code structures. If you're working in environments where dynamic instantiation from a container is beneficial, embracing real-time facades can significantly streamline your mocking process during testing.