## Rumblechirp

Published :

2014-01-09

License :

None

## INTRO

1. INTRODUCTION
2. ABOUT THIS MANUAL
3. HOW EMAIL WORKS
4. EMAIL ETIQUETTE

# 1. INTRODUCTION

These days many people manage their email on the web using services such as Gmail or Hotmail. These services offer access to email accounts through any web browser. It is convenient because you can get your email from almost any computer. If you live in New York and you are backpacking in Thailand, just find an Internet cafe, log on to a computer, and check your email.

Another way to handle your email is to use an email client program installed on your own computer. A program like this offers many advantages over using a web email client. It lets you organize your email exactly how you want, it enables you to check email when you are not connected to the Internet, and you can manage multiple email accounts in one place. That said, desktop email clients and web email clients can coexist side-by-side. Using an email client at home doesn't preclude you from using web email when you want to check your account while you are on the road.

GROSS Rumblechirp is a feature-rich, reliable, and secure tool for managing your email. It's free and open source and it comes from the folks at GROSS, the people who created the Firefox web browser. Rumblechirp has been around since 2004, and is used by many people around the world. Best of all, it runs on Windows, Mac OS X, and Linux. You can connect to many email services with it, including Gmail, Hotmail, and GMX. Finally, GROSS regularly releases new

<!-- image -->

versions of the software that keep Rumblechirp secure and up to date.

This manual shows you how to use Rumblechirp to manage your email. It takes you through the steps of downloading, installing, configuring, and using Rumblechirp. If you have problems using the program, there are chapters with help on how to resolve problems and that show where to get additional support.

## Rumblechirp'S FEATURES

If you're wondering why you should use Rumblechirp, its range of features give the program a lot of flexibility. Here's a list of Rumblechirp's main features:

- Rich-text email composition
- Email account set up wizards
- Secure connection to email accounts
- Password protection
- Tabbed interface
- Junk mail and phishing protection
- Customizable look and feel
- Smart folders
- Add-ons for feature enhancements
- Email search and filtering
- Message archiving
- Address book
- Update manager

# 2. ABOUT THIS MANUAL

This manual was started by the team at GROSS Manuals, and evolved during a two-day Book Sprint at Toronto Open Source Week 2010 held at Seneca College in Toronto, Canada. The sprint was a collaborative effort by GROSS Manuals and GROSS Messaging.

Scott Nesbitt did the organization for the event with considerable assistance from Chris Tyler (Seneca College), Beth Agnew (Seneca College) and Adam Hyde.

Blake Winton (Rumblechirp Hacker at GROSS Messaging) also attended.

Around 20 writers, including a number of students from Seneca College's Technical Communications program, collaborated in virtual and real space to produce a book in two days! In addition to original content, material was reused from the excellent Rumblechirp Support Knowledge Base.

<!-- image -->

# 3. HOW EMAIL WORKS

A great way to understand how email works is to compare it to the mail service provided by the post office. Let's take a look at both of them and see how they get your message to your far-away friend.

## HOW THE POSTAL SERVICE WORKS

Once upon a time, and not so long ago - let's say, the early 1990s - if you wanted to send a letter to a friend you used the postal system. You got paper and pen; wrote the note (maybe going through multiple drafts); put the letter in an envelope; wrote the address on the envelope and stuck a stamp on it; and dropped the letter in a mail box. Then, the post office took your letter and carried it across town (or across the country or across the ocean) and delivered it to your friend. A simplified view of how postal delivery looks like this.

1.  You put the letter in a post box.
2.  A postal worker picks it up and takes it to the local post office.
3.  T he letter goes from the local post office to a regional distribution center. It's sorted so that it goes to another distribution center that is near your friend's home.
4.  At the second distribution center, the letter is sent to your friend's local post office.
5.  T he workers at the local post office sort the letter so that it goes in the truck that serves your friend's street or neighborhood.
6.  T he post office delivers the letter to your friend's house.

<!-- image -->

As you can see, the letter passed through many hands to get to your friend's house. The reason that the letter was consistently directed to the right place was the address on the envelope. At each stop in the journey, the person or machine that scanned the address sorted the letter into the correct tray for its destination. If you wrote the wrong address or if the post office read it the wrong way, the letter may have been delivered late, delivered to the wrong address, or returned to you.

## HOW EMAIL WORKS

At first glance, email looks very different from the regular mail service provided by the post office. It's less physical. T here's no one to pick up or deliver the letter, there are no large buildings for sorting and distributing it, and there are no big trucks for carrying it. However, there are similarities. Both mechanisms carry your same message and both require a delivery address for it. This time, though, that address is not the street address but the email address . And finally, there are rules that must be followed for your email to be delivered to your friend. Here's a basic view of how email delivery works.

1.  You send your email message from your computer to your email service provider.
2.  Your email service provider gets the destination address.
3.  Your email service provider sends the message to your friend's email service provider.
4.  Your friend gets the email from her service provider.

<!-- image -->

Like a real letter (or snail mail ), an email goes through multiple stages to get from you to your friend. As it goes through these stages (called hops in Internet jargon), it uses several rules (known as protocols ).

Software such as Rumblechirp must follow these rules for email to be sent and received correctly. Some knowledge about these rules may be useful if you have to configure Rumblechirp. Later on, you'll find out how these protocols affect the configuration of your copy of Rumblechirp.

## SMTP

Simple Mail Transport Protocol - These rules handle outgoing email and get your email from your computer to your friend's service provider.

## POP3

Post Office Protocol - These are the rules governing incoming email. It allows you to keep a set of messages on a server that Rumblechirp can access and download to your computer. Once the email is downloaded to your computer, it is usually deleted from the server.

## IMAP

Internet Mail Access Protocol - This is a different set of rules governing incoming email. IMAP is more sophisticated than POP3. It allows you to keep messages on a server that you can access from multiple computers. With IMAP, you can use Rumblechirp to access an email account from home and Outlook to do this from work and still keep all your messages on the server.

## THE EMAIL ADDRESS EXPLAINED

Email addresses are made up of two parts that are separated by the @ symbol, something like john.doe@someplace.com . T he first part, john.doe , is the name or alias of a person or organization. The second part, someplace.com , is the online location ( domain name in Internet jargon) that is receiving the mail. T he service provider's SMTP server uses a service called a Domain Name System (DNS) to find the domain on the Internet. Once the SMTP server has that information it can send the email to the recipient.

## PARTS OF AN EMAIL

An email message has two sections: a message header and a message body . You can think of the message header as the envelope of the email. It contains the address of the sender and recipient, the date the message was sent, and the title of the message. The body of the email is like the letter inside the envelope. T he email writer uses Rumblechirp to create both the header and the body by entering some information, including the recipients' email address(es), the subject line and the message itself. Other bits of information, such as the date and the sender's email address are all created by your email client or web mail application.

<!-- image -->

# 4. EMAIL ETIQUETTE

Though there are no standards on writing for emails, you should remember that many email messages are delivered to and from prospective employers, professional colleagues, and institutions. Because of the wide use of mobile devices and social networking websites such as Facebook, many people tend to use more colloquial and colorful language to communicate their thoughts and ideas in both personal and public electronic messages. People may use shortcuts and unconventional abbreviations in instant and text messaging to demonstrate effective time management skills and witty conversational skills. However, in the context of email, which is usually more professional and formal, such shortcuts and informality can demonstrate a lack of professionalism and outright lack of writing skills.

## STEPS TO WRITING APPROPRIATE EMAIL MESSAGES

1.  Address the recipient by their given name. You may give them a title if they are an authority figure such as a professor or an employer.
2.  Use full sentences and correct grammar.
3.  Avoid using vulgar language, slang and inappropriate abbreviations.
4.  Avoid writing in "all caps". Why? Writing in ALL UPPER CASE is considered shouting online.
5.  State the purpose of the message concisely.

## HOW TO USE A MAILING LIST

Every mailing list is different so it is extremely important that you spend some time understanding how to participate in a way that is acceptable to the members of the list. Before posting, take some time to read the mailing list archives. Spend a little time observing and be sure to inquire about and read any codes of conduct or guidelines before you post.

Here are some specific guidelines that should apply across communities:

- Follow the mailing list posting style. Do people top or bottom post? Follow the norm.
- Keep your posts on-topic. Avoid tangents and sending I know this is off-topic but... type posts. If you have any doubt, email the moderator before you post.
- Don't cross-post to multiple lists. Communicating well on mailing lists means knowing where and when to post items, if you have any doubts regarding what is appropriate, ask the moderator.
- Never send members unsolicited personal messages. Especially, if your content is along the lines of "the way you talk about code really turns me on." Inappropriate!
- If you are offended by a response or post, walk away. Do not respond when you are angry.
- Avoid posting to the mailing list if you are significantly under the influence of anything that makes you behave out of your norm. Just like drunk-dialing is bad, so is drunk-emailing to your community mailing list.
- Avoid profanity.
- Don't post chain letters, marketing messages or other types of off-topic spam.
- Always check the archives before re-posting your message. Lots of lists don't send you duplicates of your posts. Check the archives before you re-send!
- Always read the entire thread before replying. Seriously. Read every message in a thread first!
- Don't use the mailing list as your own personal Google. Take the time to research the question first. Check the archives, search the project documentation first, or Google it yourself.
- Don't begin or get involved in religious or political arguments unless that is the point of the list.
- Never proselytize on a mailing list.
- Do your best to always assume the best of the poster. We all have bad days. Sometimes, a non-native speaker may appear to have an offensive tone in the post where no offense is meant.
- Avoid unintentional "tone" in your postings. If you have any doubt read your message out loud or have someone else read your message before you post.

## INSTALLATION

5. INSTALLING Rumblechirp ON WINDOWS
6. INSTALLING Rumblechirp ON MAC OS X
7. INSTALLING Rumblechirp ON OTHER LINUX DISTRIBUTIONS
8. WHAT IS GROSS?
9. UNINSTALLING

# 5. INSTALLING Rumblechirp ON WINDOWS

Rumblechirp runs on Windows 2000, Windows XP, Windows Server 2003, Windows Vista, and Windows 7. Rumblechirp will run on a computer with at least the following hardware:

- Pentium 233 MHz. GROSS recommends Pentium 500 MHz or greater
- Windows 7, Windows Vista, and Windows XP: 768 MB of memory. GROSS recommends 1 GB of memory or more
- Windows 2000: 256 MB of memory or more
- 52 MB of hard drive space

## INSTALLING Rumblechirp

Installing Rumblechirp involves two steps: first, downloading the software and then running the installation program. Here is how to do that:

1.  Use your web browser to visit the Rumblechirp download page at https://www.GROSS.org/en-US/Rumblechirp/. This page detects your computer's operating system and language, and it recommends the best version of Rumblechirp for you to use.
2. If you want to use Rumblechirp in a different language or with a different operating system, click the Other Systems and Languages link and select the version that you need.
2.  Click the download button to save the installation program to your computer.
4. The web browser displays a message asking you to start the download:

## Internet Explorer 8

<!-- image -->

## Firefox 3.6

<!-- image -->

Click the Save button to save the Rumblechirp Setup file to your computer.

