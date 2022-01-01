from tkinter import ttk, messagebox, font, filedialog
import tkinter as tk
import webbrowser
import threading
import pyperclip
import winsound
import asyncio
import time
import os


async def window_warn(text : str, playSound : bool = True):
    if playSound:
        winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC);
    win = tk.Tk();
    win.title('BiliDownloader');
    win.geometry('395x65+200+200');
    win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
    win.resizable(tk.TRUE, tk.FALSE);
    f = font.Font(root=win, name='TkTextFont', exists=True);
    f['size'] = 11;
    mainframe = ttk.Frame(win, padding=5);
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
    win.columnconfigure(0, weight=1);
    win.rowconfigure(0, weight=1);
    t0 = tk.Variable(win);
    t0.set(text);
    lab0 = ttk.Label(mainframe, textvariable=t0, font=f);
    lab0.grid(column=1, row=1, sticky=(tk.N, tk.W));
    def callback():
        win.destroy();
    btn0 = ttk.Button(mainframe, text='OK', command=callback);
    btn0.grid(column=1, row=2, sticky=(tk.W, tk.S));
    win.mainloop();
    return;


async def window_warn_big_2(text : str, playSound : bool = True):
    if playSound:
        winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC);
    win = tk.Tk();
    win.title('BiliDownloader');
    win.geometry('395x80+200+200');
    win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
    f = font.Font(root=win, name='TkTextFont', exists=True);
    f['size'] = 11;
    mainframe = ttk.Frame(win, padding=5);
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
    win.columnconfigure(0, weight=1);
    win.rowconfigure(0, weight=1);
    tmp = str();
    for i in range(len(text)):
        tmp += text[i];
        if (i + 1) % 28 == 0:
            tmp += '\n';
    t0 = tk.Variable(win);
    t0.set(tmp);
    lab0 = ttk.Label(mainframe, textvariable=t0, font=f);
    lab0.grid(column=1, row=1, sticky=(tk.N, tk.W));
    def callback():
        win.destroy();
    btn0 = ttk.Button(mainframe, text='OK', command=callback);
    btn0.grid(column=1, row=2, sticky=(tk.W, tk.S));
    win.mainloop();
    return;


async def window_ask() -> str:
    global retv;
    retv = 'a';
    win = tk.Tk();
    win.title('BiliDownloader');
    win.geometry('395x112+200+200');
    win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
    win.resizable(tk.FALSE, tk.FALSE);
    def showmessage():
        tmp = messagebox.askyesno(title='确认', message='确认关闭?', parent=win, type='yesno');
        if tmp:
            global PID;
            os.kill(PID, 15);
    win.protocol('WM_DELETE_WINDOW', showmessage);
    f = font.Font(root=win, name='TkTextFont', exists=True);
    f['size'] = 11;
    mainframe = ttk.Frame(win, padding=5);
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
    win.columnconfigure(0, weight=1);
    win.rowconfigure(0, weight=1);
    lab0 = ttk.Label(mainframe, text='请输入视频的BV号、AV号或MD号\n(包含开头的BV、AV和MD):', font=f);
    lab0.grid(column=1, row=1, sticky=(tk.N, tk.W));
    text = tk.Variable(win);
    etr0 = ttk.Entry(mainframe, width=42, textvariable=text);
    etr0.grid(column=1, row=2, sticky=(tk.N, tk.W));
    def callback0():
        global retv;
        retv = (0, text.get().replace(' ', ''));
        win.destroy();
    def callback1():
        global retv;
        retv = (1, 'set');
        win.destroy();
    def callback2(e):
        text.set(pyperclip.paste());
    etr0.bind('<Button-3>', callback2);
    fra0 = ttk.Frame(mainframe);
    fra0.grid(column=1, row=3, sticky=(tk.E), pady=1);
    btn0 = ttk.Button(fra0, text='OK', command=callback0);
    btn0.grid(column=2, row=1, sticky=(tk.E));
    btn1 = ttk.Button(fra0, text='设置', command=callback1);
    btn1.grid(column=1, row=1, sticky=(tk.E));
    win.mainloop();
    return retv;


