import wordcloud


f = open("D:\\Python-based\\name.txt","r",encoding="utf-8")
t = f.read()
f.close()
w = wordcloud.WordCloud( font_path = "msyh.ttc",
                         width = 1000,
                         height = 700,
                         background_color = "white",
                         max_words = 80)
w.generate(t)
w.to_file("new7.png")
