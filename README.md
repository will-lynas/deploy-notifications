# deploy-notifications

GitHub Action for sending a Telegram notification after a successful deploy

## Example Usage

```yml
on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - uses: will-lynas/deploy-notifications@main
        with:
          to: ${{ secrets.TELEGRAM_TO }}
          token: ${{ secrets.TELEGRAM_TOKEN }}
```
