%define debug_package %{nil}

%define name    a2jmidid
%define version 8
%define release 2

Name:           %{name}
Summary:        ALSA to JACK MIDI Bridging tools
Version:        %{version}
Release:        %{release}

Source:         http://download.gna.org/%name-%version.tar.bz2
Patch:		    a2jmidid-8-glib.patch
URL:            http://home.gna.org/a2jmidid/
License:        GPLv2
Group:          Sound

BuildRequires:  python2
BuildRequires:  python2-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(expat)
Requires:       python2-dbus


%description
A tools suite allowing the use of ALSA MIDI applications and hardware
in a JACK MIDI system. The package provides a2j, a2jmidi_bridge,
a2j_control, j2amidi_bridge and a2jmidid, which are small commandline
applications establishing the bridge between ALSA and JACK MIDI.

%prep
%setup -q
%patch -p1


%build
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH

./waf configure --prefix=%{_prefix}
./waf build --verbose

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

