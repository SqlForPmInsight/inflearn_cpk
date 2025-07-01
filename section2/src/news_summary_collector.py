import requests
import feedparser
from bs4 import BeautifulSoup
import openai

# OpenAI API 키 입력 (환경변수 등으로 관리 권장) --> .env 파일을 사용해서 관리 
openai.api_key = "YOUR_KEY" # 여기에 api 키를 넣어주세요 

# 1. RSS 피드 수집
def fetch_rss_items(rss_url):
    feed = feedparser.parse(rss_url)
    items = []
    for entry in feed.entries:
        items.append({
            'title': entry.title,
            'link': entry.link,
            'description': entry.get('description', ''),
            'pubDate': entry.published
        })
    return items

def merge_title_description(items):
    merged_texts = []
    for item in items:
        merged = f"title: {item['title']}\ndescription: {item['description']}"
        merged_texts.append(merged)
    return "\n\n".join(merged_texts)

def summarize_top5_issues(text):
    prompt = f"아래 뉴스 기사들을 5개의 주요 이슈로 요약해줘:\n{text}"
    client = openai.OpenAI(api_key=openai.api_key)
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        temperature=0.5
    )
    summary = response.choices[0].message.content.strip()
    return summary

# 4. 전체 파이프라인
def main():
    rss_url = 'https://www.mk.co.kr/rss/50300009/'
    items = fetch_rss_items(rss_url)
    merged_text = merge_title_description(items)
    summary = summarize_top5_issues(merged_text)
    print(summary)

    with open('section2/src/summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)

if __name__ == '__main__':
    main() 