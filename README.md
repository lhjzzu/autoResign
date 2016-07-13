# autoResign
这是一个python格式的自动化重签名ipa包的脚本

# Usage

    -f --file the name of ipa
    即:-f xxx(ipa包的名字)
    
    *****一定要注意*****
    使用脚本的时候，脚本中的CODE_SIGN_IDENTITY = "iPhone Distribution: Hangzhou Ouer Technology Co., Ltd"，CODE_SIGN_IDENTITY对应的企业证书信息，一定要改成自己的企业证书信息。
# prepare

首先阅读[ios打包--ipa包重签(四)](http://www.lhjzzu.com/2016/05/03/ios-ipa-codesign/),做好准备工作


* 一个已经签名的ipa包（例如 Test.ipa）
* 企业发布证书，以及distribution的.mobileprovision文件，命名为embedded
* embedded.mobileprovision的bundle identify可以自定(例如com.ouer.test)
* 创建一个entitlements.plist文件,内容如下


        <dict>
           	<key>application-identifier</key>
       	    <string>7T2277EURS.com.ouer.test</string>
	        <key>com.apple.developer.team-identifier</key>
       	    <string>7T2277EURS</string>
	        <key>get-task-allow</key>
	        <false/>
	        <key>keychain-access-groups</key>
	        <array>
		    <string>7T2277EURS.com.ouer.test</string>
	        </array>
        </dict>


其中`7T2277EURS`为`team-identifier`，`com.ouer.test`为`bundle identify`


# Example
    
    如果你的ipa文件为Test.ipa
    那么进入相应的路径，在终端中执行
    python autoResign.py -f Test
    
    
# Problem

如果第二次执行`python autoResign.py -f Test`命令，会出现 `Archive:  Test.ipa
replace Payload/Test.app/_CodeSignature/CodeResources? [y]es, [n]o, [A]ll, [N]one, [r]ename: `,直接输入A，然后enter即可。