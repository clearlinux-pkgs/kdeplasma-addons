#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kdeplasma-addons
Version  : 5.16.3
Release  : 24
URL      : https://download.kde.org/stable/plasma/5.16.3/kdeplasma-addons-5.16.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.16.3/kdeplasma-addons-5.16.3.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.16.3/kdeplasma-addons-5.16.3.tar.xz.sig
Summary  : All kind of addons to improve your Plasma experience
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kdeplasma-addons-data = %{version}-%{release}
Requires: kdeplasma-addons-lib = %{version}-%{release}
Requires: kdeplasma-addons-license = %{version}-%{release}
Requires: kdeplasma-addons-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kholidays-dev
BuildRequires : kross-dev
BuildRequires : krunner-dev
BuildRequires : plasma-framework-dev
BuildRequires : qtwebengine-dev

%description
Wikipedia Runner
========================
This runner searches on Wikipedia for the term typed into KRunner.

%package data
Summary: data components for the kdeplasma-addons package.
Group: Data

%description data
data components for the kdeplasma-addons package.


%package dev
Summary: dev components for the kdeplasma-addons package.
Group: Development
Requires: kdeplasma-addons-lib = %{version}-%{release}
Requires: kdeplasma-addons-data = %{version}-%{release}
Provides: kdeplasma-addons-devel = %{version}-%{release}
Requires: kdeplasma-addons = %{version}-%{release}
Requires: kdeplasma-addons = %{version}-%{release}

%description dev
dev components for the kdeplasma-addons package.


%package lib
Summary: lib components for the kdeplasma-addons package.
Group: Libraries
Requires: kdeplasma-addons-data = %{version}-%{release}
Requires: kdeplasma-addons-license = %{version}-%{release}

%description lib
lib components for the kdeplasma-addons package.


%package license
Summary: license components for the kdeplasma-addons package.
Group: Default

%description license
license components for the kdeplasma-addons package.


%package locales
Summary: locales components for the kdeplasma-addons package.
Group: Default

%description locales
locales components for the kdeplasma-addons package.


