from xml.dom.minidom import parse 
import xml.dom.minidom


# 读取xml文件
file = open(r"C:\Users\86188\Desktop\IBI\practical\go_obo.xml", "r")
tree = xml.dom.minidom.parse(file)
root = tree.documentElement
terms = root.getElementsByTagName('term')

results = []
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0]
    if 'autophagosome' in defstr.firstChild.data:
        id = term.getElementsByTagName('id')[0].firstChild.data
        name = term.getElementsByTagName('name')[0].firstChild.data
        children = term.childNodes # 获取所有子节点
        count = len(children)
    results.append(id, name, defstr.firstChild.data, count)
file.close()


for result in results:
  print(result)