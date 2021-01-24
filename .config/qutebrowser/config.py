# Autogenerated config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Always restore open sites when qutebrowser is reopened. Without this
# option set, `:wq` (`:quit --save`) needs to be used to save open tabs
# (and restore them), while quitting qutebrowser in any other way will
# not save/restore the session. By default, this will save to the
# session which was last loaded. This behavior can be customized via the
# `session.default_name` setting.
# Type: Bool
c.auto_save.session = True

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Directory to save downloads to. If unset, a sensible OS-specific
# default is used.
# Type: Directory
c.downloads.location.directory = '~/Clipboard/'

# Which categories to show (in which order) in the :open completion.
# Type: FlagList
# Valid values:
#   - searchengines
#   - quickmarks
#   - bookmarks
#   - history
c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history']

# Default program used to open downloads. If null, the default internal
# handler is used. Any `{}` in the string will be expanded to the
# filename, else the filename will be appended.
# Type: String
c.downloads.open_dispatcher = None

# Editor (and arguments) to use for the `open-editor` command. The
# following placeholders are defined:  * `{file}`: Filename of the file
# to be edited. * `{line}`: Line in which the caret is found in the
# text. * `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ['gvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']

# Encoding to use for the editor.
# Type: Encoding
c.editor.encoding = 'utf-8'

# CSS border value for hints.
# Type: String
c.hints.border = '0px solid #EEEEEE'

# Show a filebrowser in download prompts.
# Type: Bool
c.prompt.filebrowser = True

# Rounding radius (in pixels) for the edges of prompts.
# Type: Int
c.prompt.radius = 6

# When/how to show the scrollbar.
# Type: String
# Valid values:
#   - always: Always show the scrollbar.
#   - never: Never show the scrollbar.
#   - when-searching: Show the scrollbar when searching for text in the webpage. With the QtWebKit backend, this is equal to `never`.
#   - overlay: Show an overlay scrollbar. With Qt < 5.11 or on macOS, this is unavailable and equal to `when-searching`; with the QtWebKit backend, this is equal to `never`. Enabling/disabling overlay scrollbars requires a restart.
c.scrolling.bar = 'when-searching'

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# Type: Bool
c.scrolling.smooth = True

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
# for a blank page.
# Type: FuzzyUrl
c.url.default_page = 'https://google.com'

# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`).  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://google.com/search?query={}'}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'https://google.com'

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = ['#EEEEEE', '#EEEEEE', '#EEEEEE']

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#333333'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#333333'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#EEEEEE'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#222222'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#222222'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#222222'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#222222'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#BBBBBB'

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#BBBBBB'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#BBBBBB'

# Foreground color of the matched text in the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.match.fg = '#222222'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#EEEEEE'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = '#EEEEEE'

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = '#222222'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#222222'

# Color gradient start for download text.
# Type: QtColor
c.colors.downloads.start.fg = '#222222'

# Color gradient start for download backgrounds.
# Type: QtColor
c.colors.downloads.start.bg = '#EEEEEE'

# Color gradient end for download text.
# Type: QtColor
c.colors.downloads.stop.fg = '#EEEEEE'

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = '#222222'

# Color gradient interpolation system for download backgrounds.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'rgb'

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = '#EEEEEE'

# Background color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.bg = '#222222'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#222222'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = '#EEEEEE'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#BBBBBB'

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = '#EEEEEE'

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = '#BBBBBB'

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = '#333333'

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = '#EEEEEE'

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = '#FF2222'

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = '#FF2222'

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = '#EEEEEE'

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = '#222222'

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = '#222222'

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = '#EEEEEE'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#222222'

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = '#222222'

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = '#EEEEEE'

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '#333333'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#333333'

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = '#222222'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#EEEEEE'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#222222'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#222222'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#EEEEEE'

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = '#EEEEEE'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#222222'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#EEEEEE'

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = '#222222'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#EEEEEE'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#222222'

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = '#EEEEEE'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#222222'

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = '#EEEEEE'

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = '#222222'

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = '#EEEEEE'

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = '#222222'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#EEEEEE'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#EEEEEE'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#FF2222'

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = '#EEEEEE'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#EEEEEE'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#EEEEEE'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#FF2222'

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#222222'

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = '#0000FF'

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = '#00FF00'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#FF2222'

# Color gradient interpolation system for the tab indicator.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'rgb'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#EEEEEE'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#222222'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#EEEEEE'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#222222'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#222222'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#EEEEEE'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#222222'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#EEEEEE'

# Foreground color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.fg = '#222222'

# Background color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.bg = '#222222'

# Foreground color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.fg = '#222222'

# Background color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.bg = '#333333'

# Foreground color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.fg = '#222222'

# Background color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.bg = '#EEEEEE'

# Foreground color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.fg = '#222222'

# Background color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.bg = '#BBBBBB'

# Background color for webpages if unset (or empty to use the theme's
# color).
# Type: QtColor
c.colors.webpage.bg = '#FFFFFF'

# Default font families to use. Whenever "default_family" is used in a
# font setting, it's replaced with the fonts listed here. If set to an
# empty value, a system-specific monospace default is used.
# Type: List of Font, or Font
c.fonts.default_family = ['xos4 Terminus', 'Terminus', 'Monospace', 'DejaVu Sans Mono', 'Monaco', 'Bitstream Vera Sans Mono', 'Andale Mono', 'Courier New', 'Courier', 'Liberation Mono', 'Noto Sans', 'Fixed', 'Consolas', 'Terminal']

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = '10pt Noto Sans'

# Font used in the completion categories.
# Type: Font
c.fonts.completion.category = 'bold 10pt Noto Sans'

# Font used for the debugging console.
# Type: Font
c.fonts.debug_console = '10pt Noto Sans'

# Font used for the downloadbar.
# Type: Font
c.fonts.downloads = '10pt Noto Sans'

# Font used for the hints.
# Type: Font
c.fonts.hints = 'bold 10pt Noto Sans'

# Font used in the keyhint widget.
# Type: Font
c.fonts.keyhint = '10pt Noto Sans'

# Font used for error messages.
# Type: Font
c.fonts.messages.error = '10pt Noto Sans'

# Font used for info messages.
# Type: Font
c.fonts.messages.info = '10pt Noto Sans'

# Font used for warning messages.
# Type: Font
c.fonts.messages.warning = '10pt Noto Sans'

# Font used for prompts.
# Type: Font
c.fonts.prompts = '10pt Noto Sans'

# Font used in the statusbar.
# Type: Font
c.fonts.statusbar = '10pt Noto Sans'

# Font used for selected tabs.
# Type: Font
c.fonts.tabs.selected = '10pt Noto Sans'

# Font used for unselected tabs.
# Type: Font
c.fonts.tabs.unselected = '10pt Noto Sans'

# Bindings for normal mode
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('L', 'forward')
config.unbind('v')

c.aliases['zotero'] = "spawn --userscript qute-zotero"
c.aliases['Zotero'] = "hint links userscript qute-zotero"
c.aliases['bibtex'] = "spawn --userscript getbib"

config.bind('a', 'zotero')
config.bind('A', 'Zotero')