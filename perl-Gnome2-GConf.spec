#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Gnome2-GConf
Summary:	Perl interface to the GNOME GConf
Summary(pl.UTF-8):   Interfejs perlowy do GNOME GConf
Name:		perl-Gnome2-GConf
Version:	1.043
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	bc3fe822c5dc3324f42bd02a3d6933b7
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	gtk+2-devel >= 2:2.10.3
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.140
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	GConf2 >= 2.14.0
Requires:	perl-Glib >= 1.140
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allow to use the GConf configuration system in order to
store/retrieve the configuration of an application.

%description -l pl.UTF-8
Moduł pozwalający korzystać z systemu konfiguracji GConf w celu
zapisania/odczytania konfiguracji programu.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/GConf/*.pod
rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Gnome2/GConf/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHOR ChangeLog NEWS README
%{perl_vendorarch}/Gnome2/GConf.pm
%dir %{perl_vendorarch}/auto/Gnome2/GConf
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/GConf/*.so
%dir %{perl_vendorarch}/Gnome2/GConf
%{perl_vendorarch}/auto/Gnome2/GConf/*.bs
%{perl_vendorarch}/Gnome2/GConf/Install
%{_mandir}/man3/*
