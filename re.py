import re
'''p=re.compile('.')
m=p.match('dgb')
print(m.group())
m2=p.match('\n')

p=re.compile(r'(\d)abc\1')
m=p.match('ad1abc1',2)
print(m.group())

p=re.compile(r'((?P<id>abc)123(?P=id)){2}')
m=p.match('abc123abcabc123abc')
print(m.groupdict())'''
'''
p=re.compile(r'a[^\d]')
m=p.findall('a22adcac')
print(m)


cr = re.compile("123[^(123)|p]*?ab")
s = "a123abvpd123d“p”f12ab123sabd123f1123abc"
print(cr.findall(s))
cr = re.compile("a.*?123") 
s = "abcd123d123ad1v123da123123"
print(cr.findall(s))
p=re.compile(r'(?:19|20)[0-9]{2}-(?:1[0-2]|0[1-9])-(?:[12][0-9]|0[1-9]|3[0-1])')
m=p.search('2015-11-29')
print(m.group())
p=re.compile(r"\b[abdf-hj-z]*(?:(c[abdf-hj-z]*i)|(i[abdf-hj-z]*c))e[abdf-hj-z]*\b")
m=p.search(r'ancient,science,viel,weigh')
print(m.group())
p=re.compile(r'http(s?)://([\w-]+\.)+[\w-]+[^>]*')
m=p.search(r"IT面试题博客中包含很多  <a href=http://hi.baidu.com/mianshiti/blog/category/微软面试题> 微软面试题 </a> ")
print(m.group())'''