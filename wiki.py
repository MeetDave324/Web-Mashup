import wikipedia
abc=wikipedia.search("Heart", results=1)
print(abc)
print(wikipedia.summary(str(abc)))