async def window_settings(downloadP : str, haveC : bool):
    global retv;
    retv = None;
    win = tk.Tk();
    win.title('BiliDownloader');
    win.geometry('395x125+200+200');
    win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
    win.resizable(tk.FALSE, tk.FALSE);
    def showmessage():
        tmp = messagebox.askyesno(title='确认', message='确认关闭?', parent=win, type='yesno');
        if tmp:
            global PID;
            os.kill(PID, 15);
    win.protocol('WM_DELETE_WINDOW', showmessage);
    f = font.Font(root=win, name='TkTextFont', exists=True);
    f['size'] = 11;
    mainframe = ttk.Frame(win, padding=5);
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
    win.columnconfigure(0, weight=1);
    win.rowconfigure(0, weight=1);
    labf0 = ttk.Labelframe(mainframe, text='设置');
    labf0.grid(column=1, row=1, sticky=(tk.N, tk.W, tk.E));
    def callback0():
        global retv;
        retv = (0, filedialog.askdirectory(parent=win, title='选择下载路径'));
        win.destroy();
    btn0 = ttk.Button(labf0, text='设置下载位置', command=callback0);
    btn0.grid(column=1, row=1, sticky=(tk.W));
    v0 = tk.Variable(win);
    v0.set(downloadP);
    etn0 = ttk.Entry(labf0, textvariable=v0, state='readonly', width=29, font=f);
    etn0.grid(column=2, row=1, sticky=(tk.W));
    def callback1():
        global retv;
        retv = (1,);
        win.destroy();
    btn1 = ttk.Button(labf0, text='设置通行证', command=callback1);
    btn1.grid(column=1, row=2, sticky=(tk.W));
    v1 = tk.Variable(win);
    v1.set('已设置' if haveC else '未设置');
    etn1 = ttk.Entry(labf0, textvariable=v1, state='readonly', width=29, font=f);
    etn1.grid(column=2, row=2, sticky=(tk.W));
    fra0 = ttk.Frame(mainframe);
    fra0.grid(column=1, row=2, pady=1);
    def callback2():
        global retv
        retv = None;
        win.destroy();
    btn2 = ttk.Button(fra0, text='返回', command=callback2);
    btn2.grid(column=1, row=1);
    def callback3():
        tmp = messagebox.askyesno(title='确认', message='确认重置?', parent=win, type='yesno');
        if tmp:
            global retv;
            retv = (2,);
            win.destroy();
    btn3 = ttk.Button(fra0, text='重置', command=callback3);
    btn3.grid(column=2, row=1);
    win.mainloop();
    return retv;


