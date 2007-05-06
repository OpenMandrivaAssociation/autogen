%define lib_name %mklibname %{name} 0

Name:           autogen
Version:        5.9.1
Release:        %mkrel 1
Source0:        http://ovh.dl.sourceforge.net/autogen/autogen-%{version}.tar.bz2
Url:            http://autogen.sourceforge.net/
Summary:        Simplifies the creation and maintenance of programs
Group:          Development/Other
License:        GPL
Requires(post): info-install
Requires(preun): info-install
BuildRequires:  chrpath
BuildRequires:  libguile-devel
BuildRequires:  libxml2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

%description
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{lib_name}
Summary:        Main library for %{name}
Group:          Development/Other

%description -n %{lib_name}
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{lib_name}-devel
Summary:        Development headers and libraries for %{name}
Group:          Development/Other
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       %{_lib}autogen-devel = %{version}-%{release}
Requires:       %{lib_name} = %{version}-%{release}

%description -n %{lib_name}-devel
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

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

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

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(0755,root,root,0755)
%{_bindir}/autoopts-config
%defattr(0644,root,root,0755)
%{_includedir}/autoopts
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
