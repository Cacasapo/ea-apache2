Summary: Meta-package that only requires libnghttp2
Name: nghttp2
Version: 1.19.0
Release: 0
License: MIT
Group: Applications/Internet
URL: https://nghttp2.org/
Source0: https://github.com/tatsuhiro-t/nghttp2/releases/download/v%{version}/nghttp2-%{version}.tar.bz2
BuildRequires: openssl >= 1.0.2
BuildRequires: zlib-devel

Requires: libnghttp2%{?_isa} = %{version}-%{release}

%description
This package installs no files.  It only requires the libnghttp2 package.


%package -n libnghttp2
Summary: A library implementing the HTTP/2 protocol
Group: Development/Libraries

%description -n libnghttp2
libnghttp2 is a library implementing the Hypertext Transfer Protocol
version 2 (HTTP/2) protocol in C.


%package -n libnghttp2-devel
Summary: Files needed for building applications with libnghttp2
Group: Development/Libraries
Requires: libnghttp2%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description -n libnghttp2-devel
The libnghttp2-devel package includes libraries and header files needed
for building applications with libnghttp2.


%prep
%setup -q


%build

export OPENSSL_CFLAGS="-I/opt/ssl/include" OPENSSL_LIBS="-L/opt/ssl/lib"

%configure				    

# avoid using rpath
sed -i libtool                              \
    -e 's/^runpath_var=.*/runpath_var=/'    \
    -e 's/^hardcode_libdir_flag_spec=".*"$/hardcode_libdir_flag_spec=""/'

make %{?_smp_mflags} V=1


%install
%make_install

# not needed on Fedora/RHEL
rm -f "$RPM_BUILD_ROOT%{_libdir}/libnghttp2.la"
rm -f "$RPM_BUILD_ROOT%{_libdir}/libnghttp2.a"

# will be installed via %%doc
rm -f "$RPM_BUILD_ROOT%{_datadir}/doc/nghttp2/README.rst"

# do not install man pages and helper scripts for tools that are not available
rm -fr "$RPM_BUILD_ROOT%{_datadir}/nghttp2"
rm -fr "$RPM_BUILD_ROOT%{_mandir}/man1"

%post -n libnghttp2 -p /sbin/ldconfig

%postun -n libnghttp2 -p /sbin/ldconfig


%check
# test the just built library instead of the system one, without using rpath
export "LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}:$LD_LIBRARY_PATH"
make %{?_smp_mflags} check


%files

%files -n libnghttp2
%{!?_licensedir:%global license %%doc}
%license COPYING
%attr(755,root,root) %{_libdir}/libnghttp2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnghttp2.so.14



%files -n libnghttp2-devel
%{_includedir}/nghttp2
%{_libdir}/pkgconfig/libnghttp2.pc
%{_libdir}/libnghttp2.so
%doc README.rst


%changelog
* Mon Jan 04 2016 Kamil Dudka <kdudka@redhat.com> 1.6.0-1.el6.1
- make the package build on RHEL-6 (libnghttp2 only)

* Fri Dec 25 2015 Kamil Dudka <kdudka@redhat.com> 1.6.0-1
- update to the latest upstream release (fixes CVE-2015-8659)

* Thu Nov 26 2015 Kamil Dudka <kdudka@redhat.com> 1.5.0-1
- update to the latest upstream release

* Mon Oct 26 2015 Kamil Dudka <kdudka@redhat.com> 1.4.0-1
- update to the latest upstream release

* Thu Sep 24 2015 Kamil Dudka <kdudka@redhat.com> 1.3.4-1
- update to the latest upstream release

* Wed Sep 23 2015 Kamil Dudka <kdudka@redhat.com> 1.3.3-1
- update to the latest upstream release

* Wed Sep 16 2015 Kamil Dudka <kdudka@redhat.com> 1.3.2-1
- update to the latest upstream release

* Mon Sep 14 2015 Kamil Dudka <kdudka@redhat.com> 1.3.1-1
- update to the latest upstream release

* Mon Aug 31 2015 Kamil Dudka <kdudka@redhat.com> 1.3.0-1
- update to the latest upstream release

* Mon Aug 17 2015 Kamil Dudka <kdudka@redhat.com> 1.2.1-1
- update to the latest upstream release

* Sun Aug 09 2015 Kamil Dudka <kdudka@redhat.com> 1.2.0-1
- update to the latest upstream release

* Wed Jul 15 2015 Kamil Dudka <kdudka@redhat.com> 1.1.1-1
- update to the latest upstream release

* Tue Jun 30 2015 Kamil Dudka <kdudka@redhat.com> 1.0.5-1
- packaged for Fedora (#1237247)

