Name:		texlive-dsptricks
Version:	34724
Release:	2
Summary:	Macros for Digital Signal Processing plots
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dsptricks
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dsptricks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dsptricks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a set of LaTeX macros (based on PSTricks)
for plotting the kind of graphs and figures that are usually
employed in digital signal processing publications. DSPTricks
provides facilities for standard discrete-time "lollipop"
plots, continuous-time and frequency plots, and pole-zero
plots. The companion package DSPFunctions (dspfunctions.sty)
provides macros for computing frequency responses and DFTs,
while the package DSPBlocks (dspblocks.sty) supports DSP block
diagrams.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/dsptricks
%doc %{_texmfdistdir}/doc/latex/dsptricks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
