%global		debug_package %{nil}

Summary:	ALSA to JACK MIDI Bridging tools
Name:	a2jmidid
Version:	9
Release:	2
License:	GPLv2+
Group:	Sound
Url:	https://github.com/linuxaudio/a2jmidid
Source0:	https://github.com/linuxaudio/a2jmidid/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:	a2jmidid-9-spelling-fixes.patch
Patch1:	a2jmidid-9-correct-a2j_control-arguments.patch
BuildRequires:		meson
BuildRequires:		ninja
BuildRequires:		pkgconfig(alsa)
BuildRequires:		pkgconfig(dbus-1)
BuildRequires:		pkgconfig(expat)
BuildRequires:		pkgconfig(jack)
BuildRequires:		pkgconfig(python)
Requires:	python

%description
A tools suite allowing the use of ALSA MIDI applications and hardware in a
JACK MIDI system. The package provides a2j, a2jmidi_bridge,
a2j_control, j2amidi_bridge and a2jmidid, which are small command-line
applications establishing the bridge between ALSA and JACK MIDI.

%files
%doc AUTHORS.rst README.rst CHANGELOG.rst
%license LICENSE
%{_bindir}/a2j
%{_bindir}/a2j_control
%{_bindir}/%{name}
%{_bindir}/a2jmidi_bridge
%{_bindir}/j2amidi_bridge
%{_datadir}/dbus-1/services/org.gna.home.%{name}.service
%{_mandir}/man1/*.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

# Fix Python shebangs
sed -i 's|^#!/usr/bin/env python3|#!/usr/bin/python3|' a2j_control


%build
%meson
%meson_build


%install
%meson_install


