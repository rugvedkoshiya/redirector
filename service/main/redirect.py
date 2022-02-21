from urllib import parse

def redirectToLink(requestObj):
    print(requestObj.get("link"))
    print(parse.quote(requestObj.get("link"), safe=''))
    return requestObj.get("link")