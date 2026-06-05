# Influencer Radar

A tool that searches for TikTok influencers by hashtag and filters them by follower count. Available as both a web interface and a command-line tool.

## Web Interface

Open `index.html` in any browser — no installation required. Enter your Apify token, hashtag, and follower range, then click Search.

To use it online, enable GitHub Pages in the repo settings (`Settings → Pages → Source: main`).

## Features

- Search TikTok influencers by any hashtag (e.g. `筋トレ`, `プロテイン`, `fitness`)
- Filter by minimum and maximum follower count
- Automatically removes accounts that haven't posted in the last 6 months
- Removes duplicate accounts
- Results sorted by follower count (highest first)

## CLI Usage

Requires Python 3.8+ and an [Apify](https://apify.com) account (free tier includes $5 credit).

```bash
git clone https://github.com/xhqi01/influencer-radar.git
cd influencer-radar
pip install apify-client python-dotenv
```

Create a `.env` file:

```
APIFY_API_TOKEN=your_apify_token_here
```

Run:

```bash
python influencer_radar.py
```

You will be prompted to enter a hashtag and follower count range.

## Notes

- Never commit your `.env` file — it is already listed in `.gitignore`
- The Apify free credit ($5) is enough to run hundreds of searches
- Your API token is never stored by the web interface
