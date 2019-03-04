#4339355365370915
# token 是刚刚获得的 token，可以一直使用

from weibopy import  WeiboClient
import webbrowser

# suffix 指定 API 的名称，parmas 是参数，在文档中有详细描述
result = client.get(suffix='comments/show.json', params={'id': 4339355365370915, 'count': 200, 'page': 1})

print(result)
