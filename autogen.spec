%define major 25
%define libname %mklibname opts %{major}
%define develname %mklibname opts -d

Summary:	Simplifies the creation and maintenance of programs
Name:		autogen
Version:	5.16
Release:	4
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



%changelog
* Sat Jun 09 2012 Bernhard Rosenkraenzer <bero@bero.eu> 5.16-3
+ Revision: 803761
- Kill /bin/cat dependency

* Sat Jun 02 2012 Andrey Bondrov <abondrov@mandriva.org> 5.16-2
+ Revision: 801902
- Don't use info-install in post scripts as new RPM handles it with triggers

* Thu May 17 2012 Matthew Dawkins <mattydaw@mandriva.org> 5.16-1
+ Revision: 799441
- patch1 to fix build for guile-2.0

  + Alexander Khrukin <akhrukin@mandriva.org>
    - configure2_5x
    - version update 5.16
    - trying build it again
    - BR:pkgconfig(guile-2.0)
    - BR:guile-devel
    - rebuild for guile

* Sat Mar 03 2012 Alexander Khrukin <akhrukin@mandriva.org> 5.15-1
+ Revision: 782040
- version update 5.15

* Thu Sep 29 2011 Andrey Bondrov <abondrov@mandriva.org> 5.12-1
+ Revision: 701895
- New version: 5.12

* Wed May 18 2011 Funda Wang <fwang@mandriva.org> 5.11.9-1
+ Revision: 676023
- new version 5.11.9

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 5.11.8-1
+ Revision: 657752
- New version 5.11.8
- use multiarch macros for config file

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 5.10-3mdv2011.0
+ Revision: 603482
- rebuild

* Tue Feb 09 2010 Funda Wang <fwang@mandriva.org> 5.10-2mdv2010.1
+ Revision: 503359
- rebuild for new gmp

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 5.10-1mdv2010.1
+ Revision: 463355
- new version 5.10

* Sat May 16 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 5.9.8-1mdv2010.0
+ Revision: 376464
- update to new version 5.9.8

* Thu Jan 29 2009 Funda Wang <fwang@mandriva.org> 5.9.7-2mdv2009.1
+ Revision: 335074
- rebuild for new libtool

* Sun Jan 04 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 5.9.7-1mdv2009.1
+ Revision: 324500
- update to new version 5.9.7

* Thu Nov 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 5.9.6-2mdv2009.1
+ Revision: 305356
- do not protect major (ffs this is my second mistake...)
- update to new version 5.9.6
- correct urls
- get rid of -Werror flag as it breaks build
- major has changed from 0 to 25, since it is now protected
- add provides/obsoletes for main library

* Mon Jun 23 2008 Oden Eriksson <oeriksson@mandriva.com> 5.9.5-2mdv2009.0
+ Revision: 227986
- rebuilt due to PayloadIsLzma problems

* Sun Jun 22 2008 Oden Eriksson <oeriksson@mandriva.com> 5.9.5-1mdv2009.0
+ Revision: 227867
- 5.9.5
- added P0 to fix linkage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Dec 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 5.9.4-1mdv2008.1
+ Revision: 139564
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 26 2007 Funda Wang <fwang@mandriva.org> 5.9.3-1mdv2008.1
+ Revision: 102347
- update to new version 5.9.3

* Tue Sep 04 2007 David Walluck <walluck@mandriva.org> 5.9.2-1mdv2008.0
+ Revision: 78922
- 5.9.2
- new lib policy

* Sun May 06 2007 David Walluck <walluck@mandriva.org> 5.9.1-1mdv2008.0
+ Revision: 23681
- 5.9.1


* Tue Mar 06 2007 Emmanuel Andry <eandry@mandriva.org> 5.9-1mdv2007.0
+ Revision: 133427
- New version 5.9

* Sun Feb 18 2007 Emmanuel Andry <eandry@mandriva.org> 5.8.9-1mdv2007.1
+ Revision: 122213
- New version 5.8.9
- Import autogen

* Fri Sep 01 2006 Couriousous <couriousous@mandriva.org> 5.8.5-1mdv2007.0
- 5.8.5

* Sun Apr 16 2006 Couriousous <couriousous@mandriva.org> 5.8.4-1mdk
- 5.8.4

* Mon Aug 01 2005 Couriousous <couriousous@mandriva.org> 5.7.2-1mdk
- 5.7.2

* Sat Jul 16 2005 Couriousous <couriousous@mandriva.org> 5.7.1-1mdk
- 5.7.1

* Mon Apr 04 2005 Couriousous <couriousous@mandriva.org> 5.7-1mdk
- 5.7

* Sat Mar 19 2005 Couriousous <couriousous@mandrake.org> 5.6.6-1mdk
- Some spec fix
- From trem <trem@zarb.org> : 
	- First Mandrakelinux release

