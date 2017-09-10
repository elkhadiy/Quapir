## Notifications

We will probably want to have notifications pop up. It seems that this is not well handled on windows, but for linux we could use [notify2][1.1]. For Mac, there is [a simple snippet][1.2] 

[1.1]: https://pypi.python.org/pypi/notify2
[1.2]: https://weareopensource.me/2015/04/11/python-osx/

## System tray
There is such possible thing [with Qt][2.1]. However, it allows only for an icon to be put. It might be useful to display instead text.

[2.1]: http://pyqt.sourceforge.net/Docs/PyQt5/api/QtWidgets/qsystemtrayicon.html#PyQt5-QtWidgets-QSystemTrayIcon