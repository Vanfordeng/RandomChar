#!usr/bin/env python
# _*_coding:utf-8_*_

import wx
import win32api

class RandomCharwxUI(wx.Frame):
    def __init__(self,parent,title):
        super(RandomCharwxUI,self).__init__(parent,title = title,size=(800,600))
        exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
        icon = wx.Icon(exeName,wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        self.InitUI()

    def InitUI(self):

        panel = wx.Panel(self)
        #-vbox
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        #1.设置静态文本
        self.m_text = wx.StaticText(panel,-1,style = wx.ALIGN_LEFT)
        font = wx.Font(18, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.m_text.SetFont(font)
        self.m_text.SetLabel("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        self.vbox.Add(self.m_text,0,wx.ALIGN_LEFT)

        #2.设置CheckBox
        self.china_check = wx.CheckBox(panel,label="含中文",pos=(10,10))
        self.single_check = wx.CheckBox(panel,label="单字符",pos=(10,40))
        self.number_check = wx.CheckBox(panel,label="含数字",pos=(10,70))
        self.symbol_check = wx.CheckBox(panel,label="含字符",pos=(10,100))

        self.vbox1 = wx.BoxSizer(wx.VERTICAL)
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.vbox1.Add((0, 10))
        self.vbox1.Add(self.china_check, 0,wx.ALIGN_LEFT)
        self.vbox1.Add((0, 10))
        self.vbox1.Add(self.single_check, 0,wx.ALIGN_LEFT)
        self.vbox1.Add((0, 10))
        self.vbox1.Add(self.number_check, 0,wx.ALIGN_LEFT)
        self.vbox1.Add((0, 10))
        self.vbox1.Add(self.symbol_check, 0,wx.ALIGN_LEFT)
        self.hbox1.Add(10,0)
        self.hbox1.Add(self.vbox1,1,wx.EXPAND)
        self.vbox.Add(self.hbox1)

        #3.设置Button
        #-hbox
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.m_text1 = wx.StaticText(panel,-1,"生成字符长度  ")
        self.textctrl = wx.TextCtrl(panel)

        self.m_button = wx.Button(panel,label = "生成")
        self.vbox.Add((0, 10))
        self.hbox.Add(10,0)
        self.hbox.Add(self.m_text1,0,wx.ALIGN_LEFT)
        self.hbox.Add(self.textctrl,0,wx.ALIGN_LEFT)
        self.hbox.Add(self.m_button,0,wx.ALIGN_LEFT)
        self.vbox.Add(self.hbox)

        #4.设置TextCtrl
        # self.m_text2 = wx.StaticText(panel, -1, "字符串")
        # self.vbox.Add((0, 10))
        # self.vbox.Add(self.m_text2)

        self.vbox1 = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(panel, size=(200, 100), style=wx.TE_MULTILINE)
        self.vbox.Add((0, 10))
        self.vbox1.Add(self.text1,1,wx.EXPAND | wx.ALIGN_CENTER)

        self.vbox.Add(self.vbox1,1,wx.EXPAND)
        #状态栏
        self.statusbar = wx.StatusBar(panel,wx.ID_ANY,name = "状态栏")
        self.statusbar.SetFieldsCount(3)
        # self.statusbar.SetStatusWidths([-1, -2, -3])
        self.vbox.Add(self.statusbar,0,wx.EXPAND)

        #绑定事件
        self.Bind(wx.EVT_CHECKBOX, self.onChecked)
        self.textctrl.Bind(wx.EVT_TEXT, self.onKeyTyped)
        self.m_button.Bind(wx.EVT_BUTTON,self.onClicked)
        self.text1.Bind(wx.EVT_TEXT,self.onKeyTypedIn)

        panel.SetSizer(self.vbox)
        self.Centre()
        self.Show()

    def onChecked(self,evnet):
        pass
    def onClicked(self,event):
        pass
    def onKeyTyped(self,event):
        pass
    def onKeyTypedIn(self,event):
        pass

if __name__ == '__main__':
    app = wx.App()
    RandomCharwxUI(None,"字符串生成器")
    app.MainLoop()