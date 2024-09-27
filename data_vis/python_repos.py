import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status Code:", r.status_code)
# 将API响应存储在一个变量中
dic=r.json()
print("Total repositories:", dic['total_count'])
# 研究有关仓库的信息
repo_dics=dic['items']
print("Number of repositories:", len(repo_dics))
names,plot_dics=[],[]
for repo in repo_dics:
    names.append(repo['name'])
    plot_dic={'value':repo['stargazers_count'],
              'label':repo['description'],
              'xlink':repo['html_url']}
    plot_dics.append(plot_dic)
my_style=LS("#333366",base_style=LCS)
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000
chart=pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels=names
chart.add('',plot_dics)
chart.render_to_file('python_repos.svg')
