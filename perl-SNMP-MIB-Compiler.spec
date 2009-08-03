%define	upstream_name	 SNMP-MIB-Compiler
%define	upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	A MIB Compiler for perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/SNMP/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Data-Compare
BuildRequires:	perl(File::Find::Rule)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	perl-Data-Compare

%description
SNMP::MIB::Compiler is a MIB compiler that
fully supports both SMI(v1) and SMIv2. This
module can be use to compile MIBs (recursively
or not) or load already compiled MIBs for
later use.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
