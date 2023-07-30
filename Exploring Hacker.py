import requests
from tabulate import tabulate

def fetch_hacker_news_top_posts():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url)
    if response.status_code == 200:
        top_post_ids = response.json()[:10]  # Fetching the top 10 post IDs
        return top_post_ids
    else:
        print("Failed to fetch Hacker News top posts.")
        return []

def fetch_hacker_news_post_details(post_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        post_data = response.json()
        title = post_data.get("title", "N/A")
        url = post_data.get("url", "N/A")
        score = post_data.get("score", 0)
        num_comments = post_data.get("descendants", 0)
        return [title, url, score, num_comments]
    else:
        return ["N/A", "N/A", 0, 0]

def main():
    print("Exploring Hacker News Top Posts")
    top_post_ids = fetch_hacker_news_top_posts()

    if not top_post_ids:
        print("No data to display.")
        return

    table_data = []
    for post_id in top_post_ids:
        post_details = fetch_hacker_news_post_details(post_id)
        table_data.append(post_details)

    headers = ["Title", "URL", "Score", "Comments"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
