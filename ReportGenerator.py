

# 正式用的List
#PageInformation = [ 
#    page01{ 'title':'梯廳壁磚','案別':'七賢A案','期別':'第十二期','項目':'梯廳壁磚','位置':'19F 20F','photo01':'test.jpg' } ,
#    page02{ 'title':'室內地磚','案別':'七賢A案','期別':'第十二期','項目':'室內地磚','位置':'5F 6F 7F','photo01':'test.jpg' } ,
#    page03{ 'title':'樓梯地磚','案別':'七賢A案','期別':'第十二期','項目':'室內地磚','位置':'3F 9F 11F 15F','photo01':'test.jpg' }   
#    ]

# 測試用的List
PageInformation = [
    page01{ 'title':'梯廳壁磚', 'photo':'test.jpg' }
    page02{ 'title':'梯廳壁磚', 'photo':'testVertical.jpg'}
]

class HtmlReport:

    def __init__(self):
        pass

    def getOutputPath(self):
        pass

    def makePage(self,pageInfo):
        
        for page in PageInfo:
            pageData = {}
            pageData = page
            Title = pageData['title']
            Image = pageData['photo']
        
# -------------------------

test = HtmlReport()
test.makePage(PageInformation)
