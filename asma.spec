Summary:	ASMA - The Atari Sap Music Archive
Summary(pl):	ASMA - Archiwum Muzyki W Formacie Sap
Name:		asma
Version:	2.4
Release:	1
License:	Various
Group:		Applications/Sound
Source0:	http://asma.dspaudio.com/bin/%{name}24.zip
NoSource:	0
URL:		http://asma.dspaudio.com
Buildarch:	noarch
Requires:	sapplay
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atari SAP music archive is a collection of the Atari XL/XE music in a
format playable by the SAP player. It contains hundreds of the best
Atari tunes while the number of them should grow rapidly.

%description -l pl
Archiwum Muzyki W Formacie SAP (ASMA) jest kolekcj± muzyki pochodz±cej
z Atari XL/XE w formacie odgrywalnym przez SAP player. Archiwum
zawiera setki najlepszych melodii z atari i ci±gle siê powiêksza.

%prep
%setup -q -c
unzip files.zip

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/asma/{Classics,Demos,Games,Unsorted,Various}
cp -r ASMA/{Classics,Demos,Games,Unsorted,Various} $RPM_BUILD_ROOT%{_datadir}/asma/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ASMA/Docs/*
%{_datadir}/asma/*
