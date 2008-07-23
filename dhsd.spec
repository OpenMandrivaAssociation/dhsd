Summary:	A daemon that updates your DNS record in DHS.ORG whenever your IP changes
Name:		dhsd
Version:	1.0
Release:	%mkrel 10
Group:		Networking/Other
License:	GPL
URL:		http://dhsd.sourceforge.net

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

