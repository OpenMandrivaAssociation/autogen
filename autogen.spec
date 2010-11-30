%define major 0
%define libnamedevelold %mklibname %{name} 0 -d
%define libname %mklibname %{name} %{major}
%define libnamedevel %mklibname %{name} -d
%define libnamestaticdevel %mklibname %{name} -d -s

Summary:	Simplifies the creation and maintenance of programs
Name:		autogen
Version:	5.10
Release:	%mkrel 3
Group:		Development/Other
License:	GPLv2+
URL:		http://www.gnu.org/software/autogen/
Source0:	http://sourceforge.net/projects/autogen/files/AutoGen/AutoGen-%{version}/%{name}-%{version}.tar.bz2
Patch0:		autogen-libguile_linkage_fix.diff
Requires(post):	info-install
Requires(preun):	info-install
BuildRequires:	chrpath
BuildRequires:	libguile-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		Development/Other

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
# (tpg) breaks compiling
sed -i -e 's/-Werror//g' configure*

%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%{_bindir}/chrpath -d %{buildroot}/%{_libdir}/lib*.so.* %{buildroot}/%{_bindir}/{autogen,columns,getdefs,xml2ag}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/autogen
%{_bindir}/columns
%{_bindir}/getdefs
%{_bindir}/xml2ag
%{_infodir}/autogen.info*
%{_mandir}/*/*
%{_datadir}/aclocal/*
%{_datadir}/autogen

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libnamedevel}
%defattr(0755,root,root,0755)
%{_bindir}/autoopts-config
%defattr(0644,root,root,0755)
%{_includedir}/autoopts
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n %{libnamestaticdevel}
%defattr(0644,root,root,0755)
%{_libdir}/*.a
