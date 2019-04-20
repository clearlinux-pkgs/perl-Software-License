#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Software-License
Version  : 0.103014
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Software-License-0.103014.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Software-License-0.103014.tar.gz
Summary  : packages that provide templated software licenses
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Software-License-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Data::Section)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Text::Template)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Software-License,
version 0.103014:
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


%prep
%setup -q -n Software-License-0.103014

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Software-License
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Software-License/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Software/License.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/AGPL_3.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/Apache_1_1.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/Apache_2_0.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/Artistic_1_0.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/Artistic_2_0.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/BSD.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/CC0_1_0.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/Custom.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/EUPL_1_1.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/EUPL_1_2.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/FreeBSD.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/GFDL_1_2.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/GFDL_1_3.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/GPL_1.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/GPL_2.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/GPL_3.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/LGPL_2_1.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/LGPL_3_0.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/MIT.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/Mozilla_1_0.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/Mozilla_1_1.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/Mozilla_2_0.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/None.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/OpenSSL.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/Perl_5.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/PostgreSQL.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/QPL_1_0.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/SSLeay.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/Sun.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/License/Zlib.pm
/usr/lib/perl5/vendor_perl/5.28.2/Software/LicenseUtils.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Software::License.3
/usr/share/man/man3/Software::License::AGPL_3.3
/usr/share/man/man3/Software::License::Apache_1_1.3
/usr/share/man/man3/Software::License::Apache_2_0.3
/usr/share/man/man3/Software::License::Artistic_1_0.3
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
/usr/share/package-licenses/perl-Software-License/LICENSE
