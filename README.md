


# 🧪 XO Drops

A creative scaffold and drop deployment system for the XO ecosystem. This repository hosts Pulse Drops, NFT metadata, vault-integrated teasers, and self-contained digital + physical bundles.

---

## 📁 Folder Structure

```
drops/
├── brie_scroll/         # Personalized teaser bundle
├── eighth_seal/         # Upcoming seal character drop
├── ...
scripts/
├── drop_generate.py     # Generator for new drop bundles
wrangler.toml            # Cloudflare Pages config
drops.json               # Drop manifest config (see below)
```

---

## 🚀 Deploy Guide

### Cloudflare Pages

**Build Command:**
```
cp -r drops dist
```

**Output Directory:**
```
dist
```

**Custom Domains:**
Can be connected via `pages.dev` or DNS routing for `xo-drops.xo` subdomains.

---

## 🎯 Drop Manifest Example

```json
{
  "title": "Brie Scroll",
  "slug": "brie_scroll",
  "cover": "vault_extras/brie_scroll_variant_1.png",
  "description": "Scroll drop with QR intro, XO avatar, and XO Light Client app.",
  "linked": true
}
```

---

## 🛠️ Wrangler Config

```toml
name = "xo-drops"
type = "javascript"
account_id = "your_account_id"
compatibility_date = "2025-07-01"
site.bucket = "./dist"
site.entry-point = "."
```

---

## ✅ Status

[![Deploy](https://img.shields.io/github/actions/workflow/status/xo-verses/xo-drops/deploy.yml)](https://github.com/xo-verses/xo-drops/actions)
[![XO Pages](https://img.shields.io/badge/pages-live-green)](https://xo-drops.pages.dev)