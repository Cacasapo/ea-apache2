%define _unpackaged_files_terminate_build 0

Release: 2

%define openssldir /etc/pki/tls
%define prefix /opt/ssl

Summary: Secure Sockets Layer and cryptography libraries and tools
Name: openssl-parallel
Version: 1.0.2j
Source0: /root/rpmbuild/SOURCES/openssl-%{version}.tar.gz
License: OpenSSL
Group: System Environment/Libraries
Provides: Updated-SSL
#URL: http://www.openssl.org/
Packager: Damien Miller <djm@mindrot.org>
BuildRoot:   /var/tmp/%{name}-%{version}-root

%description
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, fully featured, and Open Source toolkit implementing the
Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)
protocols as well as a full-strength general purpose cryptography library.
The project is managed by a worldwide community of volunteers that use the
Internet to communicate, plan, and develop the OpenSSL tookit and its related
documentation. 

OpenSSL is based on the excellent SSLeay library developed from Eric A.
Young and Tim J. Hudson.  The OpenSSL toolkit is licensed under an
Apache-style licence, which basically means that you are free to get and
use it for commercial and non-commercial purposes. 

This package contains the base OpenSSL cryptography and SSL/TLS 
libraries and tools.

%package devel
Summary: Secure Sockets Layer and cryptography static libraries and headers
Group: Development/Libraries
Requires: openssl
%description devel
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, fully featured, and Open Source toolkit implementing the
Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)
protocols as well as a full-strength general purpose cryptography library.
The project is managed by a worldwide community of volunteers that use the
Internet to communicate, plan, and develop the OpenSSL tookit and its related
documentation. 

OpenSSL is based on the excellent SSLeay library developed from Eric A.
Young and Tim J. Hudson.  The OpenSSL toolkit is licensed under an
Apache-style licence, which basically means that you are free to get and
use it for commercial and non-commercial purposes. 

This package contains the the OpenSSL cryptography and SSL/TLS 
static libraries and header files required when developing applications.



%prep

%setup -q -n openssl-%{version}

%build 

%define CONFIG_FLAGS -DSSL_ALLOW_ADH -fPIC --prefix=%{prefix} --openssldir=%{openssldir}

perl util/perlpath.pl /usr/bin/perl

%ifarch i386 i486 i586 i686
./Configure %{CONFIG_FLAGS} linux-elf shared
%endif
%ifarch ppc
./Configure %{CONFIG_FLAGS} linux-ppc shared
%endif
%ifarch alpha
./Configure %{CONFIG_FLAGS} linux-alpha shared
%endif
%ifarch x86_64
./Configure %{CONFIG_FLAGS} linux-x86_64 shared
%endif
LD_LIBRARY_PATH=`pwd` make
LD_LIBRARY_PATH=`pwd` make rehash
LD_LIBRARY_PATH=`pwd` make test

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_PREFIX="$RPM_BUILD_ROOT" install

# Make backwards-compatibility symlink to ssleay
ln -sf %{prefix}/bin/openssl $RPM_BUILD_ROOT%{prefix}/bin/ssleay

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(0644,root,root,0755)
#%doc CHANGES CHANGES.SSLeay LICENSE NEWS README

%attr(0755,root,root) %{prefix}/*
%attr(0755,root,root) %{prefix}/lib/libcrypto.so.1*
%attr(0755,root,root) %{prefix}/lib/libssl.so.1*
%attr(0755,root,root) %{openssldir}/misc/*
#%attr(0644,root,root) /usr/man/man[157]/*

#%config(noreplace) %{openssldir}/openssl.cnf 
%dir %attr(0755,root,root) %{openssldir}/certs
%dir %attr(0755,root,root) %{openssldir}/misc
#%dir %attr(0750,root,root) %{openssldir}/private

%files devel
%defattr(0644,root,root,0755)
#%doc CHANGES CHANGES.SSLeay LICENSE NEWS README

%attr(0644,root,root) %{prefix}/lib/*.a
%attr(0644,root,root) %{prefix}/lib/pkgconfig/openssl.pc
%attr(0644,root,root) %{prefix}/include/openssl/*
#%attr(0644,root,root) /usr/man/man[3]/*


%post
echo %{prefix}/lib >> /etc/ld.so.conf.d/openssl.conf
ldconfig

%postun
sed '%{prefix}/lib' /etc/ld.so.conf.d/openssl.conf
ldconfig

