Name:           xdg-dbus-proxy
Version:        0.1.4
Release:        1
Summary:        Filtering proxy for D-Bus connections
Group:          Security
License:        LGPLv2+
URL:            https://github.com/flatpak/xdg-dbus-proxy/
Source0:        https://github.com/flatpak/xdg-dbus-proxy/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  docbook-style-xsl
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  xsltproc
BuildRequires:  autoconf-archive
BuildRequires:  autoconf

Requires:       dbus

%description
xdg-dbus-proxy is a filtering proxy for D-Bus connections. It was originally
part of the flatpak project, but it has been broken out as a standalone module
to facilitate using it in other contexts.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/xdg-dbus-proxy
%{_mandir}/man1/xdg-dbus-proxy.1*
