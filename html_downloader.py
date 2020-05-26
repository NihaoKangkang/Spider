from urllib import request


class HtmlDownloader():
    def download(self, url):
        if url is None:
            return None

        ret = request.Request(url)
        response = request.urlopen(ret)

        #if response.getcode != 200:
        #    print('空相因')
        #    return None

        return response.read()