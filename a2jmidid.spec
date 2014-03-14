%define debug_package %{nil}

%define name    a2jmidid
%define version 8
%define release 1

Name:           %{name}
Summary:        ALSA to JACK MIDI Bridging tools
Version:        %{version}
Release:        %{release}

Source:         http://download.gna.org/%name-%version.tar.bz2
Patch:		a2jmidid-8-glib.patch
URL:            http://home.gna.org/a2jmidid/
License:        GPLv2
Group:          Sound

BuildRequires:  python
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(expat)
Requires:       python-dbus


%description
A tools suite allowing the use of ALSA MIDI applications and hardware
in a JACK MIDI system. The package provides a2j, a2jmidi_bridge,
a2j_control, j2amidi_bridge and a2jmidid, which are small commandline
applications establishing the bridge between ALSA and JACK MIDI.

%prep
%setup -q
%patch -p1


%build
./waf configure --prefix=%{_prefix}
./waf

%install
./waf install --destdir=%{buildroot}
mkdir %{buildroot}%{_datadir}/%{name}
cp README %{buildroot}%{_datadir}/%{name}
cp AUTHORS %{buildroot}%{_datadir}/%{name}
cp NEWS %{buildroot}%{_datadir}/%{name}

%files
%doc %{_datadir}/%{name}/README
%doc %{_datadir}/%{name}/AUTHORS
%doc %{_datadir}/%{name}/NEWS
%doc %{_mandir}/man1/*.1.*
%{_bindir}/*
%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service


%changelog
* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 7-3mdv2011.0
+ Revision: 640423
- rebuild to obsolete old packages

* Mon Feb 14 2011 Frank Kober <emuse@mandriva.org> 7-2
+ Revision: 637799
- add python-dbus requires

* Sun Jan 23 2011 Frank Kober <emuse@mandriva.org> 7-1
+ Revision: 632421
- new version 7
  o new man pages added to docs

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 6-2mdv2011.0
+ Revision: 609898
- rebuild

* Tue Feb 23 2010 Frank Kober <emuse@mandriva.org> 6-1mdv2010.1
+ Revision: 510381
- python added to BR
- BR adjusted
- import a2jmidid


