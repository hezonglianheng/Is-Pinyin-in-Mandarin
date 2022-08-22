# encoding:utf8
import json
import os.path
import tkinter.messagebox as box
from tkinter import *
import initialize


class Window:
    def __init__(self):
        abs_path = os.path.abspath(r'source')
        json_path = os.path.join(abs_path, r'pinyin_set.json')
        if not os.path.exists(json_path):
            initialize.read_pinyin()
        with open(json_path, mode='r+') as file:
            self.pinyin = json.load(file)
            file.close()
        self.window = Tk()
        self.window.title('汉语声韵配合系统（粗制滥造版）')
        self.window.geometry('600x600+0+0')
        self.entry_label = Label(master=self.window,
                                 text='待查询的拼音',
                                 font=('楷体', 16))
        self.entry_label.place(x=20, y=20)
        self.text_entry = Entry(master=self.window,
                                font=('Times New Roman', 16))
        self.text_entry.place(x=180, y=20)
        self.query_button = Button(master=self.window,
                                   text='查询',
                                   font=('楷体', 16),
                                   height=1, width=4,
                                   command=self.pinyin_query)
        self.query_button.place(x=420, y=20)
        self.clear_button = Button(master=self.window,
                                   text='清除',
                                   font=('楷体', 16),
                                   height=1, width=4,
                                   command=self.clear)
        self.clear_button.place(x=480, y=20)
        self.exit_button = Button(master=self.window,
                                  text='退出',
                                  font=('楷体', 16),
                                  height=1, width=4,
                                  command=self.exit_it)
        self.exit_button.place(x=540, y=20)

        self.shengmu_label = Label(master=self.window,
                                   text='声母',
                                   font=('楷体', 16))
        self.shengmu_label.place(x=20, y=100)
        self.b_button = Button(master=self.window,
                               text='b',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_b)
        self.b_button.place(x=20, y=140)
        self.p_button = Button(master=self.window,
                               text='p',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_p)
        self.p_button.place(x=50, y=140)
        self.m_button = Button(master=self.window,
                               text='m',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_m)
        self.m_button.place(x=80, y=140)
        self.f_button = Button(master=self.window,
                               text='f',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_f)
        self.f_button.place(x=110, y=140)
        self.d_button = Button(master=self.window,
                               text='d',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_d)
        self.d_button.place(x=20, y=180)
        self.t_button = Button(master=self.window,
                               text='t',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_t)
        self.t_button.place(x=50, y=180)
        self.n_button = Button(master=self.window,
                               text='n',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_n)
        self.n_button.place(x=80, y=180)
        self.l_button = Button(master=self.window,
                               text='l',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_l)
        self.l_button.place(x=110, y=180)
        self.g_button = Button(master=self.window,
                               text='ɡ',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_g)
        self.g_button.place(x=20, y=220)
        self.k_button = Button(master=self.window,
                               text='k',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_k)
        self.k_button.place(x=50, y=220)
        self.h_button = Button(master=self.window,
                               text='h',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_h)
        self.h_button.place(x=80, y=220)
        self.j_button = Button(master=self.window,
                               text='j',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_j)
        self.j_button.place(x=20, y=260)
        self.q_button = Button(master=self.window,
                               text='q',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_q)
        self.q_button.place(x=50, y=260)
        self.x_button = Button(master=self.window,
                               text='x',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_x)
        self.x_button.place(x=80, y=260)
        self.z_button = Button(master=self.window,
                               text='z',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_z)
        self.z_button.place(x=20, y=300)
        self.c_button = Button(master=self.window,
                               text='c',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_c)
        self.c_button.place(x=50, y=300)
        self.s_button = Button(master=self.window,
                               text='s',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_s)
        self.s_button.place(x=80, y=300)
        self.zh_button = Button(master=self.window,
                                text='zh',
                                font=('times new roman', 14),
                                height=1, width=2,
                                command=self.input_zh)
        self.zh_button.place(x=20, y=340)
        self.ch_button = Button(master=self.window,
                                text='ch',
                                font=('times new roman', 14),
                                height=1, width=2,
                                command=self.input_ch)
        self.ch_button.place(x=50, y=340)
        self.sh_button = Button(master=self.window,
                                text='sh',
                                font=('times new roman', 14),
                                height=1, width=2,
                                command=self.input_sh)
        self.sh_button.place(x=80, y=340)
        self.r_button = Button(master=self.window,
                               text='r',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_r)
        self.r_button.place(x=110, y=340)
        self.y_button = Button(master=self.window,
                               text='y',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_y)
        self.y_button.place(x=20, y=380)
        self.w_button = Button(master=self.window,
                               text='w',
                               font=('times new roman', 14),
                               height=1, width=2,
                               command=self.input_w)
        self.w_button.place(x=50, y=380)

        self.yunmu_label = Label(master=self.window,
                                 text='韵母',
                                 font=('楷体', 16))
        self.yunmu_label.place(x=220, y=100)
        self.a_button = Button(master=self.window,
                               text='a',
                               font=('times new roman', 16),
                               height=1, width=3,
                               command=self.input_a)
        self.a_button.place(x=220, y=140)
        self.o_button = Button(master=self.window,
                               text='o',
                               font=('times new roman', 16),
                               height=1, width=3,
                               command=self.input_o)
        self.o_button.place(x=270, y=140)
        self.e_button = Button(master=self.window,
                               text='e',
                               font=('times new roman', 16),
                               height=1, width=3,
                               command=self.input_e)
        self.e_button.place(x=320, y=140)
        self.i_button = Button(master=self.window,
                               text='i',
                               font=('times new roman', 16),
                               height=1, width=3,
                               command=self.input_i)
        self.i_button.place(x=370, y=140)
        self.u_button = Button(master=self.window,
                               text='u',
                               font=('times new roman', 16),
                               height=1, width=3,
                               command=self.input_u)
        self.u_button.place(x=420, y=140)
        self.v_button = Button(master=self.window,
                               text='ü',
                               font=('times new roman', 16),
                               height=1, width=3,
                               command=self.input_v)
        self.v_button.place(x=470, y=140)
        self.ai_button = Button(master=self.window,
                                text='ai',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_ai)
        self.ai_button.place(x=220, y=180)
        self.ei_button = Button(master=self.window,
                                text='ei',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_ei)
        self.ei_button.place(x=270, y=180)
        self.ui_button = Button(master=self.window,
                                text='ui',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_ui)
        self.ui_button.place(x=320, y=180)
        self.ao_button = Button(master=self.window,
                                text='ao',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_ao)
        self.ao_button.place(x=220, y=220)
        self.ou_button = Button(master=self.window,
                                text='ou',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_ou)
        self.ou_button.place(x=270, y=220)
        self.iu_button = Button(master=self.window,
                                text='iu',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_iu)
        self.iu_button.place(x=320, y=220)
        self.ie_button = Button(master=self.window,
                                text='ie',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_ie)
        self.ie_button.place(x=220, y=260)
        self.ve_button = Button(master=self.window,
                                text='üe',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_ve)
        self.ve_button.place(x=270, y=260)
        self.er_button = Button(master=self.window,
                                text='er',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_er)
        self.er_button.place(x=220, y=300)
        self.an_button = Button(master=self.window,
                                text='an',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_an)
        self.an_button.place(x=220, y=340)
        self.en_button = Button(master=self.window,
                                text='en',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_en)
        self.en_button.place(x=270, y=340)
        self.in_button = Button(master=self.window,
                                text='in',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_in)
        self.in_button.place(x=320, y=340)
        self.un_button = Button(master=self.window,
                                text='un',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_un)
        self.un_button.place(x=370, y=340)
        self.vn_button = Button(master=self.window,
                                text='ün',
                                font=('times new roman', 16),
                                height=1, width=3,
                                command=self.input_vn)
        self.vn_button.place(x=420, y=340)
        self.ang_button = Button(master=self.window,
                                 text='anɡ',
                                 font=('times new roman', 16),
                                 height=1, width=3,
                                 command=self.input_ang)
        self.ang_button.place(x=220, y=380)
        self.eng_button = Button(master=self.window,
                                 text='enɡ',
                                 font=('times new roman', 16),
                                 height=1, width=3,
                                 command=self.input_eng)
        self.eng_button.place(x=270, y=380)
        self.ing_button = Button(master=self.window,
                                 text='inɡ',
                                 font=('times new roman', 16),
                                 height=1, width=3,
                                 command=self.input_ing)
        self.ing_button.place(x=320, y=380)
        self.ong_button = Button(master=self.window,
                                 text='onɡ',
                                 font=('times new roman', 16),
                                 height=1, width=3,
                                 command=self.input_ong)
        self.ong_button.place(x=370, y=380)

        self.shengdiao_label = Label(master=self.window,
                                     text='声调',
                                     font=('楷体', 16))
        self.shengdiao_label.place(x=20, y=450)
        self.yinping_button = Button(master=self.window,
                                     text='1',
                                     font=('times new roman', 16),
                                     height=1, width=1,
                                     command=self.input_1)
        self.yinping_button.place(x=100, y=450)
        self.yangping_button = Button(master=self.window,
                                      text='2',
                                      font=('times new roman', 16),
                                      height=1, width=1,
                                      command=self.input_2)
        self.yangping_button.place(x=130, y=450)
        self.shangsheng_button = Button(master=self.window,
                                        text='3',
                                        font=('times new roman', 16),
                                        height=1, width=1,
                                        command=self.input_3)
        self.shangsheng_button.place(x=160, y=450)
        self.qusheng_button = Button(master=self.window,
                                     text='4',
                                     font=('times new roman', 16),
                                     height=1, width=1,
                                     command=self.input_4)
        self.qusheng_button.place(x=190, y=450)
        self.qingsheng_button = Button(master=self.window,
                                       text='0',
                                       font=('times new roman', 16),
                                       height=1, width=1,
                                       command=self.input_0)
        self.qingsheng_button.place(x=220, y=450)
        self.window.mainloop()

    def pinyin_query(self):
        pinyin_text = self.text_entry.get()
        for i in range(len(pinyin_text)):
            if pinyin_text[i] == 'ɡ':
                pinyin_text = pinyin_text.replace(pinyin_text[i], 'g')
            if pinyin_text[i] == 'ü':
                if i == 0:
                    pinyin_text = pinyin_text.replace(pinyin_text[i], 'v')
                elif pinyin_text[i-1] == 'l' or pinyin_text[i-1] == 'n':
                    pinyin_text = pinyin_text.replace(pinyin_text[i], 'v')
                elif pinyin_text[i-1] == 'j' or \
                        pinyin_text[i-1] == 'q' or \
                        pinyin_text[i-1] == 'x' or \
                        pinyin_text[i-1] == 'y':
                    pinyin_text = pinyin_text.replace(pinyin_text[i], 'u')
        if pinyin_text in self.pinyin:
            box.showinfo('提示', '您所输入的音节是汉语中的合法音节。')
        else:
            box.showerror('提示', '您所输入的音节不是汉语中的合法音节。\n您可以检查您的输入然后重试。')
        self.clear()

    def clear(self):
        self.text_entry.delete(0, END)

    def get_help(self):
        pass

    def exit_it(self):
        is_quit = box.askokcancel('提示', '您确定要退出吗？')
        if is_quit:
            self.window.destroy()

    def input_b(self):
        self.text_entry.insert(END, 'b')

    def input_p(self):
        self.text_entry.insert(END, 'p')

    def input_m(self):
        self.text_entry.insert(END, 'm')

    def input_f(self):
        self.text_entry.insert(END, 'f')

    def input_d(self):
        self.text_entry.insert(END, 'd')

    def input_t(self):
        self.text_entry.insert(END, 't')

    def input_n(self):
        self.text_entry.insert(END, 'n')

    def input_l(self):
        self.text_entry.insert(END, 'l')

    def input_g(self):
        self.text_entry.insert(END, 'ɡ')

    def input_k(self):
        self.text_entry.insert(END, 'k')

    def input_h(self):
        self.text_entry.insert(END, 'h')

    def input_j(self):
        self.text_entry.insert(END, 'j')

    def input_q(self):
        self.text_entry.insert(END, 'q')

    def input_x(self):
        self.text_entry.insert(END, 'x')

    def input_z(self):
        self.text_entry.insert(END, 'z')

    def input_c(self):
        self.text_entry.insert(END, 'c')

    def input_s(self):
        self.text_entry.insert(END, 's')

    def input_zh(self):
        self.text_entry.insert(END, 'zh')

    def input_ch(self):
        self.text_entry.insert(END, 'ch')

    def input_sh(self):
        self.text_entry.insert(END, 'sh')

    def input_r(self):
        self.text_entry.insert(END, 'r')

    def input_y(self):
        self.text_entry.insert(END, 'y')

    def input_w(self):
        self.text_entry.insert(END, 'w')

    def input_a(self):
        self.text_entry.insert(END, 'a')

    def input_o(self):
        self.text_entry.insert(END, 'o')

    def input_e(self):
        self.text_entry.insert(END, 'e')

    def input_i(self):
        self.text_entry.insert(END, 'i')

    def input_u(self):
        self.text_entry.insert(END, 'u')

    def input_v(self):
        self.text_entry.insert(END, 'ü')

    def input_ai(self):
        self.text_entry.insert(END, 'ai')

    def input_ei(self):
        self.text_entry.insert(END, 'ei')

    def input_ui(self):
        self.text_entry.insert(END, 'ui')

    def input_ao(self):
        self.text_entry.insert(END, 'ao')

    def input_ou(self):
        self.text_entry.insert(END, 'ou')

    def input_iu(self):
        self.text_entry.insert(END, 'iu')

    def input_ie(self):
        self.text_entry.insert(END, 'ie')

    def input_ve(self):
        self.text_entry.insert(END, 'üe')

    def input_er(self):
        self.text_entry.insert(END, 'er')

    def input_an(self):
        self.text_entry.insert(END, 'an')

    def input_en(self):
        self.text_entry.insert(END, 'en')

    def input_in(self):
        self.text_entry.insert(END, 'in')

    def input_un(self):
        self.text_entry.insert(END, 'un')

    def input_vn(self):
        self.text_entry.insert(END, 'ün')

    def input_ang(self):
        self.text_entry.insert(END, 'anɡ')

    def input_eng(self):
        self.text_entry.insert(END, 'enɡ')

    def input_ing(self):
        self.text_entry.insert(END, 'inɡ')

    def input_ong(self):
        self.text_entry.insert(END, 'onɡ')

    def input_1(self):
        self.text_entry.insert(END, '1')

    def input_2(self):
        self.text_entry.insert(END, '2')

    def input_3(self):
        self.text_entry.insert(END, '3')

    def input_4(self):
        self.text_entry.insert(END, '4')

    def input_0(self):
        self.text_entry.insert(END, '0')


if __name__ == '__main__':
    w = Window()
