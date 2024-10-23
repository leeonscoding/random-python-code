import requests
import json

def get_example():
    request_url = 'https://jsonplaceholder.typicode.com/posts'

    posts = requests.get(request_url).json()

    print(f'total posts: {len(posts)}')

    for post in posts:
        print(post['title'])


def post_example():
    request_url = 'https://jsonplaceholder.typicode.com/posts'

    post = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1,
    }

    response = requests.post(request_url, json=post)

    print(response.text)

post_example()
get_example()