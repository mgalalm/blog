+++
date = '2024-12-22T20:49:29Z'
draft = false
title = 'Demystifying Laravel Jetstream'
image = '/images/jetstream-arch.jpg'
tags = ['Laravel', 'Jetstream']
+++

Laravel Jetstream is a polished UI scaffolding package for Laravel applications. It provides developers with a refined starting point for building user interfaces, offering pre-built components and workflows for common features like authentication, profile management, and two-factor authentication. <!--more-->

Jetstream’s real power lies in its seamless integration with other Laravel features, enabling developers to focus on crafting unique application logic while leveraging robust, pre-configured workflows.

### What's JetStream and what it's actually doing?

Jetstream acts as the user interface (UI) layer, focusing on front-end interactions and workflows. This separation of concerns allows developers to customize the front-end experience without worrying about the complexities of back-end implementation.

Jetstream supports two primary stacks:

1. Livewire: For developers who prefer server-rendered pages with minimal JavaScript.

2. Vue with Inertia.js: For those who want a modern single-page application experience.

For instance, when a user updates their profile, Jetstream captures the input and routes it to the back end for processing. The actions executed depend on how Fortify has been configured in your application.

### Installing Jetstream
Jetstream is designed for fresh Laravel projects. To integrate Jetstream, follow these steps

1. Set Up a New Laravel Application

```sh
composer create-project laravel/laravel example-app
cd example-app
```

 Install Jetstream Package

 ```sh
 composer require laravel/jetstream

 ```
 Install Jetstream  
```sh
 php artisan jetstream:installjetstream:install
```

 This will ask you to choose between Livewire and Vue with Inertia.js. Select the stack you prefer.

3. publish Jetstream's assets

```sh
@php artisan vendor:publish --tag=laravel-assets --ansi --force
```
That's how jetstream look like when you go to the registration page of your application.

![Jetstream](/images/jetstream.png)

### Jestream and Fortify Actions 

As we touched JetStream is pretty much just a UI layer and fortify is the workhorse that's actually computing and working out how to update profile information, how to enable or disable two-factor authentication, how to manage browser sessions etc. 

When we install Jetstream, it comes with one action class which is DeleteUser, The DeleteUser action handles the removal of user accounts. By default, it:

- Deletes the user’s profile photo.

- Revokes all API tokens.
 Removes the user record from the database.

Here’s the default implementation:

```php
class DeleteUser implements DeletesUsers
{
    /**
     * Delete the given user.
     */
    public function delete(User $user): void
    {
        $user->deleteProfilePhoto();
        $user->tokens->each->delete();
        $user->delete();
    }
}
```

You can extend this logic to include additional cleanup tasks, such as logging the deletion or notifying team members. 

Also when you install Jetsream, it install also fortify, which comes with the rest of the actions like UpdateUserProfileInformation, UpdateUserPassword, TwoFactorAuthentication etc.

```sh
└── app
    ├── Actions
    │   └── Fortify
    │       ├── CreateNewUser.php
    │       ├── PasswordValidationRules.php
    │       ├── ResetUserPassword.php
    │       ├── UpdateUserPassword.php
    │       └── UpdateUserProfileInformation.php

```



### Conclusion

Jetstream is a powerful tool for Laravel developers, providing a solid foundation for building user interfaces. By integrating Jetstream into your Laravel application, you can leverage pre-built components and workflows to streamline development and focus on crafting unique application logic. Jetstream’s seamless integration with other Laravel features makes it an excellent choice for developers looking to build robust, user-friendly applications.
