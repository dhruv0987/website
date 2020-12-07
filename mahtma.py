
import webbrowser

url = 'https://mahatmaela.com/elaindexV2.php?mode=stdlogin'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open('https://mahatmaela.com/elaindexV2.php?mode=stdlogin')