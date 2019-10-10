

# 父类
class SearchEnginBase(object):
	def __init__(self):
		pass
	#搜索集 读取文本
	def add_corpus(self,file_path):
		with open(file_path,'r') as fin:
			text = fin.read()
		self.process_corpus(file_path,text)
	
	def process_corpus(self,id,text):
		raise Exception('process_corpus not implemented.')
	
	def search(self,query):
		raise Exception('search not implemented')

class SimpleEngine(SearchEnginBase):
	def __init__(self):
		super(SimpleEngine,self).__init__()
		self.__id_to_texts = {}
	#键值对，定义文件名 文件
	def process_corpus(self,id,text):
		self.__id_to_texts[id] = text
	#搜索 返回结果集	
	def search(self,query):
		results = []
		for id,text in self.__id_to_texts.items():
			if query in text:
				results.append(id)
		return results
		
def main(search_engine):
	for file_path in ['1.txt','2.txt','3.txt','4.txt','5.txt']:
		search_engine.add_corpus(file_path)
	#搜索引擎	
	while True:
		query = input('请输入查询内容：')
		results = search_engine.search(query)
		print('found{}result(s):'.format(len(results)))
		for result in results:
			print(result)
			
			
search_engine = SimpleEngine()
main(search_engine)