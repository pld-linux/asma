Summary:	ASMA - the Atari Sap Music Archive
Summary(pl.UTF-8):   ASMA - archiwum muzyki z Atari w formacie SAP
Name:		asma
Version:	3.1
%define		_ver	%(echo %{version} | tr -d .)
Release:	1
License:	various, not distributable
Group:		Applications/Sound
Source0:	http://asma.atari.org/bin/%{name}%{_ver}.rar
# NoSource0-md5:	bcdfb7e5af3a39e9d4608a710f8aef1a
NoSource:	0
URL:		http://asma.atari.org/
BuildRequires:	unrar
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atari SAP music archive is a collection of the Atari XL/XE music in a
format playable by the SAP player. It contains hundreds of the best
Atari tunes while the number of them should grow rapidly.

%description -l pl.UTF-8
Archiwum muzyki w formacie SAP (ASMA) jest kolekcją muzyki pochodzącej
z Atari XL/XE w formacie odgrywalnym przez SAP player. Archiwum
zawiera setki najlepszych melodii z Atari i ciągle się powiększa.

%prep
%setup -q -c -T
unrar x -idq %{SOURCE0}
unrar x -idq files.rar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/asma/{Classics,Demos,Games,Unsorted,Various}
cp -r ASMA/{Classics,Demos,Games,Unsorted,Various} $RPM_BUILD_ROOT%{_datadir}/asma

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ASMA/Docs/*
%{_datadir}/asma
