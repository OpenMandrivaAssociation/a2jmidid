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
#patch0 -p1

%build
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH

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


