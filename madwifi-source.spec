%define name madwifi-source
%define short_name madwifi

%define version 0.9.3.3
%define snaprev r3114
%define snapdate 20080104
%define rel 11
%if %{snapdate}
%define distname madwifi-ng-%{snaprev}-%{snapdate}
%define release %mkrel %{rel}.%{snaprev}
%else
%define distname %{short_name}-%{version}
%define release %mkrel %{rel}
%endif

Summary: Madwifi drivers source code
Name: %{name}
Version: %{version}
Release: %{release}
# to run in BUILD tree of madwifi package:
# tar cjf madwifi-r3114-20080104-source.tar.bz2 madwifi-ng-r3114-20080104/net80211/*.h madwifi-ng-r3114-20080104/include/*.h
Source0: %{distname}-source.tar.bz2
License: GPL
Group: Development/Kernel
Url: https://madwifi.org/
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
This package contains parts of the madwifi drivers source code.

The whole source code cannot be distributed in the distribution
because it contains non-free binary code in the HAL.

%prep
%setup -q -n %{distname}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/usr/src/%{short_name}
cp -a net80211 include %{buildroot}/usr/src/%{short_name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /usr/src/%{short_name}
/usr/src/%{short_name}/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.3.3-11.r3114mdv2011.0
+ Revision: 666356
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.3.3-10.r3114mdv2011.0
+ Revision: 606621
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.3.3-9.r3114mdv2010.1
+ Revision: 523238
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.3.3-8.r3114mdv2010.0
+ Revision: 426056
- rebuild

* Thu Aug 07 2008 Olivier Blin <oblin@mandriva.com> 0.9.3.3-7.r3114mdv2009.0
+ Revision: 266067
- sync with madwifi-0.9.3.3-7.r3114mdv2009.0
- do not package .c files

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.9.3-4mdv2009.0
+ Revision: 223140
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.9.3-3mdv2008.1
+ Revision: 152892
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.9.3-2mdv2008.1
+ Revision: 152891
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 21 2007 Olivier Blin <oblin@mandriva.com> 0.9.3-1mdv2008.0
+ Revision: 29416
- 0.9.3
- Import madwifi-source



* Wed Sep  6 2006 Olivier Blin <blino@mandriva.com> 0.9.2-1mdv2007.0
- initial Mandriva release