%prep
%setup -q -n kdeplasma-addons-5.16.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562725355
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1562725355
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdeplasma-addons
cp COPYING %{buildroot}/usr/share/package-licenses/kdeplasma-addons/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kdeplasma-addons/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang plasma_applet_org.kde.plasma.binaryclock
%find_lang plasma_applet_org.kde.plasma.calculator
%find_lang plasma_applet_org.kde.plasma.colorpicker
%find_lang plasma_applet_org.kde.plasma.comic
%find_lang plasma_applet_org.kde.plasma.diskquota
%find_lang plasma_applet_org.kde.plasma.fifteenpuzzle
%find_lang plasma_applet_org.kde.plasma.fuzzyclock
%find_lang plasma_applet_org.kde.plasma.konsoleprofiles
%find_lang plasma_applet_org.kde.plasma.mediaframe
%find_lang plasma_applet_org.kde.plasma.notes
%find_lang plasma_applet_org.kde.plasma.private.grouping
%find_lang plasma_applet_org.kde.plasma.quicklaunch
%find_lang plasma_applet_org.kde.plasma.quickshare
%find_lang plasma_applet_org.kde.plasma.systemloadviewer
%find_lang plasma_applet_org.kde.plasma.timer
%find_lang plasma_applet_org.kde.plasma.userswitcher
%find_lang plasma_applet_org.kde.plasma.weather
%find_lang plasma_packagestructure_comic
%find_lang plasma_runner_CharacterRunner
%find_lang plasma_runner_converterrunner
%find_lang plasma_runner_datetime
%find_lang plasma_runner_katesessions
%find_lang plasma_runner_krunner_dictionary
%find_lang plasma_runner_mediawiki
%find_lang plasma_runner_spellcheckrunner
%find_lang plasma_applet_org.kde.plasma.keyboardindicator
%find_lang plasma_applet_org.kde.plasma_applet_dict
%find_lang plasma_calendar_astronomicalevents
%find_lang plasma_runner_konsoleprofiles

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/scalable/apps/accessories-dictionary.svgz
/usr/share/icons/hicolor/scalable/apps/fifteenpuzzle.svgz
/usr/share/kdevappwizard/templates/plasmapotdprovider.tar.bz2
/usr/share/knsrcfiles/comic.knsrc
/usr/share/kservices5/kwin/kwin4_desktop_switcher_previews.desktop
/usr/share/kservices5/kwin/kwin4_window_switcher_big_icons.desktop
/usr/share/kservices5/kwin/kwin4_window_switcher_compact.desktop
/usr/share/kservices5/kwin/kwin4_window_switcher_informative.desktop
/usr/share/kservices5/kwin/kwin4_window_switcher_present_windows.desktop
/usr/share/kservices5/kwin/kwin4_window_switcher_small_icons.desktop
/usr/share/kservices5/kwin/kwin4_window_switcher_text.desktop
/usr/share/kservices5/kwin/kwin4_window_switcher_thumbnails.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.activitypager.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.binaryclock.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.calculator.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.colorpicker.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.comic.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.diskquota.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.fifteenpuzzle.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.fuzzyclock.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.grouping.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.keyboardindicator.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.kickerdash.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.konsoleprofiles.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.mediaframe.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.notes.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.private.grouping.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.quicklaunch.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.quickshare.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.systemloadviewer.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.timer.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.userswitcher.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.weather.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.webbrowser.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma_applet_dict.desktop
/usr/share/kservices5/plasma-dataengine-comic.desktop
/usr/share/kservices5/plasma-dataengine-konsoleprofiles.desktop
/usr/share/kservices5/plasma-dataengine-potd.desktop
/usr/share/kservices5/plasma-runner-character.desktop
/usr/share/kservices5/plasma-runner-character_config.desktop
/usr/share/kservices5/plasma-runner-converter.desktop
/usr/share/kservices5/plasma-runner-datetime.desktop
/usr/share/kservices5/plasma-runner-dictionary.desktop
/usr/share/kservices5/plasma-runner-dictionary_config.desktop
/usr/share/kservices5/plasma-runner-katesessions.desktop
/usr/share/kservices5/plasma-runner-konsoleprofiles.desktop
/usr/share/kservices5/plasma-runner-spellchecker.desktop
/usr/share/kservices5/plasma-runner-spellchecker_config.desktop
/usr/share/kservices5/plasma-wallpaper-org.kde.haenau.desktop
/usr/share/kservices5/plasma-wallpaper-org.kde.hunyango.desktop
/usr/share/kservices5/plasma-wallpaper-org.kde.potd.desktop
/usr/share/kservicetypes5/plasma_comicprovider.desktop
/usr/share/kwin/desktoptabbox/previews/contents/ui/main.qml
/usr/share/kwin/desktoptabbox/previews/metadata.desktop
/usr/share/kwin/tabbox/big_icons/contents/ui/IconTabBox.qml
/usr/share/kwin/tabbox/big_icons/contents/ui/main.qml
/usr/share/kwin/tabbox/big_icons/metadata.desktop
/usr/share/kwin/tabbox/compact/contents/ui/main.qml
/usr/share/kwin/tabbox/compact/metadata.desktop
/usr/share/kwin/tabbox/informative/contents/ui/main.qml
/usr/share/kwin/tabbox/informative/metadata.desktop
/usr/share/kwin/tabbox/present_windows/contents/ui/main.qml
/usr/share/kwin/tabbox/present_windows/metadata.desktop
/usr/share/kwin/tabbox/small_icons/contents/ui/IconTabBox.qml
/usr/share/kwin/tabbox/small_icons/contents/ui/main.qml
/usr/share/kwin/tabbox/small_icons/metadata.desktop
/usr/share/kwin/tabbox/text/contents/ui/main.qml
/usr/share/kwin/tabbox/text/metadata.desktop
/usr/share/kwin/tabbox/thumbnails/contents/ui/main.qml
/usr/share/kwin/tabbox/thumbnails/metadata.desktop
/usr/share/metainfo/org.kde.haenau.appdata.xml
/usr/share/metainfo/org.kde.hunyango.appdata.xml
/usr/share/metainfo/org.kde.plasma.activitypager.appdata.xml
/usr/share/metainfo/org.kde.plasma.binaryclock.appdata.xml
/usr/share/metainfo/org.kde.plasma.calculator.appdata.xml
/usr/share/metainfo/org.kde.plasma.colorpicker.appdata.xml
/usr/share/metainfo/org.kde.plasma.comic.appdata.xml
/usr/share/metainfo/org.kde.plasma.diskquota.appdata.xml
/usr/share/metainfo/org.kde.plasma.fifteenpuzzle.appdata.xml
/usr/share/metainfo/org.kde.plasma.fuzzyclock.appdata.xml
/usr/share/metainfo/org.kde.plasma.grouping.appdata.xml
/usr/share/metainfo/org.kde.plasma.keyboardindicator.appdata.xml
/usr/share/metainfo/org.kde.plasma.kickerdash.appdata.xml
/usr/share/metainfo/org.kde.plasma.konsoleprofiles.appdata.xml
/usr/share/metainfo/org.kde.plasma.mediaframe.appdata.xml
/usr/share/metainfo/org.kde.plasma.notes.appdata.xml
/usr/share/metainfo/org.kde.plasma.quicklaunch.appdata.xml
/usr/share/metainfo/org.kde.plasma.quickshare.appdata.xml
/usr/share/metainfo/org.kde.plasma.systemloadviewer.appdata.xml
/usr/share/metainfo/org.kde.plasma.timer.appdata.xml
/usr/share/metainfo/org.kde.plasma.userswitcher.appdata.xml
/usr/share/metainfo/org.kde.plasma.weather.appdata.xml
/usr/share/metainfo/org.kde.plasma.webbrowser.appdata.xml
/usr/share/metainfo/org.kde.plasma_applet_dict.appdata.xml
/usr/share/metainfo/org.kde.potd.appdata.xml
/usr/share/plasma/desktoptheme/default/icons/quota.svg
/usr/share/plasma/desktoptheme/default/weather/wind-arrows.svgz
/usr/share/plasma/desktoptheme/default/widgets/timer.svgz
/usr/share/plasma/plasmoids/org.kde.plasma.activitypager/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.activitypager/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.binaryclock/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.binaryclock/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.binaryclock/contents/ui/BinaryClock.qml
/usr/share/plasma/plasmoids/org.kde.plasma.binaryclock/contents/ui/Dot.qml
/usr/share/plasma/plasmoids/org.kde.plasma.binaryclock/contents/ui/DotColumn.qml
/usr/share/plasma/plasmoids/org.kde.plasma.binaryclock/contents/ui/configGeneral.qml
/usr/share/plasma/plasmoids/org.kde.plasma.binaryclock/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.binaryclock/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.binaryclock/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.calculator/contents/ui/calculator.qml
/usr/share/plasma/plasmoids/org.kde.plasma.calculator/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.calculator/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.colorpicker/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.colorpicker/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.colorpicker/contents/ui/configGeneral.qml
/usr/share/plasma/plasmoids/org.kde.plasma.colorpicker/contents/ui/logic.js
/usr/share/plasma/plasmoids/org.kde.plasma.colorpicker/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.colorpicker/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.colorpicker/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.comic/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.comic/contents/ui/ButtonBar.qml
/usr/share/plasma/plasmoids/org.kde.plasma.comic/contents/ui/ComicBottomInfo.qml
/usr/share/plasma/plasmoids/org.kde.plasma.comic/contents/ui/ComicCentralView.qml
/usr/share/plasma/plasmoids/org.kde.plasma.comic/contents/ui/FullViewWidget.qml
/usr/share/plasma/plasmoids/org.kde.plasma.comic/contents/ui/ImageWidget.qml
/usr/share/plasma/plasmoids/org.kde.plasma.comic/contents/ui/configAdvanced.qml
/usr/share/plasma/plasmoids/org.kde.plasma.comic/contents/ui/configAppearance.qml
/usr/share/plasma/plasmoids/org.kde.plasma.comic/contents/ui/configGeneral.qml
/usr/share/plasma/plasmoids/org.kde.plasma.comic/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.comic/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.comic/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.diskquota/contents/ui/ListDelegateItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.diskquota/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.diskquota/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.diskquota/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.fifteenpuzzle/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.fifteenpuzzle/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.fifteenpuzzle/contents/ui/FifteenPuzzle.qml
/usr/share/plasma/plasmoids/org.kde.plasma.fifteenpuzzle/contents/ui/Piece.qml
/usr/share/plasma/plasmoids/org.kde.plasma.fifteenpuzzle/contents/ui/blanksquare.svg
/usr/share/plasma/plasmoids/org.kde.plasma.fifteenpuzzle/contents/ui/configAppearance.qml
/usr/share/plasma/plasmoids/org.kde.plasma.fifteenpuzzle/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.fifteenpuzzle/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.fifteenpuzzle/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.fuzzyclock/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.fuzzyclock/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.fuzzyclock/contents/ui/FuzzyClock.qml
/usr/share/plasma/plasmoids/org.kde.plasma.fuzzyclock/contents/ui/configAppearance.qml
/usr/share/plasma/plasmoids/org.kde.plasma.fuzzyclock/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.fuzzyclock/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.fuzzyclock/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.grouping/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.grouping/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.grouping/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.keyboardindicator/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.keyboardindicator/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.keyboardindicator/contents/ui/configAppearance.qml
/usr/share/plasma/plasmoids/org.kde.plasma.keyboardindicator/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.keyboardindicator/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.keyboardindicator/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.kickerdash/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.kickerdash/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.konsoleprofiles/contents/ui/konsoleprofiles.qml
/usr/share/plasma/plasmoids/org.kde.plasma.konsoleprofiles/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.konsoleprofiles/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.mediaframe/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.mediaframe/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.mediaframe/contents/ui/ConfigGeneral.qml
/usr/share/plasma/plasmoids/org.kde.plasma.mediaframe/contents/ui/ConfigPaths.qml
/usr/share/plasma/plasmoids/org.kde.plasma.mediaframe/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.mediaframe/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.mediaframe/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.notes/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.notes/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.notes/contents/ui/configAppearance.qml
/usr/share/plasma/plasmoids/org.kde.plasma.notes/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.notes/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.notes/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.private.grouping/contents/applet/CompactApplet.qml
/usr/share/plasma/plasmoids/org.kde.plasma.private.grouping/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.private.grouping/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.private.grouping/contents/ui/items/AbstractItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.private.grouping/contents/ui/items/PlasmoidItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.private.grouping/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.private.grouping/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.private.grouping/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/ConfigGeneral.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/IconItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/Popup.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/UrlModel.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/layout.js
/usr/share/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quicklaunch/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.quicklaunch/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.quickshare/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quickshare/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.quickshare/contents/ui/PasteMenuItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quickshare/contents/ui/ShareDialog.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quickshare/contents/ui/ShowUrlDialog.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quickshare/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quickshare/contents/ui/settingsGeneral.qml
/usr/share/plasma/plasmoids/org.kde.plasma.quickshare/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.quickshare/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/contents/ui/BarMonitor.qml
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/contents/ui/CircularMonitor.qml
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/contents/ui/ColorSettings.qml
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/contents/ui/CompactBarMonitor.qml
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/contents/ui/ConditionallyLoadedMonitors.qml
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/contents/ui/ConditionallyRoundedRectangle.qml
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/contents/ui/GeneralSettings.qml
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/contents/ui/SystemLoadViewer.qml
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.systemloadviewer/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.timer/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.timer/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.timer/contents/ui/TimerDigit.qml
/usr/share/plasma/plasmoids/org.kde.plasma.timer/contents/ui/TimerView.qml
/usr/share/plasma/plasmoids/org.kde.plasma.timer/contents/ui/configAdvanced.qml
/usr/share/plasma/plasmoids/org.kde.plasma.timer/contents/ui/configAppearance.qml
/usr/share/plasma/plasmoids/org.kde.plasma.timer/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.timer/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.timer/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.userswitcher/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.userswitcher/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.userswitcher/contents/ui/ListDelegate.qml
/usr/share/plasma/plasmoids/org.kde.plasma.userswitcher/contents/ui/configGeneral.qml
/usr/share/plasma/plasmoids/org.kde.plasma.userswitcher/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.userswitcher/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.userswitcher/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/CompactRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/DetailsView.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/ForecastView.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/FullRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/IconAndTextItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/NoticesView.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/SwitchPanel.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/TopPanel.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/config/ConfigAppearance.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/config/ConfigUnits.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/config/ConfigWeatherStation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/config/WeatherStationPicker.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/config/WeatherStationPickerDialog.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.weather/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.weather/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma.webbrowser/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.webbrowser/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.webbrowser/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.webbrowser/metadata.json
/usr/share/plasma/plasmoids/org.kde.plasma_applet_dict/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma_applet_dict/contents/ui/ConfigDictionaries.qml
/usr/share/plasma/plasmoids/org.kde.plasma_applet_dict/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma_applet_dict/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma_applet_dict/metadata.json
/usr/share/plasma/services/org.kde.plasma.dataengine.konsoleprofiles.operations
/usr/share/plasma/wallpapers/org.kde.haenau/contents/ui/BackgroundElement.qml
/usr/share/plasma/wallpapers/org.kde.haenau/contents/ui/BottomBackgroundElement.qml
/usr/share/plasma/wallpapers/org.kde.haenau/contents/ui/RightBackgroundElement.qml
/usr/share/plasma/wallpapers/org.kde.haenau/contents/ui/main.qml
/usr/share/plasma/wallpapers/org.kde.haenau/contents/ui/wallpaper.svgz
/usr/share/plasma/wallpapers/org.kde.haenau/metadata.desktop
/usr/share/plasma/wallpapers/org.kde.haenau/metadata.json
/usr/share/plasma/wallpapers/org.kde.hunyango/contents/ui/main.qml
/usr/share/plasma/wallpapers/org.kde.hunyango/contents/ui/wallpaper.svgz
/usr/share/plasma/wallpapers/org.kde.hunyango/metadata.desktop
/usr/share/plasma/wallpapers/org.kde.hunyango/metadata.json
/usr/share/plasma/wallpapers/org.kde.potd/contents/config/main.xml
/usr/share/plasma/wallpapers/org.kde.potd/contents/ui/config.qml
/usr/share/plasma/wallpapers/org.kde.potd/contents/ui/main.qml
/usr/share/plasma/wallpapers/org.kde.potd/metadata.desktop
/usr/share/plasma/wallpapers/org.kde.potd/metadata.json

