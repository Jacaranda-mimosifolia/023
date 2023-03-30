import requests  # 第三方模块 类库   请求  7种方法  get  post
import parsel  # 第三方模块 解析  css xpath re
import os  # 内置  文件

filename = '图片\\'
if not os.path.exists(filename):  # 判断 如果没有这个文件夹
    os.mkdir(filename)  # 新建这么一个文件

for page in range(1, 31):  # 左闭右开的一个区间1可以取到 31是取不到
    print(f'===========================正在下载第{page}页图片===========================')
    filename_page = f'图片\\{page}\\'
    if not os.path.exists(filename_page):  # 判断 如果没有这个文件夹
        os.mkdir(filename_page)
    if page == 1:
        url = 'https://www.kanxiaojiejie.com/'
    else:
        url = f'https://www.kanxiaojiejie.com/page/{page}'
    # 伪装
    headers = {
        # 浏览器的身份标识
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    # .text 获取网页源码（文本信息）
    # print(response.text)
    # <Response [200]>    200  对象
    selector = parsel.Selector(response.text)
    # print(selector)
    # :: 属性提取器
    # attr(src) 表示取标签下的属性
    # .getall() 列表  遍历  索引  切片
    img_urls = selector.css('.entry-top img::attr(src)').getall()
    # print(img_urls)
    # print(len(img_urls))
    for index, img_url in enumerate(img_urls):
        # print(img_url)
        # .content 获取二进制数据
        img_content = requests.get(url=img_url, headers=headers).content
        with open(filename_page + f'{index + 1}' + '.jpg', mode='wb') as f:  # as 取小名
            f.write(img_content)

            print(f'正在下载第{index + 1}张图片')
