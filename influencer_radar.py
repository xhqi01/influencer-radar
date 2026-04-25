import os
from datetime import datetime
from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

hashtag = input("搜索什么标签？（例如：筋トレ、プロテイン）：")
min_followers = int(input("最少粉丝数："))
max_followers = int(input("最多粉丝数："))

print("\n正在搜索，请稍等...\n")

run = client.actor("clockworks/tiktok-hashtag-scraper").call(
    run_input={
        "hashtags": [hashtag],
        "resultsPerPage": 50,
    }
)

seen = {}

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    author = item.get("authorMeta", {})
    username = author.get("name", "")
    followers = author.get("fans", 0)
    create_time = item.get("createTime", 0)

    if not username or not (min_followers <= followers <= max_followers):
        continue

    if username not in seen or create_time > seen[username]["create_time"]:
        seen[username] = {
            "followers": followers,
            "create_time": create_time,
        }

def hyperlink(url, text):
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

results = []
for username, data in seen.items():
    url = f"https://www.tiktok.com/@{username}"
    last_post = datetime.fromtimestamp(data["create_time"]).strftime("%Y-%m-%d") if data["create_time"] else "未知"
    results.append({
        "username": username,
        "url": url,
        "followers": data["followers"],
        "last_post": last_post,
    })

six_months_ago = datetime.now().timestamp() - (180 * 24 * 60 * 60)
results = [r for r in results if seen[r["username"]]["create_time"] >= six_months_ago]

results.sort(key=lambda x: x["followers"], reverse=True)

print(f"找到 {len(results)} 个网红：\n")
print(f"{'用户名':<25} {'链接':<45} {'粉丝数'}")
print("-" * 75)
for r in results:
    link = hyperlink(r["url"], r["url"])
    padding = " " * max(0, 45 - len(r["url"]))
    print(f"@{r['username']:<24} {link}{padding} {r['followers']}")