%files dev
%defattr(-,root,root,-)
/usr/include/plasma/potdprovider/plasma_potd_export.h
/usr/include/plasma/potdprovider/potdprovider.h
/usr/lib64/cmake/PlasmaPotdProvider/PlasmaPotdProviderConfig.cmake
/usr/lib64/cmake/PlasmaPotdProvider/PlasmaPotdProviderConfigVersion.cmake
/usr/lib64/cmake/PlasmaPotdProvider/PlasmaPotdProviderTargets-relwithdebinfo.cmake
/usr/lib64/cmake/PlasmaPotdProvider/PlasmaPotdProviderTargets.cmake
/usr/lib64/libplasmapotdprovidercore.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libplasmacomicprovidercore.so.1
/usr/lib64/libplasmacomicprovidercore.so.1.0.0
/usr/lib64/libplasmapotdprovidercore.so.1
/usr/lib64/libplasmapotdprovidercore.so.1.0.0
/usr/lib64/qt5/plugins/kcm_krunner_charrunner.so
/usr/lib64/qt5/plugins/kcm_krunner_dictionary.so
/usr/lib64/qt5/plugins/kcm_krunner_spellcheck.so
/usr/lib64/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_comic.so
/usr/lib64/qt5/plugins/krunner_charrunner.so
/usr/lib64/qt5/plugins/krunner_converter.so
/usr/lib64/qt5/plugins/krunner_datetime.so
/usr/lib64/qt5/plugins/krunner_dictionary.so
/usr/lib64/qt5/plugins/krunner_katesessions.so
/usr/lib64/qt5/plugins/krunner_konsoleprofiles.so
/usr/lib64/qt5/plugins/krunner_spellcheck.so
/usr/lib64/qt5/plugins/plasma/applets/org.kde.plasma.grouping.so
/usr/lib64/qt5/plugins/plasma/applets/org.kde.plasma.private.grouping.so
/usr/lib64/qt5/plugins/plasma/applets/plasma_applet_comic.so
/usr/lib64/qt5/plugins/plasma/applets/plasma_applet_weather.so
/usr/lib64/qt5/plugins/plasma/dataengine/plasma_engine_comic.so
/usr/lib64/qt5/plugins/plasma/dataengine/plasma_engine_konsoleprofiles.so
/usr/lib64/qt5/plugins/plasma/dataengine/plasma_engine_potd.so
/usr/lib64/qt5/plugins/plasma_comic_krossprovider.so
/usr/lib64/qt5/plugins/plasmacalendarplugins/astronomicalevents.so
/usr/lib64/qt5/plugins/plasmacalendarplugins/astronomicalevents/AstronomicalEventsConfig.qml
/usr/lib64/qt5/plugins/potd/plasma_potd_apodprovider.so
/usr/lib64/qt5/plugins/potd/plasma_potd_bingprovider.so
/usr/lib64/qt5/plugins/potd/plasma_potd_epodprovider.so
/usr/lib64/qt5/plugins/potd/plasma_potd_flickrprovider.so
/usr/lib64/qt5/plugins/potd/plasma_potd_natgeoprovider.so
/usr/lib64/qt5/plugins/potd/plasma_potd_noaaprovider.so
/usr/lib64/qt5/plugins/potd/plasma_potd_wcpotdprovider.so
/usr/lib64/qt5/qml/org/kde/plasma/private/colorpicker/libcolorpickerplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/colorpicker/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/private/dict/libdictplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/dict/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/private/diskquota/libdiskquotaplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/diskquota/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/private/fifteenpuzzle/libfifteenpuzzleplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/fifteenpuzzle/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/private/mediaframe/libmediaframeplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/mediaframe/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/private/notes/libnotesplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/notes/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/private/purpose/libpurposeplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/purpose/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/private/quicklaunch/libquicklaunchplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/quicklaunch/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/private/timer/libtimerplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/timer/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/private/weather/libweatherplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/weather/qmldir
/usr/lib64/qt5/qml/org/kde/plasmacalendar/astronomicaleventsconfig/libplasmacalendarastronomicaleventsconfig.so
/usr/lib64/qt5/qml/org/kde/plasmacalendar/astronomicaleventsconfig/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdeplasma-addons/COPYING
/usr/share/package-licenses/kdeplasma-addons/COPYING.LIB

