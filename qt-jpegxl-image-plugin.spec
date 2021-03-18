%define date 20210318

Summary:	Qt plugin for handling JPEG XL images
Name:		qt-jpegxl-image-plugin
Version:	0.0.0
Release:	%{?date:0.%{date}.}1
Source0:	https://github.com/novomesk/qt-jpegxl-image-plugin/archive/main/%{name}-%{version}%{?date:-%{date}}.tar.gz
BuildRequires:	cmake ninja
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	pkgconfig(libjxl)
BuildRequires:	qt5-macros
BuildRequires:	qmake5
License:	GPLv3
Supplements:	%mklibname qt5gui 5

%description
Qt plugin for handling JPEG XL images

%prep
%autosetup -p1 -n %{name}-main
%cmake_qt5 \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/plugins/imageformats/qjpegxl.so
%{_datadir}/kservices5/qimageioplugins/jxl.desktop
