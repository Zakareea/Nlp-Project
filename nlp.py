import numpy as np
import openai
import re
import streamlit as st

class NLP:
	
	def generator(self, prompt):
		response = openai.Completion.create(
		  model="text-davinci-003",
		  prompt=prompt,
		  temperature=0.7,
		  max_tokens=256,
		  top_p=1,
		  frequency_penalty=0,
		  presence_penalty=0
		)
		res = response['choices'][0]['text']
		return res
	
	def summarize(self):
		st.header('Text Summarization')
		text = st.text_area('Text to summarize')
		if st.button('Summarize'):
			summarization = self.generator(f"""summarize the following text: {text}""")
			st.write(summarization)

	def sentiment_analysis(self):
		st.header('Sentiment Analysis')
		text = st.text_input('')
		if st.button('Submit'):
			sentiment_analysis = self.generator(f"""give me the sentiment analysis of the following text: {text}""")
			st.text(sentiment_analysis)

	def generate_article(self):
		st.header('Article Generator')
		topic = st.text_input('About')
		if st.button('Generate'):
			article = self.generator(f"write an article about {topic}")
			st.write(article)

	def generate_story(self):
		st.header('Story Generator')
		topic = st.text_input('About')

		if st.button('Generate'):
			story = self.generator(f"write a story about {topic}")
			st.write(story)

def main():
	st.title('Nlp Tasks')
	nlp = NLP()
	pages = {'Text Summarization': nlp.summarize,
		 'Sentiment Analysis': nlp.sentiment_analysis,
		 'Article Generator': nlp.generate_article,
		 'Story Generator': nlp.generate_story}

	page = st.selectbox('Choose some NLP Task', pages.keys())
	pages[page]()

main()
# You run this code by typing "streamlit run nlp.py" on the command line
