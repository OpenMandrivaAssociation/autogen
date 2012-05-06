%define major 25
%define libname %mklibname opts %{major}
%define libnamedevel %mklibname opts -d
%define libnamestaticdevel %mklibname opts -d -s

Summary:	Simplifies the creation and maintenance of programs
Name:		autogen
Version:	5.15
Release:	2
Group:		Development/Other
License:	GPLv2+
URL:		http://www.gnu.org/software/autogen/
Source0:	http://ftp.gnu.org/gnu/autogen/rel%{version}/%{name}-%{version}.tar.gz
Requires(preun):	info-install
BuildRequires:	chrpath
BuildRequires:	libguile-devel
BuildRequires:	libxml2-devel

%description
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		Development/Other
Obsoletes:	%{_lib}autogen0 < 5.11.8

%description -n	%{libname}
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%package -n %{libnamedevel}
Summary:	Development headers and libraries for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}autogen0-devel < 5.11.8
Obsoletes:	%{_lib}autogen-devel < 5.11.8
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
Requires:	%{libnamedevel} = %{version}-%{release}
Obsoletes:	%{_lib}autogen-static-devel < 5.11.8

%description -n	%{libnamestaticdevel}
AutoGen is a tool designed to simplify the creation and maintenance 
of programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text 
that must be kept synchronized.

%prep
%setup -q

%build
%configure2_5x
%make

%install

%makeinstall_std
find %{buildroot} -name *.la -delete

mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_datadir}/pkgconfig %{buildroot}%{_libdir}

%{_bindir}/chrpath -d %{buildroot}/%{_libdir}/lib*.so.* %{buildroot}/%{_bindir}/{autogen,columns,getdefs,xml2ag}

%multiarch_binaries %{buildroot}%{_bindir}/autoopts-config

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
%{_datadir}/autogen

%files -n %{libname}
%{_libdir}/libopts.so.%{major}
%{_libdir}/libopts.so.%{major}.*

%files -n %{libnamedevel}
%defattr(0755,root,root,0755)
%{_bindir}/autoopts-config
%multiarch_bindir/autoopts-config

%defattr(0644,root,root,0755)
%{_includedir}/autoopts
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n %{libnamestaticdevel}
%defattr(0644,root,root,0755)
%{_libdir}/*.a
