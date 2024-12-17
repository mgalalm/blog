+++
date = '2024-12-17T20:25:20Z'
draft = false
title = 'Extracting and Reusing Functions in Pest Tests'
image = '/images/extracting-and-reusing-functions-pest.jpeg'
+++
When working with Pest—the modern and elegant testing framework for PHP—you might encounter scenarios where a custom function is being used across multiple test files. Maybe it's a function to mock a client request, handle repetitive setup tasks, or simulate specific data conditions. Whatever the case, it’s a great opportunity to extract that function to a reusable location. But where should you place it? <!--more-->

There are two common options:

1. Define it in your Pest.php file.
2. Create a dedicated Helpers.php file.

I prefer the second option for better organization. The Pest.php file handles global helpers and configurations but can become cluttered with reusable functions. Creating a Helpers.php file keeps things clean, and Pest automatically loads it without extra setup or namespaces.

### Setting Up Helpers.php

First, create a Helpers.php file in your tests directory. This file will contain all your reusable functions. Here’s an example of a simple function that mocks a client request:

```php
use App\Clients\StockStatus;
use Facades\App\Clients\ClientFactory;
use Cknow\Money\Money;

function mockClientRequest($available, $price)
{
    ClientFactory::shouldReceive('make->checkAvailability')
        ->andReturn(new StockStatus($available, Money::parse($price)));
}
```

### Using the Helper Function in Tests

Here’s how you can use the `mockClientRequest` function in your Pest tests:

```diff
it('updates local status after tracking', function () {

- ClientFactory::shouldReceive('make->checkAvailability')->andReturn(new StockStatus($available, Money::parse($price)));
+ mockClientRequest(available: true, price: '£299.99');

$stock = tap(Stock::first())->track();

$this->assertTrue($stock->in_stock);
$this->assertEquals(29999, $stock->price); // Price in cents
$this->assertEquals('GBP', $stock->currency);
});
```

### What Happens?

1. Mocking requests: Simulates client response with availability and price.

2. Tracking stock: Updates the database using mocked data.

3. Assertions: Verifies stock status, price, and currency, using the new custom function.


### Final Thoughts
Extracting functions into Helpers.php improves test suite clarity and maintainability. It saves time and keeps your workflow organized. Pest’s ability to autoload this file makes it effortless to reuse functions across your test suite. Give it a try and see how it enhances your testing experience.