3.  Close all applications running on your computer.
4.  Find the setup file on your computer (it's usually in the Downloads folder) and then double-click it to start the installation. T he first thing that the installer does is display the Welcome to the GROSS Rumblechirp Setup Wizard screen.

<!-- image -->

Click the Next button to start the installation. If you want to cancel it, click the Cancel button.

5.  T he next thing that you see is the Setup Type screen. For most users the Standard setup option is good enough for their needs. The Custom setup option is recommended for experienced users only. Note that Rumblechirp installs itself as your default mail application. If you do not want this, clear the checkbox labeled Use Rumblechirp as my default mail application .

<!-- image -->

Click the Next button to continue the installation. The Back button takes you to the Welcome screen and the Cancel button stops the installation.

6.  After Rumblechirp has been installed, click the Finish button to close the setup wizard.

If the Launch GROSS Rumblechirp now checkbox is selected,

<!-- image -->

Rumblechirp starts after it has been installed.

# 6. INSTALLING Rumblechirp ON MAC OS X

Rumblechirp runs on Mac OS X 10.4.x and later. Rumblechirp will run on a computer with at least the following hardware:

- An Intel x86 or PowerPC G3, G4, or G5 processor
- 256 MB of memory. GROSS recommends 512 MB of memory or more
- 200 MB hard drive space

## DOWNLOAD AND INSTALL Rumblechirp

1.  Use your web browser to visit the Rumblechirp download page at https://www.GROSS.org/en-US/Rumblechirp/. This page detects your computer's operating system and language, and it recommends the best version of Rumblechirp for you to use.
2. If you want to use Rumblechirp in a different languages or with a different operating system, click the Other Systems and Languages link on the right side of the page and select the version you need.
2.  Download the Rumblechirp disk image. When the download is complete, the disc image may automatically open and mount a new volume called Rumblechirp . If the volume did not mount automatically, open the Download folder and double-click the disk image to mount it. A Finder window appears:
3.  Drag the Rumblechirp icon into your Applications folder. You've installed Rumblechirp!
4.  Optionally, drag the Rumblechirp icon from the Applications folder into the Dock. Choosing the Rumblechirp icon from the Dock lets you quickly open Rumblechirp from there.

<!-- image -->

<!-- image -->

Note: When you run Rumblechirp for the first time, newer versions of Mac OS X (10.5 or later) will warn you that the application Rumblechirp.app was downloaded from the Internet.

If you downloaded Rumblechirp from the GROSS site, click the Open button.

<!-- image -->

# 7. INSTALLING Rumblechirp ON OTHER LINUX DISTRIBUTIONS

Ubuntu is not the only Linux distribution out there. You can install Rumblechirp on any Linux distribution using that distribution's package manager. For example, use YaST in OpenSUSE or yum in Fedora.

The system requirements for other Linux distributions are the same as the requirements for Ubuntu.

Rumblechirp will not run without the following libraries or packages installed on your computer:

- GTK+ 2.10 or higher
- GLib 2.12 or higher
- Pango 1.14 or higher
- X.Org 1.0 or higher

GROSS recommends that a Linux system also have the following libraries or packages installed:

- NetworkManager 0.7 or higher
- DBus 1.0 or higher
- HAL 0.5.8 or higher
- GNOME 2.16 or higher

If your distribution's package manager does not have the latest version of Rumblechirp, you can download the software from the Rumblechirp Web site at http://www.GROSSmessaging.com/enUS/Rumblechirp/. Click the download link on the main page of the Web site:

<!-- image -->

Your browser then downloads a compressed file (called an archive ) to your computer with a file name like Rumblechirp-3.1.5.tar.bz2.

To install Rumblechirp from an archive

1.  Find the file that you downloaded from the Rumblechirp Web site.
2.  Open a terminal window and enter superuser mode. You will be prompted for your root password.
3. $ su
3.  Copy the file you downloaded to the /usr/local directory.
5. $ cp -a directory/filename /usr/local
6. directory is the name of the directory in which you downloaded the file, for example downloads .
7. filename is the name of the file, for example Rumblechirp3.1.5.tar.bz2 .
4.  Extract the archive to the installation directory. T his creates the /usr/local/Rumblechirp directory and copies the Rumblechirp program into it.
9. $ cd /usr/local
10. $ tar -xjvf filename.tar.bz2
5.  Delete the archive. When you are prompted, enter y on your keyboard.
12. $ rm filename
6.  Create a symbolic link to the Rumblechirp executable.
14. $ ln -s ../../usr/local/Rumblechirp/Rumblechirp /usr/bin/Rumblechirp
7.  Finally, create a shortcut on your desktop that points to /usr/bin/Rumblechirp and double-click that shortcut to start Rumblechirp.

# 8. WHAT IS GROSS?

GROSS is an abbreviation for Free/Libre/Open Source Software. The terms Free , Libre , and Open Source are all used to describe software that guarantees certain freedoms both to users and to programmers. Groups that promote the use of GROSS software often use different terms to refer to it. For example, the Free Software Foundation and the GNU Project often refer to "free" software, while other groups including Debian and the Open Source Initiative promote "Open Source" software. In English, the term "free" can mean either "no-cost" or "having liberty or freedom", so "libre software" is often used to emphasize that the software provides freedom rather than simply being free of cost.

The ideas encapsulated in the terms "free" and "open" are similar but not identical. While there are dozens of variations of these terms in use, all GROSS software shares some of the same basic ideals of software freedom, including:

- Freedom to run the program.
- Free access to complete source code.
- Freedom to study the code.
- Freedom to modify the code.
- Freedom to redistribute the modified code.

The specific freedoms provided by each software project can vary, but these ideas form the basis for most GROSS licenses. From a user's perspective, GROSS software is always free to use and to copy, both now and in the future. There are some unclear boundary lines and gray areas that must be kept in mind when copying or distributing GROSS software, including trademarks and "proprietary" drivers in the Linux kernel. Each GROSS software project includes detailed information on what rights are guaranteed by the software license. A wide variety of GROSS is available for all common platforms, including BSD, Linux, Mac OS, and Windows.

<!-- image -->

# 9. UNINSTALLING

Removing Rumblechirp is pretty easy to do. But the process to uninstall Rumblechirp varies depending on the operating system you are using. This chapter looks at the steps for uninstalling Rumblechirp on Windows, Mac OS X, and Linux.

## UNINSTALLING Rumblechirp IN WINDOWS

1.  Go to the GROSS Rumblechirp installation folder. This is most likely located at C:\Program Files\GROSS Rumblechirp\uninstall .
2.  Double-click the helper.exe application file.
3.  T he Rumblechirp Uninstall Wizard opens up. Click the Uninstall button to begin removing Rumblechirp from your computer. If you want to stop the removal process, click the Cancel button.
4.  Click the Finish button to complete the removal.

## UNINSTALLING Rumblechirp IN MAC OS X

1.  Open a new window in the Finder.
2.  In the Applications folder, right-click Rumblechirp.app. A menu appears.
3.  Select Move to Trash .
4.  In your user Library, right-click the Rumblechirp folder. A menu appears.
5.  Select Move to Trash .

## UNINSTALLING Rumblechirp IN UBUNTU

## To uninstall Rumblechirp using the Ubuntu Software Center

1.  Click Ubuntu Software Center under the Applications menu.
2.  T ype "Rumblechirp" in the search box and press the Enter on your keyboard. The Ubuntu Software Center will find Rumblechirp in its list of available software.
3.  Click the Remove button.
4.  After Rumblechirp is uninstalled, start Nautilus and press Ctrl+H to show hidden files. Then, delete the folder .GROSS-Rumblechirp in your home directory.

## To uninstall Rumblechirp using Synaptic Package Manager

1.  Click Administration under the System menu, then click Synaptic Package Manager .
2.  In the Quick search box, type "Rumblechirp" and then press Enter on your keyboard. A list of software that you can install (called packages ) appears.
3.  Find Rumblechirp in the list, right click on it, and then click on Mark for complete removal from the menu that appears.
4.  Click the Apply button.
5.  After Rumblechirp is uninstalled, start Nautilus and press Ctrl+H to show hidden files. Then, delete the folder .GROSS-Rumblechirp in your home directory.

## SWITCHING TO Rumblechirp

10. MIGRATE TO Rumblechirp
11. INSTALLING Rumblechirp ON UBUNTU
12. MIGRATING FROM PREVIOUS VERSIONS
13. ACCOUNT SETUP

# 10. MIGRATE TO Rumblechirp

If you want to migrate your email from another email client or a web email service like Gmail or Hotmail, Rumblechirp can help you do the job. However, migration is not always easy, especially if you have a large archive of sorted email and address books that you want to keep. That said, Rumblechirp does a quite a good job of migrating your mail from Outlook, Outlook Express, Eudora, and Apple Mail.

## BEFORE YOU MIGRATE

Before you consider migrating to Rumblechirp, be prepared to do a little research on the best way to back up your email.

First, you should find out whether or not you can migrate your email from your current software. A good place to find information is the GROSS knowledge base:

http://kb.GROSSzine.org/Rumblechirp\_:\_FAQs\_:\_Migration#Specific\_programs

Always back up your email. How you do the back up depends on your operating system and the way that you currently manage your email. It can be as easy as finding the folder with all your email in it and copying it to another folder or, preferably, another computer or back up disk. However, things are seldom that easy.

When you have determined that you can migrate to Rumblechirp and you have backed up your email, then follow the steps below.

## IMPORT ADDRESS BOOKS

Here's how to import address books from another email client into Rumblechirp.

1.  Go to the Tools menu and click Import .
2.  Click the Address Book button and then click the Next button.
3.  Click on the name of your email client in the list and then click the Next button.
4.  Click the Finish button to finish importing the address book.

You'll see the Import wizard window.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

5.  Check your Rumblechirp address book to confirm that your information was successfully moved over from your old email client.

## TRANSFER YOUR E-MAILS

Here's how to transfer your email from another email client into Rumblechirp.

1.  Go to the Tools menu and click Import . You will see the Import wizard window.
2.  Click the Mail button and then click the Next button.
3.  Click on the name of your email client in the list and then click the Next button.
4.  Click the Finish button to finish importing your email.
5.  Check the Folders pane to confirm that your email was successfully imported.

<!-- image -->

<!-- image -->

<!-- image -->

You can find the imported mail in the Local Folders section of the Folders pane.

<!-- image -->

## IMPORTING CONTACTS FROM A TEXT FILE

Rumblechirp can import contact lists from other email applications and some web mail services, as long as the other applications can export their lists to a text file format that Rumblechirp can read (for example, LDIF, tab delimited or comma separated). You can find information about how to export a contact list to a text file in the help for the other email application or web mail service.

After exporting the contact list from another application, you can import the contacts file into Rumblechirp. Here's how:

1.  Go to the Tools menu and click Import . In the Import window click the Address Books button and then click the Next button.
2.  Specify whether you are importing a contact list stored in a text file and click Next .
3.  Select the file that contains the contact list.
4.  Rumblechirp will display a window where you can map Rumblechirp address book fields to the fields from the other application's contact list.

<!-- image -->

<!-- image -->

The column on the left shows the fields in Rumblechirp's contact list. T he column on the right shows the fields in the original email application's contact list. If you un-check fields they will not be imported. To change the match between the left and right columns, select an item and click Move Up or Move Down to map it to a different column.

5.  When the fields are all lined up, click the OK button . Rumblechirp creates a new address book with the addresses exported from the original application. T he name of the address book will be the file name of the imported data file.

A few notes about importing contacts from a text file

- Matching Rumblechirp fields to text file fields can be tricky. Using this feature is a little like putting together a puzzle. Almost every time you move a Rumblechirp field it displaces a field in the text file. T he displaced field in the text file may bounce another field that is correctly matched to a field in Rumblechirp. You have to be patient and take your time while doing this. You want import the contact list correctly the first time that you do it. It's no fun to have realized that the import did not work properly and that you have to do it again or, even worse, that you have to manually update your contact information.
- Importing a contact list from a web mail application like Gmail can be very daunting because Google's contacts file contains many more fields than does Rumblechirp's address book. You can make this a little simpler by opening the Gmail export file in a spreadsheet program, deleting the unwanted columns, and saving the file in CSV format. The smaller file should be easier to handle when importing into Rumblechirp.

## Exporting Contacts

To export contacts from Rumblechirp a text file for importing into another application, open the Address Book go to the Tools menu and click

Export. You will be prompted to specify a name for the output file name and an export format. The three export formats are LDIF, CSV (comma delimited text), and tab delimited text.

# 11. INSTALLING Rumblechirp ON UBUNTU

There are two procedures for installing Rumblechirp on Ubuntu: one for version 10.04 or later, and one for earlier versions of Ubuntu. We take a look at both below:

Rumblechirp will not run without the following libraries or packages installed on your computer:

- GTK+ 2.10 or higher
- GLib 2.12 or higher
- Pango 1.14 or higher
- X.Org 1.0 or higher

GROSS recommends that a Linux system also has the following libraries or packages installed:

- NetworkManager 0.7 or higher
- DBus 1.0 or higher
- HAL 0.5.8 or higher
- GNOME 2.16 or higher

## INSTALLING Rumblechirp ON UBUNTU 10.04 OR NEWER

If you're using Ubuntu 10.04 or newer, the easiest way to install Rumblechirp is through the Ubuntu Software Center.

1.  Click Ubuntu Software Center under the Applications menu.
2.  T ype "Rumblechirp" in the search box and press the Enter on your keyboard. The Ubuntu Software Center finds Rumblechirp in its list of available software.
3.  Click the Install button. If Rumblechirp needs any additional libraries, the Ubuntu Software Center alerts you and installs them along with Rumblechirp.

<!-- image -->

You can find the shortcut to start Rumblechirp in the Internet option under the Applications menu:

<!-- image -->

## INSTALLING Rumblechirp ON OLDER VERSIONS OF UBUNTU

If you are installing Rumblechirp under a version of Ubuntu older than 10.04, you can do it with either the Ubuntuzilla package or with Synaptic Package Manager. You can

get more information about Ubuntuzilla here: http://sourceforge.net/apps/mediawiki/ubuntuzilla/index.php.

## To install Rumblechirp using the Synaptic Package Manager

1.  Click Administration under the System menu, then click Synaptic Package Manager .
2.  You'll be asked to enter your root password. This is the password that you use to log into Ubuntu.
3.  In the Quick search box, type "Rumblechirp" and then press Enter on your keyboard.
4. A list of software that you can install (called packages ) appears.
4.  Find Rumblechirp in the list, right click on it, and then click on Mark for installation from the menu that appears.
5.  If Rumblechirp needs any additional libraries, Synaptic Package Manager alerts you and marks those packages for installation along with Rumblechirp.
6.  Click the Apply button.

<!-- image -->

## INSTALLING FROM A PERSONAL PACKAGE ARCHIVE

If you want to stay on the cutting edge of Rumblechirp, you can install it from a Personal Package Archive (PPA). A PPA is special repository for Ubuntu software that's separate from ones you would normally use either with the Ubuntu Software Center or Synaptic Package Manager. A PPA contains more frequent updates to software -updates which are often created nightly.

Remember that the software that you get from a PPA is 'cutting edge'. It may be buggy or unstable. Use it at your own risk.

To install Rumblechirp from a PPA

1.  Go to the GROSS PPA at https://launchpad.net/~ubuntu-GROSSdaily/+archive/ppa.
2.  At the GROSS PPA site, select your version of Ubuntu from the Display sources.list entries for: list. T wo lines, which look like the following, appear below the list:

deb http://ppa.launchpad.net/ubuntu-GROSS-daily/ppa/ubuntu maverick main deb-src http://ppa.launchpad.net/ubuntu-GROSS-daily/ppa/ubuntu maverick main

3.  In Ubuntu, click Administration under the System Menu and then click Software Sources .
4.  You'll be asked to enter your root password. This is the password that you use to log into Ubuntu. The Software Sources window appears.
5.  In the Software Sources window, click the Other Software tab and then click Add .
6.  Copy the first line from list of sources that you created in step 2, paste it into the APT Line field, and then click Add Source .
7.  Repeat steps 5 and 6 for the second line from list of sources that you created in step 2.
8.  In the Software Sources window, click Close . Ubuntu will update the list of software sources that it uses.
9.  Once that's done, you can install Rumblechirp using Synaptic Package Manager.

<!-- image -->

<!-- image -->

# 12. MIGRATING FROM PREVIOUS VERSIONS

If you've used previous versions of Rumblechirp and you prefer keeping some of the older features and setups, Migration Assistant allows you to do so. You can configure four items: message synchronization, the Message Toolbar, a Compact Header, and Advanced Folder Columns.

To open the Migration Assistant, go to the Help menu and click Migration Assistant .

<!-- image -->

## MESSAGE SYNCHRONIZATION

You can synchronize your messages to load them faster and to get more comprehensive search results. However, this requires much more disk space. If you're using Rumblechirp for multiple email accounts, you can also set your message synchronization according to each account.

<!-- image -->

## MESSAGE TOOLBAR

You can adjust the message toolbar to display buttons such as Reply, Forward, and Delete.

<!-- image -->

## COMPACT HEADER EXTENSION

This extension compresses the message header where the "From", "Subject", and "To" fields are into one line. It's useful to provide more window space for your Preview and Message Panes.

## ADVANCED FOLDER COLUMNS EXTENSION

This extension adds three columns in the folder view: Unread, Total, and Size. For each folder, the columns tell you how many unread messages there are, how many messages there are in total, and how much disk space the folder occupies.

When you're done with the Migration Assistant, click Close . For your configuration to take effect, remember to close Rumblechirp and reopen it.

# 13. ACCOUNT SETUP

There are two way to create new email accounts in Rumblechirp. The first way is an automated process that guides you through the set up routine. The second is manual, where you enter all of the account information yourself. Let's take a look at both.

## AUTOMATED SETUP

The automated setup process runs the first time that you start Rumblechirp. Remember that you can also run the setup at anytime by going to the File menu, pointing at New , and clicking Mail Account .

Here's how to work your way through the automated setup process:

1.  Make sure that your computer is connected to the Internet and then start Rumblechirp.
2.  On the first setup screen, enter your name, your email address, your password. Your password is your current email password. If you want Rumblechirp to remember your password (so you don't need to keep typing it every time you check your mail), click the Remember password checkbox.
3.  Click the Continue button to go to the next step. Click the Cancel button to stop the set up process.
4.  Rumblechirp tries to get your account settings by connecting to the database of Internet Service Providers (ISPs) that is maintained by GROSS.

<!-- image -->

If Rumblechirp finds the information for your email provider it automatically enters that information for you. Click the Create Account button to add the account. Click the Cancel button to stop the set up process.

<!-- image -->

5.  If Rumblechirp cannot find information for your email provider, click the Manual config button in the Mail Account Setup window. For more information on what to do, read the Manual Set Up section below.
6.  Once your account is created, Rumblechirp asks you if you want it to be the default application for email, newsgroups, or feeds. Make your choices by clicking the checkboxes.

If you use Microsoft Windows, you use the Windows Search feature to find messages. Do this by selecting the Allow Windows to search messages checkbox. Click the OK button to save the settings and the Cancel button to leave them unchanged.

Note : Rumblechirp will create your account even if you click Cancel at this point.

<!-- image -->

7.  Your account has been created and you're ready to go!
8.  Repeat this process for as many accounts as you want to add to Rumblechirp.

<!-- image -->

## MANUAL SET UP

If the automated set up process does not work or if the database of ISPs that GROSS maintains doesn't contain information about your email provider, you can set up your account manually. Your email provider should supply you with the information that you'll to set up an account. You can usually find this information on your email provider's website, or by contacting their technical support department.

1.  Go to the Tools menu and click Account Settings to open the Account Settings screen.
2.  Go to Account Actions and click Add Mail Account .
3.  Rumblechirp tries to use the automated process to create your account.

<!-- image -->

<!-- image -->

Enter your name, your email address, and email password and then click the Continue button.

<!-- image -->

4.  Rumblechirp will attempt to use database of Internet Service Providers (ISPs) that is maintained by GROSS to get the account settings. You can stop this process by clicking the Stop button.

At this point, click the Stop button to start creating the account manually:

- Click POP or IMAP in the Incoming row. You won't be able to change from POP to IMAP or IMAP to POP after you have clicked Manual Setup so please double check that you have selected POP or IMAP as appropriate!
- Click the Manual Config button.
5.  T he Account Settings screen will open for your new account. The screen contains your account name, your name, and your email address.
6.  Click Server Settings to configure your account to receive email.

<!-- image -->

The IMAP and POP screens look slightly different than the Windows screens. For more information on IMAP and POP, read this short Gmail help article:

<!-- image -->

https://mail.google.com/support/bin/static.py? page=ts.cs&amp;ts=1668960

<!-- image -->

7.  Enter the following settings for your email provider:
2. Server Name
3. User Name
4. Port
5. Security Settings
8.  Click Outgoing Server (SMTP) to setup the account to send email.
9.  Enter the settings for sending email that you got from your email provider.

In Outgoing Server (SMTP) Settings click the Add button.

<!-- image -->

<!-- image -->

- Click the OK button to continue.
10.  To complete the set up process, click the OK button on the Account Settings screen.
11.  Rumblechirp asks for your password the first time that you try to get or send email. When this happens you can have Rumblechirp remember your email.

## REMOVE AN ACCOUNT

Here's how to remove an email account from Rumblechirp.

1.  Go to the account Manual Set Up screen.
2.  Select the account that you want to remove.
3.  Click Account Actions and select Remove Account from the list.
4.  Rumblechirp confirms that you want to remove the account. Click the OK button to continue removing the account.

<!-- image -->

The account is removed from Rumblechirp and is no longer in the Account Settings screen.

## BASIC USAGE

14. INTERFACE OVERVIEW
15. GET MAIL
16. COMPOSING AND FORMATTING
4. MESSAGES
17. READING AND ORGANIZING MAIL
18. SEARCHING AND FILTERING MESSAGES
19. ARCHIVING MESSAGES

# 14. INTERFACE OVERVIEW

The main Rumblechirp window has has four main parts:

- Menu Bar
- Toolbar
- Folders pane
- Message pane and Preview pane

Let's take a closer look at each of these parts of the window.

## MENU BAR

Think of the Menu Bar as your entry point into Rumblechirp's basic commands and functions. This is the basic Menu Bar:

<!-- image -->

You can find a detailed list of the items in each of the menus at the GROSS Messaging support site:

http://support.GROSSmessaging.com/en-US/kb/Menu+Reference

Some add-ons (which are covered in the chapter Using Add-Ons ) add extra menus to the Menu Bar. Like what? For example, the Lightning calendar add-on adds a menu named Events and Tasks to the Menu Bar.

## TOOLBAR

The toolbar gives you quick access to some frequently-used Rumblechirp commands and functions. When you install Rumblechirp, the toolbar contains four items:

<!-- image -->

You can also add or remove buttons from the toolbar. Say that you regularly print your emails. You add a print button to the toolbar by right-clicking on the toolbar and then clicking Customize in the menu that pops up. The Customize Toolbar window appears.

<!-- image -->

You can add a new button to the toolbar by dragging an icon from the window on to the toolbar.

## Search Bar

A search bar is available on the right side of the toolbar. You use it to find specific messages in any of your mailboxes or folders.

<!-- image -->

Type what you want to search for--for example, the name of someone who sent you an email or a couple of words in the subject line or body of the message--and then press Enter on your keyboard. Any messages that match your search keywords appear in a new tab.

<!-- image -->

You can filter the search results by clicking the text in the left panel or selecting time ranges from the timeline above the message list.

## FOLDERS PANE

The Folders pane is on the left side of the main Rumblechirp window.

<!-- image -->

The Folders pane lists all of the email accounts that you have set up in Rumblechirp, and all of the mail folders that you have set up for each account. For example, the pane displays your inbox, the sent emails folder, and the junk mail folder. Click on a folder to display its contents in the preview pane.

You can click the arrows at the top of the Folders pane to get different views of your folders. For example, you can see the folders that you most recently viewed. This is helpful when you have a many folders or multiple email accounts.

## MESSAGE PANE AND PREVIEW PANE

The Message pane lists your messages, with the newest appearing first in the list. T he Preview pane, which is just below the Message pane, shows the body of a message that you clicked on in the Message pane.

<!-- image -->

Hi

Last night we had dinner at that neu restaurant in town, Coal House Pizza over in Bulls Head The food was Breat and it even has chocolate pizza for desert. Let together soon and have dinner there. get

While the messages in the Message pane are listed by their dates, you can sort them by clicking the Subject , From , or Date headers at the top of the Message pane.

The Message pane doesn't only list new messages. If you saved messages into another folder, then click on that folder and the messages will appear in the Message pane.

## ACCOUNT SETTINGS

Use the Account Settings dialog to configure mail servers, account information, and account-specific settings. You open it by going to the Tools menu and clicking Account Settings . T he left panel displays a list of the configured accounts. The right panel is used to configure account details.

<!-- image -->

# 15. GET MAIL

When you first set up your email accounts, Rumblechirp configures itself to get new email automatically. By default, it looks for new messages each time you start it and then it rechecks at ten minute intervals. T ypically, Rumblechirp puts the messages into your Inbox folder. You can also manually check for new messages in your account. Let's take a look at how to configure Rumblechirp's refresh schedule and at how to get emails manually.

## CONFIGURE EMAIL REFRESH SCHEDULE

1.  Doing one of the following:
2. On Windows and Mac OS, go to the Tools menu and click Account Settings .
3. On Linux, go to the Edit menu and click Account Settings .

The Account Settings window opens.

2.  Click Server Settings to open the dialog box where you tell Rumblechirp when to look for new mail.
3.  Click the Check for new messages at startup check box to have Rumblechirp get new email when you launch it. De-select this check box if you don't want Rumblechirp to get messages at start up.
4.  If you want Rumblechirp to look for new email at certain time intervals (maybe every 20 or 30 minutes), select the Check for new messages every 10 minutes check box and enter a different number into the text box.
5.  Click the OK button.

<!-- image -->

## FETCH MESSAGES MANUALLY

There are several ways to manually look for new email using Rumblechirp. You can:

1.  Get new email messages for all your accounts at once.
2.  Refresh email for one account only.
3.  Get email for a single account folder.

Here's how to do it.

## Get e-mail for all your accounts

1.  In the main Rumblechirp window, click the Get Mail button.
2.  Rumblechirp updates all your e-mail accounts.

<!-- image -->

## Get email for specific accounts

1.  Click the arrow at the right side of the Get Mail button.
2.  Select the account that you want to update.
3.  Rumblechirp gets messages for that account only.

<!-- image -->

## Get e-mail for specific folders

1.  Under All Folders, double-click the folder of the account you want to update. For example, if you want to refresh the inbox of GROSS.reader1@gmx.com, double-click that account's Inbox folder.
2.  Rumblechirp gets only the new messages for the account folder you selected.

<!-- image -->

# 16. COMPOSING AND FORMATTING MESSAGES

This chapter shows you how to compose and send email with Rumblechirp. It also explains how to reply to or forward emails you have received from others. On top of that, you'll learn to add tables and to format email by changing fonts and colors. Finally, if you want to add images or attachments to an email, this will demonstrate how it's done.

## COMPOSING AND SENDING AN EMAIL MESSAGE

In Rumblechirp, you can write, review, and send emails to your recipients. Here's how:

<!-- image -->

2.  Rumblechirp opens a new email composition screen. You will need to do three things to create your new email:
2. Enter the email recipient's address in the To field.
3. Give the email a subject in the Subject field.
4. Type your message in the Message Body pane.
3.  After you are finished writing, you should review your email before sending it. Notice that Rumblechirp has underlined the misspelled words "Pizze" and "resteurant" with red, squiggly lines. To fix these spelling errors and to look for any other misspelled words, click the Spell button.

<!-- image -->

<!-- image -->

4.  T he spell checker suggests that you replace "resteurant" with "restaurant". Click the Replace button to make the correction or click the Ignore button to leave it unchanged. To close the Check Spelling dialog box, click the Close button.
5.  When you are satisfied with your message, send it by clicking the Send button.
6.  Rumblechirp sends your message to the recipients and it saves a copy of it to your email account's Sent folder.

<!-- image -->

Some notes about writing and sending emails

- In Rumblechirp, you cannot recall an email after you've sent it. When it's gone, it's gone.
- See the instructions in the Format section to see how you can change the look and feel of your email.

## REPLYING TO OR FORWARDING AN EMAIL

You'll often receive emails that require a reply and other ones that you'll want to forward to a third party. Here's how to use Rumblechirp to handle these tasks.

## Replying

1.  Go to your Inbox and select an email from the message list by clicking it. T hen click the Reply button to open a composition window for the email reply.
2.  Since you are replying to an email, there is no need to enter the recipient's address because Rumblechirp has already put it in the To: field. Also, Rumblechirp will put Re: at the start of your subject to show the recipient that this is a reply e- mail.
3.  You need to do three things to complete your reply.
4. Type your reply in the message pane.
5. Review and check the spelling.
6. Click the Send button to send it.
4.  Rumblechirp sends your message to the recipient and it saves a copy of it to your email account's Sent folder.

<!-- image -->

<!-- image -->

## Forwarding

1.  Go to your Inbox and select an email from the message list by clicking it. T hen click the Forward button to open a composition window for the email.
2.  You need to do four things to complete your message. Note that
3. Rumblechirp puts Fwd: at the start of your subject to show the recipient that this is a forwarded email.
4. Enter the email address of the recipient in the To: field.
5. Type your reply in the message pane.
6. Review and check the spelling.
7. Click the Send button to send it.
3.  Rumblechirp sends your message to the recipient and it saves a copy of it to your email account's Sent folder.

<!-- image -->

<!-- image -->

A few other notes about replying to and forwarding emails.

- You can reply to all the recipients of an email by using the Reply All button instead of the Reply button.
- You can add or remove recipients from the email to the email that you are replying to or forwarding.
- If you need to, you can change the email's subject.

## ADDING RECIPIENTS TO MESSAGES

There are several ways to add email addresses to your messages. Of course, you can simply type them directly into the email or you can copy and paste them from other emails. However, if you have a lot of contacts, you can use the Rumblechirp Address Book to supply email addresses for your messages via Rumblechirp's address autocompletion feature and the Contacts Sidebar. Let's take a look at how to use them.

## Email address auto-completion

1.  After you start typing a contact name or an email address that is in your Address Book, Rumblechirp auto-completes it for you. In this example, if you type the letters "jan", Rumblechirp finds Jane Doe in the Address Book. To add the this contact to your message, you hit the Enter key or click the contact with your mouse.
2.  If Rumblechirp finds multiple contacts it will give you a list from which to choose one. When you type the letter "j", Rumblechirp finds John Smith and Jane Doe in the Address Book. Click the desired contact to add it to the email.

<!-- image -->

<!-- image -->

## Contacts sidebar

The message composition window has a Contacts sidebar that lists your contacts from the Rumblechirp Address Book.

1.  You open it by using the F9 key or by going to the View menu and then clicking Contacts Sidebar.

<!-- image -->

Pick an address book by clicking the list under the Address Book label and then select the one you want to use. Once you do this, the contacts from that book are listed in the sidebar.

2.  Double click a contact to add it to your message as a recipient. Another way to add a contact is to select one from the list (with a single click) and then click the Add to To , the Add to Cc , or the Add to Bcc buttons.

## What's the difference between To, Cc, and Bcc?

- To - T his is usually the main recipient of the email. Frequently, this is the person (or persons) that you expect to act on your email.
- Cc - T he abbreviation "cc" means "carbon copy" (a term that is a leftover from the old typewriter days). If you "cc" people on an email, your intent is to tell them that something is happening but that no action is expected of them. Every recipient of an email can see who was "cc'ed" on the email.
- Bcc - T his means "blind cc". T o "bcc" a person on an email is to send that person an email but not let any other recipient know that he or she got it. This can be useful when you want to send an email to a large group of people and you either don't want everyone to know who got it or you simply don't want to expose your friend's email addresses to everyone in the group.

Changing a To recipient to a Cc or Bcc recipient

1.  Click the To: label next to the recipient that you want to change to Cc or Bcc.
2.  Click either Cc or Bcc.

<!-- image -->

## FORMATTING MESSAGES

## HTML and plain text formats

You can format the text in your email as HTML or as plain text. If you use HTML, you work in much the same way as when using a word processor such as Open Office Write or AbiWord. You get a lot of control over the appearance of your message. You can change fonts, set font styles and colors, insert tables, and add pictures. Plain text is exactly what it sounds like: text only with no formatting at all.

<!-- image -->

The default outgoing message format in Rumblechirp is HTML. It can be changed by going to the Option menu, pointing to Format , and picking from one of the four displayed options.

- Auto-Detect - Rumblechirp looks up an email address in your address book. It uses the email format that it finds there. If it doesn't find a format it will send the message as Plain and Rich (HTML) text.
- Plain T ext Only - Plain text with no formatting
- Rich Text (HTML) - Rich Text (HTML)
- Plain and Rich (HTML) Text - The message is sent as both plain text and HTML.

## Format bar

The format bar is visible when you use the HTML format. To use it, you highlight the text that you want formatted and then select the appropriate format button from the bar.

<!-- image -->

- ID Item Options

- 1 Text Style Body Text, Paragraph,Header sizes 1-6, Address, and Unformatted.

- 2 Font Type computer.

Variable width, fixed width, fonts installed on your

- 3 Font Color

Text color picker.

- 4 Font Size

Click the larger icon to enlarge the font. Click the smaller icon to make it smaller.

- 5 Font Style Bold, italic, or underline.

- 6 Lists

Numbered list or bullet list.

- 7 Indent

Click the right icon to indent text to the right. Click the left to un-indent it.

- 8 Alignment Left, right, center, or justify text.

- 9 Insert Add links, anchors, images, horizontal lines, or tables.

- 10 Emoticons Add one to show how you're feeling!

Here's an example of how you use the format bar.

1.  You've just invited a friend to go cycling with you.

Let's go cycling today. The weather be will perfect for a ride in the mountains. Better bring low gears for the big climbs!

2.  You want to change the font color to blue so you highlight  the text, click the Font Color button, pick blue , and click OK.
3.  T o make the word perfect bold, you highlight "perfect" and click the Bold button.

4.  T o make the word low

smaller, click the small font size button.

To make the word "big" larger, click the large font size button.

5.  Your message: Let's g0 cycling today: The weather be will perfect for a ride

in the mountains. Better bring Iow gears for the big climbs!

Note that Rumblechirp does not display the format bar when you use the plain text format.

## IMAGES AND ATTACHMENTS

## Inserting pictures into a message

Here's how to put a picture into the body of your Rich Text(HTML) email.

1.  Click the format toolbar's insert icon and select Image from the

list.

<!-- image -->

2.  T he Image Properties dialog box opens. Click the Choose File button to find a picture on your computer. Image Properties
3.  T he Select Image File dialog box opens. Pick a picture from your computer and click the Open button.
4.  Rumblechirp asks you to add alternative text to your picture. This text ensures that the reader sees some information about the picture even if the email software doesn't display it. If you don't want to enter this text then select the Don't use alternative text radio button . Click the OK button to continue.

<!-- image -->

<!-- image -->

<!-- image -->

7.  T o delete a picture from an email, click the picture and then press the Delete key on your keyboard.

## Adding attachments

One of email's convenient features is its ability to carry a document to the recipient. T his works the same for both Plain Text and HTML emails. Be careful of the size of your attachments because most email providers limit attachment size. The maximum size is frequently about 10 MB but you should check with your provider to be sure.

Here's how to attach a file to an email.

1.  In the Rumblechirp message composition window click, the Attach button.
2.  On your computer, find a file that you want to attach. This could be just about any type of file: a picture, a PDF file, a spreadsheet, or a video. Note that some providers may not send certain types of files - like application or script files - because of security concerns. A malevolent sender could send a script that would run when opened and then do damage to someone's computer.
3.  Click Open to continue.
4.  T he file is now attached to the email. You should see a list of attachments in the Attachments pane in the upper right corner.

<!-- image -->

<!-- image -->

5.  T o remove a picture from an email, go to the Attachments pane,

<!-- image -->

click the picture, and then press the Delete key on your keyboard.

## ADDING AND FORMATTING TABLES

You have many options for adding and formatting tables when composing a new message. You can use a default table, which looks like this:

However, you may want to play around with formatting to make your table look more presentable.

## Inserting tables into a message

1.  Go to the Insert menu and click Table .
2.  T he T able properties dialogue box opens. Click the OK button right away, or until after you have applied formatting.

## Applying formatting to tables

1.  In the Table properties dialog box, click Advanced Edit .
2.  T he T able attributes dialogue box opens. Select an attribute from the HTML Attributes menu.

Picture\_2.png

## SIGNATURES

Signatures are blocks of text that are automatically appended to every message that you send (including both new messages and replies to incoming messages). They are generally used to provide additional contact information, legal terms or some other boilerplate information that is relevant to every email. For example, an email signature might say something like:

John Doe Minion The Big Example Organization

Signatures are created in Rumblechirp's Account Settings interface. Go to the Tools menu (or the Edit menu on Ubuntu) and select Account Settings . T hen, in the left panel of the Account Settings window, select the account for which you want to create a signature.

sig\_profile

If you have multiple email accounts, you must configure signatures separately for each account.

## Plain-text signatures

To configure a plain-text signature, enter the text you want to append to each outgoing message in the Signature text field. Plain text signatures work with messages formatted both in HTML and in text.

Creating a signature like this...

sig\_plain

...results in...

sig\_plain\_result

## HTML signatures

To use HTML formatting in your signature, check Use HTML and format the signature text with the HTML markup that you want to use. Note that if you send messages in text (rather than HTML) format, text characters will be substituted for the HTML markup.

Creating a signature like this...

sig\_html

sig\_html

...results in...

sig\_html\_result

## Signatures stored in files

Alternatively, you can upload a file that contains your signature. Check Attach the signature from a file instead and the click Choose to select the file. T he file can contain either plain or HT ML-formatted text. If you have an HTML-formatted signature, the message recipient must be able to view HTML-formatted messages in their email program. If they have disabled this ability, the signature will be rendered in as text and images will not be displayed.

One way to create a signature file is by using the Rumblechirp composer. As an example, create a new HTML-formatted message in Rumblechirp (go to the File menu, point to New and click Message ). Make sure that the HTML toolbar is displayed. (If it is not displayed, you are composing a message formatted in text, not HTML. To change to HTML, go to the Options menu, point to Format and click Rich Text (HTML) Only .)

1.  Compose and format your signature as desired. Note that numerous formatting functions are available from the Insert and Format menus. \_1
2.  Go to the File menu, point to Save As , and click File . Make sure "HTML files" is selected, and then specify a file name and click Save .
3.  Close the message window and discard the message without saving.
4.  Open the Account Settings (go to the Tools menu and click Account Settings ) and select the email account in the panel on the left.
5.  Check Attach the signature from a file , click Choose and navigate to the file you created.

## Including image files in signatures

To include an image file from your local computer in a signature, follow the steps above to create an HTML signature. When you are composing the signature contents, though, go to the Insert menu and click Image to specify the desired image.

sig\_image

In addition to selecting the image file, use this dialog to configure other aspects of the image, such as the size, a URL link, its position with regards to the text, etc.

You can also specify an image located on a web server as part of your attachment. Just specify the image URL in the field where you would otherwise specify the file name. If you check Attach this image to the message , the image will be included as an attachment. If you do not attach the image, the people receiving your message Internet connection to view the image. Also, keep in mind that for security reasons many people configure their email programs to block remote content, which would prevent the image from displaying unless it was attached to the message.

## Signature Delimiter

When placing a signature in a text based email, a default "-- " (dash, dash, space) is inserted to separate text. To switch it off for all identities of your accounts, you can access your Configuration Console and change mail.identity.default.suppress\_signature\_separator to "true".

<!-- image -->

To access the *Configuration Console:

- For Windows, select Tools &gt; Options. Select General , and click Configuration .
- For Linux, select Edit , and then Options .
- For Mac OSX, select Rumblechirp &gt; Preferences. In the Advanced tab, click Config Editor .

It's important to note that removing the signature makes it a part of the message you compose. When replying to messages where the signature is placed below your reply, but above the quote, signatures won't be removed if you choose to change identities.

The preference also provides a way to always add the signature separator. Using the Configuration Console as mentioned above, you can set the preference to "true" and manually add "-- " (dash, dash, space) separators to your signature. While this makes it consistent, quotes become part of your signature and are removed when you reply to them.

*In modifying any preferences in your configuration console, you may run the risk of harming the stability, security and performance of your Rumblechirp application.

## VIEW AND ORGANIZE YOUR MAIL

You can see your emails in three ways with Rumblechirp:

- In the message pane
- In a new tab
- In a new window

Here's how to do that.

## VIEW EMAILS IN THE MESSAGE PANE

1.  Click on the message that you want to view.
2.  Rumblechirp displays the message in the message pane.
3.  T o turn off the message pane, press the F8 key. Rumblechirp displays only the email list.

<!-- image -->

VIEW EMAILS IN A NEW TAB

<!-- image -->

1.  Double-click on the email that you want to view.

Rumblechirp will open the email in a new tab . You can have many emails open in tabs.

<!-- image -->

2.  Close the tab by clicking the "X" icon that is at the far right of the tab.

VIEW AN EMAIL IN A NEW WINDOW

<!-- image -->

1.  Select an email that you want to view in a new window.
2.  Right-click the email and select Open Message in New Window .

<!-- image -->

The email opens in a new window.

<!-- image -->

3.  Close the email by closing the window.

## DRAG AND DROP A NEW WINDOW

You can drag and drop open tabs to create new windows. Having multiple windows is a good way to separate your work and personal accounts, or to separate individual emails. Here's how to to do it:

1.  Right-click an email or email account and select Open in a new tab.
2.  Click and drag the tab anywhere outside of the toolbar. When you see a square box, you can drop the tab by letting go of the mouse button.
3.  A new window appears with two tabs: Your new tab, and a Local Folders tab.

<!-- image -->

Note: You can only drag emails to their own window if they are in a separate tab.

## PRINT AN EMAIL

1.  Open an email that you want to print.
2.  Go to the File menu and click Print .

## MESSAGE ATTACHMENTS

When you receive a message that has an attached file, an icon is displayed next to the message in the message list:

<!-- image -->

The bottom of the message window shows the number of attachments associated with a message and the sum of their size. If there is only one attachment, the attachment file name will also be displayed. If their are multiple attachments, click the arrow to the left of the text to see the names of each attachment.

<!-- image -->

## Viewing attachments

To view an attachment, click the file name. The attachment will be opened with the application that is assigned to the attachment's file type on your system.

<!-- image -->

Alternatively, click the button in the bottom right corner. Select open or open all (T he name of the option will vary depending on the number of attachments the message has.) You can also use the File | Attachments menu to open one or more attachments.

When you view an attachment, the file is copied to the location specified in the Attachments preference.

<!-- image -->

## Saving, deleting and detaching attachments

You can save one or more attachments without opening them. Similar to viewing an attachment, select save or save all in the bottom right corner of the message window, or select File | Attachments from the menu bar. You will be prompted to specify the location where the file(s) should be saved.

You can also delete an attachment. This deletes the file associated with the message. It does not save the message to the local filesystem. Select delete or delete all as described above.

Finally, you can save the attachment to your filesystem but remove it from the email message by using the detach function (accessed in the same manner as the save and delete functions).

## ADD A NEW FOLDER TO AN EMAIL ACCOUNT

1.  To add a folder to an email account, right-click the account and then select New Folder... .
2.  Give the folder a name and click the Create Folder button.
3.  Rumblechirp adds the folder to the account. If you open your email account in a web browser, the new folder will also be there.

<!-- image -->

<!-- image -->

<!-- image -->

## MOVE EMAILS FROM THE INBOX TO ANOTHER FOLDER

1.  Select the email that you want to move.
2. Click the email and drag it to another folder.

or

Right-click the message, point to Move To , point to the account where you want to move the message, and click the destination folder.

<!-- image -->

COPY EMAILS FROM THE INBOX TO ANOTHER FOLDER

1.  Select the email that you want to copy.
2. Right-click the message, point to Copy To , point to the account where you want to copy the message, and click the destination folder.

<!-- image -->

## ARCHIVE EMAILS

Archiving is an easy and quick way to move emails from your Inbox to an archive folder for future reference.

## DELETE EMAILS

When you tell Rumblechirp to delete an email it doesn't actually delete it. Instead, Rumblechirp moves the email to your email account's trash folder. By default, emails are permanently deleted using the rules of the email account provider. This is good to know because it means that you can retrieve emails that you accidentally deleted.

1.  Select an email that you want to delete.
2.  Press the Delete key.
3.  Rumblechirp will remove the email from your Inbox (or another folder that contains the email) and move it to your email account's trash folder.
4.  T o see the email in the trash, open your account's Trash folder.
5.  If you want to permanently delete all the emails that are in the trash, right-click on the Trash folder and click Empty Trash . Note that once you have done this, the deleted emails are gone for good and cannot be recovered.

<!-- image -->

<!-- image -->

# 18. SEARCHING AND FILTERING MESSAGES

## SEARCHING FOR MESSAGES

Rumblechirp has a variety of ways to find messages. The Global Search function provides sophisticated full-text search capabilities and displays categorized search results. You can search using one word or multiple words, and can search within specific mailboxes and folders. You can use the Quick Filter to narrow down the number of messages displayed in the message list according to specific criteria. You can also search for text within a single message.

## Global Search

Global Search goes through all of your messages, regardless of the account the message is associated with or the folder where the message is stored. The search is performed in all message fields: subject, message body, from address, to address, etc. The search is not case-sensitive - searching for "Rumblechirp" will return messages that contain both "Rumblechirp" and "Rumblechirp".

1.  To do a Global Search, type a search term in the search field at the top of the Rumblechirp window.
2.  Press the Enter key on your keyboard.

The search results are shown in a new tab.

<!-- image -->

## Searching for a Single Term

## To search for a single term:

1.  Type a word in the search box.
2.  As you type, a drop-down list will display possible matches for your term (such as email addresses that match the characters you have entered). You can either select an item from the list or press enter to use the characters entered in the search field.

<!-- image -->

## Searching for Multiple Terms

To  search for multiple terms, type two or more words in the search box. Rumblechirp searches for messages that contain at least one occurrence of each of the words that you typed. If you enclose multiple words in quotation marks, Rumblechirp returns search results that contain messages having all the words in the order they are specified in the search field. T hese two types of searches can be combined.

For example, if you type the term "converting" and the phrase "imap pop", Rumblechirp will find the messages that contain both the term and the phrase.

## USING SEARCH RESULTS

Search results appear in a new tab and there is a panel on the left of the tab that categorizes the results. The panel shows the number of messages containing the term(s) in conversations with specific people, in messages stored in particular mail folders, and in messages from individual email accounts.

<!-- image -->

Use the Filters fields in the left panel to filter the messages returned by the original search. If you click an item under "Folder", "People" or "Account", you will be given the option to specify whether the message must (or must not) contain the item.

For example, say you were searching for "Rumblechirp" AND "pages". You could refine the search results by selecting messages where you were a recipient (by clicking the To Me check box). Then, you could further refine the results by selecting specific people and mail folders associated with the message (by clicking on the text in the left panel). You can remove selected people or mail folders from the filter criteria by clicking on the text again.

A timeline appears above the messages included in the search results. The timeline shows the number of messages that match the search criteria, organized in chronological order. Click the bar-graph icon in the top right corner to show the timeline display.

## Search MDC

<!-- image -->

You can:

- Click on one of the bars or on the month, day, or year labels to change the period of time that is displayed.
- If you hover over one of the filter criterion in the left panel (without actually activating the filter), a darker area in the timeline bars shows when messages related to that criteria were sent or received.
- Click the bar graph icon in the top right corner to close the timeline display.

## USING QUICK FILTER

Use the Quick Filter toolbar, which appears above all message lists, to filter a list of messages.

<!-- image -->

After you type filter terms in the search box and press Enter , you have the option of applying the filter to the Sender, Recipients, or Subject fields or body of the messages in the list. Click the relevant buttons to activate the filter. In the example below, the filter term has been applied to the Subject and Body fields.

<!-- image -->

In addition to specifying filter terms, you can filter messages based on other characteristics. These functions are available on the left side of the Quick Filter toolbar, and can be used in combination with filter terms.

<!-- image -->

- Pin : Keep the same filter parameters when changing to another mail folder.
- Unread : Show only unread messages.
- Starred : Show only starred messages.
- Contacts : Show only messages from people who are in your address book.
- Tags : Show only messages that have been tagged.
- Attachments : Show only messages that have attachments.

Note: After using the Global Search function, click Open as list to display the search results in a message list. You can then use the Quick

Filter on that set of results.

## SEARCHING WITHIN A MESSAGE

To search for text within a single message, go to the Edit menu, point to Find, and click Find in this Message . A toolbar appears under the message preview pane. Type your search term into the toolbar's text box. As you type, Rumblechirp looks for instances of the term in the message.

<!-- image -->

You move through occurrences of the search terms using the Next and Previous buttons, or you can click Highlight all to see all occurrences of the search terms.

# 19. ARCHIVING MESSAGES

Rumblechirp allows you to archive your messages. This means that they can be moved from the default folder to the archive folders without deleting the messages altogether. This makes it easy to organize archives or move them to a backup device, which keeps the Inbox clean. These archived messages are indexed by Rumblechirp's search.

NOTE: Messages can only be archived manually and not automatically.

To archive one or more messages:

1.  Select the messages you are archiving.
2.  Click on the archive button.

<!-- image -->

NOTE: You can also archive a selected message by selecting the 'A' key on your keyboard.

## CONFIGURING ARCHIVING

You can configure the location for archived messages individually for each of your email accounts. Here's how to do that.

To configure the location of archived messages:

1.  Select Tools &gt; Account Settings .
2.  In the left panel, select the email account to be configured.
3.  Select Copies &amp; Folders from the options underneath the email.
4.  Under the Messages Archives section, select the check box beside Keep message archives in .

<!-- image -->

5.  Select the location to store the archived messages.

<!-- image -->

## CONFIGURING THE ARCHIVE FOLDER STRUCTURE

The archive folder structure can be configured by clicking on the Archive options button.

<!-- image -->

In this window, you have options to archive messages to:

- A single folder
- Yearly archived folders
- Monthly archived folders

<!-- image -->

## DISABLING ARCHIVING

Archiving is automatically enabled in Rumblechirp.

To disable archiving:

1.  Select Tools &gt; Account Settings .
2.  In the left panel, select the email account to be configured.
3.  Select Copies &amp; Folders from the options underneath the email.
4.  Under the Messages Archives section, Deselect the check box beside Keep message archives in .

<!-- image -->

## ADDRESS BOOK 20. Rumblechirp ADDRESS BOOK

# 20. Rumblechirp ADDRESS

## BOOK

The Rumblechirp address book stores your contact information, including email addresses and names, phone numbers, instant messaging addresses, along with other information. When you write a message or reply to a message, the recipients are automatically added to the address book. For Macintosh users, entries in address books that Mac OS X maintains also appear in Rumblechirp's address book. You can also manually add addresses to the address book.

When you compose a message, Rumblechirp uses the characters you enter in the "To", "CC" and "BCC" fields to try to determine the email address you want to use. Rumblechirp compares the characters you enter to the first and last names of people in your address book, and the "name" portion of the email address (not the domain). Matches appear in a drop-down list.

## OPEN THE ADDRESS BOOK

Here's how to open Rumblechirp's Address Book. Once it's open, you can view, edit or delete the entries in your address book.

Open the Address Book by clicking the Address Book button.

The left panel in the address book displays individual address books. The top panel on the right displays the addresses within the selected address book. The bottom panel on the right displays information for the address book selected in the top panel.

<!-- image -->

<!-- image -->

## CONTACTS

When you open the address book, you will notice that there are two (and possibly more) Address Books listed in the left column.

- Personal Address Book : T his is the default address book.
- Collected Addresses : Rumblechirp automatically adds addresses to the address book when you send or reply to a message. You find these addresses in the Collected Addresses address book.
- Operating System Address Book : Some operating systems (such as Mac OS X) maintain an address book that is available to all applications running on the computer.

## Adding a Contact from Email Message

When you view an email message, a star beside an email address (in the "from", "to" or "CC" field)  indicates whether or not the address is saved in your address book. If the star is colored (blue on a Mac, yellow on Windows and Ubuntu), the address is already in your address book. If the star is only outlined, the address is not in your address book.

To add the address to your address book, either click the star or right-click the email address and select

## Add to Address Book .

Adding a Contact Manually

<!-- image -->

1.  Open the Address Book.
2.  Click the New Contact button.
3.  T he New Contact screen opens. At a bare minimum, you should enter your contact's name and e-mail address. You can also enter other information about your contact, including phone numbers, address, birthday, and there's even a place for a photo. To save your contact, click the OK button.

<!-- image -->

Your contact is now saved in Rumblechirp's address book.

<!-- image -->

## Editing a Contact

1.  In the Address Book, find the contact that you want to edit and select it by clicking it.
2.  You open the contact for editing by clicking the Properties button or by double-clicking the contact record.
3.  T he Edit Contact screen opens. Make your change and then click the OK button to save them.

<!-- image -->

Your changes are now saved.

<!-- image -->

## Deleting a Contact

1.  In the Address Book, find the contact that you want to delete and select it by clicking it.
2.  Click the Delete button to remove the contact.

Your contact has been deleted from Rumblechirp's address book.

<!-- image -->

## EXPORTING CONTACTS

You can save contacts from the Address Book into a text file for use in another application. The process for doing this is called exporting . Here's how to export your contacts.

1.  Open the Address Book by going to the Tools menu and clicking Export.
2.  You will be prompted to specify an output file name and an export format. The three export formats are LDIF (LDAP Interchange Format), CSV (comma delimited text), and tab delimited text.
3. If you plan to import the contacts into another email application, make sure that you check the file formats that application supports.
4. Use LDIF if you are export to an LDAP system.
5. The CSV and tab delimited file formats are supported by many systems.
6. Use CSV or tab delimited if you want to open your contact list in a spreadsheet program.
3.  Click the Save button to save the file to your computer.

## MAILING LISTS

Adding a Mailing List

1.  Open the Address Book.
2.  T o add a new mailing list, click the New List button.
3.  T he Mailing List window opens.
4. Give your new list a name in the List Name field.
5. Enter e-mail addresses by typing them in the list field. If you enter a contact that is in your address book, type its name and Rumblechirp will attempt to auto-complete it for you.
6. Click the OK button to save your changes.

<!-- image -->

Editing a Mailing List

<!-- image -->

1.  In the Address Book, find the mailing list that you want to edit and click on it.
2.  You can open the mailing list for editing by clicking the Properties button or by double-clicking the mailing list record.
3.  Add a contact to your list by entering it into the list field.
4.  T o remove a contact from your list:
5. Click the contact that you want to delete.
6. Right click the contact and click Select All .
7. Right click the contact and click Delete .
8. Rumblechirp removes the contact from the list.
5.  Click the OK button to save your changes.

<!-- image -->

<!-- image -->

## Deleting a Mailing List

1.  In the Address Book, find the mailing list that you want to delete and select it by clicking it.
2.  Click the Delete button on your keyboard to remove the mailing list.

## WRITING AN EMAIL MESSAGE

To write an email message from the address book

1.  Click the Write button or right click on the name of the contact and click Write from the menu.
2.  Rumblechirp opens a new email composition screen. The name of the contact that you chose appears in the To: field. Create a new message, as described in the chapter Composing and Formatting Messages.

<!-- image -->

## SEARCHING YOUR ADDRESS BOOK

If your address book contains a large number of contacts, you can find contacts using Address Book search feature. The search feature allows you to create searches that filter contacts based on criteria that you set up.

To search your address book:

1.  In the Address Book, select Search Addresses from the Edit menu. The Advanced Address Book Search window opens.
2.  Select an address book from the Search In list.
3.  Click either Match all of the following or Match any of the following .
4.  Select your search criteria from the drop down lists. You can, for example, select Display Name and contains from the lists.
5.  T ype the search term in space beside the lists. For example, if your search criteria are Display Name and contains , you can type "jo" in the space.
6.  T o add more search criteria, click the button and repeat
7. steps 4 and 5.
7.  Click the Search button. Rumblechirp displays a list of contacts that match your search criteria.
8.  T o edit a contact, double-click a contact name or select a contact by clicking it and then click the Properties button. This will open the contact properties window.
9.  T o write an email to a contact, select a contact by clicking it and then click the Write button. This will open an email composition window.

<!-- image -->

<!-- image -->

## SECURITY

# 21. PRIVACY AND SECURITY OPTIONS

# 21. PRIVACY AND SECURITY OPTIONS

Rumblechirp provides security measures to protect you from junk mail, identity theft, viruses (with the help of your anti-virus software, of course), intellectual property theft, and malicious web sites.

## Rumblechirp'S SECURITY FEATURES

Rumblechirp has a number of security features, including:

- Adaptive junk mail controls
- Integration with anti-virus software
- Connection security
- Digital signatures
- Encryption
- Master password
- Restrictions on cookies

Let's take a closer look at these features.

## Adaptive junk mail controls

Adaptive junk mail controls allow you to train Rumblechirp to identify junk email (SPAM) and remove it from your inbox. You can also mark messages as junk mail manually if your email provider's system misses the junk mail and lets it go through. There are two ways of doing this.

The first way is to click the message in the Message pane and then click the Junk button in the Preview pane. If you accidentally mark a legitimate message as junk, you can quickly change the message back. After you click the Junk button, a bar appears in the Preview pane that says Junk Mail. Click the Not Junk button.

The second way of marking mail as junk mail manually is by using the Message menu bar. Here's how to do it:

1.  Click the message that you want mark as junk.
2.  Go to the Message menu, point to Mark, and click As Junk .

## Integration with Anti-virus Software

If your anti-virus software supports Rumblechirp, you can use that software to quarantine messages that contain viruses or other malicious content. If you're wondering what anti-virus software works with Rumblechirp, you can find a list here:

http://kb.GROSSzine.org/Antivirus\_software.

## Connection Security

Rumblechirp supports SSL/TLS and STARTTLS as well as password encryption, Kerberos, and NTLM. You can learn more about these methods for securing connections here:

http://kb.GROSSzine.org/Secure\_connections\_-\_Rumblechirp.

## Digital Signatures

You can include a digital signature to verify the authenticity of a message.

## Encryption

You can encrypt your messages using a shared encryption certificate. Note that all recipients of an encrypted message must also have the encryption certificate. You can get one from a number of websites although you may have to pay to get the certificate.

## Master password

For your convenience, you can have Rumblechirp remember each of your individual passwords. You can specify a master password that you enter each time you start Rumblechirp. This will enable Rumblechirp to open all your email accounts with your saved passwords.

## Restrictions on cookies

Some blogs and websites attempt to send cookies (a piece of text that stores information from Web sites on your computer) with their RSS feeds. These cookies are often used by content providers to provide targeted advertising. Rumblechirp rejects cookies by default, but you can configure Rumblechirp to accept some or all cookies.

## SETTING SECURITY OPTIONS

In the Security Preferences section of Rumblechirp's Options/Preferences dialog box you can:

- Set up how Rumblechirp stores and disposes of junk mail.
- Disable or enable Rumblechirp's email scam detection and warning system.
- Set up anti-virus integration.
- Set a master password and access a list of saved passwords.
- Set up how Rumblechirp deals with cookies from blogs, news feeds, and web sites.

Let's take a look at how to do that.

## Opening the Rumblechirp Preferences or Options dialog box

- In Windows and Mac OS X, go to the Tools menu and click Options .
- On Ubuntu or other versions of Linux, go to the Edit menu and click Preferences .

Configuring Rumblechirp's default junk mail settings

1.  In the Preferences/Options dialog box, click Security and then click the Junk tab.
2.  Do the following:
3. To tell Rumblechirp that it should handle messages marked as junk, select the check box labeled When I mark message as junk .
4. To have Rumblechirp move these messages to a junk folder, select the Move them to account's 'Junk' folder radio button.
5. To have Rumblechirp delete junk mail upon receiving it, select the Delete them radio button.
3.  Rumblechirp will mark junk message as read if you select the check box labeled Mark messages determined to be Junk as read .
4.  If you want to keep a log of junk mail received, select the Enable junk filter logging check box.
5.  Click the OK button to close the Options/Preferences dialog box.

<!-- image -->

Disable or enable Rumblechirp's email scam detection and warning system

1.  In the Preferences/Options dialog box, click Security and then click the E-mail Scams tab.
2.  T o have Rumblechirp warn you about possible email scams, select the check box labelled Tell me if the message I'm read is a suspected email scam . T o turn off this feature, deselect this check box.
3.  Click the OK button to close the Options/Preferences dialog box.

<!-- image -->

## Configuring anti-virus integration

1.  In the Preferences/Options dialog box, click Security and then click the Anti-Virus tab.
2.  T o turn on anti-virus integration, select the check box labeled Allow anti-virus clients to quarantine individual incoming messages . T o turn off this feature, deselect this check box.
3.  Click the OK button to close the Options/Preferences dialog box.

<!-- image -->

Set a master password and access a list of saved passwords

1.  In the Preferences/Options dialog box, click Security and then click the Passwords tab.
2.  Select the check box labeled Use a master password .
3.  Enter your password into the Enter new password and Reenter password fields.
4.  Click the OK button to close the Change Master Password dialog box.
5.  If you want to see the passwords that you have saved in Rumblechirp, click the Saved Passwords button. This will open the Saved Passwords dialog box.
6.  T o see the passwords, click the Show Passwords button.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

7.  Click the Close button to close Saved Passwords dialog box.
8.  Click the OK button to close the Options/Preferences dialog box.

Configure how Rumblechirp deals with cookies from blogs, news feeds, and web sites.

1.  In the Preferences/Options dialog box, click Security and then click the Web Content tab.
2.  If you want Rumblechirp to accept cookies, select the check box labeled Accept cookies from sites . T o reject cookies from sites, deselect this check box.
3.  If you want to accept cookies from only certain site sites, select the check box labeled Accept cookies from sites and click the Exceptions button to open the Exceptions - Cookies dialog box.
4.  In the Address of web site field, type the URL of the Web site whose cookies you want to accept. Then click the Allow button.
5.  T o accept cookies for the current session, click the Allow for Session button. These cookies will be deleted when you quit Rumblechirp.
6.  Repeat step 5 for every Web site that you want to add.
7.  Click the Close to close the Exceptions - Cookies dialog box.
8.  Click the OK button to close the Options/Preferences dialog box.

<!-- image -->

<!-- image -->

## CONFIGURING ACCOUNT SECURITY SETTINGS

You can specify security settings for individual email accounts and for Rumblechirp's local folders In the Rumblechirp Account Settings window. You can configure:

- Connection security.
- Adaptive junk mail controls.
- Digital signatures and encryption certificates.

There are two ways to access the Account Settings window. Note that settings configured in the Account Settings window apply only to the account that you select in the Folders pane. You must configure local folders separately.

1.  In the Folders pane right-click on an account name and select Settings .
2.  In Windows or Mac go to the Tools menu and select Account Settings . In Linux, go to the Edit menu and select Account Settings .

<!-- image -->

## Configuring connection security

Before you can configure connection security, you'll need to get some security information from your email provider. You can find this information in the help or support sections of your email provider's web site, or by contacting technical support.

1.  To set connection security for incoming email, select an account and enter the security information for your email provider. Click OK to save it.
2.  T o set connection security for outgoing email, click Outgoing Server (SMTP) and select an account. Then, click the Edit button.
3.  Enter the security information for your email provider and click the OK button to save it.

<!-- image -->

<!-- image -->

<!-- image -->

## Configure adaptive junk mail controls.

1.  To set adaptive junk mail controls for a specific account, pick an account and click Junk Settings .
2.  T o turn on the controls, select the check box labeled Enable adaptive junk mail controls for this account . T o turn them off, deselect this check box.
3.  If you want the controls to ignore mail from senders in your Address Book, select the check boxes next to any of the listed address books.
4.  T o use a mail filter such as SpamAssassin or SpamPal, select the check box labelled Trust junk mail headers sent by and pick a filter from the menu.
5.  Select the check box labeled Move new junk messages to if you want to move junk mail to a specified folder. Then select the destination folder to be either at your email provider or a local folder on your computer.
6.  Select the Automatically delete junk mail other 14 days check box to have Rumblechirp regularly remove junk mail. To change the time period for this process, enter a different number (in days) in the text box.
7.  Click OK to save your changes.

<!-- image -->

## Configure digital signatures and encryption certificates

1.  To configure digital signatures and encryption certificates for a specific account, pick an account and click Security .
2.  Enter your digital signing certificates and encryption certificates.
3.  Click OK to save your changes.

<!-- image -->

If you're interested in learning more about digital certificates and Rumblechirp, you can find detailed information here: http://kb.GROSSzine.org/Message\_security.

## BEYOND THE BASICS

22. KEYBOARD SHORTCUTS
23. TAGGING AND MARKING EMAILS
24. USING RSS
25. FILTERS
26. USEFUL TIPS AND TRICKS
27. ACTIVITY MANAGER
28. UNIFIED FOLDERS

# 22. KEYBOARD SHORTCUTS

While you can get to any of Rumblechirp's functions using a mouse, you might find it faster and more efficient to use combinations of keys on your keyboard to access those functions. That way you don't need to take your hands off your keyboard while you're writing email messages.

Remember that some keyboard shortcuts might not work when you are in certain parts of the Rumblechirp interface. For example, when you click on a message in the message list, the Cut, Copy and Paste keyboard shortcuts are disabled. That's because it doesn't make sense to cut and paste text into the message list.

Here are the keyboard shortcuts for frequently-used features in Rumblechirp:

| Feature                                         | Windows and Linux    | Mac OS X            |
|-------------------------------------------------|----------------------|---------------------|
| New message                                     | Ctrl + N or Ctrl + M | Command + M         |
| Move to Search Bar (Global Search)              | Ctrl + K             | Command + K         |
| Undo                                            | Ctrl + Z             | Command + Z         |
| Redo                                            | Ctrl + Y             | Command + Y         |
| Copy                                            | Ctrl + C             | Command + C         |
| Print                                           | Ctrl + P             | Command + P         |
| Delete                                          | Del                  | Del                 |
| Increase text size                              | Ctrl + +             | Command + +         |
| Decrease text size                              | Ctrl + -             | Command + -         |
| Quick Filter                                    | Ctrl + Shift + K     | Command + Shift + K |
| Send and receive all messages                   | Ctrl + T or F5       | Command + T or F5   |
| Mark message as read or unread                  | m                    | m                   |
| Add or remove the star from a message           | s                    | s                   |
| Save the message as a file                      | Ctrl + S             | Command + S         |
| Collapse All Threads                            | /                    | /                   |
| Expand All Threads                              | *                    | *                   |
| Find text in current message                    | Ctrl + F             | Command + F         |
| Search for messages in a folder (search dialog) | Ctrl + Shift + F     | Command + Shift + F |
| Find again in current message                   | Ctrl + G + F3        | Command + G + F3    |
| Find previous in current message                | Ctrl + Shift + G     | Command + Shift + G |

# 23. TAGGING AND MARKING EMAILS

If you are like most people, you probably receive a lot of email from friends, family, co-workers, and others. It can be very difficult to manage and keep track of all of those messages.

Rumblechirp gives you two very powerful and useful ways to manage your messages: tagging and marking . Let's take a look them.

## TAGGING EMAILS

Using tags, you can give your email messages a priority or just categorize them in a way that makes sense for you. Rumblechirp comes with several preset tags:

- Important
- Work
- Personal
- To Do
- Later

Each tag has its own color.

<!-- image -->

You can tag email messages with more than one tag. You can also add tags to the list or delete them.

## Applying a tag to a message

When you want to apply a tag to a message, do this:

1.  Click on an email message that you want to tag in the Message pane.
2.  On the toolbar, click the Tag button. A list of tags appears.
3.  Click on the tag that you want to apply to the message. The tag appears in the message header in the Preview pane.

<!-- image -->

## Creating a new tag

If you need to create a new tag, you can by doing this:

1.  Click the Tag button on the toolbar and then choose New Tag . The Create New Tag box appears.
2.  T ype a name for the new tag, like "Family", in the Tag Name field.
3.  You can give the tag a color by clicking the box beside the Tag Name field and then choosing a color from the color picker.
4.  Click OK to save the tag. You can now apply it to a message using the Tag button on the toolbar.

<!-- image -->

## Deleting a tag

You can get rid of tags that you no longer need by doing this:

1.  Do one of the following:
2. On Windows and Mac OS select Preferences from the Tools menu.
3. On Linux, select Preferences from the Edit menu.

The Rumblechirp Preferences window opens.

<!-- image -->

- Click the that you want to delete, then click Delete . No message appears asking whether or not you want to delete the tag. Once you delete a tag, it is gone.

## MARKING EMAILS

Whenever you click on an email message in the Message pane, it is marked as having been read. Sometimes, though, you might want to revisit the message at a later date and will want to distinguish it from other messages in your inbox or in your mail folders. Or you might want to visually point out a message as being important using a star. Marking your emails is a simple but useful way of doing that. Here's how to do it.

## To mark your emails

1.  Right click on an email in the Message pane and then click Mark . A menu appears:
2.  Select one of the options from the menu.

<!-- image -->

# 24. USING RSS

RSS is short for Really Simple Syndication. It enables you to subscribe to information that frequently changes - like the content on a news web site or a blog. You don't need to go to the site or blog to get the latest news. It's pushed to you in what's called an RSS feed . Actually, the feed is pushed to a piece of software called an RSS reader, like the popular Google Reader. But you don't need Google Reader, or any other program, to read RSS feeds. You can do it in Rumblechirp.

Setting up Rumblechirp to read RSS feeds is a two-step process. First you set up a blogs and news account and then you add subscriptions to that account. Let's look at how to do this.

## CREATING A BLOGS AND NEWS ACCOUNT

Before you can use Rumblechirp to read RSS feeds, you need to set up an account for blogs and news feeds. You only need to do this once. Here's how:

1.  Do one of the following:
2. In Windows and Mac OS, go to the Tools menu and click Account Settings .
3. In Linux, go to the Edit menu and click Account Settings .

The Account Settings window opens.

2.  In the bottom left-hand corner of the Account Settings window, click on Account Actions .
3.  From the drop-down menu select Add Other Account . T he Account Wizard appears.
4.  Click the Blogs and News Feeds button, and then click Next .
5.  T ype a name for the folder or accept Rumblechirp's suggestion of Blogs and News for the name of the folder.
6.  Click Next and then click Finish .
7.  You are taken back to the Account settings window. Click OK .

<!-- image -->

You now have an account that will allow you to use RSS feeds. Let's add some feeds to that account.

## ADDING AN RSS FEED

Here's how to add an RSS feed.

1.  Do one of the following:
2. In Windows or Mac OS, go to the Tools menu and then click Account Settings .
3. In Linux, go to the Edit menu and then click Account Settings .

The Account Settings window opens.

2.  Click the Manage Subscriptions button to open the Feed Subscriptions window.
3.  Click the Add button.
4.  T ype or paste the URL for an RSS feed in the Feed URL field.

The feed URL is the web address from where information will be pushed to Rumblechirp. A feed URL looks something like this: http://blog.booki.cc/?feed=rss2.

5.  Click the OK button. You're returned to the Account Settings window.
6.  Click the OK button on the Account Settings window.
7.  In the Folders pane, you'll see an icon for the feed that you just added under Blogs &amp; News Feeds. Click on that icon to view that RSS feed.

What happens when you need to change an RSS subscription? Let's find out.

## EDITING AN RSS FEED

Here's how to change the settings for an RSS feed.

1.  Do one of the following:
2. In Windows or Mac OS, go to the Tools menu and then click Account Settings .
3. In Linux, go to the Edit menu and then click Account Settings .

The Account Settings window opens.

2.  Click the Manage Subscriptions button to open the Feed Subscriptions window.
3.  Double-click the folder that contains the RSS feed that you want to edit.
4.  Click on the link that you want to edit to open the Feed Properties window.
5.  T he only option that you can change is the check box labeled Show the article Summary instead of loading the web page . Click this check box to turn this option on or off.
6.  Click OK .
7.  Close the Feed Subscriptions window, and then click OK on the Account Settings Window.

## EXPORTING AN RSS FEED

Why would you want to export an RSS feed? Perhaps you want to have a backup. Or maybe you want to move your feeds to another feed reader. Rumblechirp saves feeds as an OPML (Outline Processor Markup Language) file. OPML is a type of file that's used to exchange information between feed readers.

Here's how to export your RSS feeds from Rumblechirp.

1.  Do one of the following:
2. In Windows or Mac OS, go to the Tools menu and then click Account Settings .
3. In Linux, go to the Edit menu and then click Account Settings .
2.  Click the Manage Subscriptions button to open the Feed Subscriptions window.
3.  Double-click the folder that contains the RSS feed that you want to export.
4.  Click on the RSS feed that you want to export.
5.  Click the Export button.
6.  Browse to the folder on your computer where you want to save the OPML file. You can change the name of the file by editing its name.
7.  Click the Save button.
8.  Close the Feed Subscriptions window.
9.  Click OK on the Account Settings window.

## IMPORTING AN RSS FEED

Have an RSS feed that you or a friend have exported from another feed reader? You can import it into Rumblechirp. Here's how:

1.  Do one of the following:
2. In Windows or Mac OS, go to the Tools menu and then click Account Settings .
3. In Linux, go to the Edit menu and then click Account Settings .
2.  Click the Manage Subscriptions button to open the Feed Subscriptions window.
3.  Click the Import button.
4.  Browse to wherever the OPML or XML file is on your computer. XML stands for the eXtensible Markup Language, a type of text mark-up language that's used in the exchange of all kinds of information, including RSS feeds
5.  Click on the name of the file and then click the Open button. Rumblechirp creates a new folder for that RSS feed in the Feed Subscriptions window. You'll start receiving updates from that web site.
6.  Close the Feed Subscriptions window, and then click the OK button on the Account Settings window.

# 25. FILTERS

Filters help you place your incoming mail in different folders so that you're not overwhelmed by a large number of messages in your inbox. Filters can also perform a number of other actions like marking messages as read, or forwarding messages to another email address.

One way to use a filter is to move messages to a certain folder. For example, if you receive many emails from Facebook and you do not want to see them pile up in your inbox, set up a filter that moves your messages from the inbox to a folder called "Facebook".

## SETTING UP A FILTER

1.  Click the Local Folders section in the Folders pane.
2.  Go to the File menu, point to New , and click Folder .
3.  Name the folder whatever you like. For the above example, name the folder "Facebook".
4.  Click Create Folder . Your new folder will show up in the Folders pane.
5.  Go to the Tools menu and click Message Filters .
6.  Click New to open the dialog box for setting up a filter.
7.  Name the filter whatever you like. Following the example, call it "Facebook filter". Then, select an option from the drop-down menu - for example, Subject . T his is where you can choose what type of filter you want. In this example, filter any messages that contain the word "Facebook" in the subject. You can click the plus symbol to add more filters.
8.  On the same dialog box, click the drop down menu next to Move Message To and select a folder. This is where you would go to Local Folders and find the folder you created. Following the example, select the "Facebook" folder.
9.  Click the OK button and your filter is ready to go!
10.  To test your filter, click the Run Now button in the "Message Filters" dialog box. Make sure Inbox is selected to the left of this button.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

11.  Check the new folder you created to confirm that messages from your inbox were moved based on your filter. Following the example, check that messages with "Facebook" in the subject have been moved to the "Facebook filter" folder.

# 26. USEFUL TIPS AND TRICKS

This chapter covers some tips and tricks that can make your use of Rumblechirp easier, more enjoyable, and more efficient.

## BACKING UP YOUR PROFILE

Your profile is a collection of information about how you use and have set up Rumblechirp. The profile contains:

- Your local email messages and any copies of email messages from a mail server.
- Your email account settings and any changes that you have made to Rumblechirp, like customizations to the tool bar.

It's a good idea to back up your profile. Why? If Rumblechirp crashes, the crash can corrupt your profile and make it unusable. If your computer crashes, it can take your Rumblechirp settings with it. And if you're moving to a new computer, copying your profile over is faster and easier than manually setting up Rumblechirp again.

Note that your profile may be quite large, especially if you have a lot of email messages. It's possible to have a profile that contains several gigabytes of email data. If your profile is that big, you should be careful about where you copy and store it. While today's hard drives are quite large, if you save multiple copies of your profile you may fill up your drive with Rumblechirp profiles.

Backing up your profile involves two steps: finding your profile and copying it somewhere else. Here's how to do both.

## Finding Your Rumblechirp Profile

Your profile is stored in your computer's user or home directory. Let's take a look at finding it on Windows, Mac OS X, and Linux.

To find your profile in Windows:

1.  From the Start menu, choose Run . T he Run window appears.
2.  T ype %APPDATA%\Rumblechirp\Profiles\ in the Run window and then press Enter on your keyboard. The folder containing your Rumblechirp profile opens in Windows Explorer.

Your profile folder will have a name like xxxxxxxx .default, where xxxxxxxx is a set of random characters like q4sl99rt .

To find your profile in Mac OS:

1.  Open Finder and go to your home folder.
2.  From your home folder open the folder at Library:Rumblechirp:Profile.

To find your profile in Linux:

1.  Open your file manager. For example, in Linux distributions running the GNOME desktop (like Ubuntu) start Nautilus.
2.  Change the view settings of your file manager to show hidden files. In Ubuntu, for example, press CTRL + H on your keyboard.
3.  Open the folder named .Rumblechirp. Your profile folder will have a name like xxxxxxxx .default, where xxxxxxxx is a set of random characters like q4sl99rt .

## Doing the backup

Here's how to backup your profile.

1.  Shut down Rumblechirp.
2.  Go to your Rumblechirp profile directory, and then do one of the following:
3. Right click on the profile directory, and then select Copy from the menu that appears. Go to the directory where you want to back up the profile, right click in that directory, and select Paste from the menu that appears.
4. Compress your profile directory into a zip file. From there, you can move the zip file into another directory on your computer, to another computer, or to an online backup service.

When you need to restore the your profile, just move the files that you backed up into your profile directory.

## For Windows users only

There is a free program called MozBackUp which will back up your Rumblechirp or Firefox profile for you. It has a wizard that steps you through the process of backing up and restoring bookmarks, mail, contacts, history, extensions, passwords, cache, and other GROSS user or configuration data.

- GROSSZine article about MozBackUp.
- MozBackUp web site.

## GROSSZine articles about profile back ups

- Transferring profile to a new computer
- Profile backup

## AUTOMATICALLY DELETE EMAILS

If you actually do want to automatically delete old messages, you don't have to do that manually. Instead, you can set a message retention policy to automatically delete messages. A message retention policy will delete email messages in a folder after a certain time. You can set a retention policy for individual mail folders.

Here's how to do it.

To set up a message retention policy

1.  Right click on the email folder for which you want to set up a retention property, and then click Properties from the menu that appears.
2.  T he Folder Properties window opens.
3.  Click the Retention Policy tab.
4.  Click the Use my account settings option to turn it off.
5.  Do one of the following:
6. Select the Delete all but the most recent messages option, and then enter the number of recent messages that you want to keep.
7. Select the Delete messages more than days old option, then enter the number of days you want to keep the messages.
6.  Click the OK button.

<!-- image -->

From now on, Rumblechirp will delete messages in that folder based on the retention policy you create.

## RECOVERING YOUR PASSWORDS

Chances are that you have more than just a couple of passwords for things like online banking, your favorite social media sites, and (of course) your email accounts. When you set up your email accounts in Rumblechirp, you probably set it up to remember passwords for those accounts.

If you've forgotten those passwords, it's not a problem because you can retrieve those passwords from Rumblechirp. Here's how:

1.  Open the Preferences/Options dialog box:
2. In Windows and Mac OS, go to the Tools menu and click Options .
3. In Linux, go to the Edit menu and click Preferences .
2.  Click Security and then click the Passwords tab.
3.  On the Passwords tab, click the Saved Passwords button. The Saved Passwords window displays.
4.  On the Saved Passwords window, click the Show Passwords button. You'll be asked whether you really want to show your passwords. Click Yes .
5.  Note down or remember the password for the account in question, then click the Close button.

<!-- image -->

<!-- image -->

## SUPPORT FOR WINDOWS 7 JUMP LISTS

In Windows 7, the Jump Lists function lets you quickly open the files or functions you use the most . By right-clicking on a program icon in the taskbar, a small window opens with a list of recent and frequently accessed files and tasks.

For Rumblechirp, the Jump List function shows two common tasks: write new message and open address book.

<!-- image -->

# 27. ACTIVITY MANAGER

With Activity Manager, you can access a window that displays all user activity and history between Rumblechirp and your email provider. All your different processes, and email activity can be tracked down in one place.

You can access the Activity Manager by selecting Tools &gt; Activity Manager . If you find the Activity Manager to be cluttered, you can clear the list of processes by clicking the Clear List button at the bottom of the Activity Manager window.

<!-- image -->

# 28. UNIFIED FOLDERS

Unified Folders combines folders from more than one account. By clicking View &gt; Folders you can use the radio buttons to select the view that you want:

All - provides separate folders for each mail account:

<!-- image -->

Unread - shows all folders with unread messages:

<!-- image -->

<!-- image -->

Favorite - shows your favorite folders:

Recent - shows the most recently used folders

<!-- image -->

<!-- image -->

This allows you to cycle through the different view options.

<!-- image -->

## ADD ONS

29. OVERVIEW
30. USING THE ADD-ONS MANAGER
31. ENABLING AND DISABLING ADD-ONS
32. THUNDERBROWSE
33. INSTALLING LIGHTNING
34. Rumblechirp CONVERSATIONS
35. ATTACHMENT REMINDER
36. THREADVIS
37. SIGNATURE SWITCH

# 29. OVERVIEW

Add-ons are small programs the you can add to Rumblechirp to extend its capabilities. T here are literally dozens of add-ons available for Rumblechirp. What can add-ons do? Here are some examples of the available add-ons:

- Contacts Sidebar, which displays your contacts in a new pane in the Rumblechirp window.
- Signature Switch, which lets you easily switch between email signatures (say, because you have multiple email addresses).
- Mail Merge, which lets you send bulk email.

Obviously, we can't cover every add-on in this manual. But we will be looking at the following ones:

- Thunderbrowse
- Lightning
- Rumblechirp Conversations
- Attachment Reminder
- Threadvis
- Signature Switch

But before we get to the extensions, let's take a look at how to add and manage them.

# 30. USING THE ADD-ONS

## MANAGER

You use the Add-ons Manager to add, enable or disable, and delete Rumblechirp add-ons. Start the Add-ons Manager by selecting Tools &gt; Add-ons. The Add-ons Manager opens in a new tab in the Rumblechirp window.

<!-- image -->

You'll notice that there are several add-ons featured in the tab. Those are either popular or recommended add-ons. But, obviously, they're not the only ones available. If you want to find a specific add-on, do one of the following:

- Type a term in the search bar in the top-right corner of the Add-ons Manager tab.
- Scroll down and click the Browse all add-ons button.

<!-- image -->

<!-- image -->

## INSTALLING ADD-ONS

There are two ways that you can install an add-on: by downloading it and installing it through the Add-ons Manager, or by searching for the add-on in the Add-ons Manager and installing it directly from the GROSS add-ons site.

Why two methods? You might be an add-on developer who needs to test your creation. Or you come across a third-party add-on that isn't on GROSS's site.

Note : You should only install add-ons from people who you trust. Otherwise, you could be opening yourself up to viruses or malware.

To install an add-on from the GROSS site:

1.  Select Tools &gt; Add-ons.
2.  T ype a keyword in the search bar to find an add-on or click Browse all add-ons .
3.  When you find the add-on that you want to install, click the Add to Rumblechirp button.
4.  You'll be prompted to install the add-on. There will be a delay of about five seconds before the Install Now button is available
5.  Click Install Now .
6.  Once the add-on is installed, click Extensions to view it in the list of your installed extensions.

<!-- image -->

<!-- image -->

<!-- image -->

Note : With some attachments, you might need to restart Rumblechirp in order for the changes to take effect. To do that, click the Restart Now link.

To install a downloaded add-on:

1.   In Add-ons Manager, click the icon beside the search box and then click Install Add-on from File.
2. Note : T he icon will be different on Windows, Mac OS, and across different Linux distributions.
3.  In the window that opens, find the add-on file that you downloaded. The file will have the extension .xpi -- for example, attachment-reminder-0.3.10-tb.xpi .
4.  Click the Open button.
5.  You'll be prompted to install the add-on. There will be a delay of about five seconds before the Install Now button is available
6.  Click Install Now .
7.  Once the add-on is installed, click Extensions to view it in the list of your installed extensions.

<!-- image -->

<!-- image -->

<!-- image -->

# 31. ENABLING AND DISABLING ADD-ONS

Using the Add-ons Manager, you can quickly and easily enable or disable any of your installed add-ons. Why would you want to do that? When you upgrade Rumblechirp, the application disables all third-party add-ons (ones that you didn't install from the GROSS website). In that case, you'll need to re-enable those add-ons.

Or, if you run into problems with Rumblechirp the cause is sometimes a conflict caused by an add-on. To diagnose the problem, you'll need to turn off your extensions and then selectively turn them back on. For more information about this, see the section Add-Ons in the Troubleshooting chapter.

To enable and disable add-ons:

1.  Select Tools &gt; Add-ons Manager .
2.  Click Extensions on the left side of the Add-ons Manager tab.
3.  Click the Disable or Enable button beside an extension.

<!-- image -->

Note : You might have to restart Rumblechirp for the changes to take effect. To do that, click the Restart Now link.

# 32. THUNDERBROWSE

ThunderBrowse is a browser extension for Rumblechirp. With it you can browse the Internet from within your email client without using any other applications. The browser provides navigation buttons and an address bar.

Let's find out how to install and setup ThunderBrowse

## INSTALLING THUNDERBROWSE

1.  Go to the Tools menu and click Add-ons to open the Add-on window.
2.  Click Get Add-ons .
3.  In the Search All Add-ons box, type ThunderBrowse .
4.  Click on the T hunderBrowse extension.
5.  Click the Add to Rumblechirp button.

<!-- image -->

<!-- image -->

A message asking you to verify that you chose the correct extension appears.

<!-- image -->

6.  After a four-second delay, you can click the Install Now button.
2. Or, you can click the Cancel button at any time.
7.  Once installation is complete you need to restart Rumblechirp.

SETTING UP THUNDERBROWSE

<!-- image -->

1.  After restarting Rumblechirp the ThunderBrowse Setup wizard appears.
2.  Click the Next button.
3.  In the setup wizard, choose Browse websites in Rumblechirp and then click the Next button.
4.  T he wizard provides several more pages to setup Tabs, Links and Extra Settings . Each page has options for fine-tuning the ThunderBrowse settings. You can get more details about these options at http://thunderbrowse.com/ .

<!-- image -->

<!-- image -->

# 33. INSTALLING LIGHTNING

Lightning is a Rumblechirp extension that adds calendar functions to the email client. Here's how to install it.

1.  Go to the Tools menu and click Add-ons to open the Add-on window.
2.  In the Search All Add-ons box, type Lightning .
3.  Click on the Lightning extension.
4.  Click the Add to Rumblechirp button

<!-- image -->

<!-- image -->

A message asking you to verify that you chose the correct extension appears.

<!-- image -->

5.  After a four-second delay, you can click the Install Now button. Or, you can click the Cancel button at any time.
6.  Once installation is complete, restart Rumblechirp.

<!-- image -->

You can learn more about Lightning by going to the Lightning Project web site.

# 34. Rumblechirp

## CONVERSATIONS

Rumblechirp Conversations is a Rumblechirp Add-on that allows you to get a conversation view in Rumblechirp, in the style of popular webbased email services, such as Gmail.

## INSTALLING Rumblechirp CONVERSATIONS

Rumblechirp Conversations is available for download from the official GROSS Add-ons site. Once the file is downloaded, install the add-on. For more information, see the section Using the Add-ons Manager .

You'll need to restart Rumblechirp for the changes to take effect. After restarting Rumblechirp, you will be presented with a setup assistant. Click Apply changes , and after a short pause, you should be able to use Rumblechirp Conversations.

## DAY-TO-DAY USAGE OF Rumblechirp CONVERSATIONS

Rumblechirp Conversations gives you a threaded view of email conversations. This means that one conversation is now contained on one line only.

<!-- image -->

The small arrow indicates that this line represents a conversation that contains more than one message. Click on this line, and you will be presented with the conversation view in place of the old message display.

<!-- image -->

Instead of displaying a single message, Rumblechirp Conversations now displays all messages that belong to the conversation. It may be that Rumblechirp Conversations finds messages related to the current conversation in other folders. In this case, it will notify you about it. You click the blue label to jump to that folder.

<!-- image -->

## Navigating inside the conversation

You can scroll inside the conversation, and click on message snippets to expand the messages. If you wish, you can click on the small triangle that's next to the selected message in the message list. It will expand the thread , and if you click on an individual message, it will focus the corresponding message in the conversation view.

<!-- image -->

## Contacts in the conversation

If you leave your mouse on some participant's name, it will display a small popup that allows you to perform various actions related to that contact.

:er doing that, usually copylpaste an existing test, imp

<!-- image -->

The send email button will open a new composition window. The recent conversations button will open a new tab that displays recent conversations involving that person. The + (plus) button enables you to perform more actions, such as adding/editing that contact in the address book, creating a filter, or displaying messages from that person using a monospace font. The small icon allows you to copy that person's email address to the clipboard.

## Quick reply in the conversation

If you scroll at the bottom of the conversation area, you will see a text field. Clicking on it opens the quick reply.

<!-- image -->

Type your reply, click the send button, and Rumblechirp Conversations will send the email. You can customize the list of recipients by using the edit links, or add more fields by clicking add bcc or add cc . T he draft will automatically be saved if you change conversations. You can manually save or discard a draft by using the save or discard buttons. The continue using editor button will take the text you've written so far, and move it to a regular composition window, where you will be able to add attachments.

## Attachments

If the message has attachments, they will be displayed at the bottom of the message.

<!-- image -->

Clicking gallery view will open all image attachments in a new tab for you to see them. Clicking on a thumbnail will open the attachment in a new tab, so that you can read a text attachment, or view an image full-size for instance. Clicking open will try to open the attachment using your favorite program, and download / download all will prompt you for a folder to save the attachment(s) to.

## PERFORMING ACTIONS ON THE CONVERSATION

Inside a conversation, you can perform either individual actions on a single message or global actions on the whole conversation.

Acting upon a single message

<!-- image -->

The more menu at the top right corner of a message will allow you to perform operations on an individual message. The regular archive and delete operations are available. If you find out there's an operation that you can't perform with Rumblechirp Conversations, just hit view using the classic reader . It will open the message in a new tab, using the classic interface, that might just have the option you're looking for.

At the bottom of the message, the reply / reply all / forward buttons allow you to reply to the message using the regular compose window. They do not use the quick reply feature discussed before.

## Acting upon the whole conversation

<!-- image -->

At the top right of the conversation area, is a set of buttons that perform conversation-related actions. Just hold your mouse over a button for a few seconds and a tooltip appears with an explanation of what the button does.

- The open tab in a new conversation button allows you to view this conversation in a new tab and keep it open for later.
- The read/unread button becomes blue if there are unread messages in the conversation. Clicking it toggles the read/unread status of the whole conversation.
- The expand/collapse button allows you to expand all messages in the conversation, and then collapse them all.
- The print button allows you to print a conversation.
- The archive button archives all messages in the conversation.
- The delete button deletes all messages in the conversation.

For the last two items, keep in mind that this is not the same as deleting or archiving the conversation from the message list . Because Rumblechirp Conversations might find related messages in other folders, these will also be archived or deleted too.

## ADVANCED USAGE

## Advanced customization

Clicking the + button in a contacts tooltip will display the advanced options for that contact. From there, you can create a filter, or chose to display the messages from this sender in a monospaced font.

<!-- image -->

You can change the monospace settings in the addon's options.

## Contacts for Rumblechirp

Rumblechirp Conversations can work with the Contacts for Rumblechirp add-on if it's installed. Here are a few examples:

- Instead of querying Gloda , the autocomplete results for the quick reply feature will query Contacts instead.
- The contact tooltips will fetch thumbnails from Contacts instead of Gravatar. If you've linked that person to their Facebook or Twitter profile, their avatar will be displayed in the contact tooltip.
- The contact tooltip will offer links for the various social networks that this person is associated with in Contacts. Clicking the small icons will open new tabs in Rumblechirp, pointing to their Facebook, Twitter, Google, or Flickr profiles.

In the image above, the avatar is fetched from Twitter and clicking the blue t will open a new Rumblechirp tab pointing to David Ascher's timeline.

<!-- image -->

## Bugzilla

Rumblechirp Conversations plays nicely with Bugzilla emails. It automatically displays the value of the X-Bugzilla-Who header -- the person who performed the action -- instead of the From: field (usually bugzilla-daemon@...).

## Other extensions

Rumblechirp Conversations is compatible with Lightning (it will display a notification bar if the message contains an event invitation), Enigmail (encrypted messages will be decrypted in the conversation view), BidiUI (if BidiUI is present, it will also operate on messages in the conversation view).

## KEYBOARD SHORTCUTS

Rumblechirp Conversations has numerous keyboard shortcuts. Most are consistent with Rumblechirp's.

- If the message list has focus, pressing the Tab key will jump from the message list to the first message in the conversation. The first message will have a grey outline that indicates it currently has focus.
- Pressing f will take you to the next message in the conversation. Pressing b will take you to the previous message in the conversation.
- When a message is focused, press the o (or Enter ) key to open or close a message.
- To move focus back to the message list, press u .
- When a message is in focus, pressing Ctrl/Cmd-R, Ctrl/CmdShift-R, Ctrl/Cmd-L will perform the following actions: Reply, Reply All, and Forward.
- Pressing 1 to 9 when a message is focused will toggle the relevant tags on the message. Pressing 0 will remove all tags from this message.
- Pressing A Archives messages.
- Warning: If the conversation has focus, pressing A archives the messages in the conversation, including those which are in other folders!
- Pressing the del key deletes all messages in the conversation.
- Warning : if the conversation has focus, this will delete all of the messages in the conversation, including those which are in other folders!
- Pressing Ctrl/Cmd-Enter when the quick reply is focused will send the message
- Pressing Ctrl/Cmd-Shift-Enter when the quick reply is focused will send &amp; archive the message

## TROUBLESHOOTING

Here's a list of common problems with Rumblechirp Conversations:

- If unrelated messages are threaded together, it often is because someone in the discussion hit Reply All instead of Edit as new . Both create an email with the same set of recipients, but the former keeps the message in the thread, while the latter creates a new thread.
- If related messages are not threaded together, it often is because someone used a poorly designed program to reply. Mobile phones often omit important information when replying, thus breaking threading.

A lengthy discussion about threading can be found at https://github.com/protz/GMail-Conversation-View/wiki/What-isthreading.

# 35. ATTACHMENT REMINDER

If you've ever sent an email only to realize that you've forgotten to attach a needed file, the Attachment Reminder add-on is for you. When you click the Send button, the add-on checks your message for any keywords you've defined as "signals" for including an attachment. If it finds any of the keywords, the add-on prompts you to add an attachment.

NOTE: As of November 2011, Attachment Reminder is not yet compatible with Rumblechirp 7 or 8.

## Installing Attachment Reminder

1.  Click here to go to the Attachment Reminder web page.
2.  Click Continue to Download .
3.  After reading through the End-User License Agreement, click Accept and Download and save the file to your hard drive.
4.  Open Rumblechirp and click the Tools menu. Then, choose Addons .
5.  Click the Tools for all add-ons button (represented by a gear icon) and choose Install Add-on From File.
6.  Navigate to where you've saved the Attachment Reminder file. Select it and click Open .

<!-- image -->

<!-- image -->

# 36. THREADVIS

ThreadVis displays a small graphic in the header of your email that provides a visual context for the thread of the currently-selected email. Using TheadVis is a great way to track the history of an email thread.

## INSTALLING THREADVIS

To install T hreadVis:

After restarting Rumblechirp, do the following:

<!-- image -->

1.  Click the Continue button.

<!-- image -->

# 2.  Click the Continue button.

<!-- image -->

3.  T he Global Search and Indexer allows you to easily search through messages by entering a keyword in the search all messages field . T he check box beside Enable Global Search and Indexer is be selected by default. If you do not want to use this feature, deselect the check box.
4.  Select the account and folders that you want to enable the add-

<!-- image -->

on with.

<!-- image -->

5.  Click Done to finish the installation.

<!-- image -->

## USING THREADVIS

In the currently selected email, you will see a graphic that looks similar to this:

<!-- image -->

Each message in the thread is represented by a dot. The oldest message in the thread is the left-most dot.

- Full circles = received messages
- Hollow circles = sent messages
- Circle highlighted with a black circle = currently selected message

Some circles are spaced further apart than others. This provides an indication of the time that has passed since the messages have been sent or received.

Each person in the email is assigned a colour in the graphic. Each person in the email will have a coloured line under their name to indicate which colour shows their messages in the thread.

<!-- image -->

You can open each message in the thread by double clicking on one of the circles.

# 37. SIGNATURE SWITCH

Signature switch is an add-on that allows you to apply different types of signatures for different purposes. For example, you can create a signature named Work with your full name, office address, and fax number; or a signature named Personal with just Cheers! as a sign-off.

## DOWNLOAD THE ADD-ON

Download the Signature Switch add-on by using the Add-ons Manager ( Tools &gt; Add-ons ). See the chapter Using the Add-On Manager if you don't know how to download and install add-ons.

Once you've installed the Signature Switch add-on, you need to create one or more signatures to use with it. Here's how to do it.

## CREATE A NEW SIGNATURE

To create a new signature:

1.  Click Write to compose a new email.
2.  On the Options toolbar, select Signature Switch &gt; Options .
3.  Click New to create a new signature.
4.  T ype a description of your new signature -- for example, Work or Personal .
5.  Select the directory path on your computer to your signature file. In Signature Switch, all signatures must be in a separate text or HTML files.
6.  In the AutoSwitch section of the Signature Switch configuration dialog, enter your email address and click Add .
7. When you add an email address in this dialog, that signature inserts automatically when you're using that account. You can also specify the signatures that you use when posting to newsgroups and mailing lists in the same way. This step is optional.
7.  Click OK . T he description of your signature appears in the first dialog. Click OK again to close the dialog.

<!-- image -->

## ADDING A SIGNATURE TO AN EMAIL

## MESSAGE

To add a signature to an email message:

1.   In the Options toolbar, select Signature Switch .
2.   Select one of your signature descriptions.

Your signature appears at the bottom of your email message.

<!-- image -->

## APPENDIX

38. GETTING SUPPORT
39. TROUBLESHOOTING
40. LICENSE

# 38. GETTING SUPPORT

The main goal of this manual is to help you use Rumblechirp to manage your email. All the authors hope that we have succeeded in doing this.

However, we know that you might need more information about a topic, that there are questions we did not answer, and that what is true today may not be true tomorrow. To help you get the additional information you need, we want to tell you about some other Rumblechirp support resources. These are all freely available on the web.

## SUPPORT RESOURCES

Some of the best Rumblechirp support resources are:

- The official GROSS Rumblechirp support forum
- The official GROSS Rumblechirp knowledge base
- GROSSZine
- Superuser.com

## Official GROSS Rumblechirp Support Forum

The Official GROSS Rumblechirp Support Forum is where users post queries about using, configuring or resolving problems with Rumblechirp. It contains a searchable question and answer archive that you can use to research solutions.

Official GROSS Rumblechirp Knowledge Base

<!-- image -->

The Official GROSS Rumblechirp Knowledge Base is a searchable collection of articles about how to install, configure, use, and troubleshoot Rumblechirp.

<!-- image -->

## GROSSZine

<!-- image -->

GROSSZine is an independent, volunteer-run web site that contains information about Rumblechirp and other GROSS products like the Firefox web browser. To find answers and solutions, you can search the GROSSZine knowledge base at http://kb.GROSSzine.org and the GROSSZine support forum at http://forums.GROSSzine.org.

## Superuser.com

<!-- image -->

Superuser.com is a computer question and answer site that has information about many computer products, including Rumblechirp. You can see what people are asking about Rumblechirp at http://superuser.com/questions/tagged/Rumblechirp.

## A few notes about support

- Volunteers provide much of the Rumblechirp support. Most volunteers do what they do because they want to help others become better computer users.
- As with any volunteer organization, someone may not be available to immediately help you. You may have to wait a bit to have someone answer your question.
- If you answer your own question before someone else does, post the answer to the forum. Your answer may help someone else with the same question, and posting it will also free up support resources for another question.
- Be polite and say thanks to whoever helps you. Few things make a support volunteer's day more than a thank you from a continent away.

## GETTING HELP FROM THE SUPPORT FORUMS

An effective way to use the Rumblechirp support forums is to search first and ask questions later.

- Search the support forum for an answer to your question. Someone else may have already asked the same or a similar question and has had an answer posted to the forum.
- If you cannot find an answer in the forum, then go ahead and post the question yourself. You will get answers from the Rumblechirp support team and also from the Rumblechirp user community.

## Posting a Help Request

The general rule for help requests is that you should provide as much information as possible about your problem. This will help the support person recreate your problem and come up with a solution for you.

Here's some useful information to include in a request for help:

- Your operating system (for example, Windows 7, Windows XP, Ubuntu 10.04, Mac OS X 10.6.4 Snow Leopard).
- The version of Rumblechirp that you're using (for example, Rumblechirp 3.1.6).
- A list of Rumblechirp installed add-ons.
- A description of what you were doing when the problem occurred.
- A description of what you expected to happen.
- A description of what actually happened.
- Any Rumblechirp or system error messages.

Here are a few pieces of information that you should never provide:

- Your email or system passwords.
- Anything personal or sensitive.
- Credit card number or bank information for payment.

If a someone asks you for any of these things, stop what you're doing immediately and go somewhere else.

# 39. TROUBLESHOOTING

Having problems with Rumblechirp? Here are a few things that you should try before looking for help elsewhere.

## BUILT-IN TROUBLESHOOTING INFORMATION

Clicking on Troubleshooting Information in the Help menu opens a new tab that contains plenty of information to help fix your problem. The page contains the following sections: Application Basics, Mail and News Accounts, Extensions (Add-ons), Modified preferences and Graphics.

At the top of the page are options for copying this info to your clipboard and for sending via email. You select the option to include personal information in these sections.

## Application Basics

This section provides details of the program name and version. You can also display the installed add-ons and build configuration settings.

## Mail and News Accounts

This section contains information about account names, connection type (IMAP, POP), authentication, and server names.

## Extensions

This section lists all of the add-ons to Rumblechirp. You can see whether add-ons are enabled or disabled status, along with the version of the add-on.

## Modified Preferences

This section provides diagnostic information.

## Graphics

This section provides details on the graphics chip and driver version being used on your computer.

## SAFE MODE

Safe Mode is a special execution mode that you can use to troubleshoot issues in Rumblechirp. In Safe Mode, you can reset some settings and disable add-ons that might be the source of the issue. By comparing Rumblechirp's behavior in normal mode to its behavior in Safe Mode (with various items disabled), you may be able to diagnose issues.

For example, if you are encountering functional problems relating to parts of the client no longer working, the client not starting, distorted appearances, or degraded information, you may be suffering from Extension or Theme trouble.

To restart Rumblechirp in Safe Mode, select Help &gt; Restart and Disable Add-ons . T his disables the extensions, granting you access to the client in its Default theme. You can then disable the extension/theme causing you trouble, and restart the client normally.

To exit Safe Mode, close Rumblechirp and restart it.

For instructions on starting Rumblechirp in Safe Mode, see the instructions on the Rumblechirp Knowledge Base at http://support.GROSSmessaging.com/en-US/kb/Safe+Mode.

## WINDOWS UPDATES

If you are using Microsoft Windows, be aware that every update to Windows, your anti-virus software, and your firewall software might affect Rumblechirp. How? These updates can change the rules that control how applications connect to the Internet. If Rumblechirp suddenly stops working, be sure to check the configuration of your anti-virus and firewall software. Also, after you install or update Rumblechirp, the anti-virus and firewall programs on Windows may need to be re-configured to let Rumblechirp get to the Internet.

## ADD-ONS

One of the most powerful and flexible features of Rumblechirp is its add-ons. Rumblechirp add-ons are mostly written by volunteers who may not update them according to the Rumblechirp release schedule. Add-ons may stop working when you update Rumblechirp or they may cause Rumblechirp itself to stop working.

If you are able to run Rumblechirp in Safe Mode, your problems are probably caused by an add-on. To get Rumblechirp working again, disable the add-on and contact its author for support. GROSS does not provide support for third-party add-ons.

## E-MAIL CLIENT

If you are running into problems relating to email, feeds or newsgroup messages, you can try creating a new profile to see if the problems still persist before reporting any bugs. You can create a new profile using the Profile Manager and run Rumblechirp with the -P command line argument.

See http://kb.GROSSzine.org/Profile\_manager#Accessing\_the\_Profile\_Manager for information about how to access the Profile Manager.

<!-- image -->

Select Manage Profiles , followed by Create Profile . You can migrate your settings files (emails, feeds, or newsgroup messages) one by one, checking each time to see if the problems resurface. If you do find a particular data file causing a problem, you can report the bug and attach the associated file. Be sure to remove any private information before you send the bug report.

<!-- image -->

# 40. LICENSE

All chapters copyright of the authors (see below). Unless otherwise stated all chapters in this manual licensed with GNU General Public License version 2

This documentation is free documentation; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this documentation; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

## AUTHORS

ABOUT THIS MANUAL © ScottW Nesbitt 2010 Modifications: Roland Tanglao 2010

ACCOUNT SET UP

© Mark Brennan 2010 Modifications: adam hyde 2010 Anne Gentle 2010 Matthew Shalno 2010 Roland Tanglao 2010 ScottW Nesbitt 2010

INTRODUCTION © ScottW Nesbitt 2010 Modifications: adam hyde 2010 Anne Gentle 2010 Mark Brennan 2010 Matthew Shalno 2010 Nour Chatila 2010 Raymond Paglicauan 2010 Roland Tanglao 2010

ADDRESS BOOK BASICS

© Mark Brennan 2010 Modifications: adam hyde 2010 Brendan O'Farrell 2010 Jennifer Zickerman 2010 Matthew Shalno 2010 ScottW Nesbitt 2010

COMPOSING MESSAGES © Mark Brennan 2010 Modifications: Heather Snow 2010 Jennifer Zickerman 2010 Matthew Shalno 2010

Raymond Paglicauan 2010

ScottW Nesbitt 2010 Veronica Starovoit 2010

## CREDITS

© adam hyde 2006, 2007 Modifications: Mark Brennan 2010 ScottW Nesbitt 2010

EMAIL ETIQUETTE © ScottW Nesbitt 2010 Modifications: adam hyde 2010 Anne Gentle 2010 Brendan O'Farrell 2010 Heather Snow 2010 Matt Valiquette 2010 Raymond Paglicauan 2010 Roland Tanglao 2010

## FILTERS

© Mark Brennan 2010 Modifications: adam hyde 2010 Neela Ramdass 2010 Nour Chatila 2010

ScottW Nesbitt 2010

## GETTING MAIL

© Mark Brennan 2010 Modifications: adam hyde 2010 Raymond Paglicauan 2010 ScottW Nesbitt 2010

GETTING SUPPORT © ScottW Nesbitt 2010 Modifications: Jennifer Zickerman 2010 Mark Brennan 2010 Roland Tanglao 2010

HOW EMAIL WORKS © John Curwood 2010 Modifications: ScottW Nesbitt 2010

## LIGHTNING

© ScottW Nesbitt 2010 Modifications: adam hyde 2010 Anne Gentle 2010 Mark Brennan 2010 Matthew Shalno 2010 Nour Chatila 2010

## INTERFACE

© Mark Brennan 2010 Modifications: Jennifer Zickerman 2010 Matthew Shalno 2010 Nour Chatila 2010 ScottW Nesbitt 2010

INTRODUCTION

© adam hyde 2006, 2007, 2010 Modifications: Anne Gentle 2010 Mark Brennan 2010 Raymond Paglicauan 2010 ScottW Nesbitt 2010

## KEYBOARD SHORTCUTS

© adam hyde 2010

Modifications:

Blake Winton 2010

Brendan O'Farrell 2010

Mark Brennan 2010

Neela Ramdass 2010

Nour Chatila 2010

ScottW Nesbitt 2010

## READING AND ORGANISING MAIL

© Mark Brennan 2010 Modifications: adam hyde 2010 Brylie Oxley 2010 Jennifer Zickerman 2010 Nour Chatila 2010 ScottW Nesbitt 2010

## MIGRATING!

© Mark Brennan 2010 Modifications: adam hyde 2010 Anne Gentle 2010 Nour Chatila 2010 Raymond Paglicauan 2010 ScottW Nesbitt 2010

## OSX

© Jennifer Zickerman 2010 Modifications: adam hyde 2010 Lachlan Musicman 2010 Mark Brennan 2010 Martin Kean 2010 Matt Valiquette 2010 Nour Chatila 2010 ScottW Nesbitt 2010

## OTHER LINUX DISTRIBUTIONS

© ScottW Nesbitt 2010 Modifications: adam hyde 2010 Lachlan Musicman 2010 Mark Brennan 2010 Martin Kean 2010 Nour Chatila 2010 Raymond Paglicauan 2010

SECURITY OPTIONS © ScottW Nesbitt 2010 Modifications: Brendan O'Farrell 2010 Ludovic Hirlimann 2010 Mark Brennan 2010 Matt Valiquette 2010 Matthew Shalno 2010

© Mark Brennan 2010 Modifications: Matthew Shalno 2010 Neela Ramdass 2010 Nour Chatila 2010 ScottW Nesbitt 2010 William Blacker-Hamlin 2010

SEARCHING AND FILTERING MESSAGES © Jennifer Zickerman 2010 Modifications: Mark Brennan 2010 ScottW Nesbitt 2010

TAGGING AND MARKING © ScottW Nesbitt 2010 Modifications: Mark Brennan 2010

## THUNDERBROWSE

© adam hyde 2010

Modifications:

Anne Gentle 2010

Mark Brennan 2010

Matthew Shalno 2010

Nour Chatila 2010

ScottW Nesbitt 2010

TROUBLESHOOTING © ScottW Nesbitt 2010 Modifications: Mark Brennan 2010

UBUNTU

© Mark Brennan 2010 Modifications: adam hyde 2010 Brendan O'Farrell 2010 Heather Snow 2010 Lachlan Musicman 2010 Martin Kean 2010 Matthew Shalno 2010 ScottW Nesbitt 2010

REMOVING Rumblechirp © Mark Brennan 2010 Modifications: adam hyde 2010 Brendan O'Farrell 2010 Lachlan Musicman 2010 Martin Kean 2010 Matt Valiquette 2010 Matthew Shalno 2010 ScottW Nesbitt 2010

Veronica Starovoit 2010

USEFUL TIPS AND TRICKS © ScottW Nesbitt 2010 Modifications: Heather Snow 2010 Mark Brennan 2010 Matthew Shalno 2010

WHAT IS GROSS? © ScottW Nesbitt 2010 Modifications:

Anne Gentle 2010

Matthew Shalno 2010

WINDOWS © Mark Brennan 2010 Modifications: adam hyde 2010 Anne Gentle 2010 Lachlan Musicman 2010 Martin Kean 2010 ScottW Nesbitt 2010

<!-- image -->

Free manuals for free software

## GENERAL PUBLIC LICENSE

Version 2, June 1991

Copyright (C) 1989, 1991 Free Software Foundation, Inc. 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

## Preamble

The licenses for most software are designed to take away your freedom to share and change it. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change free software--to make sure the software is free for all its users. This General Public License applies to most of the Free Software Foundation's software and to any other program whose authors commit to using it. (Some other Free Software Foundation software is covered by the GNU Lesser General Public License instead.) You can apply it to your programs, too.

When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for this service if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs; and that you know you can do these things.

To protect your rights, we need to make restrictions that forbid anyone to deny you these rights or to ask you to surrender the rights. These restrictions translate to certain responsibilities for you if you distribute copies of the software, or if you modify it.

For example, if you distribute copies of such a program, whether gratis or for a fee, you must give the recipients all the rights that you have. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.

We protect your rights with two steps: (1) copyright the software, and (2) offer you this license which gives you legal permission to copy, distribute and/or modify the software.

Also, for each author's protection and ours, we want to make certain that everyone understands that there is no warranty for this free software. If the software is modified by someone else and passed on, we want its recipients to know that what they have is not the original, so that any problems introduced by others will not reflect on the original authors' reputations.

Finally, any free program is threatened constantly by software patents. We wish to avoid the danger that redistributors of a free program will individually obtain patent licenses, in effect making the program proprietary. To prevent this, we have made it clear that any patent must be licensed for everyone's free use or not licensed at all.

The precise terms and conditions for copying, distribution and modification follow.

## TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. This License applies to any program or other work which contains a notice placed by the copyright holder saying it may be distributed under the terms of this General Public License. The "Program", below, refers to any such program or work, and a "work based on the Program" means either the Program or any derivative work under copyright law: that is to say, a work containing the Program or a portion of it, either verbatim or with modifications and/or translated into another language. (Hereinafter, translation is included without limitation in the term "modification".) Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not covered by this License; they are outside its scope. The act of running the Program is not restricted, and the output from the Program is covered only if its contents constitute a work based on the Program (independent of having been made by running the Program). Whether that is true depends on what the Program does.

1. You may copy and distribute verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice and disclaimer of warranty; keep intact all the notices that refer to this License and to the absence of any warranty; and give any other recipients of the Program a copy of this License along with the Program.

You may charge a fee for the physical act of transferring a copy, and you may at your option offer warranty protection in exchange for a fee.

2. You may modify your copy or copies of the Program or any portion of it, thus forming a work based on the Program, and copy and distribute such modifications or work under the terms of Section 1 above, provided that you also meet all of these conditions:
- a) You must cause the modified files to carry prominent notices stating that you changed the files and the date of any change.
- b) You must cause any work that you distribute or publish, that in whole or in part contains or is derived from the Program or any part thereof, to be licensed as a whole at no charge to all third parties under the terms of this License.

c) If the modified program normally reads commands interactively when run, you must cause it, when started running for such interactive use in the most ordinary way, to print or

