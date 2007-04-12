%define name autogen
%define version 5.9
%define release %mkrel 1
%define lib_name %mklibname %{name} 0

Name: %{name}
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Url: http://autogen.sf.net
Summary: Simplify the creation and maintenance of programs
Group: Development/Other
License: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: chrpath
# libxml2-devel is correct, even on amd64.
BuildRequires: guile-devel, libxml2-devel

%description
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.


%package -n %{lib_name}
Summary: Simplify the creation and maintenance of programs
Group: Development/Other
License: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description -n %{lib_name}
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.


%package -n %{lib_name}-devel
Summary: Simplify the creation and maintenance of programs
Group: Development/Other
License: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Provides: lib%name-devel = %{version}-%{release}
Requires: %{lib_name} = %{version}

%description -n %{lib_name}-devel
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.


%prep
%setup -q

%configure 

%build

#parallel build randomly fail
make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove rpath
chrpath -d %{buildroot}/%{_libdir}/lib*.so.* %{buildroot}/%{_bindir}/{autogen,columns,getdefs,xml2ag}

%post
%_install_info %{name}.info

%postun
%_remove_install_info %{name}.info

%post -n %lib_name -p /sbin/ldconfig

%postun -n %lib_name -p /sbin/ldconfig

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

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(755,root,root,755)
%{_bindir}/autoopts-config
%defattr(644,root,root,755)
%{_includedir}/autoopts
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


