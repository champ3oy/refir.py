# Refir - Grow your user-base with referrals

Refir is a Python library that simplifies the management of referral programs for startups. With Refir, you can easily integrate referral functionality into your application, allowing you to track referrals, assign referral codes, and more.

## Prerequisites

Before you can start using Refir, you'll need to complete the following steps:

1. **Sign Up at Our Website**: To access the Refir API and obtain an API key, you must first sign up at our website [refir](https://refir.xyz). Once you've signed up, you'll be able to log in to your dashboard to manage your referral program, track users, and access insights and reports.

2. **Obtain Your API Key**: After signing up and logging in to your dashboard, you'll find your unique API key in the campaign settings or API section of your dashboard. This API key is required to configure Refir and make API requests.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Adding a User](#adding-a-user)
  - [Getting a User by ID](#getting-a-user-by-id)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with Refir, you can install it using pip:

```bash
pip install my-python-package
```

## Configuration

Before using Refir, you need to configure it with your API key. You can do this as follows:

```python
from refir import Refir

refir = Refir()
refir.configure({"api_key": "your-api-key"})
```

## Usage

### Adding a User

You can use Refir to add a user to your referral program. The following example demonstrates how to do this:

```python
const user = {
user = {
  "userId": "unique-user-id",
  "name": "John Doe",
  "email": "johndoe@example.com",
}

success = refir.add_user(user)

if success:
  print("User added successfully.")
else:
  print("Failed to add user.")

```

### Getting a User by ID

You can retrieve a user's referral code by their unique ID using Refir. Here's an example of how to do it:

```python
user_id = "unique-user-id"

referral_code = refir.get_user_by_id(user_id)

if referral_code:
  print(f"User's referral code: {referral_code}")
else:
  print("Failed to get user referral code.")

```

## Error Handling

Refir provides basic error handling for API requests. If an error occurs during an API request, an error message will be logged to the console, and the function will return `false`. You can customize error handling to suit your application's needs.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to contribute to the development of Refir, please check out our [contribution guidelines](CONTRIBUTING.md).

## License

Refir is licensed under the [MIT License](LICENSE).
