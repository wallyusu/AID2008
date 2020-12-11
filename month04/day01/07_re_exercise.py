import re

html = """
<div class="animal">
    <p class="name">
			<a title="Tiger"></a>
    </p>
    <p class="content">
			Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
			<a title="Rabbit"></a>
    </p>

    <p class="content">
			Small white rabbit white and white
    </p>
"""
a = '<a title="(.*?)".*?"content">(.*?)</p>'
regex = re.findall(a, html, re.S)

for i in regex:
    print(i[0], i[1].strip(), sep='\n')
