import pymongo


conn = pymongo.MongoClient('localhost', 27017)
db = conn["information"]
cursor = db["news"]
my_new = cursor.find({"newsType":"news"}).sort([("create_time", -1)]).limit(10)

def newsText(source_url, newsType):
    data = cursor.find({"source_url":source_url, "newsType":newsType}).sort([("create_time", -1)])
    number = data.count()
    return (data, number)


if __name__ == '__main__':
    for i in my_new:
        print(i)