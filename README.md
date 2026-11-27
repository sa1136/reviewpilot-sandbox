# reviewpilot-sandbox

Test bed for [ReviewPilot](https://github.com/sa1136/reviewpilot). PRs against this repo carry
planted bugs so we can check what the reviewer catches.

`cart.py` on `main` is the clean baseline. Each test PR branches from it and plants bugs.

## shop/

A Django storefront API lives in `shop/`. Production notes: `docs/database.md`.