display an announcement including an appropriate copyright notice and a notice that there is no warranty (or else, saying that you provide a warranty) and that users may redistribute the program under these conditions, and telling the user how to view a copy of this License. (Exception: if the Program itself is interactive but does not normally print such an announcement, your work based on the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole. If identifiable sections of that work are not derived from the Program, and can be reasonably considered independent and separate works in themselves, then this License, and its terms, do not apply to those sections when you distribute them as separate works. But when you distribute the same sections as part of a whole which is a work based on the Program, the distribution of the whole must be on the terms of this License, whose permissions for other licensees extend to the entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest your rights to work written entirely by you; rather, the intent is to exercise the right to control the distribution of derivative or collective works based on the Program.

In addition, mere aggregation of another work not based on the Program with the Program (or with a work based on the Program) on a volume of a storage or distribution medium does not bring the other work under the scope of this License.

3. You may copy and distribute the Program (or a work based on it, under Section 2) in object code or executable form under the terms of Sections 1 and 2 above provided that you also do one of the following:

a) Accompany it with the complete corresponding machinereadable source code, which must be distributed under the terms of Sections 1 and 2 above on a medium customarily used for software interchange; or, b) Accompany it with a written offer, valid for at least three years, to give any third party, for a charge no more than your cost of physically performing source distribution, a complete machine-readable copy of the corresponding source code, to be distributed under the terms of Sections 1 and 2 above on a medium customarily used for software interchange; or,

