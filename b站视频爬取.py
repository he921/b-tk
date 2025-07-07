import requests
import time
import tkinter as tk
import re
import json
import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from PIL import Image, ImageTk
from moviepy.editor import *
import threading
import os
import vlc


class lasthomework:
    def firstsearch(self):
        kw = self.input_va.get()
        url = 'https://api.bilibili.com/x/web-interface/wbi/search/all/v2'
        header = {
            "referer": "https://www.bilibili.com/",
            'cookie': 'buvid3=D75E0553-98C9-4536-92CA-8EAF0DE3DC49148829infoc; LIVE_BUVID=AUTO8616371355802560; _ga=GA1.2.146641365.1637476521; i-wanna-go-back=-1; CURRENT_BLACKGAP=0; blackside_state=0; is-2022-channel=1; buvid_fp_plain=undefined; fingerprint3=f08246011c100678e3b27e63ee69a807; hit-dyn-v2=1; DedeUserID=350899877; DedeUserID__ckMd5=3767451e536967f8; b_nut=100; CURRENT_QUALITY=80; _uuid=FBF4E2C9-42AC-1056E-4910D-C2108E4A6EC1717098infoc; rpdid=|(YYlm)~||J0JuYY)~YukuJ; buvid4=BDD569EC-7811-8E19-85F0-50004C2A9E1530831-022012015-RHIZMoo3tChX1%2FOaVLD9fg%3D%3D; b_ut=5; header_theme_version=CLOSE; hit-new-style-dyn=1; nostalgia_conf=-1; CURRENT_PID=696e59e0-cd54-11ed-a798-07221dfa732a; CURRENT_FNVAL=4048; PVID=1; fingerprint=a731e9f189a149b3abecb81b89ac49d6; buvid_fp=7f1d28266b7dcb2b5978e3c0a2fbceb2; FEED_LIVE_VERSION=V8; bp_video_offset_350899877=784751784305360900; SESSDATA=a77d74b1%2C1697111264%2C6358b%2A42; bili_jct=ab0e41ebaceb265111bab230efd4efff; b_lsid=25AD2B7B_18787A14537; home_feed_column=5',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
        }
        t = int(time.time())
        self.list1 = []
        data = {
            '__refresh__': 'true',
            '_extra': '',
            'context': '',
            'page': '1',
            'page_size': '42',
            'order': '',
            'duration': '',
            'from_source': '',
            'from_spmid': '333.337',
            'platform': 'pc',
            'highlight': '1',
            'single_column': '0',
            'keyword': kw,
            'qv_id': 'ybfYXx0RcX4G50Sp9zWqDbOJYGoTjrND',
            'ad_resource': '5646',
            'source_tag': '3',
            'w_rid': 'e1e676e2d66d9a6e3d7b5b36395af912',
            'wts': t,
        }
        response = requests.get(url=url, headers=header, params=data)
        print(response.text)
        datas = response.json()['data']['result'][11]['data']
        j = 0
        for i in datas:
            j += 1
            if i['type'] != 'video':
                datas.remove(i)
        self.listx = [datas[i]['arcurl'] for i in range(len(datas))]
        for i in range(len(datas)):
            s = str(datas[i]['title'])
            s = s.replace('<em class="keyword">', '')
            s = s.replace('</em>', '')
            self.list1.append(s)
        # list是综合排序的视频地址
        # list1是综合排序名称
        self.hebing = dict(zip(self.list1, self.listx))
        self.root.destroy()
        self.secondpage()

    def fisrtpage(self):
        global kw
        self.root = tk.Tk()
        self.root.title('b站搜索')
        self.root.geometry('1000x700+220+100')
        img = tk.PhotoImage(file='img\\02.png')
        tk.Label(self.root, image=img).pack()
        self.input_frame = tk.LabelFrame(self.root)
        self.input_frame.pack(fill='both', pady=8)
        tk.Label(self.input_frame, text='视频名称', font=('黑体', 14)).pack(side=tk.LEFT)
        self.input_va = tk.StringVar()
        # 设置输入框width 设置宽度relief 输入框样式输入
        ent=tk.Entry(self.input_frame, width=180,relief='ridge', textvariable=self.input_va)
        ent.pack(side=tk.LEFT,fill='both')
        # 设置按钮
        bu=tk.Button(self.root, text='搜索', font=('宋体', 20), bg='skyblue', fg='black', command=self.getentry)
        bu.pack(fill='both')
        bu1=tk.Button(self.root, text="退出", font=('宋体', 20), bg='skyblue', fg='black',command=self.continue_or_exit)
        bu1.pack(fill='both')
        self.root.mainloop()

    def continue_or_exit(self):
        result = msgbox.askyesno("温馨提醒", "确定退出吗?")
        if result == True:
            self.root.destroy()
        else:
            pass

    def getentry(self):
        kw = self.input_va.get()
        if kw == "":
            msgbox.showinfo("提示", "请输入内容")
        else:
            self.thread_it(self.firstsearch())

    def secondpage(self):
        self.root1 = tk.Tk()
        self.var1 = tk.StringVar()
        self.titleshow="请选择你需要的视频"
        self.root1.title(self.titleshow)
        self.listcomputer()
        screenwidth = self.root1.winfo_screenwidth()
        screenheight = self.root1.winfo_screenheight()
        width = 1300
        if screenheight < 900:
            height = 690
        else:
            height = 800
        alignstr = "%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root1.geometry(alignstr)
        self.root1.resizable(0, 0)

        self.root1['bg'] = '#C1FFE4'

        img4 = Image.open("img\\download.png")
        self.photoxiazai = ImageTk.PhotoImage(img4)
        img5 = Image.open("img\\fanhui.png")
        self.photofanhui = ImageTk.PhotoImage(img5)
        bt = tk.Button(self.root1, image=self.photoxiazai, command=self.check, bd=0)
        bt.place(x=50, y=190)
        bt1 = tk.Button(self.root1, image=self.photofanhui, command=self.destory, bd=0)
        bt1.place(x=300, y=190)
        self.lb = tk.Listbox(self.root1, bd=5, height=10, width=75)
        self.lb.place(x=10, y=0)
        for item in self.list1:
            self.lb.insert('end', item)
        sc = tk.Scrollbar(self.root1)
        sc.pack(side="left", fill="y")
        sc.config(command=self.lb.yview)
        self.lb.config(yscrollcommand=sc.set)
        self.lb.select_set(0)
        self.frame1 = tk.Frame(self.root1, bg="black", width=755, height=600, relief="groove", bd=1)
        self.frame1.place(x=538, y=0)
        self.media_player = vlc.MediaPlayer()
        self.canvas = tk.Canvas(self.frame1, width=755, height=590, bg="black")
        self.canvas.pack()
        self.media_player.set_hwnd(self.canvas.winfo_id())
        img = Image.open("img\\heizi.jpg")
        self.photo = ImageTk.PhotoImage(img)
        # 蔡徐坤
        self.canvas.create_image(0, 0, image=self.photo, anchor="nw")
        img1 = Image.open("img\\OIP.png")
        self.photo1 = ImageTk.PhotoImage(img1)
        # 暂停按钮
        img2 = Image.open("img\\OIP-C.png")
        self.photo2 = ImageTk.PhotoImage(img2)
        # 开始按钮
        img3 = Image.open("img\\OIP-.png")
        self.photo3 = ImageTk.PhotoImage(img3)
        # 结束按钮
        self.play_button = tk.Button(self.root1, image=self.photo2, bd=0, command=self.play)  # 开始
        self.stop_button = tk.Button(self.root1, image=self.photo1, bd=0, command=self.stop)  # 暂停
        self.pause_button = tk.Button(self.root1, image=self.photo3, bd=0, command=self.pause)  # 结束
        self.play_button.place(x=630, y=620)
        self.stop_button.place(x=880, y=620)
        self.pause_button.place(x=1130, y=620)

        self.root1.mainloop()
    def listcomputer(self):
        self.canvas1 = tk.Canvas(self.root1, bg="black", width=520, height=365, relief="groove", bd=1)
        self.canvas1.place(x=15, y=320)
        tableColums = ["name", "view"]
        self.table = ttk.Treeview(self.canvas1, columns=tableColums, show="headings", height=17)
        self.table.heading("name", text="文件名称", anchor=tk.CENTER)
        self.table.heading("view", text="状态", anchor=tk.CENTER)
        self.table.column("name", width=440)
        self.table.column("view", width=80)
        for dirs in os.walk(f"{os.getcwd()}//movies"):
            for i, data in enumerate(dirs[-1]):
                self.table.insert('', 'end', iid=str(i), values=(data,"yes"))
        self.table.insert("", "end", )
        self.table.pack()
    def destory(self):
        self.root1.destroy()
        self.fisrtpage()

    def play(self):
        value1 = self.lb.curselection()
        self.num1 = int((list(value1))[0])
        name = self.list1[self.num1].translate(str.maketrans({":": "：","/":"or"," ":"","?":"？","\\":"or"}))
        filepath = f'{os.getcwd()}/movies/{name}.mp4'
        if os.path.isfile(filepath):
            media = vlc.Media(filepath)
            self.media_player.set_media(media)
            self.media_player.play()
        else:
            msgbox.showinfo("提示", "文件未下载")

    def pause(self):
        self.media_player.stop()

    def stop(self):
        self.media_player.pause()
    def check(self):
        value1 = self.lb.curselection()
        self.num1 = int((list(value1))[0])
        name1=self.list1[self.num1]
        listlast=[]
        for dirs in os.walk(f"{os.getcwd()}//movies"):
            dir=dirs[-1]
            for i in dir:
                listlast.append(i[0:-4])
            if name1 in listlast:
                msgbox.showinfo("提示", "文件已存在")
            else:
                self.thread_it(self.xiazai)

    def xiazai(self):
        value = self.lb.curselection()
        self.num = int((list(value))[0])
        url = self.listx[self.num]
        header = {
            "referer": "https://www.bilibili.com/",
            'cookie': 'buvid3=D75E0553-98C9-4536-92CA-8EAF0DE3DC49148829infoc; LIVE_BUVID=AUTO8616371355802560; _ga=GA1.2.146641365.1637476521; i-wanna-go-back=-1; CURRENT_BLACKGAP=0; blackside_state=0; is-2022-channel=1; buvid_fp_plain=undefined; fingerprint3=f08246011c100678e3b27e63ee69a807; hit-dyn-v2=1; DedeUserID=350899877; DedeUserID__ckMd5=3767451e536967f8; b_nut=100; CURRENT_QUALITY=80; _uuid=FBF4E2C9-42AC-1056E-4910D-C2108E4A6EC1717098infoc; rpdid=|(YYlm)~||J0JuYY)~YukuJ; buvid4=BDD569EC-7811-8E19-85F0-50004C2A9E1530831-022012015-RHIZMoo3tChX1%2FOaVLD9fg%3D%3D; b_ut=5; header_theme_version=CLOSE; hit-new-style-dyn=1; nostalgia_conf=-1; CURRENT_PID=696e59e0-cd54-11ed-a798-07221dfa732a; CURRENT_FNVAL=4048; PVID=1; fingerprint=a731e9f189a149b3abecb81b89ac49d6; buvid_fp=7f1d28266b7dcb2b5978e3c0a2fbceb2; FEED_LIVE_VERSION=V8; bp_video_offset_350899877=784751784305360900; SESSDATA=a77d74b1%2C1697111264%2C6358b%2A42; bili_jct=ab0e41ebaceb265111bab230efd4efff; b_lsid=25AD2B7B_18787A14537; home_feed_column=5',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
        }
        rep = requests.get(url, headers=header)
        result = rep.text
        list2 = re.findall('__playinfo__=(.*?)</script>', result)[0]
        nr = json.loads(list2)
        video = nr["data"]["dash"]['video'][0]["baseUrl"]
        audio = nr["data"]["dash"]['audio'][0]["baseUrl"]
        data = requests.get(video, headers=header).content#mp4
        data1 = requests.get(audio, headers=header).content#mp3
        if os.path.exists(f'{os.getcwd()}\\movies'):
            pass
        else:
            os.mkdir(f'{os.getcwd()}\\movies')
        with open(f"{os.getcwd()}\\abc.mp3", mode="wb") as w:
            w.write(data1)
        with open(f"{os.getcwd()}\\abc.mp4", mode="wb") as w:
            w.write(data)
        self.thread_it(self.ff())
    def ff(self):
        file1 = f"{os.getcwd()}\\abc.mp3"  # mp3地址
        file2 = f"{os.getcwd()}\\abc.mp4"  # MP4地址
        result = f'{os.getcwd()}\\movies\\abcd.mp4'  # 合成音频地址
        # 合成代码

        os.system(f"{os.getcwd()}\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe -i {file1} -i {file2} -acodec copy -vcodec copy {result}")  # 合成代码
        namelist = self.list1[self.num1].translate(str.maketrans({":": "：", "/": "or", " ": "", "?": "？", "\\": "or"}))
        src=os.path.join(f'{os.getcwd()}\\movies',"abcd.mp4")
        src1=os.path.join(f'{os.getcwd()}\\movies',f"{namelist}.mp4")
        os.rename(src,src1)
        os.remove(file2)
        os.remove(file1)
        self.listcomputer()
        msgbox.showinfo("温馨提示",'你所需要的视频下载完成')


    def thread_it(self,func,*args):
        self.myThread=threading.Thread(target=func,args=args)
        self.myThread.setDaemon(True)
        self.myThread.start()

if __name__ == '__main__':
    last = lasthomework()
    last.fisrtpage()
