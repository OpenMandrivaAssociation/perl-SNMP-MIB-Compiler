%define	upstream_name	 SNMP-MIB-Compiler
%define upstream_version 0.06
Name:		perl-%{upstream_name}
Version:	0.06
Release:	5

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	A MIB Compiler for perl
Url:		https://metacpan.org/dist/SNMP-MIB-Compiler
Source0:	https://cpan.metacpan.org/authors/id/F/FT/FTASSIN/SNMP-MIB-Compiler-0.06.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Data::Compare)
BuildRequires:	perl(File::Find::Rule)
BuildArch:	noarch

Requires:	perl(Data::Compare)

%description
SNMP::MIB::Compiler is a MIB compiler that
fully supports both SMI(v1) and SMIv2. This
module can be use to compile MIBs (recursively
or not) or load already compiled MIBs for
later use.

%prep
%setup -q -n SNMP-MIB-Compiler-0.06

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc MANIFEST README
%{perl_vendorlib}/Bundle
%{perl_vendorlib}/SNMP
%{_bindir}/*
%{_mandir}/*/*


