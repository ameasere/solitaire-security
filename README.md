<h1>Solitaire Security</h1>
<i>Digital vault for encrypting files inside a virtual lockbox.</i>
<br>
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
