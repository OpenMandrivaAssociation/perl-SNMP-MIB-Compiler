%define	upstream_name	 SNMP-MIB-Compiler
%define	upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	A MIB Compiler for perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/SNMP/%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc MANIFEST README
%{perl_vendorlib}/Bundle
%{perl_vendorlib}/SNMP
%{_bindir}/*
%{_mandir}/*/*


%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 408046
- rebuild using %%perl_convert_version

* Wed Oct 01 2008 Oden Eriksson <oeriksson@mandriva.com> 0.06-11mdv2009.0
+ Revision: 290444
- fix deps
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.06-8mdv2008.0
+ Revision: 23910
- rebuild


* Thu Dec 15 2005 Arnaud de Lorbeau <devel@madriva.com> 0.06-7mdk
- rebuild
- mkrel

* Mon Feb 23 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.06-6mdk
- rebuild
- fix source url
- own all dir

* Mon Aug 18 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.06-5mdk
- rebuild for new perl
- drop Prefix tag
- don't use PREFIX
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.06-4mdk
- rebuild for new auto{prov,req}

* Fri Feb 14 2003 Pixel <pixel@mandrakesoft.com> 0.06-3mdk
- rebuild with vendorlib

* Fri Jan 24 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.06-2mdk
- Rebuilt

* Fri Mar 08 2002 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.06-1mdk
- First MandrakeSoft Package

