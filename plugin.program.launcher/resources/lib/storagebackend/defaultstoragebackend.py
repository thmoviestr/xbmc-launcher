from os.path import join as pjoin
import os
import re

class AbstractStorageBackend(object):

    '''set up the backend'''
    def __init__(self, plugin_data_path=None):
        self.plugin_data_path = plugin_data_path

    '''save launchers to whatever source backend uses'''
    def save_launchers(self, launchers):
        pass

    '''return a dict containing all launchers'''
    def get_launchers(self):
        pass


class XMLStorageBackend(AbstractStorageBackend):

    def __init__(self,plugin_data_path=None):
        super(XMLStorageBackend, self).__init__(plugin_data_path)
        self.xml_file = pjoin(self.plugin_data_path, "launchers.xml")
        self.launchers = None

    def save_launchers(self, launchers):
        print "SAVING LAUNCHER FILE"
        # make settings directory if doesn't exists
        if (not os.path.isdir(os.path.dirname(self.xml_file))):
            os.makedirs(os.path.dirname(self.xml_file));

        usock = open(self.xml_file, 'w' )
        usock.write("<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\"?>\n")
        usock.write("<launchers>\n")
        for launcherIndex in launchers:
            launcher = launchers[launcherIndex]
            usock.write("\t<launcher>\n")
            usock.write("\t\t<name>"+launcher["name"]+"</name>\n")
            usock.write("\t\t<application>"+launcher["application"]+"</application>\n")
            usock.write("\t\t<args>"+launcher["args"]+"</args>\n")
            usock.write("\t\t<rompath>"+launcher["rompath"]+"</rompath>\n")
            usock.write("\t\t<romext>"+launcher["romext"]+"</romext>\n")
            usock.write("\t\t<thumb>"+launcher["thumb"]+"</thumb>\n")
            usock.write("\t\t<wait>"+launcher["wait"]+"</wait>\n")
            usock.write("\t\t<roms>\n")
            for romIndex in launcher["roms"]:
                romdata = launcher["roms"][romIndex]
                usock.write("\t\t\t<rom>\n")
                usock.write("\t\t\t\t<name>"+romdata["name"]+"</name>\n")
                usock.write("\t\t\t\t<filename>"+romdata["filename"]+"</filename>\n")
                usock.write("\t\t\t\t<thumb>"+romdata["thumb"]+"</thumb>\n")
                usock.write("\t\t\t</rom>\n")
            usock.write("\t\t</roms>\n")
            usock.write("\t</launcher>\n")
        usock.write("</launchers>")
        usock.close()

    def get_launchers(self):
        if not self.launchers:
            self._load_launchers()
        return self.launchers

    def _read_xml_source(self):
        try:
            usock = open(self.xml_file, 'r' )
            xml_source = usock.read()
            usock.close()
            return xml_source.replace("\n","").replace("\r","")
        except:
            print "%s: %s not found, this is probably the first run" % (
                    self.__class__.__name__, self.xml_file)
            return False

    def _load_launchers(self):
        launchers = {}
        xmlSource = self._read_xml_source()
        if not xmlSource:
            return None
        self.launchers = {} 
        launchers = re.findall( "<launcher>(.*?)</launcher>", xmlSource )
        print "Launcher: found %d launchers" % ( len(launchers) )
        for launcher in launchers:
            name = re.findall( "<name>(.*?)</name>", launcher )
            application = re.findall( "<application>(.*?)</application>", launcher )
            args = re.findall( "<args>(.*?)</args>", launcher )
            rompath = re.findall( "<rompath>(.*?)</rompath>", launcher )
            romext = re.findall( "<romext>(.*?)</romext>", launcher )
            thumb = re.findall( "<thumb>(.*?)</thumb>", launcher )
            wait = re.findall( "<wait>(.*?)</wait>", launcher )
            romsxml = re.findall( "<rom>(.*?)</rom>", launcher )

            if len(name) > 0 : name = name[0]
            else: name = "unknown"

            if len(application) > 0 : application = application[0]
            else: application = ""

            if len(args) > 0 : args = args[0]
            else: args = ""

            if len(rompath) > 0 : rompath = rompath[0]
            else: rompath = ""

            if len(romext) > 0: romext = romext[0]
            else: romext = ""

            if len(thumb) > 0: thumb = thumb[0]
            else: thumb = ""

            if len(wait) > 0: wait = wait[0]
            else: wait = ""
            
            roms = {}
            for rom in romsxml:
                romname = re.findall( "<name>(.*?)</name>", rom )
                romfilename = re.findall( "<filename>(.*?)</filename>", rom )
                romthumb = re.findall( "<thumb>(.*?)</thumb>", rom )

                if len(romname) > 0 : romname = romname[0]
                else: romname = "unknown"

                if len(romfilename) > 0 : romfilename = romfilename[0]
                else: romfilename = ""

                if len(romthumb) > 0 : romthumb = romthumb[0]
                else: romthumb = ""

                # prepare rom object data
                romdata = {}
                romdata["name"] = romname
                romdata["filename"] = romfilename
                romdata["thumb"] = romthumb

                # add rom to the roms list (using name as index)
                roms[romname] = romdata

            # prepare launcher object data
            launcherdata = {}
            launcherdata["name"] = name
            launcherdata["application"] = application
            launcherdata["args"] = args
            launcherdata["rompath"] = rompath
            launcherdata["romext"] = romext
            launcherdata["thumb"] = thumb
            launcherdata["wait"] = wait
            launcherdata["roms"] = roms

            # add launcher to the launchers list (using name as index)
            self.launchers[name] = launcherdata
