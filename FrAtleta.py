#-----------------------------------------------------------------------------
# Name:        FrAtleta.py
# Purpose:     
#
# Author:      Valentina Espinosa
#
# Created:     2014/05/10
# RCS-ID:      $Id: FrAtleta.py $
# Copyright:   (c) 2014
# Licence:     <your licence>
#-----------------------------------------------------------------------------
#Boa:Frame:carrera

import wx
import random
import time

def create(parent):
    return carrera(parent)

[wxID_CARRERA, wxID_CARRERABTB, wxID_CARRERABTC, wxID_CARRERABTSALIR, 
 wxID_CARRERABTSIMULAR, wxID_CARRERALINEA, wxID_CARRERALINEB, 
 wxID_CARRERALINEC, wxID_CARRERASTA, wxID_CARRERASTATICLINE1, 
 wxID_CARRERASTGANADOR, wxID_CARRERASTMETA, 
] = [wx.NewId() for _init_ctrls in range(12)]

class carrera(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_CARRERA, name=u'carrera', parent=prnt,
              pos=wx.Point(509, 255), size=wx.Size(341, 196),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Carrera de Atletas')
        self.SetClientSize(wx.Size(333, 165))
        self.SetBackgroundColour(wx.Colour(213, 255, 255))
        self.Center(wx.HORIZONTAL)
        self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Candara'))
        self.SetForegroundColour(wx.Colour(0, 128, 64))

        self.lineA = wx.StaticLine(id=wxID_CARRERALINEA, name=u'lineA',
              parent=self, pos=wx.Point(49, 40), size=wx.Size(0, 10), style=0)

        self.lineB = wx.StaticLine(id=wxID_CARRERALINEB, name=u'lineB',
              parent=self, pos=wx.Point(49, 72), size=wx.Size(0, 10), style=0)

        self.lineC = wx.StaticLine(id=wxID_CARRERALINEC, name=u'lineC',
              parent=self, pos=wx.Point(49, 104), size=wx.Size(0, 10), style=0)

        self.staticLine1 = wx.StaticLine(id=wxID_CARRERASTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(298, 32),
              size=wx.Size(6, 88), style=0)

        self.stMeta = wx.StaticText(id=wxID_CARRERASTMETA, label=u'Meta',
              name=u'stMeta', parent=self, pos=wx.Point(280, 8),
              size=wx.Size(36, 19), style=0)

        self.btsimular = wx.Button(id=wxID_CARRERABTSIMULAR, label=u'Simular',
              name=u'btsimular', parent=self, pos=wx.Point(152, 128),
              size=wx.Size(80, 29), style=0)
        self.btsimular.Bind(wx.EVT_BUTTON, self.OnBtsimularButton,
              id=wxID_CARRERABTSIMULAR)

        self.btSalir = wx.Button(id=wxID_CARRERABTSALIR, label=u'Salir',
              name=u'btSalir', parent=self, pos=wx.Point(240, 128),
              size=wx.Size(80, 29), style=0)
        self.btSalir.Bind(wx.EVT_BUTTON, self.OnBtSalirButton,
              id=wxID_CARRERABTSALIR)

        self.stA = wx.StaticText(id=wxID_CARRERASTA, label=u'A', name=u'stA',
              parent=self, pos=wx.Point(16, 32), size=wx.Size(10, 19), style=0)

        self.btB = wx.StaticText(id=wxID_CARRERABTB, label=u'B', name=u'btB',
              parent=self, pos=wx.Point(16, 64), size=wx.Size(10, 19), style=0)

        self.btC = wx.StaticText(id=wxID_CARRERABTC, label=u'C', name=u'btC',
              parent=self, pos=wx.Point(16, 96), size=wx.Size(9, 19), style=0)

        self.stGanador = wx.StaticText(id=wxID_CARRERASTGANADOR, label=u'',
              name=u'stGanador', parent=self, pos=wx.Point(16, 134),
              size=wx.Size(0, 19), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        event.Skip()

    def OnBtSalirButton(self, event):
        self.Close()
        event.Skip()

    def OnBtsimularButton(self, event):
        a = random.randint(0,231)
        b = random.randint(0,231)
        c = random.randint(0,231)
        while self.lineA.GetSize()<a:
            while self.lineB.GetSize()<b:
                while self.lineC.GetSize()<c:
                    A = self.lineA.GetSize()
                    B = self.lineB.GetSize()
                    C = self.lineC.GetSize()
                    self.lineA.SetSize(wx.Size(A+1,10))
                    self.lineB.SetSize(wx.Size(B+1,10))
                    self.lineC.SetSize(wx.Size(C+1,10))
                    time.sleep(0.01)
        if self.lineA.GetSize():
            if self.lineB.GetSize():
                if self.lineC.GetSize():                      
                        if (a>b and a>c):
                            self.stGanador.SetLabel("El ganador es: A" )
            
                        if (b>c and b>a):
                            self.stGanador.SetLabel("El ganador es: B" )
                
                        if (c>b and c>a):
                            self.stGanador.SetLabel("El ganador es: C" )
        event.Skip()
