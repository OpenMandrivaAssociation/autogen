%define major 25
%define libnamedevelold %mklibname %{name} 0 -d
%define libname %mklibname opts %{major}
%define libnamedevel %mklibname %{name} -d
%define libnamestaticdevel %mklibname %{name} -d -s

Summary:	Simplifies the creation and maintenance of programs
Name:		autogen
Version:	5.16
Release:	1
Group:		Development/Other
License:	GPLv2+
URL:		http://www.gnu.org/software/autogen/
Source0:	http://sourceforge.net/projects/autogen/files/AutoGen/AutoGen-%{version}/%{name}-%{version}.tar.gz
Requires(post):	info-install
Requires(preun):	info-install
BuildRequires:	chrpath
BuildRequires:	pkgconfig(guile-2.0)
BuildRequires:	libxml2-devel
Patch0:		autogen-5.12-pkgconfig.patch

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
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{libnamedevel}
Summary:	Development headers and libraries for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{libnamedevelold} < %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libnamedevel}
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{libnamestaticdevel}
Summary:	Static libraries for %{name}
Group:		Development/Other
Provides:	%{name}-static-devel = %{version}-%{release}
Provides:	lib%{name}-static-devel = %{version}-%{release}
Requires:	%{libnamedevel} = %{version}-%{release}

%description -n	%{libnamestaticdevel}
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%prep
%setup -q
%patch0 -p1

%build

export LDFLAGS="-lguile"
%configure

%make

%install
%makeinstall_std

%{_bindir}/chrpath -d %{buildroot}/%{_libdir}/lib*.so.* %{buildroot}/%{_bindir}/{autogen,columns,getdefs,xml2ag}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info


%files
%doc README TODO
%{_bindir}/autogen
%{_bindir}/columns
%{_bindir}/getdefs
%{_bindir}/xml2ag
%{_infodir}/autogen.info*
%{_mandir}/*/*
%{_datadir}/aclocal/*
%{_datadir}/autogen/

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{libnamedevel}
%defattr(0755,root,root,0755)
%{_bindir}/autoopts-config
%defattr(0644,root,root,0755)
%{_includedir}/autoopts/
%{_libdir}/*.so
%{_datadir}/pkgconfig/*

%files -n %{libnamestaticdevel}
%defattr(0644,root,root,0755)
%{_libdir}/*.a
