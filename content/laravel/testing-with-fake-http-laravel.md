---
title: "Testing with Fake HTTP Requests in Laravel"
date: 2024-12-03T10:48:00Z
draft: false
tags: ["Laravel", "Testing", "HTTP", "Fake"]
image: "/images/fake-http.jpg"
---
In Laravel, one of the powerful tools for testing is the ability to simulate HTTP responses without actually hitting an external API. This is particularly useful when you need to ensure your application behaves correctly regardless of the API's response. <!--more-->

Here's how you can use `Http::fake()` to test a scenario where you're checking the stock status and price of an item from an Amazon-like service.


## The Tracking Functionality

Let's consider a method `track()` in a `Stock` model which checks the stock status and price from an external service:

```php
public function track()
{
    if ($this->retailer->name === 'Amazon UK') {
        $results = Http::get('http://foo.test')->json();
        $this->update([
            'in_stock' => $results['available'],
            'price' => $results['price'],
        ]);
    }
}
```

This function assumes that when it makes an HTTP GET request to http://foo.test, it receives JSON data with keys available and price.

### Faking the HTTP Response

To test this method without real network calls, we can use Laravel's Http::fake() method:

```php
/** @test */
it("tracks products stock", function () {
    // Fake the HTTP response for 'foo.test'
    Http::fake([
        'foo.test' => Http::response([
            'available' => false,
            'price' => 2000,
        ], 200)
    ]);

    // Setup the stock instance
    $stock = new Stock([
        'price' => 2000,
        'url' => 'http://www.amazon.uk',
        'in_stock' => true, // Initially, we assume it's in stock
        'sku' => '12345',
    ]);

    // Assuming $amazon_uk is an instance of a Retailer model or similar
    $amazon_uk->addStock($my_book, $stock);

    // Call the track method which should update the stock
    $stock->track();

    // Assert that the stock is now reflected as not in stock
    $this->assertFalse($stock->fresh()->in_stock);
});
```

### How it works
 We use Http::fake() to define what http://foo.test should respond with. Here, we're saying it should return a JSON response with available set to false and price at 2000.

### Why Use Http::fake()?

- *Consistency*: Tests are not dependent on external service availability or data changes.
- Speed: Reduces test time by avoiding actual HTTP requests.
- Isolation: Keeps tests isolated from the network and external dependencies, making them more reliable and easier to maintain.

By leveraging Http::fake(), you can thoroughly test how your application handles different scenarios from external APIs without the need for actual integration with those services during your test runs. This approach is essential for developing robust, reliable, and efficient applications.