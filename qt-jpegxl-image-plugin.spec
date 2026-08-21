Summary:	Qt plugin for handling JPEG XL images
Name:		qt-jpegxl-image-plugin
Version:	0.8.4
Release:	1
License:	GPLv3
Group:		System/Libraries
Url:		https://github.com/novomesk/qt-jpegxl-image-plugin
Source0:	https://github.com/novomesk/qt-jpegxl-image-plugin/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	pkgconfig(libjxl) >= 0.7
BuildRequires:	pkgconfig(libjxl_threads) >= 0.7
BuildRequires:	pkgconfig(libjxl_cms) >= 0.9
BuildRequires:	qt5-macros
BuildRequires:	qmake5
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6DBusTools)
Supplements:	%mklibname qt5gui 5

%description
Qt plugin for handling JPEG XL images

%package qt6
Summary:	JPEG XL plugin for Qt 6.x
Group:		System/Libraries
Supplements:	%mklibname Qt6Gui

%description qt6
JPEG XL plugin for Qt 6.x

%prep
%autosetup -p1

%cmake_qt5 \
	-DKDE_INSTALL_QTPLUGINDIR:PATH=%{_libdir}/qt5/plugins \
	-DBUILD_WITH_QT6:BOOL=OFF \
	-G Ninja

cd ..
export CMAKE_BUILD_DIR=build-qt6
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DBUILD_WITH_QT6:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build
%ninja_build -C build-qt6

%install
%ninja_install -C build
%ninja_install -C build-qt6

%files
%{_libdir}/qt5/plugins/imageformats/libqjpegxl5.so

%files qt6
%{_qtdir}/plugins/imageformats/libqjpegxl6.so
