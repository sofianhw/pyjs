
class Video(Media):

    def __init__(self, src=None, **kwargs):
        print "create object"
        obj = DOM.createElement("OBJECT")
        DOM.setAttribute(obj, "type", "application/x-mplayer2")
        #DOM.setAttribute(obj, "type", "application/x-oleobject")
        #DOM.setAttribute(obj, "classid",
        #                        "CLSID:22D6F312-B0F6-11D0-94AB-0080C74C7E95")
        print "set element"
        self.setElement(obj)

        print "widget init"
        Media.__init__(self, **kwargs)

        print "setSrc"
        if src:
            self.setSrc(src)

    def setSrc(self, src):
        print "setSrc", src
        self.srcparam = DOM.createElement("PARAM")
        DOM.setAttribute(self.srcparam, "name", "FileName")
        DOM.setAttribute(self.srcparam, "VALUE", src)
        obj.appendChild(self.srcparam)

    def setControls(self, controls):
        print "setControls", controls
        self.ctrlparam = DOM.createElement("PARAM")
        DOM.setAttribute(self.ctrlparam, "name", "ShowControls")
        DOM.setBooleanAttribute(self.ctrlparam, "VALUE",
            controls and "true" or "false")
        obj.appendChild(self.ctrlparam)

    def setStatusbar(self, statusbar):
        print "setstatus", statusbar
        self.statparam = DOM.createElement("PARAM")
        DOM.setAttribute(self.statparam, "name", "ShowStatusBar")
        DOM.setBooleanAttribute(self.statparam, "VALUE",
            statusbar and "true" or "false")
        obj.appendChild(self.statparam)

    def setLoop(self, autorewind):
        print "autorewind", autorewind
        self.loopparam = DOM.createElement("PARAM")
        DOM.setAttribute(self.loopparam, "name", "autorewind")
        DOM.setBooleanAttribute(self.loopparam, "VALUE", 
            autorewind and "true" or "false")
        obj.appendChild(self.loopparam)

    def setAutoplay(self, autostart):
        print "autoplay", autostart
        self.playparam = DOM.createElement("PARAM")
        DOM.setAttribute(self.playparam, "name", "autostart")
        DOM.setBooleanAttribute(self.playparam, "VALUE", 
            autostart and "true" or "false")
        obj.appendChild(self.playparam)

