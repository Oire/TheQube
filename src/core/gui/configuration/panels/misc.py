import application
import global_vars
import sys
import wx
import url_shortener
from logger import logger
logging = logger.getChild('config.panels.misc')
from core.gui.configuration import ConfigurationPanel

class MiscPanel (ConfigurationPanel):
 def __init__ (self, *args, **kwargs):
  super(MiscPanel, self).__init__(*args, **kwargs)
  AutoStart_allowed = hasattr(sys, 'frozen') and not global_vars.portable
  self.AutoStart = wx.CheckBox(self, -1, _("Automatically start %s after Windows log on") % application.name)
  self.AskForExit = wx.CheckBox(self, -1, _("Show confirmation dialog before exiting %s") % application.name)
  wx.StaticText(parent=self, label=_("Preferred URL Shortener:"))
  self.shorteners = wx.ComboBox(parent=self, choices=url_shortener.list_services(), style = wx.CB_READONLY)
  self.shorteners.SetSizerProps(expand=True)
  self.sndupKeySizer = wx.BoxSizer(wx.HORIZONTAL)
  self.sndupKeyLabel = wx.StaticText(parent=self, label=_("Your %s API Key (optional):") % "sndup.net")
  self.sndupKey = wx.TextCtrl(parent=self)
  self.sndupKey.SetSizerProps(expand=True)
  self.sndupKeySizer.Add(self.sndupKeyLabel)
  self.sndupKeySizer.Add(self.sndupKey)
  self.sendMessagesWithEnterKey = wx.CheckBox(self, label=_("Send messages with Enter"))
  self.stdKeyHandling = wx.CheckBox(self, label=_("Perform standard actions with Home/End keys"))
  self._first = self.AutoStart if AutoStart_allowed else self.AskForExit
  if not AutoStart_allowed:
   self.AutoStart.Show(False)
  self.finish_setup()

