#
# Conditional build:
%bcond_without tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2-GConf
Summary:	Perl interface to the Gnome GConf
Summary(pl):	Interfejs perlowy do Gnome Gconf
Name:		perl-%{pnam}
Version:	0.42
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	d71fdc9a301ce7ee569e9718c2aa7b7d
URL:		http://gtk2-perl.sf.net/
BuildRequires:	GConf2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	perl-Glib >= 1.012
BuildRequires:	perl-Gtk2 >= 1.012
BuildRequires:	perl-Gnome2 >= 0.38
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
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
