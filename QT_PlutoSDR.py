#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Qt Plutosdr
# Generated: Thu Jan 28 19:45:36 2021
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import iio
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class QT_PlutoSDR(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Qt Plutosdr")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 4000000
        self.rf_gain = rf_gain = 20
        self.freq = freq = 2412000000
        self.filename = filename = '/home/ilias/Desktop/HMMY/9o/Advanced_Nets/FINAL/FINAL/new.txt'
        self.bw = bw = 2400000

        ##################################################
        # Blocks
        ##################################################
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label='freq',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=2400000000,
        	maximum=2490000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        _rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	label='rf_gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rf_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rf_gain_sizer)
        self.pluto_source_0 = iio.pluto_source("ip:192.168.2.1", freq, samp_rate, samp_rate, 0x8000, True, True, True, "manual", 64.0, "", True)
        self.fft_vxx_1 = fft.fft_vcc(1024, True, (window.blackmanharris(1024)), True, 1)
        _bw_sizer = wx.BoxSizer(wx.VERTICAL)
        self._bw_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_bw_sizer,
        	value=self.bw,
        	callback=self.set_bw,
        	label='bw',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._bw_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_bw_sizer,
        	value=self.bw,
        	callback=self.set_bw,
        	minimum=1000000,
        	maximum=3000000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_bw_sizer)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1024, 0)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_float, 50, 1024, 0)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, filename, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_divide_xx_0 = blocks.divide_cc(1024)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1024)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 1024)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_stream_to_vector_1, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_1, 0))    
        self.connect((self.blocks_stream_to_vector_1, 0), (self.blocks_divide_xx_0, 1))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_keep_m_in_n_0, 0))    
        self.connect((self.fft_vxx_1, 0), (self.blocks_divide_xx_0, 0))    
        self.connect((self.pluto_source_0, 0), (self.blocks_stream_to_vector_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.pluto_source_0.set_params(self.freq, self.samp_rate, self.samp_rate, True, True, True, "manual", 64.0, "", True)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self._rf_gain_slider.set_value(self.rf_gain)
        self._rf_gain_text_box.set_value(self.rf_gain)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.pluto_source_0.set_params(self.freq, self.samp_rate, self.samp_rate, True, True, True, "manual", 64.0, "", True)

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.blocks_file_sink_0.open(self.filename)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self._bw_slider.set_value(self.bw)
        self._bw_text_box.set_value(self.bw)


def main(top_block_cls=QT_PlutoSDR, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
