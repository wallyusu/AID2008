import re

html = """
<div class="movie-item-info">
        <p class="name"><a href="/films/1339160" title="金刚川" data-act="boarditem-click" data-val="{movieId:1339160}">金刚川</a></p>
        <p class="star">
                主演：张译,吴京,李九霄
        </p>
<p class="releasetime">上映时间：2020-10-23</p>
    </div>
"""

# a = '<div class="movie-item-info">.*?<p class="name"><.*?title="(.*?)".*?>(.*?)</a></p>.*?<p class="star">.*?</p><p class="releasetime">(.*?)</p></div>'
# regex = re.findall(a,html,re.S)
# print(regex)

"""
<div class="caption">.*?href="(.*?)" 
title="(.*?)".*?<small class="text-muted fs-12">.*?</small>.*?>(.*?)</p></div>
"""
