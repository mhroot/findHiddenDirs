#!/bin/python3

# mahmoud hamed abd elmajid

# r o o t 9 0 9 0 

from PyQt5 import QtCore, QtGui, QtWidgets
import json
from requests import get , post
from random import choice
from concurrent.futures import ThreadPoolExecutor ,wait, as_completed
import re

class userAgentS():
    def getUserAgint(self):
        userAgesList =["Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20021006 Firefox/21.0",
        "Mozilla/5.0 (Windows NT.6.2; Win64; x64) AppleWebKit/537.20 (KHTML, like Gecko) Chrome/11.0.254.20 Safari/536.34",
        "Mozilla/5.0 (Linux; Android 9; AFTWMST22) AppleWebKit/537.36 (KHTML, like Gecko) Silk/110.6.7 like Chrome/110.0.5481.212 Safari/537.36",
        "Mozilla/5.0 (Windows NT.6.2; Win64; x64) Gecko/20101111 Firefox/22.0",
        "Mozilla/5.0 (Linux; Android 12; TECNO KH6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Mobile Safari/537.36 OPR/74.1.3922.71199",
        "Mozilla/5.0 (Linux; Android 10; Fendy plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G991U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.1.1; EDA70) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.16 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G8850) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.1 Chrome/106.0.5249.126 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 12; tr-tr; Redmi 12C Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.21.1.1-gn",
        "Mozilla/5.0 (Linux; Android 12; XT2175-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 10; ART-L29N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaApp_Android/23.32.1 YaSearchBrowser/23.32.1 BroPP/1.0 SA/3 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; HarmonyOS; TAH-AN00m; HMSCore 6.10.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/13.0.5.302 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 8.1.0; BV5800 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.774.54 Safari/537.36 Edg/88.0.705.63",
        "Mozilla/5.0 (Linux; Android 9; itel W6002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
        "Mozilla/5.0 (Linux; Android 13; SM-A515F; U; en) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Tenta/5.0.5 Build/2862 Safari/537.36",
        ]
        return choice(userAgesList)