async def window_settings_credential(dafult : dict = None):
    global retv;
    retv = None;
    win = tk.Tk();
    win.title('BiliDownloader');
    win.geometry('395x142+200+200');
    win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
    win.resizable(tk.FALSE, tk.FALSE);
    def showmessage():
        tmp = messagebox.askyesno(title='确认', message='确认关闭?', parent=win, type='yesno');
        if tmp:
            global PID;
            os.kill(PID, 15);
    win.protocol('WM_DELETE_WINDOW', showmessage);
    f = font.Font(root=win, name='TkTextFont', exists=True);
    f['size'] = 11;
    mainframe = ttk.Frame(win, padding=5);
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
    win.columnconfigure(0, weight=1);
    win.rowconfigure(0, weight=1);
    v0 = tk.Variable(win);
    v1 = tk.Variable(win);
    v2 = tk.Variable(win);
    if dafult is not None:
        v0.set(dafult['sessdata']);
        v1.set(dafult['bili_jct']);
        v2.set(dafult['buvid3']);
    labf0 = ttk.Labelframe(mainframe, text='设置通行证');
    labf0.grid(column=1, row=1, sticky=(tk.N, tk.W, tk.E));
    lab0 = ttk.Label(labf0, text='sessdata:', font=f);
    lab0.grid(column=1, row=1, sticky=(tk.W));
    etr0 = ttk.Entry(labf0, textvariable=v0, width=34);
    etr0.grid(column=2, row=1, sticky=(tk.W));
    lab1 = ttk.Label(labf0, text='bili_jct:', font=f);
    lab1.grid(column=1, row=2, sticky=(tk.W));
    etr1 = ttk.Entry(labf0, textvariable=v1, width=34);
    etr1.grid(column=2, row=2, sticky=(tk.W));
    lab2 = ttk.Label(labf0, text='buvid3:', font=f);
    lab2.grid(column=1, row=3, sticky=(tk.W));
    etr2 = ttk.Entry(labf0, textvariable=v2, width=34);
    etr2.grid(column=2, row=3, sticky=(tk.W));
    fra1 = ttk.Frame(mainframe);
    fra1.grid(column=1, row=2, pady=1);
    def callback0():
        global retv;
        retv = None;
        win.destroy();
    btn0 = ttk.Button(fra1, text='返回', command=callback0);
    btn0.grid(column=1, row=2, sticky=(tk.N));
    def callback1():
        webbrowser.open('https://gitee.com/majjcom/bili-downloader/wikis/');
    btn1 = ttk.Button(fra1, text='帮助', command=callback1);
    btn1.grid(column=2, row=2, sticky=(tk.N));
    def callback2():
        global retv;
        retv = {
            'sessdata': v0.get(),
            'bili_jct': v1.get(),
            'buvid3':   v2.get()
        };
        win.destroy();
    btn2 = ttk.Button(fra1, text='确认', command=callback2);
    btn2.grid(column=3, row=2, sticky=(tk.N));
    win.mainloop();
    return retv;



async def window_showupdate():
    win = tk.Tk();
    win.title('BiliDownloader');
    win.geometry('395x85+200+200');
    win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
    win.resizable(tk.TRUE, tk.FALSE);
    def showmessage():
        tmp = messagebox.askyesno(title='确认', message='确认关闭?', parent=win, type='yesno');
        if tmp:
            win.destroy();
    win.protocol('WM_DELETE_WINDOW', showmessage);
    f = font.Font(root=win, name='TkTextFont', exists=True);
    f['size'] = 11;
    mainframe = ttk.Frame(win, padding=5);
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
    win.columnconfigure(0, weight=1);
    win.rowconfigure(0, weight=1);
    lab0 = ttk.Label(mainframe, text='有新的版本更新，即将开始下载\nP.S. 本软件正处于开发阶段，更新频繁，请见谅，每次更新都将会有稳定性的提升', font=f);
    lab0.grid(column=1, row=1, sticky=(tk.N, tk.W));
    def callback():
        win.destroy();
    btn0 = ttk.Button(mainframe, text='OK', command=callback);
    btn0.grid(column=1, row=2, sticky=(tk.S, tk.W));
    win.mainloop();
    return;


async def window_confirm(text : str):
    global retv, ifPathSet;
    ifPathSet = None;
    retv = False;
    win = tk.Tk();
    win.title('BiliDownloader');
    win.geometry('395x145+200+200');
    win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
    win.resizable(tk.FALSE, tk.FALSE);
    def showmessage():
        tmp = messagebox.askyesno(title='确认', message='确认关闭?', parent=win, type='yesno');
        if tmp:
            global PID;
            os.kill(PID, 15);
    win.protocol('WM_DELETE_WINDOW', showmessage);
    f = font.Font(root=win, name='TkTextFont', exists=True);
    f['size'] = 11;
    mainframe = ttk.Frame(win, padding=5);
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.S, tk.W));
    win.columnconfigure(0, weight=1);
    win.rowconfigure(0, weight=1);
    t = tk.Variable(win);
    t.set(text);
    lab0 = ttk.Label(mainframe, textvariable=t, font=f);
    lab0.grid(column=1, row=1, sticky=(tk.N, tk.W));
    def callback0():
        global retv
        retv = True;
        win.destroy();
    def callback1():
        win.destroy();
    fra0 = ttk.Frame(mainframe);
    fra0.grid(column=1, row=2, sticky=(tk.W));
    btn0 = ttk.Button(fra0, text='YES', command=callback0);
    btn0.grid(column=1, row=1, sticky=(tk.W));
    btn1 = ttk.Button(fra0, text='NO', command=callback1);
    btn1.grid(column=2, row=1, sticky=(tk.W));
    win.mainloop();
    return retv;


