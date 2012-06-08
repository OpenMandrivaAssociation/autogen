%define major 25
%define libname %mklibname opts %{major}
%define develname %mklibname opts -d

Summary:	Simplifies the creation and maintenance of programs
Name:		autogen
Version:	5.16
Release:	3
Group:		Development/Other
License:	GPLv2+
URL:		http://www.gnu.org/software/autogen/
Source0:	http://sourceforge.net/projects/autogen/files/AutoGen/AutoGen-%{version}/%{name}-%{version}.tar.gz
Patch0:		autogen-5.12-pkgconfig.patch

BuildRequires:	chrpath
BuildRequires:	pkgconfig(guile-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%define __noautoreq '/bin/cat'

%description
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		Development/Other
Obsoletes:	%{_lib}autogen0 < 5.11

%description -n	%{libname}
This package contains the shared library for %{name}.

%package -n %{develname}
Summary:	Development headers and libraries for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}autogen0-devel < %{version}-%{release}
Obsoletes:	%{_lib}opts-static-devel < %{version}-%{release}

%description -n	%{develname}
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%{_bindir}/chrpath -d %{buildroot}/%{_libdir}/lib*.so.* \
	%{buildroot}/%{_bindir}/{autogen,columns,getdefs,xml2ag}

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
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_bindir}/autoopts-config
%{_includedir}/autoopts/
%{_libdir}/*.so
%{_datadir}/pkgconfig/*

