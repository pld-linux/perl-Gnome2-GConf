#
# Conditional build:
%bcond_without tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2-GConf
Summary:	Perl interface to the GNOME GConf
Summary(pl):	Interfejs perlowy do GNOME Gconf
Name:		perl-GConf
Version:	1.000
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	00e81cd30c2e4a94bff526b09b60eda1
URL:		http://gtk2-perl.sf.net/
BuildRequires:	GConf2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.040
BuildRequires:	perl-Gtk2 >= 1.040
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.040
Requires:	perl-Gtk2 >= 1.040
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allow to use the GConf configuration system in order to
store/retrieve the configuration of an application.

%description -l pl
Modu³ pozwalaj±cy korzystaæ z systemu konfiguracji GConf w celu
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorarch}/Gnome2/GConf.pm
%dir %{perl_vendorarch}/auto/Gnome2/GConf
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/GConf/*.so
%{perl_vendorarch}/auto/Gnome2/GConf/*.bs
%{perl_vendorarch}/Gnome2/GConf/Install
%{_mandir}/man3/*
