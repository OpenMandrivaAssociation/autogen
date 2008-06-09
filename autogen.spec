%define major 0
%define libnamedevelold %mklibname %{name} 0 -d
%define libname %mklibname %{name} %{major}
%define libnamedevel %mklibname %{name} -d
%define libnamestaticdevel %mklibname %{name} -d -s

Name:           autogen
Version:        5.9.4
Release:        %mkrel 1
Source0:        http://ovh.dl.sourceforge.net/autogen/autogen-%{version}.tar.bz2
Url:            http://autogen.sourceforge.net/
Summary:        Simplifies the creation and maintenance of programs
Group:          Development/Other
License:        GPLv2+
Requires(post): info-install
Requires(preun): info-install
BuildRequires:  chrpath
BuildRequires:  libguile-devel
BuildRequires:  libxml2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{libname}
Summary:        Main library for %{name}
Group:          Development/Other

%description -n %{libname}
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{libnamedevel}
Summary:        Development headers and libraries for %{name}
Group:          Development/Other
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{libnamedevelold} < %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n %{libnamedevel}
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{libnamestaticdevel}
Summary:        Static libraries for %{name}
Group:          Development/Other
Provides:       %{name}-static-devel = %{version}-%{release}
Requires:       %{libnamedevel} = %{version}-%{release}

%description -n %{libnamestaticdevel}
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%prep
%setup -q

%build
%{configure2_5x}
#parallel build randomly fails
%{__make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall}
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
%{__rm} -rf %{buildroot}

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
