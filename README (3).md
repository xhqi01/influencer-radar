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

---

# Influencer Radar（日本語）

ハッシュタグでTikTokインフルエンサーを検索し、フォロワー数で絞り込むツールです。ブラウザで使えるWebインターフェースとコマンドラインツールの両方に対応しています。

## Webインターフェース

`index.html` をブラウザで開くだけで使えます。インストール不要です。Apifyトークン、ハッシュタグ、フォロワー数の範囲を入力して「Search」をクリックするだけ。

GitHubPagesを有効にすれば、オンラインでも使えます（`Settings → Pages → Source: main`）。

## 機能

- 任意のハッシュタグでTikTokインフルエンサーを検索（例：`筋トレ`、`プロテイン`、`fitness`）
- フォロワー数の下限・上限で絞り込み
- 過去6ヶ月以内に投稿していないアカウントを自動除外
- 重複アカウントを自動排除
- フォロワー数の多い順に表示

## CLIの使い方

Python 3.8以上と[Apify](https://apify.com)アカウントが必要です（無料枠に$5クレジット付き）。

```bash
git clone https://github.com/xhqi01/influencer-radar.git
cd influencer-radar
pip install apify-client python-dotenv
```

`.env` ファイルを作成：

```
APIFY_API_TOKEN=your_apify_token_here
```

実行：

```bash
python influencer_radar.py
```

ハッシュタグとフォロワー数の範囲を入力するよう求められます。

## 注意事項

- `.env` ファイルは絶対にコミットしないでください（`.gitignore` に設定済み）
- Apifyの無料クレジット（$5）で数百回の検索が可能です
- WebインターフェースはAPIトークンを保存・送信しません
