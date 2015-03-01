%define debug_package %{nil}

%define name    a2jmidid
%define version 8
%define release 2

Name:           %{name}
Summary:        ALSA to JACK MIDI Bridging tools
Version:        %{version}
Release:        %{release}

Source0:         http://download.gna.org/%name-%version.tar.bz2
Patch0:		a2jmidid-8-glib.patch

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
%patch0 -p1

%build
./waf configure --prefix=%{_prefix}
./waf

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 build/default/a2jmidi_bridge %{buildroot}%{_bindir}/
install -m755 build/default/a2jmidid %{buildroot}%{_bindir}/
install -m755 build/default/j2amidi_bridge %{buildroot}%{_bindir}/
install -m755 a2j %{buildroot}%{_bindir}/
install -m755 a2j_control %{buildroot}%{_bindir}/

sed -i -e 's,env python,python2,' %{buildroot}%{_bindir}/*

mkdir -p %{buildroot}%{_datadir}/dbus-1/services
cp -R build/default/org.gna.home.a2jmidid.service \
	%{buildroot}%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service

mkdir -p %{buildroot}%{_datadir}/%{name}
cp README %{buildroot}%{_datadir}/%{name}
cp AUTHORS %{buildroot}%{_datadir}/%{name}
cp NEWS %{buildroot}%{_datadir}/%{name}


mkdir -p %{buildroot}%{_mandir}/man1
install man/a2j.1  %{buildroot}%{_mandir}/man1/
install man/a2j_control.1 %{buildroot}%{_mandir}/man1/ 
install man/a2jmidi_bridge.1 %{buildroot}%{_mandir}/man1/ 
install man/a2jmidid.1 %{buildroot}%{_mandir}/man1/ 
install man/j2amidi_bridge.1 %{buildroot}%{_mandir}/man1/


%files
%doc %{_datadir}/%{name}/README
%doc %{_datadir}/%{name}/AUTHORS
%doc %{_datadir}/%{name}/NEWS
%doc %{_mandir}/man1/*.1.*
%{_bindir}/*
%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service


