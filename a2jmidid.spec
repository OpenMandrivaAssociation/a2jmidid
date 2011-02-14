%define name    a2jmidid
%define version 7
%define release %mkrel 2

Name:           %{name}
Summary:        ALSA to JACK MIDI Bridging tools
Version:        %{version}
Release:        %{release}

Source:         http://download.gna.org/%name-%version.tar.bz2
URL:            http://home.gna.org/a2jmidid/
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  python
BuildRequires:  alsa-lib-devel
BuildRequires:  libjack-devel
BuildRequires:  libdbus-1-devel
BuildRequires:  expat-devel
Requires:       python-dbus


%description
A tools suite allowing the use of ALSA MIDI applications and hardware
in a JACK MIDI system. The package provides a2j, a2jmidi_bridge,
a2j_control, j2amidi_bridge and a2jmidid, which are small commandline
applications establishing the bridge between ALSA and JACK MIDI.

%prep
%setup -q

%build
./waf configure --prefix=%{_prefix}
./waf

%install
rm -rf %buildroot
./waf install --destdir=%{buildroot}
mkdir %{buildroot}%{_datadir}/%{name}
cp README %{buildroot}%{_datadir}/%{name}
cp AUTHORS %{buildroot}%{_datadir}/%{name}
cp NEWS %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_datadir}/%{name}/README
%doc %{_datadir}/%{name}/AUTHORS
%doc %{_datadir}/%{name}/NEWS
%doc %{_mandir}/man1/*.1.*

%{_bindir}/*
%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service
