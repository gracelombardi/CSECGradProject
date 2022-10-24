import facebook
import requests

token = ''
# graph = facebook.GraphAPI(token)
# page_ids = []
# myID = graph.request('/me?fields=id')
# posts = graph.get_object(id=myID['id'], fields='posts.fields(object_id)')
# post_ids = []
# for post in posts:
#     post_ids.append(posts[post])
# print(post_ids)
# i = 0
# while i < len(post_ids):
#     likes = graph.get_object(id=post_ids[i], fields='likes')
#     i += 1
#     print(likes)
#
# likes = graph.put_like(object_id=str(post_ids[0]))
# print(likes)
post_id = 'pfbid0P98Kwjim73RgLy5auWg5UqtEZm8WDV4tNW2CeKJUXUfkrNh29dPi7ZP6iET1MAuMl'

endpoint = 'https://graph.facebook.com/v2.5/' + post_id + '/comments?summary=true&access_token' \
                                                     '=' + token
response = requests.get(endpoint)
fb_data = response.json()
print(fb_data)
