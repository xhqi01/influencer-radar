# 网红雷达

一个命令行工具，通过标签搜索TikTok网红，并按粉丝数量筛选。基于Python和Apify API构建。

## 功能

- 通过任意标签搜索TikTok网红（例如：`筋トレ`、`プロテイン`、`fitness`）
- 按最少和最多粉丝数筛选
- 自动过滤半年内没有发帖的账号
- 自动去除重复账号
- 显示每个网红的可点击TikTok主页链接
- 结果按粉丝数从高到低排列

## 环境要求

- Python 3.8+
- [Apify](https://apify.com) 账号（免费注册送$5额度）

## 安装步骤

1. 克隆项目：
```
git clone https://github.com/XHQI01/influencer-radar.git
cd influencer-radar
```

2. 安装依赖：
```
pip install apify-client python-dotenv
```

3. 在根目录新建 `.env` 文件：
```
APIFY_API_TOKEN=填入你的Apify Token
```
Token位置：Apify后台 → Settings → Integrations

## 使用方法

```
python influencer_radar.py
```

运行后会依次询问：
- 搜索标签（例如：`筋トレ`）
- 最少粉丝数（例如：`4000`）
- 最多粉丝数（例如：`50000`）

## 输出示例

```
找到 12 个网红：

用户名                    链接                                            粉丝数
---------------------------------------------------------------------------
@proteinking              https://www.tiktok.com/@proteinking           45000
@fitnessdaily             https://www.tiktok.com/@fitnessdaily          28000
@gymlife2024              https://www.tiktok.com/@gymlife2024           9500
```

## 注意事项

- 不要上传 `.env` 文件，它已经被添加到 `.gitignore`
- Apify免费额度（$5）足够运行几百次搜索
