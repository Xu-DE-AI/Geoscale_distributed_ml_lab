from openai import OpenAI
def main():
 c=OpenAI(base_url='http://localhost:8000/v1',api_key='EMPTY'); r=c.chat.completions.create(model='your-model',messages=[{'role':'user','content':'Explain effective stress.'}],max_tokens=100); print(r.choices[0].message.content)
if __name__=='__main__': main()
