import re
import time


def combination(news):
    # 进行html文本的组合
    coll = "collapse" + str(news["source_id"])
    head = '<div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"><a data-toggle="collapse" data-parent="#accordion" href="#' + coll + '">'
    bodyOne = '</a></h4></div><div id="' + coll + '" class="panel-collapse collapse"><div class="panel-body"><div><span>'
    bodyTwo = '</span> <span>'
    bodyThree = '</span></div>'
    bodyFour = '</div></div></div>'
    if type(news["title"]) == list:
        title = news["title"][0]
    else:
        title = news["title"]
    if type(news["format_text"]) == list:
        format_text = news["format_text"][0]
        if type(format_text) == list:
            format_text = format_text[0]
    else:
        format_text = news["format_text"]
    # 不需要块级div元素，可能运用一个框架进行修饰
    pattern = re.compile('<div[\s\S]*?>')
    format_text = re.sub(pattern, "", format_text)
    pattern = re.compile('</div>')
    format_text = re.sub(pattern, "", format_text)
    htmlString = head + title + bodyOne + news["release_time"] + bodyTwo + " " + news["author"] + bodyThree + format_text + bodyFour
    # 有个别网站需要改变
    if news["source_url"] == "com.51huolian.www":
        pattern = re.compile('src="//')
        htmlString = re.sub(pattern, 'src="http://', htmlString)
    if news["source_url"] == "net.zaoping.www":
        pattern = re.compile('src="http://zaoping.net')
        htmlString = re.sub(pattern, 'src="http://www.zaoping.net', htmlString)
    if news["source_url"] == "com.budkr.www":
        pattern = re.compile('<img[\s\S]*?ueditor/php/upload/image/20180621/1529557743802953.png[\s\S]*?>')
        htmlString = re.sub(pattern, " ", htmlString)
    # 更正图片的地址
    source_url = news["source_url"]
    source_url = source_url.split(".")
    if len(source_url) == 2:
        source_name = source_url[1] + "." + source_url[0]
    else:
        source_name = source_url[2] + "." + source_url[1] + "." + source_url[0]
    src = 'src="http://' + source_name + "/"
    pattern = re.compile('src="/')
    htmlString = re.sub(pattern, src, htmlString)
    pattern = re.compile('src="http')
    exist = re.findall(pattern, htmlString)
    if not exist:
        pattern = re.compile('src="/')
        exist = re.findall(pattern, htmlString)
        if not exist:
            pattern = re.compile('src="')
            htmlString = re.sub(pattern, src, htmlString)
    # 将不需要的标签去除
    pattern = re.compile(' width="[\s\S]*?" height="[\s\S]*?" ')
    htmlString = re.sub(pattern, " ", htmlString)
    pattern = re.compile('<script>[\s\S]*?</script>')
    htmlString = re.sub(pattern, " ", htmlString)
    pattern = re.compile('<link[\s\S]*?>')
    htmlString = re.sub(pattern, " ", htmlString)
    return htmlString


def to_obtain(source, data):
    if len(source) == 1:
        return data
    else:
        allText = []
        number = (int(source[1]) - 1) * 10
        for i in data:
            allText.append(i)
        return allText[number:]