class bruteForceDirctories(QtCore.QThread):
    resultReady = QtCore.pyqtSignal(str)
    def __init__(self, url , wList, header,threaders,  parent=None):
        super().__init__(parent)
        self.url = url
        self.wList = wList
        self.stopped = False
        self.headers = header
        self.threaders = threaders
        self.final_Result = []
        self.statusCde = []
        self.finallList = []
    def run(self):    
        dirs = self.wList
        futures = []
        with ThreadPoolExecutor(max_workers=int(self.threaders)) as executor:
            for dirr in dirs:
                futures.append(executor.submit(self.scan,self.url,''.join(dirr.split('\n'))))
            for i in as_completed(futures):
                i = i
    def scan(self, url , theDir):
        if self.headers == None:
            r = get(url+theDir,timeout=10 )
        else:
            r = get(url+theDir,headers=self.headers , timeout=10)
        if r.status_code != 404:
            self.resultReady.emit(f"{url}{theDir} : {r.status_code}")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox.setMaximum(5000)
        self.spinBox.setProperty("value", 50)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.listWidget = QtWidgets.QTextEdit(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Loc"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "~/Desktop"))
        self.label_2.setText(_translate("MainWindow", "List dirs"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "https://www.mahmoud.co"))
        self.label.setText(_translate("MainWindow", "Url"))
        self.pushButton.setText(_translate("MainWindow", "HEADER"))
        self.label_4.setText(_translate("MainWindow", "Threads"))
        self.pushButton_4.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_3.setText(_translate("MainWindow", "START"))
        self.pushButton_2.clicked.connect(self.loadDialog)
        self.pushButton_3.clicked.connect(self.startScanning)
        self.pushButton_4.clicked.connect(self.saveData)
        self.pushButton.clicked.connect(self.viewingHeaderScreen)
        self.header = None
    def saveData(self):
        placeOfrepO = QtWidgets.QFileDialog.getSaveFileName(None,'report path','~/Desktop',filter=".txt")
        if placeOfrepO[0]:
            with open(f"{placeOfrepO[0]}.txt", 'a+') as ff:
                ff.write(self.listWidget.toPlainText())
                ff.close()
            self.showInfo("I've done")
    def viewingHeaderScreen(self):
        header_dialog = viewingHeaderSettings()
        result = header_dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            json_string = "{" + header_dialog.returnData() + "}"
            self.header = json.loads(json_string)
    def loadDialog(self):
        place = QtWidgets.QFileDialog.getOpenFileNames(None, 'Select file','~/Desktop')
        if place[0]:
            self.lineEdit_2.setText(''.join(place[0]))
    def showError(self, f ):
        self.showMSg = QtWidgets.QMessageBox()
        self.showMSg.setIcon(QtWidgets.QMessageBox.Critical)
        self.showMSg.setText(str(f))
        self.showMSg.setWindowTitle('Error')
        self.showMSg.show()
    def showInfo(self , f):
        self.showMSg = QtWidgets.QMessageBox()
        self.showMSg.setIcon(QtWidgets.QMessageBox.Information)
        self.showMSg.setText(str(f))
        self.showMSg.setWindowTitle('Information')
        self.showMSg.show()
    def startScanning(self):
        if re.match(r'https?://w?w?w?\.?[a-z-A-z-A-Z-0-9]+\.?\-?[a-z-0-9]+', self.lineEdit.text()):
            self.listWidget.clear()
            if self.lineEdit_2.text():
                with open(self.lineEdit_2.text() , 'r') as file:
                    dirs = []
                    for i in file.readlines():
                        dirs.append(i.strip())
                    file.close()
            else:
                dirs = [".bash_history",".bashrc",".cache",".config",".cvs",".cvsignore",".forward",".git/HEAD",".history",".hta",".htaccess",".htpasswd",".listing",".listings",".mysql_history",".passwd",".perf",".profile",".rhosts",".sh_history",".ssh",".subversion","0","00","01","02","03","1","10","100","1000","123","2","20","200","2000","2001","2002","2003","2004","2005","3","@","ADM","ADMIN","ADMON","About","AboutUs","Admin","AdminService","AdminTools","Administration","AppsLocalLogin","AppsLogin","BackOffice","Business","C","CPAN","CVS","CVS/Entries","CVS/Repository","CVS/Root","CYBERDOCS","CYBERDOCS25","CYBERDOCS31","ChangeLog","Creatives","D","DB","Database_Administration","Extranet","Games","HTML","Health","Help","Home","INSTALL_admin","Index","Indy_admin","Internet","Log","Logs","Pages","Servlet","Servlets","SiteServer","Sources","Statistics","login","login.php","login.html","login.asp","login.js","Stats","W3SVC","W3SVC1","W3SVC2","W3SVC3","WEB-INF","WS_FTP","WS_FTP.LOG","WebAdmin","Windows","_admin","_pages","a","aa","aaa","abc","about","about-us","about_us","aboutus","abstract","abuse","ac","academic","academics","acatalog","acc","access","access.1","access_db","access_log","access_log.1","accessgranted","account","accounting","action","actions","active","adlogger","adm","admin","admin-admin","admin-console","admin-interface","admin.cgi","admin.php","admin.pl","admin1","admin2","admin3","admin4_account","admin4_colon","admin_","admin_area","admin_banner","admin_c","admin_index","admin_interface","admin_login","admin_logon","admincontrol","admincp","adminhelp","administer","administr8","administracion","administrador","administrat","administratie","administration","administrator","administratoraccounts","administrators","administrivia","adminlogin","adminlogon","adminpanel","adminpro","admins","adminsessions","adminsql","admintools","admissions","admon","adobe","adodb","ads","adserver","adsl","adv","agent","agents","alias","aliases","all","alpha","analog","analyse","announcements","answer","any","apache","api","apis","apl","apm","app","app_browser","app_browsers","app_code","app_data","app_themes","appeal","appeals","append","appl","apple","applet","applets","appliance","appliation","application","application.wadl","applications","apply","apps","apr","ar","archive","archives","arrow","asp","aspadmin","assets","attach","attachments","audit","auth","auto","autologin","automatic","b","back","back-up","backdoor","backend","background","backgrounds","backoffice","backup","backup-db","backup2","backup_migrate","backups","bad_link","bak","bak-up","bakup","balance","balances","ban","bandwidth","bank","banking","banks","banned","banner","banners","base","basic","bass","batch","bd","bdata","bea","bean","beans","beta","bill","billing","bin","binaries","biz","blog","blow","board","boards","body","boot","bot","bots","box","boxes","broken","bsd","bug","bugs","build","builder","bulk","business","button","buttons","buy","buynow","buyproduct","bypass","bz2","c","cPanel","ca","cabinet","cache","cachemgr","cachemgr.cgi","caching","cad","cadmins","cal","calc","calendar","calendar_events","calendar_sports","calendarevents","calendars","calender","call","callback","callee","caller","callin","calling","callout","cam","camel","campaign","campaigns","can","canada","captcha","car","carbuyaction","card","cardinal","cardinalauth","cardinalform","cards","career","careers","carp","carpet","cart","cas","casestudies","cash","cat","catalog","catalog.wci","catalogs","catalogsearch","catalogue","catalyst","catch","categoria","categories","category","catinfo","cc","ccs","cd","cdrom","cert","certenroll","certificate","certificates","certs","cfdocs","cfg","cgi","cgi-bin","cgi-bin/","cgi-bin2","cgi-data","cgi-exe","cgi-home","cgi-image","cgi-local","cgi-perl","cgi-pub","cgi-script","cgi-shl","cgi-sys","cgi-web","cgi-win","cgi_bin","cgibin","cgis","cgiwrap","cgm-web","chan","change","change_password","changed","changelog","changepassword","changepw","changepwd","changes","channel","charge","charges","chart","charts","chat","chats","check","checking","checkout","checkout_iclear","checkoutanon","checkoutreview","checkpoint","checks","child","children","china","chk","choosing","chpasswd","chpwd","chris","chrome","cinema","cisco","class","classes","classic","classified","classifieds","client","clients","cluster","cm","cmd","code","coffee","coke","coldfusion","collapse","collection","college","columnists","columns","com","com1","com2","com3","com_sun_web_ui","comics","comm","command","comment","commerce","commercial","common","component","compose","composer","compressed","comunicator","con","config","configs","configuration","configure","connect","connections","console","constant","constants","contact","contacts","content","contents","control","controller","controlpanel","controls","corba","core","coreg","corp","corpo","corporate","corporation","corrections","count","counter","counters","country","counts","coupon","coupons","coupons1","course","courses","cover","covers","cp","cpadmin","cpanel","cpanel_file","cpath","cpp","cps","cpstyles","cpw","cr","crack","crash","crashes","create","create_account","createaccount","createbutton","creation","creator","credit","creditcards","credits","cron","crs","css","custom-log","custom_log","customavatars","customcode","customer","customer_login","customers","customgroupicons","customize","cute","cutesoft_client","cv","cvs","cxf","cy","cyberworld","cycle_image","cz","czcmdcvt","d","da","daemon","daily","dan","dana-na","dark","dashboard","dat","data","database","database_administration","databases","datafiles","dav","db","db_connect","dba","dbase","dbm","dbms","debug","default","delete","deletion","demo","demos","deny","deploy","deployment","design","details","dev","dev60cgi","devel","develop","developement","developers","development","device","devices","devs","diag","dial","dig","dir","dir-login","dir-prop-base","directory","dirs","disabled","disallow","disclaimer","disclosure","discootra","discount","discovery","discus","discuss","discussion","disdls","disk","dispatch","dispatcher","dms","dns","doc","docs","docs41","docs51","document","documents","down","download","downloads","draft","dragon","dratfs","driver","dump","dumpenv","e","easy","ebriefs","echannel","ecommerce","edit","editor","element","elements","email","employees","en","eng","engine","english","enterprise","env","environ","environment","error","errors","es","esales","esp","established","esupport","etc","event","events","example","examples","exchange","exe","exec","executable","executables","explorer","export","external","extra","extranet","fail","failed","fcgi-bin","feedback","field","file","files","filter","firewall","first","flash","folder","foo","forget","forgot","forgotten","form","format","formhandler","formsend","formupdate","fortune","forum","forums","frame","framework","ftp","fun","function","functions","gadgets","gaestebuch","galeria","galerie","galleries","gallery","gallery2","game","gamercard","games","gaming","ganglia","garbage","gate","gateway","gb","gbook","gccallback","gdform","geeklog","gen","general","generateditems","generator","generic","gentoo","gest","get","global","globalnav","globals","gone","gp","gpapp","granted","graphics","group","groups","guest","guest-tracking","guestbook","guests","gui","guide","guidelines","hack","hacker","handler","hanlder","happening","head","header","headers","health","healthcare","hello","helloworld","help","help_answer","helpdesk","helper","helpers","hi","hidden","hide","high","highslide","hilfe","hipaa","hire","history","hit","hitcount","hits","hold","hole","holiday","holidays","home","homepage","homes","homework","honda","hooks","hop","horde","host","host-manager","hosted","hosting","hosts","hotel","hotels","hour","hourly","house","how","howto","hp","hpwebjetadmin","hr","ht","hta","htbin","htdig","htdoc","htdocs","htm","html","htmlarea","htmls","htpasswd","http","httpd","httpdocs","httpmodules","https","httpuser","hu","human","humans","humor","hyper","ibm","icons","idbc","iis","images","img","import","inbox","inc","include","includes","incoming","incs","incubator","index","index.htm","index.html","index.php","index1","index2","index3","index_01","index_1","index_2","index_adm","index_admin","index_files","index_var_de","indexes","indice","industries","industry","indy_admin","inetpub","inetsrv","inf","info","info.php","information","informer","infos","infraction","ingres","ingress","ini","inicio","init","injection","inline","inlinemod","input","inquire","inquiries","inquiry","insert","install","install-xaff","install-xaom","install-xbench","install-xfcomp","install-xoffers","install-xpconf","install-xrma","install-xsurvey","install.mysql","install.pgsql","installation","installer","installwordpress","instance","instructions","insurance","int","intel","intelligence","inter","interactive","interface","interim","intermediate","intern","internal","international","internet","interview","interviews","intl","intra","intracorp","intranet","intro","introduction","inventory","investors","invitation","invite","invoice","invoices","ioncube","ip","ipc","ipdata","iphone","ipn","ipod","ipp","ips","ips_kernel","ir","iraq","irc","irc-macadmin","is","is-bin","isapi","iso","isp","item","items","j","java","java-sys","javascript","jdbc","job","join","jrun","js","jscript","jscripts","jsession","jsp","jsps","jsr","keep","kept","kernel","key","lab","labs","launch","launchpage","ldap","left","level","lib","libraries","library","libs","link","links","linux","list","load","loader","localstart","lock","lockout","log","logfile","logfiles","logger","logging","login","logo","logon","logout","logs","lost%2Bfound","ls","magic","mail","mailbox","maillist","main","maint","makefile","man","manage","management","manager","manual","map","market","marketing","master","mbo","mdb","me","member","members","memory","menu","message","messages","messaging","meta","metabase","mgr","mine","minimum","mirror","mirrors","misc","mkstats","model","modem","module","modules","monitor","mount","mp3","mp3s","mqseries","mrtg","ms","ms-sql","msql","mssql","music","my","my-sql","mysql","names","navigation","ne","net","netscape","netstat","network","new","news","next","nl","nobody","notes","novell","nul","null","number","object","objects","odbc","of","off","office","ogl","old","oldie","on","online","open","openapp","openfile","operator","oracle","oradata","order","orders","outgoing","output","pad","page","pages","pam","panel","paper","papers","pass","passes","passw","passwd","passwor","password","passwords","path","pdf","perl","perl5","personal","personals","pgsql","phone","php","phpMyAdmin","phpmyadmin","pics","ping","pix","pl","pls","plx","pol","policy","poll","pop","portal","portlet","portlets","post","postgres","power","press","preview","print","printenv","priv","private","privs","process","processform","prod","production","products","professor","profile","program","project","proof","properties","protect","protected","proxy","ps","pub","public","publish","publisher","purchase","purchases","put","pw","pwd","python","query","queue","quote","ramon","random","rank","rcs","readme","redir","redirect","reference","references","reg","reginternal","regional","register","registered","release","remind","reminder","remote","removed","report","reports","requisite","research","reseller","resource","resources","responder","restricted","retail","right","robot","robotics","root","route","router","rpc","rss","rules","run","sales","sample","samples","save","saved","schema","scr","scratc","script","scripts","sdk","search","secret","secrets","section","sections","secure","secured","security","select","sell","send","sendmail","sensepost","sensor","sent","server","server_stats","servers","service","services","servlet","servlets","session","sessions","set","setting","settings","setup","share","shared","shell","shit","shop","shopper","show","showcode","shtml","sign","signature","signin","simple","single","site","sitemap","sites","small","snoop","soap","soapdocs","software","solaris","solutions","somebody","source","sources","spain","spanish","sql","sqladmin","src","srchad","srv","ssi","ssl","staff","start","startpage","stat","statistic","statistics","stats","status","stop","store","story","string","student","stuff","style","stylesheet","stylesheets","submit","submitter","sun","super","support","supported","survey","svc","svn","svr","sw","sys","sysadmin","system","table","tag","tape","tar","target","tech","temp","template","templates","temporal","temps","terminal","test","testing","tests","text","texts","ticket","tmp","today","tool","toolbar","tools","top","topics","tour","tpv","trace","traffic","transactions","transfer","transport","trap","trash","tree","trees","tutorial","uddi","uninstall","unix","up","update","updates","upload","uploader","uploads","usage","user","users","usr","ustats","util","utilities","utility","utils","validation","validatior","vap","var","vb","vbs","vbscript","vbscripts","vfs","view","viewer","views","virtual","visitor","votes","vp","vpg","vpn","vs","vsadmin","vuln","vvc_display","w","w3","w3c","warez","wdav","weather","web","web-beans","web-console","web-inf","web.config","web.xml","web1","web2","web3","web_users","webaccess","webadm","webadmin","webagent","webalizer","webapp","webapps","webb","webbbs","webboard","webcalendar","webcam","webcart","webcast","webcasts","webcgi","webcharts","webchat","webctrl_client","webdata","webdav","webdb","webdist","webedit","webfm_send","webhits","webim","webinar","weblog","weblogic","weblogs","webmail","webmaster","websearch","website","webstat","webstats","webvpn","welcome","wellcome","whatever","whatnot","whois","will","win","win32","windows","wink","winnt","wireless","wishlist","with","wiz","wizard","wizmysqladmin","wml","wolthuis","word","wordpress","work","workarea","workflowtasks","working","workplace","works","workshop","workshops","world","worldpayreturn","worldwide","wow","wp","wp-admin","wp-app","wp-atom","wp-blog-header","wp-comments","wp-commentsrss2","wp-config","wp-content","wp-cron","wp-dbmanager","wp-feed","wp-icludes","wp-images","wp-includes","wp-links-opml","wp-load","wp-login","wp-mail","wp-pass","wp-rdf","wp-register","wp-rss","wp-rss2","wp-settings","wp-signup","wp-syntax","wp-trackback","wpau-backup","wpcallback","wpcontent","wps","wrap","writing","ws","ws-client","ws_ftp","wsdl","wss","wstat","wstats","wt","wtai","wusage","wwhelp","www","www-sql","www1","www2","www3","wwwboard","wwwjoin","wwwlog","wwwroot","wwwstat","wwwstats","wwwthreads","wwwuser","wysiwyg","wysiwygpro","xcache","xfer","xlogin","xml","xmlrpc","xsl","xsql","xyz","zap","zip","zipfiles","zips","zone","zoom","~adm","~admin","~administrator","~bin","~ftp","~guest","~mail","~operator","~root","~sys","~sysadm","~sysadmin","~test","~user","~webmaster","~www",".htaccess",".htpasswd",".meta",".web","access_log","cgi","cgi-bin","cgi-pub","cgi-script","dummy","error","error_log","htdocs","httpd","httpd.pid","icons","index.html","logs","manual","phf","printenv","server-info","server-status","status","test-cgi","tmp","~bin","~ftp","~nobody","photos","photo","image","images","secret","secrets",]            
            if self.header:
                self.thebrute = bruteForceDirctories(self.lineEdit.text(),dirs,None, self.spinBox.text())
            else:
                self.thebrute = bruteForceDirctories(self.lineEdit.text(),dirs,self.header,self.spinBox.text())
            self.thebrute.resultReady.connect(self.on_server_thread_done)
            with ThreadPoolExecutor(max_workers=1) as executor:
                executor.submit(self.thebrute.start)
        else:
            self.showError("Invaled url\nhttps://www.example.com/")
    def on_server_thread_done(self, result):
        self.listWidget.append(result)
    
class viewingHeaderSettings(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 5, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 2, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 2, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 5, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 3, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Headers settings"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Cookie"))
        self.pushButton_5.setText(_translate("Dialog", "Add"))
        self.label_4.setText(_translate("Dialog", "User-Agent"))
        self.label_5.setText(_translate("Dialog", "Accept"))
        self.comboBox.setItemText(0, _translate("Dialog", "Random"))
        self.pushButton_2.setText(_translate("Dialog", "Add"))
        self.pushButton.setText(_translate("Dialog", "Add"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "*/*"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "https://www.example.com"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "https://www.example.com"))
        self.pushButton_4.setText(_translate("Dialog", "Add"))
        self.label.setText(_translate("Dialog", "Host"))
        self.label_2.setText(_translate("Dialog", "Cookie"))
        self.pushButton_3.setText(_translate("Dialog", "Add"))
        self.label_3.setText(_translate("Dialog", "Referer"))
        self.label_6.setText(_translate("Dialog", "other"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "any header"))
        self.label_7.setText(_translate("Dialog", "value"))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "value"))
        self.pushButton_7.setText(_translate("Dialog", "Add"))
        self.pushButton_6.setText(_translate("Dialog", "ADD"))
        self.pushButton.clicked.connect(self.addhost)
        self.pushButton_2.clicked.connect(self.addcooki)
        self.pushButton_3.clicked.connect(self.addrefer)
        self.pushButton_4.clicked.connect(self.adduseragent)
        self.pushButton_5.clicked.connect(self.addacept)
        self.pushButton_7.clicked.connect(self.addother)
        self.pushButton_6.clicked.connect(self.accept)
    
    def addhost(self):
        if self.lineEdit.text():
            self.textEdit.append(f'''"Host": "{self.lineEdit.text()}",''')
    def addcooki(self):
        if self.lineEdit_2.text():
            self.textEdit.append(f'''"Cookie": "{self.lineEdit_2.text()}",''')
    def addrefer(self):
        if self.lineEdit_3.text():
            self.textEdit.append(f'''"Referer": "{self.lineEdit_3.text()}",''')
    def adduseragent(self):
        if self.comboBox.currentText() == 'Random':
            self.textEdit.append(f'''"User-Agent": "{userAgentS().getUserAgint()}",''')
        else:     
            self.textEdit.append(f'''"User-Agent": "{self.comboBox.currentText()}",''')
    def addacept(self):
        if self.comboBox_2.currentText() == '*/*':
            self.textEdit.append(f'''"Accept": "*/*",''')
        else:
            self.textEdit.append(f'''"Accept": "{self.comboBox_2.currentText()}",''')
    def addother(self):
        if self.lineEdit_4.text() and self.lineEdit_5.text():
            self.textEdit.append(f'''"{self.lineEdit_4.text()}": "{self.lineEdit_4.text()}",''')
    def returnData(self):
        return self.textEdit.toPlainText()[:-1]

