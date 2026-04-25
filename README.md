# Influencer Radar

A command-line tool that searches for TikTok influencers by hashtag and filters them by follower count. Built with Python and powered by the Apify API.

## Features

- Search TikTok influencers by any hashtag (e.g. `筋トレ`, `プロテイン`, `fitness`)
- Filter by minimum and maximum follower count
- Automatically removes accounts that haven't posted in the last 6 months
- Removes duplicate accounts
- Displays a clickable TikTok profile link for each influencer
- Results sorted by follower count (highest first)

## Requirements

- Python 3.8+
- [Apify](https://apify.com) account (free tier includes $5 credit)

## Setup

1. Clone this repository:
```
git clone https://github.com/XHQI01/influencer-radar.git
cd influencer-radar
```

2. Install dependencies:
```
pip install apify-client python-dotenv
```

3. Create a `.env` file in the root folder:
```
APIFY_API_TOKEN=your_apify_token_here
```
You can find your API token at: Apify Dashboard → Settings → Integrations

## Usage

```
python influencer_radar.py
```

You will be prompted to enter:
- Hashtag to search (e.g. `筋トレ`)
- Minimum follower count (e.g. `4000`)
- Maximum follower count (e.g. `50000`)

## Example Output

```
找到 12 个网红：

Username                  Link                                          Followers
---------------------------------------------------------------------------
@proteinking              https://www.tiktok.com/@proteinking           45000
@fitnessdaily             https://www.tiktok.com/@fitnessdaily          28000
@gymlife2024              https://www.tiktok.com/@gymlife2024           9500
```

## Notes

- Never commit your `.env` file — it is already listed in `.gitignore`
- The Apify free credit ($5) is enough to run hundreds of searches
