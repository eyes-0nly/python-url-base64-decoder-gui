#!/usr/bin/env python3
# coding=<utf-8>

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from coder import Coder


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Decoder")
        self.set_border_width(10)
        self.set_size_request(700, 400)
        self.connect("delete-event", Gtk.main_quit)

        mainbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        self.add(mainbox)

        lbox = Gtk.HBox(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        mainbox.pack_start(lbox, True, True, 0)

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow2 = Gtk.ScrolledWindow()

        rbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        mainbox.pack_start(rbox, False, False, 0)

        label = Gtk.Label("Insert text you want to encode(decode):")
        lbox.pack_start(label, False, False, 0)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("Hello World!")
        scrolledwindow.add(self.textview)
        lbox.pack_start(scrolledwindow, True, True, 0)

        label2 = Gtk.Label("The result of encoding(decoding):")
        lbox.pack_start(label2, False, False, 0)

        self.textview_result = Gtk.TextView()
        self.textbuffer_result = self.textview_result.get_buffer()
        self.textbuffer_result.set_text("")
        scrolledwindow2.add(self.textview_result)
        lbox.pack_start(scrolledwindow2, True, True, 0)

        name_store = Gtk.ListStore(str)
        name_store.append(["base64"])
        name_store.append(["url"])

        self.name_combo = Gtk.ComboBox.new_with_model(name_store)
        self.name_combo.set_active(0)
        renderer_text = Gtk.CellRendererText()
        self.name_combo.pack_start(renderer_text, True)
        self.name_combo.add_attribute(renderer_text, "text", 0)
        rbox.pack_start(self.name_combo, False, False, 0)

        self.button_encode = Gtk.Button(label="Encode")
        self.button_encode.connect("clicked", self.encode_clicked)

        self.button_decode = Gtk.Button(label="Decode")
        self.button_decode.connect("clicked", self.decode_clicked)

        rbox.pack_start(self.button_encode, False, False, 0)
        rbox.pack_start(self.button_decode, False, False, 0)

        separator = Gtk.HSeparator()
        rbox.pack_start(separator, False, True, 15)
        separator.show()

        self.button_image_encode = Gtk.Button("Encode image to base64")
        self.button_image_encode.connect("clicked", self.choose_image_clicked)
        rbox.pack_start(self.button_image_encode, False, False, 0)

        check_dataurl = Gtk.CheckButton("DataURL")
        check_dataurl.connect("toggled", self.on_dataurl_toggled)
        rbox.pack_start(check_dataurl, False, False, 0)
        self.dataurl = False

        inbox = Gtk.HBox(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        rbox.pack_start(inbox, True, True, 0)

        button_close = Gtk.Button.new_with_mnemonic("_Close")
        button_close.connect("clicked", self.on_close_clicked)
        inbox.pack_end(button_close, False, True, 0)

    def on_close_clicked(self, button):
        Gtk.main_quit()

    def on_dataurl_toggled(self, button):
        if button.get_active():
            self.dataurl = True
        else:
            self.dataurl = False

    def encode_clicked(self, widget):
        enc = self.name_combo.get_active()
        if enc == 1:
            start = self.textbuffer.get_start_iter()
            end = self.textbuffer.get_end_iter()
            string = self.textbuffer.get_text(start, end, True)
            coder = Coder().url_encode(string)
            self.textbuffer_result.set_text(coder)
        elif enc == 0:
            start = self.textbuffer.get_start_iter()
            end = self.textbuffer.get_end_iter()
            string = self.textbuffer.get_text(start, end, True)
            coder = Coder().base64_encode(string)
            self.textbuffer_result.set_text(coder)

    def decode_clicked(self, widget):
        enc = self.name_combo.get_active()
        if enc == 1:
            start = self.textbuffer.get_start_iter()
            end = self.textbuffer.get_end_iter()
            string = self.textbuffer.get_text(start, end, True)
            coder = Coder().url_decode(string)
            self.textbuffer_result.set_text(coder)
        elif enc == 0:
            start = self.textbuffer.get_start_iter()
            end = self.textbuffer.get_end_iter()
            string = self.textbuffer.get_text(start, end, True)
            coder = Coder().base64_decode(string)
            self.textbuffer_result.set_text(coder)

    def choose_image_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose an image", self,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL,
                                        Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN,
                                        Gtk.ResponseType.OK))

        self.add_filters(dialog)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            filename = dialog.get_filename()
            coder = Coder().image_base64_encode(filename, self.dataurl)
            self.textbuffer_result.set_text(coder)
            self.textbuffer.set_text("Image encoded: " + filename)
            self.textbuffer_result.set_text(coder)
        elif response == Gtk.ResponseType.CANCEL:
            self.textbuffer.set_text("Canceled")
        dialog.destroy()

    def add_filters(self, dialog):
        filter_images = Gtk.FileFilter()
        filter_images.set_name("Images")
        filter_images.add_mime_type("image/png")
        filter_images.add_mime_type("image/jpeg")
        filter_images.add_mime_type("image/gif")
        filter_images.add_pattern("*.png")
        filter_images.add_pattern("*.jpg")
        filter_images.add_pattern("*.gif")
        dialog.add_filter(filter_images)


win = MainWindow()
win.show_all()
Gtk.main()
