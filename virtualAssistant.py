import wolframalpha as wa
import wikipedia as wp
import pyttsx3 # Text to speak
import os
import sys
import wx 

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="NINI")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,label="Hello I am NINI your virtual friend. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show(True)
    def OnEnter(self,event):
        user_input=self.txt.GetValue()
        user_input=user_input.lower()
        engine = pyttsx3.init()
        engine.say(user_input)
        engine.runAndWait()
        try:
            #wolframalpha
            app_id = "*****YOUR wolframalpha ID******"
            client = wa.Client(app_id)
            res = client.query(user_input)
            answer = next(res.results).text
            engine = pyttsx3.init()
            engine.say(answer)
            engine.runAndWait()
            print(answer)
        except:
            #wikipedia
            wp.set_lang("en")
            try:
                print(wp.summary(user_input))
            except wp.exceptions.DisambiguationError as e:
                print(e.options)
engine = pyttsx3.init()
engine.say("I am NiNi, Your Virtual Friend, Ask Me")
engine.runAndWait()
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
del app
