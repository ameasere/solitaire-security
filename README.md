<h1>Solitaire Security</h1>
<i>Digital vault for encrypting files inside a virtual lockbox.</i>
<br><br>
Solitaire Security is a digital vault that encrypts the contents of files, and will lock them inside an encrypted zip archive. Credit goes to
developer and PyPi package creator Anthon from Ruamel, for the package ruamel.std.zipfile which we tailored to allow for password handling
and encrypted zip archives. Solitaire Security works offline - with a local server that acts as an interface, and online with our global server that acts
as an interface too. Our vault uses SHA-384 salted hashes along with AES-CBC 256 bit encryption. Users' data will be kept in zip files client side, but
their encryption and decryption keys will be stored in a database on our end/local server-side. All salts, keys and IVs are randomly generated at the time the
user creates their account - and they aren't some <i>password123!</i> type "randomisation" that your 80 year old grandmother might use because she forgets
her passwords too easily. With our system, GCM keys will have a chance of 1 in 1e+32 chance to be guessed first time... that's a lot of 0s. IVs will have a 1 in 1E+16 chance to be guessed first time too... that's half as much 0s, but still a lot to keep people out of your business; especially seeing as hardware today will still struggle to guess both of these in parallel in a timely fashion.

<br>
If we already have you hooked in, you can download the archive [here:](https://enigmapr0ject.live#download) or click the download button on this repository. You
can also clone the repository with `git` on UNIX if that is easier for you.

Here is what your very own personal vault looks like:
![login](https://enigmapr0ject.live/demo/login.jpeg)
![menu](https://enigmapr0ject.live/demo/solitairesec.jpg)
![demo](https://enigmapr0ject.live/demo/contents.jpeg)
<br>
<h2>Installation</h2><br>
<p>Follow the instructions <a href=https://enigmapr0ject.live#installation>here</a>, please make sure you have a supported operating system. So far,
Windows 8, 10, Ubuntu & Debian, and Arch Linux are the currently supported systems although they may work on macOS and other OS too. If you modify
the code to work and be supported on any system that isn't currently supported, please submit an issue with "feature-request", submit a pull request
with your changes or send me an email.</p><br>
        <h2>Contents</h2><br>
        You will find folders named: <b>PHP, backups, Windows, UNIX, __pycache__ and .idea</b> with a file named bg3.gif. Here is what they do:<br>
        <br><b>/PHP</b> are the server files you will need if you plan on using this framework with your own server as an API. These need to placed in your DocumentRoot according to your Apache/Nginx virtualhost.<br>
        <br><b>/backups</b> are backup Python files in case the ones you are using get messed up or disappear somehow. You can always download the archive again with the link above.<br>
        <br><b>/Windows</b> is the directory for Windows users. You will find a Local and a Global .py file to use as open source code, and you will find a Local and Global EXE file. These EXEs were compiled with MinGW/GCC and so
        they do not have icons or a signed certificate. These are legitimate executables and you can see that if you run them through a debugger. These are around 30K lines of code, so they may take a while to start on low end hardware.<br>
        <br><b>/UNIX</b> is the directory for UNIX users. You will find a Local and Global .py file to use as open source code, and you will find a Local and Global ELF/Executable file. These were compiled with GCC and so have no icons or .desktop
        files attached. These files will need a trigger through terminal or a system service. You cannot run these simply by double-clicking them.
        <br><br><b>/__pycache__</b> are files used by Python-related programs during compilation, runtime and other processes. Keep these here but do not modify them.
        <br><br><b>/.idea</b> is a folder created by my JetBrains IDE while developing this framework. You can remove this if you like, but if you are using PyCharm, these can be very useful for you.
        <br><br><i>bg3.gif</i> is the animation on the Login screen for Solitaire Security. You can remove this if you don't want it, but you will need to edit the Python source code so that the script won't try and load it (do not remove
        if you plan to use the executables).<br><br>
        File integrity can be checked with the SHA-1 checksum listed on the download, unless your archives get saved locally or you start changing source code. Please do be aware that Solitaire Security is NOT an active security framework,
        so will not actively scan for threats nor act as a firewall. It is a passive vault built to withstand penetration and unwanted spying.<br><br>
        <b style="color: red;">Important: If you somehow cannot retrieve data encrypted via your GCM keys on the global framework, please submit a request <a href="#contact">here</a> to retrieve your keys. Please do note that once your keyys have been disclosed, you will
        have new keys regenerated automatically for you as part of our protocol. If you would like your entire account removed, please also submit a request for that. Your data will not be retrievable once discarded from our database.</b>
    </p>
    <p>We provide these projects for free, and work tirelessly to make them. In order to keep our servers running, because they don't run on magic, we are self-funded. If you would like to contribute and help out, please do donate
    with the QR code linked below. We only accept BitCoin as payment due to the costs of implementing an actual payment service into the website. BitCoin is untraceable, secure and lightning-fast. All donations are appreciated existentially,
    and will go towards keeping our servers up and running.</p>
