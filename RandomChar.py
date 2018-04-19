#!/usr/bin/env python
# _*_coding:utf-8_*_

#author:Doctor,2017,12,13

import random
import wx
import string
from UIDemo import RandomCharwxUI

Logger = "RadnomChar："

class RandomChar(RandomCharwxUI):
    def __init__(self,parent,title):
        super(RandomChar,self).__init__(parent,title = title)

        #字符串集
        # self.number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # 使用string 模块替代
        self.number = list(string.digits)
        self.chinese = ['你','好','世','界']
        # self.character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        #使用string 模块替代
        self.character = list(string.letters)
        self.symbol = list(string.punctuation)
        self.totalstr = self.character
        self.reStr = ""
        self.total = 0

    def onChecked(self,evnet):
        obj = evnet.GetEventObject()
        if self.single_check.IsChecked():
            self.china_check.SetValue(False)
            self.number_check.SetValue(False)
            self.symbol_check.SetValue(False)
            self.totalstr = self.character[random.randint(0, len(self.character) - 1)]
        elif self.china_check.IsChecked() and not self.number_check.IsChecked() and not self.symbol_check.IsChecked():
            self.totalstr = self.character + self.chinese
        elif self.number_check.IsChecked() and not self.china_check.IsChecked() and not self.symbol_check.IsChecked():
            self.totalstr = self.character + self.number
        elif self.symbol_check.IsChecked() and not self.china_check.IsChecked() and not self.number_check.IsChecked():
            self.totalstr = self.character + self.symbol
        elif self.china_check.IsChecked() and self.number_check.IsChecked() and not self.symbol_check.IsChecked():
            self.totalstr = self.character + self.chinese + self.number
        elif self.symbol_check.IsChecked() and self.number_check.IsChecked() and not self.china_check.IsChecked():
            self.totalstr = self.character + self.symbol + self.number
        elif self.symbol_check.IsChecked() and self.china_check.IsChecked() and not self.number_check.IsChecked():
            self.totalstr = self.character + self.symbol + self.chinese
        elif self.china_check.IsChecked() and self.number_check.IsChecked() and self.symbol_check.IsChecked():
            self.totalstr = self.character + self.number + self.chinese + self.symbol
        else:
            self.totalstr = self.character

    def onKeyTyped(self,event):
        obj = event.GetEventObject()
        dlg = wx.MessageDialog(self, "请输入整数", "类型错误", wx.OK)
        try:
            self.total = int(obj.GetValue())
        except ValueError,e:
            dlg.ShowModal()
            self.total = 0
        dlg.Destroy()

    def onClicked(self,event):
        self.onChecked(event)
        self.reStr = self.getRandomString(self.total,self.totalstr)
        self.text1.SetValue(self.reStr)
        self.statusbar.SetStatusText("字符长度：" + str(len(self.text1.GetValue())),0)

    def getRandomString(self,total,totalstr):
        temp = ''
        for index in range(total):
            temp += totalstr[random.randint(0, len(totalstr) - 1)]
        return temp

    def onKeyTypedIn(self,event):
        obj = event.GetEventObject()
        self.statusbar.SetStatusText("字符长度：" + str(len(self.text1.GetValue())),0)
        if self.textctrl.GetValue() == '':
            return
        self.statusbar.SetStatusText("增减长度：" + str(len(self.text1.GetValue())-int(self.textctrl.GetValue())),1)

if __name__ == '__main__':
    app = wx.App()
    fr = RandomChar(None,"字符串生成器")
    app.MainLoop()