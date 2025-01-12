+++
date = '2024-12-23T20:03:24Z'
draft = false
title = 'How to Enable Profile Photos in Jetstream'
tags = ['Laravel', 'Jetstream']
image = '/images/jetstream-profilephoto.jpg'

+++
Avatar is a great way to personalize your application! They make user profiles more engaging and ensure everyone has a recognizable avatar when creating or commenting on posts. If you’re using Jetstream and want to enable custom profile photos, here’s a simple guide to get you started. <!--more-->

### Update the Configuration File

Jetstream comes with a configuration file where you can enable or disable certain features. To enable profile photos:

Open the jetstream.php configuration file in your project’s config folder.

Look for the features section. It should look something like this:

```php
'features' => [
    // Features::termsAndPrivacyPolicy(),
    Features::profilePhotos(),
    // Features::api(),
    // Features::teams(['invitations' => true]),
    Features::accountDeletion(),
],
```

Ensure that the `Features::profilePhotos()` line is uncommented. This line enables the profile photo feature in Jetstream.

Once you’ve updated the configuration:

Refresh your profile page in the browser.

You should see a new field to upload a profile photo.

### Troubleshooting Common Issues

If you don’t see the profile photo field or encounter a 404 error or broken images, here are two common problems and how to fix them:

1. **Storage Link**: Make sure you have created a symbolic link from `public/storage` to `storage/app/public`. You can do this by running:

```bash
php artisan storage:link
```

2. **Incorrect APP_URL in .env**: Ensure that the `APP_URL` in your `.env` file is correctly set to your application’s URL. This is crucial for loading images and assets correctly. If your application is accessible via a custom domain (e.g., http://app.test) but the APP_URL in your .env file is set to http://localhost, the profile photos might not load correctly.



### Customizing Profile Photo Validation

Now we have enabled the profile photo feature in Jetstream, but we might want to customize the validation rules for the uploaded photos for example, we might want to restrict the file types or sizes.

To customize the validation rules for profile photos, you can modify the `UpdateProfileInformation` action class under `App\Actions\Fortify` directory. In this class, you can find the `update` method where the profile photo is validated. 
 
```php 
'photo' => ['nullable', 'mimes:jpg,jpeg,png', 'max:1024'],
```

### Wrapping Up!
That’s it! With these simple steps, you’ve enabled profile photos in Jetstream. Whether you’re building a blog, a social network, or any other type of app, this feature will make your users’ profiles more vibrant and engaging. Enjoy!
