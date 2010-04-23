# This is RPM spec file:

%define _topdir %(echo $PWD)/RPM

Summary:       Afanasy common files
License:       GPL
Name:          afanasy-common
Version:       @VERSION@
Release:       @RELEASE@
Group:         Applications/Graphics

%description
Afanasy common files.

%prep

%build

%install
cd ../..
mv opt $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/opt
%config /opt/cgru/afanasy/config.xml

%clean

%post
echo "Afanasy common POST INSTALL"
[ -d /opt/cgru/afanasy/python ] && find /opt/cgru/afanasy/python -type d -exec chmod a+rwx {} \;
exit 0

%preun
echo "Afanasy common PRE REMOVE:"
pkill afcmd || true
[ -d /opt/cgru/afanasy/python ] && find /opt/cgru/afanasy/python -type f -name *.pyc -exec rm -f {} \;
exit 0
