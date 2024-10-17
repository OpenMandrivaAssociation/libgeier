%define	version	    0.13
%define release	    2
%define	major	    0
%define	realname    geier
%define	libname    %mklibname %{realname} %{major}
%define	libnamedev  %mklibname -d %{realname}

Name:		libgeier
Summary:	A C-library for German tax declarations data
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		https://www.taxbird.de/
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	xmlsec1-devel

%description
libgeier is the first free library to encrypt, digitally sign, decrypt,
validate and send gathered tax declarations data to the German inland
revenue offices.

GEIER is short for GPL'd Elster Interface and part of the Taxbird project.

%package -n	%{realname}
Summary:	Command line interface to the Geier library
Group:		System/Libraries
Requires:	%{libname} = %{version}

%description -n %{realname}
Command line interface to the Geier library (libgeier), allowing to
validate, apply stylesheets, digitally sign and send Elster XML documents.

%package	common
Summary:	Non-library files for the "%{libname}" library
Group:		System/Libraries

%description common
Common files for the "%{libname}" library

%package -n	%{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries
Requires:	%{name}-common
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
libgeier is the first free library to encrypt, digitally sign, decrypt,
validate and send gathered tax declarations data to the German inland
revenue offices.

%package -n	%{libnamedev}
Summary:	Static libraries and headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
%{libnamedev} contains the libraries and header files needed to
develop programs which make use of %{name}.
The library documentation is available on header files.

%prep
%setup -q

%build
%configure2_5x --with-openssl
%make

%install
%makeinstall_std
find %{buildroot} -type f -name '*.la' -exec rm -f {} \;

%files -n %{realname}
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/%{realname}
%{_includedir}/%{realname}*.h
%{_datadir}/gtk-doc/html/%{realname}/*
%{_mandir}/man1/%{realname}.1.*

%files common
%{_datadir}/%{name}/Elster2Cry.b64.cer
%{_datadir}/%{name}/xmlsec.tmpl
%{_datadir}/%{name}/schemas/*.xsd
%{_datadir}/%{name}/stylesheets/*.xsl

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{libnamedev}
%{_libdir}/%{name}.a
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Jan 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.13-1
+ Revision: 760774
- removing la-files

* Fri Jan 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.13-1
+ Revision: 760766
- BR fixes
- BR libxml2
- imported package libgeier

