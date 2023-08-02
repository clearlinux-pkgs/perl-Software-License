#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Software-License
Version  : 0.104004
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Software-License-0.104004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Software-License-0.104004.tar.gz
Summary  : 'packages that provide templated software licenses'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Software-License-license = %{version}-%{release}
Requires: perl-Software-License-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Data::Section)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Text::Template)
BuildRequires : perl(Try::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Software-License,
version 0.104004:
packages that provide templated software licenses

%package dev
Summary: dev components for the perl-Software-License package.
Group: Development
Provides: perl-Software-License-devel = %{version}-%{release}
Requires: perl-Software-License = %{version}-%{release}

%description dev
dev components for the perl-Software-License package.


%package license
Summary: license components for the perl-Software-License package.
Group: Default

%description license
license components for the perl-Software-License package.


%package perl
Summary: perl components for the perl-Software-License package.
Group: Default
Requires: perl-Software-License = %{version}-%{release}

%description perl
perl components for the perl-Software-License package.


%prep
%setup -q -n Software-License-0.104004
cd %{_builddir}/Software-License-0.104004
pushd ..
cp -a Software-License-0.104004 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Software-License
cp %{_builddir}/Software-License-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Software-License/251a76ad1b9e4c0fca8a0ddacf95e902c43eb189 || :
cp %{_builddir}/Software-License-%{version}/lib/Software/License.pm %{buildroot}/usr/share/package-licenses/perl-Software-License/a3cf5391d3bdd0dc086788b98873af2ade848137 || :
cp %{_builddir}/Software-License-%{version}/lib/Software/LicenseUtils.pm %{buildroot}/usr/share/package-licenses/perl-Software-License/4cbe87464ddb836f7119f87474a60698b7945d6d || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Software::License.3
/usr/share/man/man3/Software::License::AGPL_3.3
/usr/share/man/man3/Software::License::Apache_1_1.3
/usr/share/man/man3/Software::License::Apache_2_0.3
/usr/share/man/man3/Software::License::Artistic_1_0.3
/usr/share/man/man3/Software::License::Artistic_1_0_Perl.3
/usr/share/man/man3/Software::License::Artistic_2_0.3
/usr/share/man/man3/Software::License::BSD.3
/usr/share/man/man3/Software::License::CC0_1_0.3
/usr/share/man/man3/Software::License::Custom.3
/usr/share/man/man3/Software::License::EUPL_1_1.3
/usr/share/man/man3/Software::License::EUPL_1_2.3
/usr/share/man/man3/Software::License::FreeBSD.3
/usr/share/man/man3/Software::License::GFDL_1_2.3
/usr/share/man/man3/Software::License::GFDL_1_3.3
/usr/share/man/man3/Software::License::GPL_1.3
/usr/share/man/man3/Software::License::GPL_2.3
/usr/share/man/man3/Software::License::GPL_3.3
/usr/share/man/man3/Software::License::ISC.3
/usr/share/man/man3/Software::License::LGPL_2_1.3
/usr/share/man/man3/Software::License::LGPL_3_0.3
/usr/share/man/man3/Software::License::MIT.3
/usr/share/man/man3/Software::License::Mozilla_1_0.3
/usr/share/man/man3/Software::License::Mozilla_1_1.3
/usr/share/man/man3/Software::License::Mozilla_2_0.3
/usr/share/man/man3/Software::License::None.3
/usr/share/man/man3/Software::License::OpenSSL.3
/usr/share/man/man3/Software::License::Perl_5.3
/usr/share/man/man3/Software::License::PostgreSQL.3
/usr/share/man/man3/Software::License::QPL_1_0.3
/usr/share/man/man3/Software::License::SSLeay.3
/usr/share/man/man3/Software::License::Sun.3
/usr/share/man/man3/Software::License::Zlib.3
/usr/share/man/man3/Software::LicenseUtils.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Software-License/251a76ad1b9e4c0fca8a0ddacf95e902c43eb189
/usr/share/package-licenses/perl-Software-License/4cbe87464ddb836f7119f87474a60698b7945d6d
/usr/share/package-licenses/perl-Software-License/a3cf5391d3bdd0dc086788b98873af2ade848137

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
