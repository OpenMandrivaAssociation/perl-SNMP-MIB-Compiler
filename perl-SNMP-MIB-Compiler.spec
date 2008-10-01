%define	module	SNMP-MIB-Compiler
%define	name	perl-%{module}
%define	version	0.06
%define	release	%mkrel 11

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	A MIB Compiler for perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/SNMP/%{module}-%{version}.tar.bz2
Url:		http://www.cpan.org
BuildRequires:	perl-devel perl-Data-Compare
BuildRequires:	perl(File::Find::Rule)
Requires:	perl >= 0:5.005 perl-Data-Compare
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SNMP::MIB::Compiler is a MIB compiler that
fully supports both SMI(v1) and SMIv2. This
module can be use to compile MIBs (recursively
or not) or load already compiled MIBs for
later use.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc MANIFEST README
%{perl_vendorlib}/Bundle
%{perl_vendorlib}/SNMP
%{_bindir}/*
%{_mandir}/*/*

