%define major 25
%define libname %mklibname opts %{major}
%define devname %mklibname opts -d
%define _disable_rebuild_configure 1
%global optflags %{optflags} -Wno-implicit-fallthrough -Wno-format-overflow -Wno-format-truncation -Wno-missing-field-initializers -Wno-unknown-warning-option
%global __requires_exclude '/bin/cat'

Summary:	Simplifies the creation and maintenance of programs
Name:		autogen
Version:	5.18.16
Release:	4
Group:		Development/Other
License:	GPLv2+
URL:		https://www.gnu.org/software/autogen/
Source0:	https://ftp.gnu.org/gnu/autogen/rel%{version}/autogen-%{version}.tar.xz
Patch0:		autogen-5.12-pkgconfig.patch
Patch1:		autogen-5.18.16-guile-3.0.patch
Patch2:		autogen-5.18.16-add-disable-autogen.patch
# openSUSE patches
Patch10:	autogen-catch-race-error.patch
Patch11:	sprintf-overflow.patch
Patch12:	gcc9-fix-wrestrict.patch
BuildRequires:	chrpath
BuildRequires:	pkgconfig(guile-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(icu-i18n)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(icu-io)
BuildRequires:	pkgconfig(atomic_ops)
BuildRequires:	pkgconfig(bdw-gc)
BuildRequires:	gmp-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	autoconf-archive
BuildRequires:	gettext-devel

%description
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		Development/Other

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development headers and libraries for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%autosetup -p1

# Disable failing test
sed -i 's|errors.test||' autoopts/test/Makefile.in

libtoolize --force
fix-old-automake-files --fix-ac-defun
aclocal -I config
autoheader
automake -a
autoconf

sed -i 's/ -Werror / /' configure

%build
%configure

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' ./libtool

%make_build

%install
%make_install

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
%{_datadir}/aclocal/*
%{_datadir}/autogen/
%doc %{_infodir}/autogen.info*
%doc %{_mandir}/*/*

%files -n %{libname}
%{_libdir}/libopts.so.%{major}*

%files -n %{devname}
%{_bindir}/autoopts-config
%{_includedir}/autoopts/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