async def window_config_p(text : str):
    global retv;
    retv = '';
    win = tk.Tk();
    win.title('BiliDownloader');
    win.geometry('395x115+200+200');
    win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
    win.resizable(tk.FALSE, tk.FALSE);
    def showmessage():
        tmp = messagebox.askyesno(title='确认', message='确认关闭?', parent=win, type='yesno');
        if tmp:
            global PID;
            os.kill(PID, 15);
    win.protocol('WM_DELETE_WINDOW', showmessage);
    f = font.Font(root=win, name='TkTextFont', exists=True);
    f['size'] = 11;
    mainframe = ttk.Frame(win, padding=5);
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.S, tk.W));
    win.columnconfigure(0, weight=1);
    win.rowconfigure(0, weight=1);
    t0 = tk.Variable(win)
    t0.set(text);
    lab0 = ttk.Label(mainframe, textvariable=t0, font=f);
    lab0.grid(column=1, row=1, sticky=(tk.N, tk.W));
    lab1 = ttk.Label(mainframe, text='请选择下载范围, 用","分隔(如1-1或1-5或1-1, 3-5): ', font=f);
    lab1.grid(column=1, row=2, sticky=(tk.W));
    t1 = tk.Variable(win);
    etr0 = ttk.Entry(mainframe, textvariable=t1);
    etr0.grid(column=1, row=3, sticky=(tk.W));
    def callback():
        global retv;
        retv = t1.get();
        win.destroy();
    btn0 = ttk.Button(mainframe, text='OK', command=callback);
    btn0.grid(column=1, row=4, sticky=(tk.W, tk.S));
    win.mainloop();
    return retv;


async def window_config_q(tip : str):
    global retv;
    retv = '';
    win = tk.Tk();
    win.title('BiliDownloader');
    win.geometry('395x92+200+200');
    win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
    win.resizable(tk.FALSE, tk.FALSE);
    def showmessage():
        tmp = messagebox.askyesno(title='确认', message='确认关闭?', parent=win, type='yesno');
        if tmp:
            global PID;
            os.kill(PID, 15);
    def showHelp():
        messagebox.showinfo(title='提示',
                            parent=win,
                            message='提示:\n\n'
                                    '120\t4K\n116\t1080p60\n112\t1080p+\n80\t1080p\n72\t720p60\n64\t720p\n32\t480p\n16\t320p\n\n'
                                    '如果出现一直无法下载的情况可以稍微降低清晰度哦ლ(´ڡ`ლ)\n'
                                    '部分会员资源下载需要设置通行证，请自行到设置中进行设置\n\n'
                                    'P.S.现已支持4k分辨率视频下载!!!');
    win.protocol('WM_DELETE_WINDOW', showmessage);
    f = font.Font(root=win, name='TkTextFont', exists=True);
    f['size'] = 11;
    mainframe = ttk.Frame(win, padding=5);
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
    win.columnconfigure(0, weight=1);
    win.rowconfigure(0, weight=1);
    lab0 = ttk.Label(mainframe, text='请选择清晰度(可选: {}): '.format(tip), font=f);
    lab0.grid(column=1, row=1, stick=(tk.N, tk.W));
    t0 = tk.Variable(win);
    t0.set(tip.split(', ', 1)[0]);
    etr0 = ttk.Entry(mainframe, textvariable=t0, width=10);
    etr0.grid(column=1, row=2, sticky=(tk.W));
    def callback():
        global retv;
        retv = t0.get();
        win.destroy();
    fra0 = ttk.Frame(mainframe);
    fra0.grid(column=1, row=3, sticky=(tk.W), pady=2);
    btn0 = ttk.Button(fra0, text='OK', command=callback);
    btn0.grid(column=1, row=1, sticky=(tk.W));
    btn1 = ttk.Button(fra0, text='提示', command=showHelp);
    btn1.grid(column=2, row=1, sticky=(tk.W));
    win.mainloop();
    return retv;


