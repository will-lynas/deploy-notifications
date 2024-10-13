# deploy-notifications

GitHub Action for sending a Telegram notification after a successful deploy

## Example Usage

```yml
on:
  push:
    branches:
      - main

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - uses: will-lynas/deploy-notifications@v0.1.0
        with:
          to: ${{ secrets.TELEGRAM_TO }}
          token: ${{ secrets.TELEGRAM_TOKEN }}
```

> [!IMPORTANT]
> Only works with a push event

## Example Output

```
✨ will-lynas/deploy-notifications-test
🎉 Deploy Successful

🥷 will-lynas
💬 Dummy commit 1

🥷 will-lynas
💬 Dummy commit 2
```
