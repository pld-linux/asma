Summary:	ASMA - the Atari Sap Music Archive
Summary(pl):	ASMA - archiwum muzyki w formacie SAP
Name:		asma
Version:	2.6
%define		_ver	%(echo %version | tr -d .)
Release:	1
License:	various, not distributable
Group:		Applications/Sound
Source0:	http://asma.dspaudio.com/bin/%{name}%{_ver}.zip
NoSource:	0
URL:		http://asma.dspaudio.com/
BuildRequires:	unzip
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atari SAP music archive is a collection of the Atari XL/XE music in a
format playable by the SAP player. It contains hundreds of the best
Atari tunes while the number of them should grow rapidly.

%description -l pl
Archiwum muzyki w formacie SAP (ASMA) jest kolekcj± muzyki pochodz±cej
z Atari XL/XE w formacie odgrywalnym przez SAP player. Archiwum
zawiera setki najlepszych melodii z Atari i ci±gle siê powiêksza.

%prep
%setup -q -c
unzip -q files.zip

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/asma/{Classics,Demos,Games,Unsorted,Various}
cp -r ASMA/{Classics,Demos,Games,Unsorted,Various} $RPM_BUILD_ROOT%{_datadir}/asma/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ASMA/Docs/*
%{_datadir}/asma
