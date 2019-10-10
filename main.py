
import re

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

#搜索模型 词袋模型 nlp领域最简单最常见的模型
class BOWEngine(SearchEnginBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)
	
	#执行查询
    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results
    
	#词是否在词袋中
    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True
	
	#静态函数将文章打碎形成词袋
    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
		# set()创建集合
        return set(word_list)

		
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
					
#search_engine = SimpleEngine()
#main(search_engine)

search_engine = BOWEngine()
main(search_engine)