async def window_finish(text):
    win = tk.Tk();
    win.title('BiliDownloader');
    win.geometry('395x90+200+200');
    win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
    win.resizable(tk.FALSE, tk.FALSE);
    f = font.Font(root=win, name='TkTextFont', exists=True);
    f['size'] = 11;
    mainframe = ttk.Frame(win, padding=5);
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
    win.columnconfigure(0, weight=1);
    win.rowconfigure(0, weight=1);
    lab0 = ttk.Label(mainframe, text='视频全部下载完成，保存在: ', font=f);
    lab0.grid(column=1, row=1, sticky=(tk.N, tk.W));
    t0 = tk.Variable(win);
    t0.set(text);
    etr0 = ttk.Entry(mainframe, textvariable=t0, state='readonly', width=30);
    etr0.grid(column=1, row=2, sticky=(tk.W));
    def callback():
        win.destroy();
    btn0 = ttk.Button(mainframe, text='OK', command=callback);
    btn0.grid(column=1, row=3, sticky=(tk.S, tk.W));
    win.mainloop();
    return;


class window_interrupt(threading.Thread):
    def __init__(self, this : tk.Tk, v):
        threading.Thread.__init__(self);
        self._this = this;
        self._v = v;

    def run(self):
        while True:
            time.sleep(0.1);
            if self._v[0]:
                self._this.destroy();
                return;

class window_geturl(threading.Thread):
    def __init__(self, v):
        threading.Thread.__init__(self);
        self._v = v; # 0: isRun, 1: t0

    def run(self) -> None:
        win = tk.Tk();
        win.title('BiliDownloader');
        win.geometry('395x35+200+200');
        win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
        win.resizable(tk.FALSE, tk.FALSE);
        def showmessage():
            tmp = messagebox.askyesno(title='确认', message='确认关闭?', parent=win, type='yesno');
            if tmp:
                global PID;
                os.kill(PID, 15);
        win.protocol('WM_DELETE_WINDOW', showmessage);
        f = font.Font(root=win, name='TkTextFont', exists=True);
        f['size'] = 11;
        mainframe = ttk.Frame(win, padding=5);
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
        win.columnconfigure(0, weight=1);
        win.rowconfigure(0, weight=1);
        t0 = tk.Variable(win);
        t0.set('null');
        self._v.append(t0);
        lab0 = ttk.Label(mainframe, textvariable=t0, font=f);
        lab0.grid(column=1, row=1, sticky=(tk.N, tk.W));
        tmp = window_interrupt(win, self._v);
        tmp.start();
        win.mainloop();
        return;


