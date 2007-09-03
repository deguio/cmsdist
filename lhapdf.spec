### RPM external lhapdf 5.2.3-CMS8
%define realversion %(echo %v | cut -d- -f1)
Source: http://cern.ch/service-spi/external/MCGenerators/distribution/%{n}-%{realversion}-src.tgz
%prep
%setup -q -n %{n}/%{realversion}
./configure 

%build
make 

%install
tar -c lib include PDFsets | tar -x -C %i
# SCRAM ToolBox toolfile
mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/%n
<doc type=BuildSystem::ToolDoc version=1.0>
<Tool name=lhapdf version=%v>
<lib name=lhapdf>
<lib name=lhapdf_dummy>
<Client>
 <Environment name=LHAPDF_BASE default="%i"></Environment>
 <Environment name=LIBDIR default="$LHAPDF_BASE/lib"></Environment>
 <Environment name=INCLUDE default="$LHAPDF_BASE/include"></Environment>
 <Environment name=LHAPATH default="$LHAPDF_BASE/PDFsets"></Environment>
</Client>
<Runtime name=LHAPATH value="$LHAPDF_BASE/PDFsets" type=path>
<use name=f77compiler>
</Tool>
EOF_TOOLFILE

%post
%{relocateConfig}etc/scram.d/%n