def global_font_size(app, font_size):
    font = app.font()
    font.setPointSize(font_size)
    app.setFont(font)
style = '''
QMainWindow {
    background-color:#ececec;
}
QPushButton, QToolButton, QCommandLinkButton{
    padding: 0 5px 0 5px;
    border-style: solid;
    border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-right-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-width: 2px;
    border-radius: 8px;
    color: #616161;
    font-weight: bold;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #fbfdfd, stop:0.5 #ffffff, stop:1 #fbfdfd);
}
QPushButton::default, QToolButton::default, QCommandLinkButton::default{
    border: 2px solid transparent;
    color: #FFFFFF;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);
}
QPushButton:hover, QToolButton:hover, QCommandLinkButton:hover{
    color: #3d3d3d;
}
QPushButton:pressed, QToolButton:pressed, QCommandLinkButton:pressed{
    color: #aeaeae;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);
}
QPushButton:disabled, QToolButton:disabled, QCommandLinkButton:disabled{
    color: #616161;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #dce7eb, stop:0.5 #e0e8eb, stop:1 #dee7ec);
}
QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QTimeEdit, QDateEdit, QDateTimeEdit {
    border-width: 2px;
    border-radius: 8px;
    border-style: solid;
    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    background-color: #f4f4f4;
    color: #3d3d3d;
}
QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QTimeEdit:focus, QDateEdit:focus, QDateTimeEdit:focus {
    border-width: 2px;
    border-radius: 8px;
    border-style: solid;
    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);
    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #85b7e3, stop:1 #9ec1db);
    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);
    background-color: #f4f4f4;
    color: #3d3d3d;
}
QLineEdit:disabled, QTextEdit:disabled, QPlainTextEdit:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled, QTimeEdit:disabled, QDateEdit:disabled, QDateTimeEdit:disabled {
    color: #b9b9b9;
}
QSpinBox::up-button, QDoubleSpinBox::up-button, QTimeEdit::up-button, QDateEdit::up-button, QDateTimeEdit::up-button {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    color: #272727;
    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    padding: 3px;
}
QSpinBox::down-button, QDoubleSpinBox::down-button, QTimeEdit::down-button, QDateEdit::down-button, QDateTimeEdit::down-button {
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
    width: 15px;
    color: #272727;
    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-bottom-right-radius: 3px;
    padding: 3px;
}
QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed, QTimeEdit::up-button:pressed, QDateEdit::up-button:pressed, QDateTimeEdit::up-button:pressed {
    color: #aeaeae;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);
}
QSpinBox::down-button:pressed, QDoubleSpinBox::down-button:pressed, QTimeEdit::down-button:pressed, QDateEdit::down-button:pressed, QDateTimeEdit::down-button:pressed {
    color: #aeaeae;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);
}
QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover, QTimeEdit::up-button:hover, QDateEdit::up-button:hover, QDateTimeEdit::up-button:hover {
    color: #FFFFFF;
    border-top-right-radius: 5px;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);
    
}
QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover, QTimeEdit::down-button:hover, QDateEdit::down-button:hover, QDateTimeEdit::down-button:hover {
    color: #FFFFFF;
    border-bottom-right-radius: 5px;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);
}
QSpinBox::up-arrow, QDoubleSpinBox::up-arrow, QTimeEdit::up-arrow, QDateEdit::up-arrow, QDateTimeEdit::up-arrow {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-up-symbolic.symbolic.png);
}
QSpinBox::down-arrow, QDoubleSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow, QDateTimeEdit::down-arrow {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png);
}
QProgressBar {
    max-height: 8px;
    text-align: center;
    font: italic bold 11px;
    color: #3d3d3d;
    border: 1px solid transparent;
    border-radius:4px;
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);
}
QProgressBar::chunk {
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
    border-radius: 4px;
}
QProgressBar:disabled {
    color: #616161;
}
QProgressBar::chunk:disabled {
    background-color: #aeaeae;
}
QSlider::groove {
    border: 1px solid #bbbbbb;
    background-color: #52595d;
    border-radius: 4px;
}
QSlider::groove:horizontal {
    height: 6px;
}
QSlider::groove:vertical {
    width: 6px;
}
QSlider::handle:horizontal {
    background: #ffffff;
    border-style: solid;
    border-width: 1px;
    border-color: rgb(207,207,207);
    width: 12px;
    margin: -5px 0;
    border-radius: 7px;
}
QSlider::handle:vertical {
    background: #ffffff;
    border-style: solid;
    border-width: 1px;
    border-color: rgb(207,207,207);
    height: 12px;
    margin: 0 -5px;
    border-radius: 7px;
}
QSlider::add-page, QSlider::sub-page {
    border: 1px transparent;
    background-color: #52595d;
    border-radius: 4px;
}
QSlider::add-page:horizontal {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);
}
QSlider::sub-page:horizontal {
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
}
QSlider::add-page:vertical {
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
}
QSlider::sub-page:vertical {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);
}
QSlider::add-page:horizontal:disabled, QSlider::sub-page:horizontal:disabled, QSlider::add-page:vertical:disabled, QSlider::sub-page:vertical:disabled {
    background: #b9b9b9;
}
QComboBox, QFontComboBox {
    border-width: 2px;
    border-radius: 8px;
    border-style: solid;
    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    background-color: #f4f4f4;
    color: #272727;
    padding-left: 5px;
}
QComboBox:editable, QComboBox:!editable, QComboBox::drop-down:editable, QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    color: #272727;
    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}
QComboBox::down-arrow {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png); /*Adawaita icon thene*/
}

QComboBox::down-arrow:on {
    top: 1px;
    left: 1px;
}
QComboBox QAbstractItemView {
    border: 1px solid darkgray;
    border-radius: 8px;
    selection-background-color: #dadada;
    selection-color: #272727;
    color: #272727;
    background: white;
}
QLabel, QCheckBox, QRadioButton {
    color: #272727;
}
QCheckBox {
    padding: 2px;
}
QCheckBox:disabled, QRadioButton:disabled {
    color: #808086;
    padding: 2px;
}

QCheckBox:hover {
    border-radius:4px;
    border-style:solid;
    padding-left: 1px;
    padding-right: 1px;
    padding-bottom: 1px;
    padding-top: 1px;
    border-width:1px;
    border-color: transparent;
}
QCheckBox::indicator:checked {
    image: url(/usr/share/icons/Adwaita/16x16/actions/object-select-symbolic.symbolic.png);
    height: 15px;
    width: 15px;
    border-style:solid;
    border-width: 1px;
    border-color: #48a5fd;
    color: #ffffff;
    border-radius: 3px;
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #48a5fd, stop:0.5 #329cfb, stop:1 #48a5fd);
}
QCheckBox::indicator:unchecked {
    
    height: 15px;
    width: 15px;
    border-style:solid;
    border-width: 1px;
    border-color: #48a5fd;
    border-radius: 3px;
    background-color: #fbfdfa;
}
QLCDNumber {
    color: #616161;;
}
QMenuBar {
    background-color: #ececec;
}
QMenuBar::item {
    color: #616161;
    spacing: 3px;
    padding: 1px 4px;
    background-color: #ececec;
}

QMenuBar::item:selected {
    background-color: #dadada;
    color: #3d3d3d;
}
QMenu {
    background-color: #ececec;
}
QMenu::item:selected {
    background-color: #dadada;
    color: #3d3d3d;
}
QMenu::item {
    color: #616161;;
    background-color: #e0e0e0;
}
QTabWidget {
    color:rgb(0,0,0);
    background-color:#000000;
}
QTabWidget::pane {
    border-color: #050a0e;
    background-color: #e0e0e0;
    border-width: 1px;
    border-radius: 4px;
    position: absolute;
    top: -0.5em;
    padding-top: 0.5em;
}

QTabWidget::tab-bar {
    alignment: center;
}

QTabBar::tab {
    border-bottom: 1px solid #c0c0c0;
    padding: 3px;
    color: #272727;
    background-color: #fefefc;
    margin-left:0px;
}
QTabBar::tab:!last {
    border-right: 1px solid;
    border-right-color: #c0c0c0;
    border-bottom-color: #c0c0c0;
}
QTabBar::tab:first {
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
}
QTabBar::tab:last {
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
    color: #FFFFFF;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);
}
QRadioButton::indicator {
    height: 14px;
    width: 14px;
    border-style:solid;
    border-radius:7px;
    border-width: 1px;
}
QRadioButton::indicator:checked {
    border-color: #48a5fd;
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #ffffff, stop:0.5 #ffffff, stop:0.6 #48a5fd, stop:1 #48a5fd);
}
QRadioButton::indicator:!checked {
    border-color: #a9b7c6;
    background-color: #fbfdfa;
}
QStatusBar {
    color:#027f7f;
}

QDial {
    background: #16a085;
}

QToolBox {
    color: #a9b7c6;
    background-color: #222b2e;
}
QToolBox::tab {
    color: #a9b7c6;
    background-color:#222b2e;
}
QToolBox::tab:selected {
    color: #FFFFFF;
    background-color:#222b2e;
}
QScrollArea {
    color: #FFFFFF;
    background-color:#222b2e;
}

QScrollBar:horizontal {
    max-height: 10px;
    border: 1px transparent grey;
    margin: 0px 20px 0px 20px;
    background: transparent;
}
QScrollBar:vertical {
    max-width: 10px;
    border: 1px transparent grey;
    margin: 20px 0px 20px 0px;
    background: transparent;
}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #52595d;
    border-style: transparent;
    border-radius: 4px;
    min-height: 25px;
}
QScrollBar::handle:horizontal:hover, QScrollBar::handle:vertical:hover {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
}
QScrollBar::add-line, QScrollBar::sub-line {
    border: 2px transparent grey;
    border-radius: 4px;
    subcontrol-origin: margin;
    background: #b9b9b9;
}
QScrollBar::add-line:horizontal {
    width: 20px;
    subcontrol-position: right;
}
QScrollBar::add-line:vertical {
    height: 20px;
    subcontrol-position: bottom;
}
QScrollBar::sub-line:horizontal {
    width: 20px;
    subcontrol-position: left;
}
QScrollBar::sub-line:vertical {
    height: 20px;
    subcontrol-position: top;
}
QScrollBar::add-line:vertical:pressed, QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed, QScrollBar::sub-line:vertical:pressed {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}
QScrollBar::up-arrow:vertical {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-up-symbolic.symbolic.png);
}
QScrollBar::down-arrow:vertical {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png);
}
QScrollBar::left-arrow:horizontal {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-previous-symbolic.symbolic.png);
}
QScrollBar::right-arrow:horizontal {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-next-symbolic.symbolic.png);
}
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(style)
    global_font_size(app, 14)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
