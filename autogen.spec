%define major 25
%define libname %mklibname opts %{major}
%define devname %mklibname opts -d
%define _disable_rebuild_configure 1

Summary:	Simplifies the creation and maintenance of programs
Name:		autogen
Version:	5.18.12
Release:	2
Group:		Development/Other
License:	GPLv2+
URL:		http://www.gnu.org/software/autogen/
Source0:	https://ftp.gnu.org/gnu/autogen/rel%{version}/autogen-%{version}.tar.xz
Patch0:		autogen-5.12-pkgconfig.patch
Patch1:		autogen-5.18.12-guile-2.2.patch

BuildRequires:	chrpath
BuildRequires:	pkgconfig(guile-2.2)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	autoconf automake libtool autoconf-archive gettext-devel

%define __noautoreq '/bin/cat'

%description
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		Development/Other

%description -n	%{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development headers and libraries for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches

libtoolize --force
fix-old-automake-files --fix-ac-defun
aclocal -I config
autoheader
automake -a
autoconf

%build
%configure \
	--disable-static
%make

%install
%makeinstall_std

%{_bindir}/chrpath -d %{buildroot}/%{_libdir}/lib*.so.* \
	%{buildroot}/%{_bindir}/{autogen,columns,getdefs,xml2ag}

# wipe duplicate
rm -rf %{buildroot}/%{_libdir}/%{name}

%files
%doc README TODO
%{_bindir}/autogen
%{_bindir}/columns
%{_bindir}/getdefs
%{_bindir}/xml2ag
%{_infodir}/autogen.info*
%{_datadir}/aclocal/*
%{_datadir}/autogen/
%{_mandir}/*/*

%files -n %{libname}
%{_libdir}/libopts.so.%{major}*

%files -n %{devname}
%{_bindir}/autoopts-config
%{_includedir}/autoopts/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
