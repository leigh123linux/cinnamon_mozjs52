Name:          cjs
Epoch:         1
Version:       3.6.1
Release:       1.1%{?dist}
Summary:       Javascript Bindings for Cinnamon

License:       MIT and (MPLv1.1 or GPLv2+ or LGPLv2+)
# The following files contain code from Mozilla which
# is triple licensed under MPL1.1/LGPLv2+/GPLv2+:
# The console module (modules/console.c)
# Stack printer (gjs/stack.c)
URL:           https://github.com/linuxmint/%{name}
Source0:       %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if 0%{?rhel}
Patch0:        old_pkconfig.patch
%endif
Patch1:        %{url}/pull/61.patch#/port_to_mozjs52.patch

#Patches from upstream.

BuildRequires: pkgconfig(mozjs-52)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.38.0
BuildRequires: readline-devel
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: gcc-c++
BuildRequires: intltool
# Require for checks
#BuildRequires: dbus-x11
#BuildRequires: xorg-x11-server-Xvfb
# Bootstrap requirements
BuildRequires: pkgconfig(gtk-doc)
BuildRequires: libtool
BuildRequires: autoconf-archive

%description
Cjs allows using Cinnamon libraries from Javascript. It's based on the
Spidermonkey Javascript engine from Mozilla and the GObject introspection
framework.


%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{?epoch}:%{version}-%{release}

%description devel
Files for development with %{name}.


%package tests
Summary: Tests for the cjs package
Requires: %{name}-devel%{?_isa} = %{?epoch}:%{version}-%{release}

%description tests
The cjs-tests package contains tests that can be used to verify
the functionality of the installed cjs package.


%prep
%autosetup -p1
NOCONFIGURE=1 ./autogen.sh


%build
%configure --disable-static \
%if 0%{?rhel}
           --without-dbus-tests \
%endif
           --enable-installed-tests
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build V=1


%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%check
#make check


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc NEWS README
%license COPYING COPYING.LGPL
%{_bindir}/cjs
%{_bindir}/cjs-console
%{_libdir}/*.so.*
%{_libdir}/cjs/
%exclude %{_libdir}/cjs/*.so


%files devel
%doc examples/*
%{_includedir}/cjs-1.0/
%{_libdir}/pkgconfig/cjs-*1.0.pc
%{_libdir}/*.so
%{_libdir}/cjs/*.so


%files tests
%{_libexecdir}/cjs/
%{_datadir}/installed-tests/


%changelog
* Thu Dec 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.6.1-1.1
- Add mozjs52 port patch

* Sat Nov 11 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.6.1-1
- update to 3.6.1 release

* Mon Oct 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.6.0-1
- update to 3.6.0 release

* Fri Sep 08 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.4.4-3
- Fix needsPostBarrier crash again (rhbz #1472008)

* Wed Aug 30 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.4.4-2
- Add build fixes for epel7

* Wed Aug 09 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.4.4-1
- update to 3.4.4 release

* Sun Aug 06 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.4.3-4
- Fix needsPostBarrier crash again (rhbz #1472008)
- Drop build requires gnome-common

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.4.3-1
- update to 3.4.3 release

* Thu Jun 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.4.2-2
- Fix log spam due to missing commit

* Wed Jun 28 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.4.2-1
- update to 3.4.2 release

* Sun Jun 25 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.4.1-3
- Fix needsPostBarrier crash (rhbz #1453008)

* Sun Jun 18 2017 Björn Esser <besser82@fedoraproject.org> - 1:3.4.1-2
- Add patches from upstream for tweener

* Tue May 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.4.1-1
- update to 3.4.1 release

* Wed May 03 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.4.0-1
- update to 3.4.0 release

* Wed Apr 26 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:3.4.0-0.1.20170426git16347ea
- update to git snapshot

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:3.2.0-2
- Rebuild for readline 7.x

* Mon Nov 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 1:3.2.0-1
- update to 3.2.0 release

* Sun May 15 2016 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.1-1
- update to 3.0.1 release

* Sat Apr 23 2016 Leigh Scott <leigh123linux@googlemail.com> - 1:3.0.0-1
- update to 3.0.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:2.8.0-2
- rebuilt

* Fri Oct 16 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:2.8.0-1
- update to 2.8.0 release

* Sat Jun 27 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:2.6.2-1
- update to 2.6.2 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:2.6.0-1
- update to 2.6.0 release

* Tue May 05 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:2.5.0-0.1.git5821be5
- update to git snapshot

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:2.4.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 31 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:2.4.2-1
- update to 2.4.2

* Sun Nov 23 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:2.4.1-1
- update to 2.4.1
- move .so files to -devel sub-package
- change requires for -tests sub-package

* Thu Oct 30 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:2.4.0-1
- update to 2.4.0

* Tue Sep 30 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:2.4.0-0.3.git7a65cc7
- add check section to spec

* Tue Sep 30 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:2.4.0-0.2.git7a65cc7
- add build requires gtk3-devel

* Tue Sep 30 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:2.4.0-0.1.git7a65cc7
- update to latest git
- swap to mozjs24

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:2.2.2-1
- update to 2.2.2

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:2.2.1-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:2.2.1-1
- update to 2.2.1

* Sat Apr 12 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:2.2.0-1
- update to 2.2.0

* Wed Oct 02 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:2.0.0-1
- update to 2.0.0

* Mon Sep 30 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:1.9.1-2
- add epoch to -devel

* Mon Sep 30 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:1.9.1-1
- update to 1.9.1
- add epoch

* Sun Sep 15 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.34.0-0.5.gita30f982
- update to latest git

* Thu Aug 22 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.34.0-0.4.gitfb472ad
- rebuilt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34.0-0.3.gitfb472ad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.34.0-0.2.gitfb472ad
- add isa tag to -devel sub-package

* Sun Jul 21 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.34.0-0.1.gitfb472ad
- Inital build
