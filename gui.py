import sys
import tkinter as tk
import tw_api_func as tfunc

root = tk.Tk()
root.title(u"TKtest")
root.geometry("400x300")

def post_event(event):
    # static1.pack_forget()
    result = EditBox.get('1.0', 'end -1c')
    EditBox.delete('1.0', 'end')
    return_str = tfunc.post_tweet(result)
    static1 = tk.Label(text=return_str)
    static1.pack()

def sfll_event(event):
    # static1.pack_forget()
    result = EditBox.get('1.0', 'end -1c')
    EditBox.delete('1.0', 'end')
    return_str = tfunc.search_follow(result)
    static1 = tk.Label(text=return_str)
    static1.pack()

def like_event(event):
    # static1.pack_forget()
    result = EditBox.get('1.0', 'end -1c')
    EditBox.delete('1.0', 'end')
    return_str = tfunc.friend_fav()
    static1 = tk.Label(text=return_str)
    static1.pack()

#テキストエリア
EditBox = tk.Text(width=50, height=3)
EditBox.pack()

#post btn
b_post = tk.Button(text=u'POST', width=50)
b_post.bind("<Button-1>",post_event)
b_post.bind("<Return>",post_event)
b_post.pack()

#SFll btn
sf_post = tk.Button(text=u'SFll', width=50)
sf_post.bind("<Button-1>",sfll_event)
sf_post.bind("<Return>",sfll_event)
sf_post.pack()

#like btn
li_post = tk.Button(text=u'Flk', width=50)
li_post.bind("<Button-1>",like_event)
li_post.bind("<Return>",like_event)
li_post.pack()


root.mainloop()