def combination_alerts(alerts):
    head = '<li class="clearfix"><div class="pull-left" style="width: 20%;"><p style="margin-top: 10px;" class="text-center">'
    bodyOne = '</p></div><div class="pull-left" style="width: 80%;"><h4>'
    bodyTwo = ' </h4><p>'
    end = '</p></div></li>'
    timeout = alerts["create_time"]
    date = time.localtime(timeout/1000)
    text= alerts["main"]
    if type(text) == list:
        main = ""
        for i in text:
            main += i + " "
    else:
        main = text
    if type(alerts["title"]) == list:
        title = alerts["title"][0]
    else:
        title = alerts["title"]
    htmlString = head + str(date.tm_hour) + ":" + str(date.tm_min) + bodyOne + title + bodyTwo + main + end
    source_url = alerts["source_url"]
    source_url = source_url.split(".")
    if len(source_url) == 2:
        source_name = source_url[1] + "." + source_url[0]
    else:
        source_name = source_url[2] + "." + source_url[1] + "." + source_url[0]
    src = 'src="http://' + source_name + "/"
    pattern = re.compile('src="http')
    exist = re.findall(pattern, htmlString)
    if exist:
        pass
    else:
        pattern = re.compile('src="/')
        exist = re.findall(pattern, htmlString)
        if exist:
            htmlString = re.sub(pattern, src, htmlString)
        else:
            pattern = re.compile('src="')
            htmlString = re.sub(pattern, src, htmlString)
    return htmlString


def notExist():
    htmlString = '<li><div class="text-center" style="font-size: 20px;color: #FFD306;">快讯信息未建立</div></li>'
    return htmlString


def initialize_the(source_url, data):
    more_the = int(data / 10)
    complementation = data % 10
    if complementation != 0:
        more_the = more_the + 1
    ulStart = '<ul class="pagination">'
    li1 = '<li> <button class="btn btn-info" onclick="pages(this)" value="' + source_url[0] + " " + "1" + " " + str(more_the) + '" id = "home-page"> 首页 </button> </li> '
    li2 = '<li> <button class="btn btn-info" onclick="pages(this)" value="" id="top-page"> 上一页 </button> </li> '
    n_page = 1
    li3 = ""
    while n_page < more_the and n_page < 4:
        li3 += '<li> <button class="btn btn-info" onclick="pages(this)" value=""> ' + str(n_page) + ' </button> </li>'
        n_page += 1
    if more_the > 3:
        li3 += '<li> <button class="btn btn-info" value=""> ... </button> </li>'
    li4 = '<li> <button class="btn btn-info" onclick="pages(this)" value="" id="bottom-page"> 下一页 </button> </li>'
    li5 = '<li> <button class="btn btn-info" onclick="pages(this)" value=""> 尾页 </button> </li>'
    ulEnd = '</ul>'
    htmlString = ulStart + li1 + li2 + li3 + li4 + li5 + ulEnd
    return htmlString


def number_page(page, source_url):
    maxNumber = int(source_url[2])
    number = int(source_url[1])
    if page == "上一页" and number != 1:
        number -= 1
    elif page == "下一页" and number != maxNumber:
        number += 1
    elif page == "尾页" or page == "下一页" and number == maxNumber:
        number = maxNumber
    elif page == "首页" or page == "上一页" and number == 1:
        number = 1
    else:
        number = int(page)
    ulStart = '<ul class="pagination">'
    li1 = '<li> <button class="btn btn-info" onclick="pages(this)" value="' + source_url[0] + " " + str(number) + " " + source_url[2] + '" id="home-page"> 首页 </button> </li> '
    li2 = '<li> <button class="btn btn-info" onclick="pages(this)" value="" id="top-page"> 上一页 </button> </li> '
    li3 = ""
    n_page = number
    if n_page > 1:
        li3 += '<li> <button class="btn btn-info" value=""> ... </button> </li>'
    while n_page < number + 3 and n_page <= maxNumber:
        li3 += '<li> <button class="btn btn-info" onclick="pages(this)" value="" > ' + str(n_page) + ' </button> </li>'
        n_page += 1
    if n_page < maxNumber:
        li3 += '<li> <button class="btn btn-info" value=""> ... </button> </li>'
    li4 = '<li> <button class="btn btn-info" onclick="pages(this)" value="" id = "bottom-page"> 下一页 </button> </li>'
    li5 = '<li> <button class="btn btn-info" onclick="pages(this)" value=""> 尾页 </button> </li>'
    ulEnd = '</ul>'
    htmlString = ulStart + li1 + li2 + li3 + li4 + li5 + ulEnd
    return htmlString
