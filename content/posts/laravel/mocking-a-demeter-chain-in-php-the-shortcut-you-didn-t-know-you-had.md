+++
date = '2024-12-08T21:39:10Z'
draft = false
title = "Mocking a Demeter Chain in PHP the Shortcut You Didn't Know You Had"
image = "/images/mocking-demeter-chain.webp"
tags = ["Laravel", "Testing", "Mocking", "PHP"]
categories = ["Programming", "Laravel"]
+++

Ever tried to mock a Demeter chain in PHP? It's like trying to thread a needle with a rope. Let’s break it down with an example using Laravel.

## Example of a Demeter Chain
Imagine you're working with Laravel, and you have this glorious chain:

```php
$order = Order::find($id);
$status = $order->payment->transaction->status;
```
Here, we're grabbing an Order, navigating through its payment, then through its transaction, to get the status.

Now you want to test something, and this chain decides to make your life miserable:

1. Too Many Mocks: For this to work, you need mocks for:
  - The Order object.
  - The Payment object.
  - The Transaction object.

2. Brittle Tests: Any change in the chain structure can break your test, even if the logic remains valid.

```php
$orderMock = Mockery::mock(Order::class);
$paymentMock = Mockery::mock(Payment::class);
$transactionMock = Mockery::mock(Transaction::class);

$orderMock->shouldReceive('getAttribute')->with('payment')->andReturn($paymentMock);
$paymentMock->shouldReceive('getAttribute')->with('transaction')->andReturn($transactionMock);
$transactionMock->shouldReceive('getAttribute')->with('status')->andReturn('paid');

Order::shouldReceive('find')->with($id)->andReturn($orderMock);
```
By the time you’re done, you’ve mocked half the universe for a single test.🤦‍♂️

### Mocking It Like a Pro
Here’s the trick: you can mock the entire chain in one go.

```php
$orderMock = Mockery::mock(Order::class);
$orderMock->shouldReceive('payment->transaction->status')->andReturn('paid');

Order::shouldReceive('find')->with($id)->andReturn($orderMock);
```

Boom! You just mocked the whole chain without creating a separate mock for Payment or Transaction. Clean and concise.

### Why This Works
Mockery’s ability to interpret chains (->) makes it easy to handle this. No need to mock intermediate objects i.e Payment and Transaction ,you only care about the final result of the chain. 

## Final Thoughts
### When to Use This
- Quick Tests: Perfect for when you need to verify outcomes and don’t care about the internals.
- Focused Testing: Keeps your test simple and avoids diving into unnecessary layers of detail.

### The Catch
This approach ties your test directly to the chain structure. If the chain changes (e.g., transaction becomes txn), your test will fail, even if the logic is still valid. To future-proof your test, always ask yourself:
Do I care about the chain itself, or just the outcome?