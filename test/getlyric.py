import requests
from bs4 import BeautifulSoup

def get_lyrics_from_google(song_name):
    # 构建Google搜索URL
    search_query = f"{song_name} 歌词"
    google_url = f"https://www.google.com/search?q={search_query}"

    # 发送HTTP请求并获取响应
    response = requests.get(google_url)

    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找包含歌词的元素，这里假设歌词在class为"lyrics"的元素下
        lyrics_element = soup.find('div', class_='fsZ')

        if lyrics_element:
            # 提取歌词文本
            lyrics_text = lyrics_element.get_text('\n', strip=True)
            return lyrics_text
        else:
            return "未找到歌词"
    else:
        return "请求失败"

# 示例用法
song_name = "宝贵十架"
lyrics = get_lyrics_from_google(song_name)
print(lyrics)