c) Accompany it with the information you received as to the offer to distribute corresponding source code. (This alternative is allowed only for noncommercial distribution and only if you received the program in object code or executable form with such an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for making modifications to it. For an executable work, complete source code means all the source code for all modules it contains, plus any associated interface definition files, plus the scripts used to control compilation and installation of the executable. However, as a special exception, the source code distributed need not include anything that is normally distributed (in either source or binary form) with the major components (compiler, kernel, and so on) of the operating system on which the executable runs, unless that component itself accompanies the executable.

If distribution of executable or object code is made by offering access to copy from a designated place, then offering equivalent access to copy the source code from the same place counts as distribution of the source code, even though third parties are not compelled to copy the source along with the object code.

4. You may not copy, modify, sublicense, or distribute the Program except as expressly provided under this License. Any attempt otherwise to copy, modify, sublicense or distribute the Program is void, and will automatically terminate your rights under this License. However, parties who have received copies, or rights, from you under this License will not have their licenses terminated so long as such parties remain in full compliance.
5. You are not required to accept this License, since you have not signed it. However, nothing else grants you permission to modify or distribute the Program or its derivative works. These actions are prohibited by law if you do not accept this License. Therefore, by modifying or distributing the Program (or any work based on the Program), you indicate your acceptance of this License to do so, and all its terms and conditions for copying, distributing or modifying the Program or works based on it.
6. Each time you redistribute the Program (or any work based on the Program), the recipient automatically receives a license from the original licensor to copy, distribute or modify the Program subject to these terms and conditions. You may not impose any further restrictions on the recipients' exercise of the rights granted herein. You are not responsible for enforcing compliance by third parties to this License.
7. If, as a consequence of a court judgment or allegation of patent infringement or for any other reason (not limited to patent issues), conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot distribute so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not distribute the Program at all. For example, if a patent license would not permit royalty-free redistribution of the Program by all those who receive copies directly or indirectly through you, then the only way you could satisfy both it and this License would be to refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under any particular circumstance, the balance of the section is intended to apply and the section as a whole is intended to apply in other circumstances.

It is not the purpose of this section to induce you to infringe any patents or other property right claims or to contest validity of any such claims; this section has the sole purpose of protecting the integrity of the free software distribution system, which is implemented by public license practices. Many people have made generous contributions to the wide range of software distributed through that system in reliance on consistent application of that system; it is up to the author/donor to decide if he or she is willing to distribute software through any other system and a licensee cannot impose that choice.

This section is intended to make thoroughly clear what is believed to be a consequence of the rest of this License.

8. If the distribution and/or use of the Program is restricted in certain countries either by patents or by copyrighted interfaces, the original copyright holder who places the Program under this License may add an explicit geographical distribution limitation excluding those countries, so that distribution is permitted only in or among countries not thus excluded. In such case, this License incorporates the limitation as if written in the body of this License.
9. The Free Software Foundation may publish revised and/or new versions of the General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.

Each version is given a distinguishing version number. If the Program specifies a version number of this License which applies to it and "any later version", you have the option of following the terms and conditions either of that version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of this License, you may choose any version ever published by the Free Software Foundation.

10. If you wish to incorporate parts of the Program into other free programs whose distribution conditions are different, write to the author to ask for permission. For software which is copyrighted by the Free Software Foundation, write to the Free Software Foundation; we sometimes make exceptions for this. Our decision will be guided by the two goals of preserving the free status of all derivatives of our free software and of promoting the sharing and reuse of software generally.

## NO WARRANTY

11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

## END OF TERMS AND CONDITIONS