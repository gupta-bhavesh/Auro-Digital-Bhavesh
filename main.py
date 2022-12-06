import xml.etree.ElementTree as ET
from queue import PriorityQueue

tree = ET.parse('orders.xml')
 
root = tree.getroot()
book = {}
for i in range(0, len(root)):
    print(root[i].tag)
    print(root[i].attrib)
    if(root[i].attrib['book'] not in book.keys()):
        book[root[i].attrib['book']] = {"BUY":PriorityQueue(), "SELL":PriorityQueue()}
    
    book[root[i].attrib['book']][root[i].attrib['operation']].put([root[i].attrib['price'], root[i].attrib['volume']])
    while(book[root[i].attrib['book']]["SELL"].get()[0] < book[root[i].attrib['book']]["BUY"].get()[0]):
        if(book[root[i].attrib['book']]["SELL"].get()[1] < book[root[i].attrib['book']]["BUY"].get()[1]):
            book[root[i].attrib['book']]["BUY"].get()[1] -= book[root[i].attrib['book']]["SELL"].get()[1]
            book[root[i].attrib['book']]["SELL"].pop()
        elif (book[root[i].attrib['book']]["SELL"].get()[1] == book[root[i].attrib['book']]["BUY"].get()[1]):
            book[root[i].attrib['book']]["BUY"].pop()
            book[root[i].attrib['book']]["SELL"].pop()
        else:
            book[root[i].attrib['book']]["SELL"].get()[1] -= book[root[i].attrib['book']]["BUY"].get()[1]
            book[root[i].attrib['book']]["BUY"].pop()