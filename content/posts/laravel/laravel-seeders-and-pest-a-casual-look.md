+++
date = '2024-12-04T20:50:12Z'
draft = false
title = 'Laravel Seeders and Pest: A Casual Look'
image = '/images/seeder.jpg'
tags = ['Laravel', 'Testing', 'Pest', 'Seeders']
+++

Let's dive into the world of Laravel seeders used with Pest.

## Setting Up Data with Seeders

Here's a snippet of how you might use a seeder:

<!--more-->


```php
$my_book = Product::create(['name' => "Zayn and Grandad's Van"]);

$amazon_uk = Retailer::create(['name' => 'Amazon UK']);

$stock = new Stock([
    'price' => 2000,
    'url' => 'http://www.amazon.uk',
    'in_stock' => false,
    'sku' => '12345',
]);

$amazon_uk->addStock($my_book, $stock);
```


## Writing Tests with Pest
```php
uses(RefreshDatabase::class);

it("tracks products stock", function () {
    $this->seed(RetailerWithProductSeeder::class);

    $product = Product::first();

    $this->assertFalse($product->inStock());

    Http::fake(fn() => ['available' => true, 'price' => 29900]);

    // Let's pretend the stock is available now
    $this->artisan('track');

    $this->assertTrue(Product::first()->inStock());
});
```
RefreshDatabase clears the database before each test, ensuring no old data messes with your results.

### Advantages of Using Seeders with Pest

- Efficient Setup: Seeders mean you're not rewriting the same setup code for every test. It's like cooking dinner where the prep work is already done.
- Reuse: Seeders are reusable across your tests. Think of them as a favorite recipe you pull out whenever needed.
- Realistic Scenarios: They let you craft complex, real-world-like data setups. Great for when you want to test how your app behaves in varied conditions

### On Readability:
- **Outside Context:** When you see RetailerWithProductSeeder::class, you've got to go look elsewhere to understand what data it's seeding. It's like a film reference that makes you want to check the movie out to get the full picture.
- **Debugging Complexity:** If things go wrong, you're not just debugging the test; you're also looking at what the seeder's doing. Adds a bit of detective work to your debugging process.
- **Test Isolation:** Mess with the seeder, and you might find a bunch of your tests falling apart. It's like a domino effect; one goes down, and they all might.
- **Implicit Reset:** The RefreshDatabase trait ensures each test begins afresh, which is great, but might not be immediately obvious to someone new to the code.


To sum up, combining seeders with Pest in Laravel is quite handy for managing your test data, but it does introduce some readability considerations. Make sure to keep your seeders well-documented and perhaps sprinkle some comments in your tests to make life easier for the next developer who looks at your code.