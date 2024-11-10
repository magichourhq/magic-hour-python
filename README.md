# Magic Hour API Python SDK

## Overview

# Introduction

Magic Hour provides an API (beta) that can be integrated into your own application to generate videos using AI.

If you have any questions, please reach out to us via [discord](https://discord.gg/JX5rgsZaJp).

# Authentication

Every request requires an API key.

To get started, first generate your API key [here](http://localhost:3000/settings/developer).

Then, add the `Authorization` header to the request.

| Key           | Value                  |
| ------------- | ---------------------- |
| Authorization | Bearer mhk_live_apikey |

> **Warning**: any API call that renders a video will utilize frames in your account.

### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
```

### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
```

### SDK Usage

See [SDK Examples](SDK_EXAMPLES.md) for example usage of all SDK functionality
