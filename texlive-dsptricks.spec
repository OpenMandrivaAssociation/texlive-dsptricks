%global tl_name dsptricks
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Macros for Digital Signal Processing plots
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/dsptricks
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dsptricks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dsptricks.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a set of LaTeX macros (based on PSTricks) for
plotting the kind of graphs and figures that are usually employed in
digital signal processing publications. DSPTricks provides facilities
for standard discrete-time "lollipop" plots, continuous-time and
frequency plots, and pole-zero plots. The companion package DSPFunctions
(dspfunctions.sty) provides macros for computing frequency responses and
DFTs, while the package DSPBlocks (dspblocks.sty) supports DSP block
diagrams.

