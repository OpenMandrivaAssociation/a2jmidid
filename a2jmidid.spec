%define debug_package %{nil}

Name:           a2jmidid
Summary:        ALSA to JACK MIDI Bridging tools
Version:        9
Release:        1

Source0:        https://github.com/linuxaudio/a2jmidid/archive/%{version}/%{name}-%{version}.tar.gz
#Patch0:		a2jmidid-8-glib.patch

URL:            https://github.com/linuxaudio/a2jmidid
License:        GPLv2
Group:          Sound

BuildRequires:	python-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(expat)
BuildRequires:  meson

Requires:       python


%description
A tools suite allowing the use of ALSA MIDI applications and hardware
in a JACK MIDI system. The package provides a2j, a2jmidi_bridge,
a2j_control, j2amidi_bridge and a2jmidid, which are small commandline
applications establishing the bridge between ALSA and JACK MIDI.

%prep
%autosetup -p1

# Fix Python shebangs
sed -i 's|^#!/usr/bin/env python3|#!/usr/bin/python3|' a2j_control

%build
%meson
%meson_build

%install
%meson_install


%files
%doc AUTHORS.rst README.rst CHANGELOG.rst
%license LICENSE
%{_bindir}/a2j
%{_bindir}/a2j_control
%{_bindir}/a2jmidid
%{_bindir}/a2jmidi_bridge
%{_bindir}/j2amidi_bridge
%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service
%doc %{_mandir}/man1/*.1.*



