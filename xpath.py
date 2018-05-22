from lxml import html
import glob


for filename in glob.glob('/home/joao/TCC_source/webpages/book/book-abebooks(2000)/0012.htm'):
	#file = open("/home/joao/Downloads/book/book-abebooks(2000)/0001.htm", 'r')

	file = open(filename, 'r')
	page = file.read()
	tree = html.fromstring(page)

	# primeiro autor: //*[@id="bookdetail"]/h3/a[1]
	# ISBN-13: //*[@id="bookmetadata"]/strong[2]


	autors = tree.xpath('//*[@id="bookdetail"]/h3/a')
	isbn13 = tree.xpath('//*[@id="bookmetadata"]/strong[2]')


	print(len(autors))
	for autor in autors:
		print(autor.text)


	print(len(isbn13))
	for isbn in isbn13:
		print(isbn.text)


	file.close()
