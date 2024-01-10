#define date 20210915

Summary:	Qt plugin for handling JPEG XL images
Name:		qt-jpegxl-image-plugin
Version:	0.5.0
Release:	%{?date:0.%{date}.}2
Source0:	https://github.com/novomesk/qt-jpegxl-image-plugin/archive/%{?date:main/%{name}-%{version}-%{date}}%{!?date:refs/tags/v%{version}}.tar.gz
BuildRequires:	cmake ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	pkgconfig(libjxl) >= 0.7
BuildRequires:	qt5-macros
BuildRequires:	qmake5
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6DBusTools)
License:	GPLv3
Supplements:	%mklibname qt5gui 5

%description
Qt plugin for handling JPEG XL images

%package qt6
Summary:	JPEG XL plugin for Qt 6.x
Supplements:	%mklibname Qt6Gui

%description qt6
JPEG XL plugin for Qt 6.x

%prep
%autosetup -p1 %{?date:-n %{name}-main}
export CMAKE_BUILD_DIR=build-qt6
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DBUILD_WITH_QT6:BOOL=ON \
	-G Ninja
cd ..

%cmake_kde5 \
	-DENABLE_BSYMBOLICFUNCTIONS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build-qt6
%ninja_build -C build

%install
%ninja_install -C build-qt6
%ninja_install -C build

%files
%{_libdir}/qt5/plugins/imageformats/libqjpegxl5.so

%files qt6
%{_qtdir}/plugins/imageformats/libqjpegxl6.so