%files locales -f plasma_applet_org.kde.plasma.binaryclock.lang -f plasma_applet_org.kde.plasma.calculator.lang -f plasma_applet_org.kde.plasma.colorpicker.lang -f plasma_applet_org.kde.plasma.comic.lang -f plasma_applet_org.kde.plasma.diskquota.lang -f plasma_applet_org.kde.plasma.fifteenpuzzle.lang -f plasma_applet_org.kde.plasma.fuzzyclock.lang -f plasma_applet_org.kde.plasma.konsoleprofiles.lang -f plasma_applet_org.kde.plasma.mediaframe.lang -f plasma_applet_org.kde.plasma.notes.lang -f plasma_applet_org.kde.plasma.private.grouping.lang -f plasma_applet_org.kde.plasma.quicklaunch.lang -f plasma_applet_org.kde.plasma.quickshare.lang -f plasma_applet_org.kde.plasma.systemloadviewer.lang -f plasma_applet_org.kde.plasma.timer.lang -f plasma_applet_org.kde.plasma.userswitcher.lang -f plasma_applet_org.kde.plasma.weather.lang -f plasma_packagestructure_comic.lang -f plasma_runner_CharacterRunner.lang -f plasma_runner_converterrunner.lang -f plasma_runner_datetime.lang -f plasma_runner_katesessions.lang -f plasma_runner_krunner_dictionary.lang -f plasma_runner_mediawiki.lang -f plasma_runner_spellcheckrunner.lang -f plasma_applet_org.kde.plasma.keyboardindicator.lang -f plasma_applet_org.kde.plasma_applet_dict.lang -f plasma_calendar_astronomicalevents.lang -f plasma_runner_konsoleprofiles.lang
%defattr(-,root,root,-)

