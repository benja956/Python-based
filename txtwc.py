import wordcloud,jieba
import pkuseg
import matplotlib.pyplot as plt



f = open("D:\\Python-based\\new.txt","r",encoding="utf-8")
t = f.read()
f.close()
seg = pkuseg.pkuseg()
ls = seg.cut(t)
txt = " ".join(ls)
backgroud_Image = plt.imread('heart.gif')
w = wordcloud.WordCloud( font_path = "msyh.ttc",
                         width = 1000,
                         height = 700,
                         background_color = "white",
                         max_words = 80,
                         mask = backgroud_Image)
w.generate(txt)
w.to_file("new7.png")
