%define		pdir	Devel
%define		pnam	ptkdb
%include	/usr/lib/rpm/macros.perl
Summary:	Tk GUI based Perl script debugger
Name:		perl-Devel-ptkdb
Version:	1.233
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/ptkdb/Devel-ptkdb-%{version}.tar.gz
# Source0-md5:	dd2a971e9bd2bf601e09ba11de3a21bb
URL:		http://sourceforge.net/projects/ptkdb/
BuildRequires:	perl-Tk >= 800.021
BuildRequires:	perl-devel >= 1:5.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ptkdb is a debugger for Perl with graphical user interface (GUI) based
on Perl/Tk.

It has following features :
- Expression Evaluation window automatically redisplays entered
  expressions each time the debugger stops.
- Hot variable evaluation. Place the mouse over a $var, @array, or
  %%hash and it's contents will be displayed in a popup balloon. You can
  also select an expression and that will be automatically evaluated.
- Conditional Breakpoints

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/Devel
%{perl_vendorlib}/Devel/ptkdb.pm
%dir %{perl_vendorarch}/auto/Devel
%{perl_vendorarch}/auto/Devel/ptkdb/
%{_mandir}/man3/Devel::ptkdb.3pm*
