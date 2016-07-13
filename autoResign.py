from optparse import OptionParser
import subprocess

#configuration for iOS build setting
CODE_SIGN_IDENTITY = "iPhone Distribution: Hangzhou Ouer Technology Co., Ltd"

def autoResign(file):

    unzipCmd = 'unzip %s.ipa' %(file)
    process = subprocess.Popen(unzipCmd, shell = True)
    process.wait()
    cpCmd = 'cp embedded.mobileprovision Payload/%s.app' %(file)
    process = subprocess.Popen(cpCmd, shell=True)
    process.wait()
    resignCmd = 'codesign -f -s "%s" --entitlements entitlements.plist Payload/%s.app' %(CODE_SIGN_IDENTITY,file)
    process = subprocess.Popen(resignCmd, shell=True)
    process.wait()
    zipCmd = 'zip -r %s_Resign.ipa Payload' %(file)
    process = subprocess.Popen(zipCmd, shell=True)
    process.wait()


def main():
	
    parser = OptionParser()
    parser.add_option("-f","--file", help="the ipa file",metavar="file.ipa")
    (options, args) = parser.parse_args()
    file = options.file
    autoResign(file)


if __name__ == '__main__':
	main()