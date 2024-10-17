Summary:	A daemon that updates your DNS record in DHS.ORG whenever your IP changes
Name:		dhsd
Version:	1.0
Release:	13
Group:		Networking/Other
License:	GPLv2+
URL:		https://dhsd.sourceforge.net

Source:		%name-%version.tar.bz2

BuildRoot:	%_tmppath/%name-buildroot

%description
DHSD is a small project spurned off the need for a proper updater for the 
DHS.ORG dynamic DNS services. There has already existed scripts to do it made
in botche bash scripts and lynxs, even some attempts in perl. This program is 
totally developed in C and sits in the background and changes your record when 
the IP changes.

%prep

%setup -q

%build
%configure

%make CFLAGS="%optflags" CXXFLAGS="%optflags"

%check
%make check

%install
rm -fr %buildroot

#echo "prefix = %buildroot/%_prefix" >> $RPM_BUILD_DIR/dhsd-%{version}/src/Makefile.am
#echo "sysconfdir = %buildroot/%_sysconfdir" >> $RPM_BUILD_DIR/dhsd-%{version}/scripts/Makefile.am

%makeinstall
mkdir -p %buildroot/%_sysconfdir/rc.d
mkdir -p %buildroot/%_sysconfdir/rc.d/init.d
mkdir -p %buildroot/%_sysconfdir/rc.d/rc3.d

cp scripts/dhsd-rh %buildroot/%_sysconfdir/rc.d/init.d/dhsd
ln -s ../init.d/dhsd %buildroot/%_sysconfdir/rc.d/rc3.d/S15dhsd

%post
if [ "$1" = 1 ]; then
   chkconfig --add dhsd
fi

%preun
if [ "$1" = 0 ]; then
   chkconfig --del dhsd
fi

%clean
rm -fr %buildroot

%files
%defattr (-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%_sbindir/dhsd
%config(noreplace) %_sysconfdir/rc.d/init.d/dhsd
%_sysconfdir/rc.d/rc3.d/S15dhsd
%config(noreplace) %_sysconfdir/dhsd.conf



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-12mdv2011.0
+ Revision: 617602
- the mass rebuild of 2010.0 packages

* Wed Jun 17 2009 Jérôme Brenier <incubusss@mandriva.org> 1.0-11mdv2010.0
+ Revision: 386540
- fix license tag

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-10mdv2009.0
+ Revision: 244113
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 8mdv2008.1-current
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import dhsd


* Fri Aug 04 2006 Lenny Cartier <lenny@mandriva.com> 1.0-8mdv2007.0
- rebuild

* Wed May 11 2005 Lenny Cartier <lenny@mandriva.com> 1.0-7mdk
- rebuild

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0-6mdk
- rebuild

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0-5mdk
- rebuild

* Wed Aug 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0-4mdk
- rebuild

* Mon Jul 02 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0-3mdk
- rebuild

* Sat Mar 31 2001 David BAUDENS <baudens@mandrakesoft.com> 1.0-2mdk
- Don't use pentium flags on non %%ix86 architectures

* Tue Feb 06 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0-1mdk
- new in contribs

* Sat Jul 29 2000 Berk D. Demir <berk@linux.org.tr>
- First release of RPM package for DHSD