class window_downloas(threading.Thread):
    def __init__(self, v):
        threading.Thread.__init__(self);
        self._v = v; # 0: isRun, 1: t0, 2: t1, 3: t2, 4: t3, 5: bar

    def run(self) -> None:
        win = tk.Tk();
        win.title('BiliDownloader');
        win.geometry('395x105+200+200');
        win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
        win.resizable(tk.FALSE, tk.FALSE);
        def showmessage():
            messagebox.showwarning('警告', '请不要关闭这个窗口...', parent=win);
        win.protocol('WM_DELETE_WINDOW', showmessage);
        f = font.Font(root=win, name='TkTextFont', exists=True);
        f['size'] = 11;
        mainframe = ttk.Frame(win, padding=5);
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
        win.columnconfigure(0, weight=1);
        win.rowconfigure(0, weight=1);
        t0 = tk.Variable(win);
        t0.set('null');
        self._v.append(t0);
        lab0 = ttk.Label(mainframe, textvariable=t0, font=f);
        lab0.grid(column=1, row=1, sticky=(tk.N, tk.W));
        t1 = tk.Variable(win)
        t1.set('null');
        self._v.append(t1);
        lab1 = ttk.Label(mainframe, textvariable=t1, font=f);
        lab1.grid(column=1, row=2, sticky=(tk.W));
        t2 = tk.Variable(win);
        t2.set('null')
        self._v.append(t2);
        lab2 = ttk.Label(mainframe, textvariable=t2, font=f);
        lab2.grid(column=1, row=3, sticky=(tk.W));
        t3 = tk.Variable(win);
        t3.set(0.0);
        self._v.append(t3);
        bar0 = ttk.Progressbar(
                mainframe,
                orient=tk.HORIZONTAL,
                length=250,
                mode='determinate',
                variable=t3
            );
        bar0.grid(column=1, row=4, sticky=(tk.S, tk.W));
        self._v.append(bar0);
        tmp = window_interrupt(win, self._v);
        tmp.start();
        win.mainloop();
        return;


class window_updating(threading.Thread):
    def __init__(self, arg : list):
        threading.Thread.__init__(self);
        self._arg = arg;

    def run(self):
        win = tk.Tk();
        win.title('BiliDownloader Update');
        win.geometry('395x60+200+200');
        win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
        win.resizable(tk.FALSE, tk.FALSE);
        def showmessage():
            messagebox.showwarning('警告', '请不要关闭这个窗口...', parent=win);
        win.protocol('WM_DELETE_WINDOW', showmessage);
        f = font.Font(root=win, name='TkTextFont', exists=True);
        f['size'] = 11;
        mainframe = ttk.Frame(win, padding=5);
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
        win.columnconfigure(0, weight=1);
        win.rowconfigure(0, weight=1);
        lab0 = ttk.Label(mainframe, text='正在下载更新...', font=f);
        lab0.grid(column=1, row=1, sticky=(tk.W, tk.N));
        t0 = tk.Variable(win);
        t0.set(0.0);
        self._arg.append(t0);
        bar0 = ttk.Progressbar(
            mainframe,
            orient=tk.HORIZONTAL,
            length=250,
            mode='determinate',
            variable=t0
        );
        bar0.grid(column=1, row=2, sticky=(tk.W, tk.S));
        tmp = window_interrupt(win, self._arg);
        tmp.start();
        win.mainloop();

class window_checkUpdate(threading.Thread):
    def __init__(self, basket : list):
        threading.Thread.__init__(self);
        self._basket = basket;

    def run(self):
        win = tk.Tk();
        win.title('BiliDownloader Update');
        win.geometry('395x112+200+200');
        win.iconbitmap(os.path.join(programPath, 'src/icon.ico'));
        win.resizable(tk.FALSE, tk.FALSE);

        def showmessage():
            messagebox.showwarning('警告', '请不要关闭这个窗口...', parent=win);

        win.protocol('WM_DELETE_WINDOW', showmessage);
        f = font.Font(root=win, name='TkTextFont', exists=True);
        f['size'] = 12;
        mainframe = ttk.Frame(win, padding=5);
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S));
        win.columnconfigure(0, weight=1);
        win.rowconfigure(0, weight=1);
        lab0 = ttk.Label(mainframe, text='正在检查更新...', font=f);
        lab0.grid(column=1, row=1, sticky=(tk.W, tk.N));
        tmp = window_interrupt(win, self._basket);
        tmp.start();
        win.mainloop();

def window_setVar(PID_get, programPath_get):
    global PID;
    global programPath;
    PID = PID_get;
    programPath = programPath_get;


def window_main():
    print('Please Run As Module...');

if __name__ == '__main__':
    window_main();
