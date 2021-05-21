%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true
%global with_texinfo 0

Name:           texlive-split-w
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1378:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-common.doc.tar.xz
Source1381:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-msg-translations.tar.xz
Source2076:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tapir.tar.xz
Source2077:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tapir.doc.tar.xz
Source2078:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tengwarscript.tar.xz
Source2079:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tengwarscript.doc.tar.xz
Source2081:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tfrupee.tar.xz
Source2082:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tfrupee.doc.tar.xz
Source2145:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-gyre.tar.xz
Source2146:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-gyre.doc.tar.xz
Source2147:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-gyre-math.tar.xz
Source2148:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-gyre-math.doc.tar.xz
Source2328:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabto-generic.tar.xz
Source2329:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/termmenu.tar.xz
Source2330:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/termmenu.doc.tar.xz
Source2335:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texapi.tar.xz
Source2336:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texapi.doc.tar.xz
Source2357:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-ps.tar.xz
Source2358:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-ps.doc.tar.xz
Source2472:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textglos.tar.xz
Source2473:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textglos.doc.tar.xz
Source2524:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-zh-cn.doc.tar.xz
Source2589:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/t2.tar.xz
Source2590:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/t2.doc.tar.xz
Source2591:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-ru.doc.tar.xz
Source2592:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-sr.doc.tar.xz
Source2606:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-cz.doc.tar.xz
Source2653:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabulars-e.doc.tar.xz
Source2654:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tamethebeast.doc.tar.xz
Source2655:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tds.doc.tar.xz
Source2656:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-font-errors-cheatsheet.doc.tar.xz
Source2657:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-overview.doc.tar.xz
Source2658:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-refs.doc.tar.xz
Source2659:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texbytopic.doc.tar.xz
Source2728:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabvar.tar.xz
Source2729:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabvar.doc.tar.xz
Source2731:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tdsfrmath.tar.xz
Source2732:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tdsfrmath.doc.tar.xz
Source2734:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-fr.doc.tar.xz
Source2778:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/templates-fenn.doc.tar.xz
Source2779:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/templates-sommer.doc.tar.xz
Source2780:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-de.doc.tar.xz
Source2826:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/teubner.tar.xz
Source2827:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/teubner.doc.tar.xz
Source2871:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-it.doc.tar.xz
Source2969:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tap.tar.xz
Source2970:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tap.doc.tar.xz
Source2971:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-virtual-academy-pl.doc.tar.xz
Source2972:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-pl.doc.tar.xz
Source3098:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textcase.tar.xz
Source3099:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textcase.doc.tar.xz
Source3290:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdraw.tar.xz
Source3291:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdraw.doc.tar.xz
Source5385:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabfigures.tar.xz
Source5386:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabfigures.doc.tar.xz
Source5388:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tableaux.tar.xz
Source5389:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tableaux.doc.tar.xz
Source5390:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tablefootnote.tar.xz
Source5391:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tablefootnote.doc.tar.xz
Source5393:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tableof.tar.xz
Source5394:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tableof.doc.tar.xz
Source5396:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tablestyles.tar.xz
Source5397:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tablestyles.doc.tar.xz
Source5399:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tablists.tar.xz
Source5400:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tablists.doc.tar.xz
Source5402:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabls.tar.xz
Source5403:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabls.doc.tar.xz
Source5404:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabstackengine.tar.xz
Source5405:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabstackengine.doc.tar.xz
Source5406:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabto-ltx.tar.xz
Source5407:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabto-ltx.doc.tar.xz
Source5408:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabu.tar.xz
Source5409:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabu.doc.tar.xz
Source5411:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabularborder.tar.xz
Source5412:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabularborder.doc.tar.xz
Source5414:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabularcalc.tar.xz
Source5415:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabularcalc.doc.tar.xz
Source5416:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabularew.tar.xz
Source5417:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabularew.doc.tar.xz
Source5419:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabulary.tar.xz
Source5420:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabulary.doc.tar.xz
Source5422:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tagging.tar.xz
Source5423:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tagging.doc.tar.xz
Source5424:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tagpair.tar.xz
Source5425:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tagpair.doc.tar.xz
Source5426:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/talk.tar.xz
Source5427:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/talk.doc.tar.xz
Source5429:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tamefloats.tar.xz
Source5430:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tamefloats.doc.tar.xz
Source5431:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tasks.tar.xz
Source5432:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tasks.doc.tar.xz
Source5433:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tcldoc.tar.xz
Source5434:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tcldoc.doc.tar.xz
Source5436:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tcolorbox.tar.xz
Source5437:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tcolorbox.doc.tar.xz
Source5438:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tdclock.tar.xz
Source5439:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tdclock.doc.tar.xz
Source5440:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/technics.tar.xz
Source5441:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/technics.doc.tar.xz
Source5442:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ted.tar.xz
Source5443:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ted.doc.tar.xz
Source5445:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/templatetools.tar.xz
Source5446:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/templatetools.doc.tar.xz
Source5448:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/termcal.tar.xz
Source5449:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/termcal.doc.tar.xz
Source5451:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/termlist.tar.xz
Source5452:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/termlist.doc.tar.xz
Source5454:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/testhyphens.tar.xz
Source5455:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/testhyphens.doc.tar.xz
Source5457:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-label.tar.xz
Source5458:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-label.doc.tar.xz
Source5460:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlogos.tar.xz
Source5461:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texmate.tar.xz
Source5462:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texmate.doc.tar.xz
Source5464:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texments.tar.xz
Source5465:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texments.doc.tar.xz
Source5467:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texpower.tar.xz
Source5468:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texpower.doc.tar.xz
Source5470:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texshade.tar.xz
Source5471:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texshade.doc.tar.xz
Source5473:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textfit.tar.xz
Source5474:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textfit.doc.tar.xz
Source5476:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textgreek.tar.xz
Source5477:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textgreek.doc.tar.xz
Source5479:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textmerg.tar.xz
Source5480:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textmerg.doc.tar.xz
Source5482:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textpos.tar.xz
Source5483:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textpos.doc.tar.xz
Source5922:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tablor.tar.xz
Source5923:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tablor.doc.tar.xz
Source5924:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tensor.tar.xz
Source5925:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tensor.doc.tar.xz
Source5927:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-ewd.tar.xz
Source5928:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-ewd.doc.tar.xz
Source6020:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textpath.tar.xz
Source6021:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textpath.doc.tar.xz
%if %{with_texinfo}
Source6112:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texinfo.tar.xz
%endif
Source6542:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabriz-thesis.tar.xz
Source6543:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tabriz-thesis.doc.tar.xz
Source6544:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texilikechaps.tar.xz
Source6545:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texilikecover.tar.xz
Source6735:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textopo.tar.xz
Source6736:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textopo.doc.tar.xz
Source6816:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-docindex.tar.xz
Source6817:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-docindex.doc.tar.xz
Source7518:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tempora.tar.xz
Source7519:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tempora.doc.tar.xz
Source7521:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-ini-files.tar.xz
Source7522:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex-ini-files.doc.tar.xz
Source7523:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-es.doc.tar.xz
Source7524:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texvc.tar.xz
Source7525:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texvc.doc.tar.xz
Source7527:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texworks.doc.tar.xz
Source7959:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/table-fct.tar.xz
Source7960:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/table-fct.doc.tar.xz
Source7961:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/termcal-de.tar.xz
Source7962:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/termcal-de.doc.tar.xz
Source7963:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/testidx.tar.xz
Source7964:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/testidx.doc.tar.xz
Source7967:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texproposal.doc.tar.xz
Source8334:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tagpdf.tar.xz
Source8335:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tagpdf.doc.tar.xz
Source8336:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdate.tar.xz
Source8337:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdate.doc.tar.xz
Source8340:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textualicomma.tar.xz
Source8341:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/textualicomma.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-texlive-common-doc
Summary:        Documentation for texlive-common
Version:        svn44191
Provides:       tex-texlive-common-doc
AutoReqProv:    No

%description -n texlive-texlive-common-doc
Documentation for texlive-common

%package -n texlive-texlive-msg-translations
Provides:       tex-texlive-msg-translations = %{tl_version}
License:        LPPL
Summary:        translations of the TeX Live installer and TeX Live Manager
Version:        svn48373
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-texlive-msg-translations
This package contains the translated messages of the TeX Live
installer and TeX Live Manager.  For information on creating or
updating translations, see
http://tug.org/texlive/doc.html#install-tl-xlate.

%package -n texlive-tapir
Provides:       tex-tapir = %{tl_version}
License:        GPL+
Summary:        A simple geometrical font
Version:        svn20484.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tap.pfb) = %{tl_version}

%description -n texlive-tapir
Tapir is a simple geometrical font mostly created of line and
circular segments with constant thickness. The font is
available as Metafont source and in Adobe Type 1 format. The
character set contains all characters in the range 0-127 (as in
cmr10), accented characters used in the Czech, Slovak and
Polish languages.

%package -n texlive-tapir-doc
Summary:        Documentation for tapir
Version:        svn20484.0.2

Provides:       tex-tapir-doc
AutoReqProv:    No

%description -n texlive-tapir-doc
Documentation for tapir

%package -n texlive-tengwarscript
Provides:       tex-tengwarscript = %{tl_version}
License:        LPPL
Summary:        LaTeX support for using Tengwar fonts
Version:        svn34594.1.3.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fp-basic.sty), tex(fp-snap.sty)
Provides:       tex(tengwaralt.enc) = %{tl_version}, tex(tengwarcap.enc) = %{tl_version}
Provides:       tex(tengwarscript.enc) = %{tl_version}, tex(tengwarscript.map) = %{tl_version}
Provides:       tex(Elfica32.tfm) = %{tl_version}, tex(Parmaite.tfm) = %{tl_version}
Provides:       tex(Parmaite_alt.tfm) = %{tl_version}, tex(Parmaite_full.tfm) = %{tl_version}
Provides:       tex(TengwarFormal12.tfm) = %{tl_version}
Provides:       tex(TengwarFormalA12.tfm) = %{tl_version}
Provides:       tex(TengwarFormal_full.tfm) = %{tl_version}
Provides:       tex(TengwarGothika050.tfm) = %{tl_version}
Provides:       tex(TengwarNoldor.tfm) = %{tl_version}, tex(TengwarNoldorAlt.tfm) = %{tl_version}
Provides:       tex(TengwarNoldorCapitals1.tfm) = %{tl_version}
Provides:       tex(TengwarNoldorCapitals2.tfm) = %{tl_version}
Provides:       tex(TengwarNoldor_full.tfm) = %{tl_version}
Provides:       tex(TengwarQuenya.tfm) = %{tl_version}, tex(TengwarQuenyaAlt.tfm) = %{tl_version}
Provides:       tex(TengwarQuenyaCapitals1.tfm) = %{tl_version}
Provides:       tex(TengwarQuenyaCapitals2.tfm) = %{tl_version}
Provides:       tex(TengwarQuenya_full.tfm) = %{tl_version}
Provides:       tex(TengwarSindarin.tfm) = %{tl_version}
Provides:       tex(TengwarSindarinAlt.tfm) = %{tl_version}
Provides:       tex(TengwarSindarinCapitals1.tfm) = %{tl_version}
Provides:       tex(TengwarSindarinCapitals2.tfm) = %{tl_version}
Provides:       tex(TengwarSindarin_full.tfm) = %{tl_version}
Provides:       tex(TengwarTelerin.tfm) = %{tl_version}, tex(UnicodeParmaite.tfm) = %{tl_version}
Provides:       tex(tngan.tfm) = %{tl_version}, tex(tngan_full.tfm) = %{tl_version}
Provides:       tex(tngana.tfm) = %{tl_version}, tex(tnganab.tfm) = %{tl_version}
Provides:       tex(tnganabi.tfm) = %{tl_version}, tex(tnganai.tfm) = %{tl_version}
Provides:       tex(tnganb.tfm) = %{tl_version}, tex(tnganb_full.tfm) = %{tl_version}
Provides:       tex(tnganbi.tfm) = %{tl_version}, tex(tnganbi_full.tfm) = %{tl_version}
Provides:       tex(tngani.tfm) = %{tl_version}, tex(tngani_full.tfm) = %{tl_version}
Provides:       tex(Parmaite_full.vf) = %{tl_version}, tex(TengwarFormal_full.vf) = %{tl_version}
Provides:       tex(TengwarNoldor_full.vf) = %{tl_version}
Provides:       tex(TengwarQuenya_full.vf) = %{tl_version}
Provides:       tex(TengwarSindarin_full.vf) = %{tl_version}
Provides:       tex(tngan_full.vf) = %{tl_version}, tex(tnganb_full.vf) = %{tl_version}
Provides:       tex(tnganbi_full.vf) = %{tl_version}, tex(tngani_full.vf) = %{tl_version}
Provides:       tex(annatar.cfg) = %{tl_version}, tex(annatarbold.cfg) = %{tl_version}
Provides:       tex(annatarbolditalic.cfg) = %{tl_version}
Provides:       tex(annataritalic.cfg) = %{tl_version}, tex(elfica.cfg) = %{tl_version}
Provides:       tex(formal.cfg) = %{tl_version}, tex(gothika.cfg) = %{tl_version}
Provides:       tex(noldor.cfg) = %{tl_version}, tex(noldorcapI.cfg) = %{tl_version}
Provides:       tex(noldorcapII.cfg) = %{tl_version}, tex(parmaite.cfg) = %{tl_version}
Provides:       tex(quenya.cfg) = %{tl_version}, tex(quenyacapI.cfg) = %{tl_version}
Provides:       tex(quenyacapII.cfg) = %{tl_version}, tex(sindarin.cfg) = %{tl_version}
Provides:       tex(sindarincapI.cfg) = %{tl_version}, tex(sindarincapII.cfg) = %{tl_version}
Provides:       tex(teleri.cfg) = %{tl_version}, tex(tengwarscript.sty) = %{tl_version}
Provides:       tex(unicodeparmaite.cfg) = %{tl_version}

%description -n texlive-tengwarscript
The package provides "mid-level" access to tengwar fonts,
providing good quality output. Each tengwar sign is represented
by a command, which will place the sign nicely in relation to
previous signs. A transcription package is available from the
package's home page: writing all those tengwar commands would
quickly become untenable. The package supports the use of a
wide variety of tengwar fonts that are available from the net;
metric and map files are provided for all the supported fonts.

%package -n texlive-tengwarscript-doc
Summary:        Documentation for tengwarscript
Version:        svn34594.1.3.1

Provides:       tex-tengwarscript-doc
AutoReqProv:    No

%description -n texlive-tengwarscript-doc
Documentation for tengwarscript

%package -n texlive-tfrupee
Provides:       tex-tfrupee = %{tl_version}
License:        GPLv3+
Summary:        A font offering the new (Indian) Rupee symbol
Version:        svn20770.1.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(tfrupee.map) = %{tl_version}, tex(tfrupee.tfm) = %{tl_version}
Provides:       tex(tfrupee.pfb) = %{tl_version}, tex(tfrupee.sty) = %{tl_version}

%description -n texlive-tfrupee
The package provides LaTeX support for the (Indian) Rupee
symbol font, created by TechFat. The original font has been
converted to Adobe Type 1 format, and simple LaTeX support
written for its use.

%package -n texlive-tfrupee-doc
Summary:        Documentation for tfrupee
Version:        svn20770.1.02

Provides:       tex-tfrupee-doc
AutoReqProv:    No

%description -n texlive-tfrupee-doc
Documentation for tfrupee

%package -n texlive-tex-gyre
Provides:       tex-tex-gyre = %{tl_version}
License:        GFSL
Summary:        TeX Fonts extending freely available URW fonts
Version:        svn48058
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(tgcursor.sty)
Requires:       tex(tgheros.sty), tex(tgchorus.sty), tex(kvoptions.sty)
Provides:       tex(q-cs-sc.enc) = %{tl_version}, tex(q-cs.enc) = %{tl_version}
Provides:       tex(q-csm-sc.enc) = %{tl_version}, tex(q-csm.enc) = %{tl_version}
Provides:       tex(q-cszc.enc) = %{tl_version}, tex(q-ec-sc.enc) = %{tl_version}
Provides:       tex(q-ec.enc) = %{tl_version}, tex(q-l7x-sc.enc) = %{tl_version}
Provides:       tex(q-l7x.enc) = %{tl_version}, tex(q-l7xzc.enc) = %{tl_version}
Provides:       tex(q-qx-sc.enc) = %{tl_version}, tex(q-qx.enc) = %{tl_version}
Provides:       tex(q-qxm-sc.enc) = %{tl_version}, tex(q-qxm.enc) = %{tl_version}
Provides:       tex(q-qxzc.enc) = %{tl_version}, tex(q-rm-sc.enc) = %{tl_version}
Provides:       tex(q-rm.enc) = %{tl_version}, tex(q-rmm-sc.enc) = %{tl_version}
Provides:       tex(q-rmm.enc) = %{tl_version}, tex(q-rmzc.enc) = %{tl_version}
Provides:       tex(q-t5-sc.enc) = %{tl_version}, tex(q-t5.enc) = %{tl_version}
Provides:       tex(q-texnansi-sc.enc) = %{tl_version}, tex(q-texnansi.enc) = %{tl_version}
Provides:       tex(q-texnansizc.enc) = %{tl_version}, tex(q-ts1.enc) = %{tl_version}
Provides:       tex(qag-cs.map) = %{tl_version}, tex(qag-ec.map) = %{tl_version}
Provides:       tex(qag-l7x.map) = %{tl_version}, tex(qag-qx.map) = %{tl_version}
Provides:       tex(qag-rm.map) = %{tl_version}, tex(qag-t5.map) = %{tl_version}
Provides:       tex(qag-texnansi.map) = %{tl_version}, tex(qag-ts1.map) = %{tl_version}
Provides:       tex(qag.map) = %{tl_version}, tex(qbk-cs.map) = %{tl_version}
Provides:       tex(qbk-ec.map) = %{tl_version}, tex(qbk-l7x.map) = %{tl_version}
Provides:       tex(qbk-qx.map) = %{tl_version}, tex(qbk-rm.map) = %{tl_version}
Provides:       tex(qbk-t5.map) = %{tl_version}, tex(qbk-texnansi.map) = %{tl_version}
Provides:       tex(qbk-ts1.map) = %{tl_version}, tex(qbk.map) = %{tl_version}
Provides:       tex(qcr-cs.map) = %{tl_version}, tex(qcr-ec.map) = %{tl_version}
Provides:       tex(qcr-l7x.map) = %{tl_version}, tex(qcr-qx.map) = %{tl_version}
Provides:       tex(qcr-rm.map) = %{tl_version}, tex(qcr-t5.map) = %{tl_version}
Provides:       tex(qcr-texnansi.map) = %{tl_version}, tex(qcr-ts1.map) = %{tl_version}
Provides:       tex(qcr.map) = %{tl_version}, tex(qcs-cs.map) = %{tl_version}
Provides:       tex(qcs-ec.map) = %{tl_version}, tex(qcs-l7x.map) = %{tl_version}
Provides:       tex(qcs-qx.map) = %{tl_version}, tex(qcs-rm.map) = %{tl_version}
Provides:       tex(qcs-t5.map) = %{tl_version}, tex(qcs-texnansi.map) = %{tl_version}
Provides:       tex(qcs-ts1.map) = %{tl_version}, tex(qcs.map) = %{tl_version}
Provides:       tex(qhv-cs.map) = %{tl_version}, tex(qhv-ec.map) = %{tl_version}
Provides:       tex(qhv-l7x.map) = %{tl_version}, tex(qhv-qx.map) = %{tl_version}
Provides:       tex(qhv-rm.map) = %{tl_version}, tex(qhv-t5.map) = %{tl_version}
Provides:       tex(qhv-texnansi.map) = %{tl_version}, tex(qhv-ts1.map) = %{tl_version}
Provides:       tex(qhv.map) = %{tl_version}, tex(qpl-cs.map) = %{tl_version}
Provides:       tex(qpl-ec.map) = %{tl_version}, tex(qpl-l7x.map) = %{tl_version}
Provides:       tex(qpl-qx.map) = %{tl_version}, tex(qpl-rm.map) = %{tl_version}
Provides:       tex(qpl-t5.map) = %{tl_version}, tex(qpl-texnansi.map) = %{tl_version}
Provides:       tex(qpl-ts1.map) = %{tl_version}, tex(qpl.map) = %{tl_version}
Provides:       tex(qtm-cs.map) = %{tl_version}, tex(qtm-ec.map) = %{tl_version}
Provides:       tex(qtm-l7x.map) = %{tl_version}, tex(qtm-qx.map) = %{tl_version}
Provides:       tex(qtm-rm.map) = %{tl_version}, tex(qtm-t5.map) = %{tl_version}
Provides:       tex(qtm-texnansi.map) = %{tl_version}, tex(qtm-ts1.map) = %{tl_version}
Provides:       tex(qtm.map) = %{tl_version}, tex(qzc-cs.map) = %{tl_version}
Provides:       tex(qzc-ec.map) = %{tl_version}, tex(qzc-l7x.map) = %{tl_version}
Provides:       tex(qzc-qx.map) = %{tl_version}, tex(qzc-rm.map) = %{tl_version}
Provides:       tex(qzc-t5.map) = %{tl_version}, tex(qzc-texnansi.map) = %{tl_version}
Provides:       tex(qzc-ts1.map) = %{tl_version}, tex(qzc.map) = %{tl_version}
Provides:       tex(texgyreadventor-bold.otf) = %{tl_version}
Provides:       tex(texgyreadventor-bolditalic.otf) = %{tl_version}
Provides:       tex(texgyreadventor-italic.otf) = %{tl_version}
Provides:       tex(texgyreadventor-regular.otf) = %{tl_version}
Provides:       tex(texgyrebonum-bold.otf) = %{tl_version}
Provides:       tex(texgyrebonum-bolditalic.otf) = %{tl_version}
Provides:       tex(texgyrebonum-italic.otf) = %{tl_version}
Provides:       tex(texgyrebonum-regular.otf) = %{tl_version}
Provides:       tex(texgyrechorus-mediumitalic.otf) = %{tl_version}
Provides:       tex(texgyrecursor-bold.otf) = %{tl_version}
Provides:       tex(texgyrecursor-bolditalic.otf) = %{tl_version}
Provides:       tex(texgyrecursor-italic.otf) = %{tl_version}
Provides:       tex(texgyrecursor-regular.otf) = %{tl_version}
Provides:       tex(texgyreheros-bold.otf) = %{tl_version}
Provides:       tex(texgyreheros-bolditalic.otf) = %{tl_version}
Provides:       tex(texgyreheros-italic.otf) = %{tl_version}
Provides:       tex(texgyreheros-regular.otf) = %{tl_version}
Provides:       tex(texgyreheroscn-bold.otf) = %{tl_version}
Provides:       tex(texgyreheroscn-bolditalic.otf) = %{tl_version}
Provides:       tex(texgyreheroscn-italic.otf) = %{tl_version}
Provides:       tex(texgyreheroscn-regular.otf) = %{tl_version}
Provides:       tex(texgyrepagella-bold.otf) = %{tl_version}
Provides:       tex(texgyrepagella-bolditalic.otf) = %{tl_version}
Provides:       tex(texgyrepagella-italic.otf) = %{tl_version}
Provides:       tex(texgyrepagella-regular.otf) = %{tl_version}
Provides:       tex(texgyreschola-bold.otf) = %{tl_version}
Provides:       tex(texgyreschola-bolditalic.otf) = %{tl_version}
Provides:       tex(texgyreschola-italic.otf) = %{tl_version}
Provides:       tex(texgyreschola-regular.otf) = %{tl_version}
Provides:       tex(texgyretermes-bold.otf) = %{tl_version}
Provides:       tex(texgyretermes-bolditalic.otf) = %{tl_version}
Provides:       tex(texgyretermes-italic.otf) = %{tl_version}
Provides:       tex(texgyretermes-regular.otf) = %{tl_version}
Provides:       tex(cs-qagb-sc.tfm) = %{tl_version}, tex(cs-qagb.tfm) = %{tl_version}
Provides:       tex(cs-qagbi-sc.tfm) = %{tl_version}, tex(cs-qagbi.tfm) = %{tl_version}
Provides:       tex(cs-qagr-sc.tfm) = %{tl_version}, tex(cs-qagr.tfm) = %{tl_version}
Provides:       tex(cs-qagri-sc.tfm) = %{tl_version}, tex(cs-qagri.tfm) = %{tl_version}
Provides:       tex(cs-qbkb-sc.tfm) = %{tl_version}, tex(cs-qbkb.tfm) = %{tl_version}
Provides:       tex(cs-qbkbi-sc.tfm) = %{tl_version}, tex(cs-qbkbi.tfm) = %{tl_version}
Provides:       tex(cs-qbkr-sc.tfm) = %{tl_version}, tex(cs-qbkr.tfm) = %{tl_version}
Provides:       tex(cs-qbkri-sc.tfm) = %{tl_version}, tex(cs-qbkri.tfm) = %{tl_version}
Provides:       tex(cs-qcrb-sc.tfm) = %{tl_version}, tex(cs-qcrb.tfm) = %{tl_version}
Provides:       tex(cs-qcrbi-sc.tfm) = %{tl_version}, tex(cs-qcrbi.tfm) = %{tl_version}
Provides:       tex(cs-qcrr-sc.tfm) = %{tl_version}, tex(cs-qcrr.tfm) = %{tl_version}
Provides:       tex(cs-qcrri-sc.tfm) = %{tl_version}, tex(cs-qcrri.tfm) = %{tl_version}
Provides:       tex(cs-qcsb-sc.tfm) = %{tl_version}, tex(cs-qcsb.tfm) = %{tl_version}
Provides:       tex(cs-qcsbi-sc.tfm) = %{tl_version}, tex(cs-qcsbi.tfm) = %{tl_version}
Provides:       tex(cs-qcsr-sc.tfm) = %{tl_version}, tex(cs-qcsr.tfm) = %{tl_version}
Provides:       tex(cs-qcsri-sc.tfm) = %{tl_version}, tex(cs-qcsri.tfm) = %{tl_version}
Provides:       tex(cs-qhvb-sc.tfm) = %{tl_version}, tex(cs-qhvb.tfm) = %{tl_version}
Provides:       tex(cs-qhvbi-sc.tfm) = %{tl_version}, tex(cs-qhvbi.tfm) = %{tl_version}
Provides:       tex(cs-qhvcb-sc.tfm) = %{tl_version}, tex(cs-qhvcb.tfm) = %{tl_version}
Provides:       tex(cs-qhvcbi-sc.tfm) = %{tl_version}, tex(cs-qhvcbi.tfm) = %{tl_version}
Provides:       tex(cs-qhvcr-sc.tfm) = %{tl_version}, tex(cs-qhvcr.tfm) = %{tl_version}
Provides:       tex(cs-qhvcri-sc.tfm) = %{tl_version}, tex(cs-qhvcri.tfm) = %{tl_version}
Provides:       tex(cs-qhvr-sc.tfm) = %{tl_version}, tex(cs-qhvr.tfm) = %{tl_version}
Provides:       tex(cs-qhvri-sc.tfm) = %{tl_version}, tex(cs-qhvri.tfm) = %{tl_version}
Provides:       tex(cs-qplb-sc.tfm) = %{tl_version}, tex(cs-qplb.tfm) = %{tl_version}
Provides:       tex(cs-qplbi-sc.tfm) = %{tl_version}, tex(cs-qplbi.tfm) = %{tl_version}
Provides:       tex(cs-qplr-sc.tfm) = %{tl_version}, tex(cs-qplr.tfm) = %{tl_version}
Provides:       tex(cs-qplri-sc.tfm) = %{tl_version}, tex(cs-qplri.tfm) = %{tl_version}
Provides:       tex(cs-qtmb-sc.tfm) = %{tl_version}, tex(cs-qtmb.tfm) = %{tl_version}
Provides:       tex(cs-qtmbi-sc.tfm) = %{tl_version}, tex(cs-qtmbi.tfm) = %{tl_version}
Provides:       tex(cs-qtmr-sc.tfm) = %{tl_version}, tex(cs-qtmr.tfm) = %{tl_version}
Provides:       tex(cs-qtmri-sc.tfm) = %{tl_version}, tex(cs-qtmri.tfm) = %{tl_version}
Provides:       tex(cs-qzcmi.tfm) = %{tl_version}, tex(ec-qagb-sc.tfm) = %{tl_version}
Provides:       tex(ec-qagb.tfm) = %{tl_version}, tex(ec-qagbi-sc.tfm) = %{tl_version}
Provides:       tex(ec-qagbi.tfm) = %{tl_version}, tex(ec-qagr-sc.tfm) = %{tl_version}
Provides:       tex(ec-qagr.tfm) = %{tl_version}, tex(ec-qagri-sc.tfm) = %{tl_version}
Provides:       tex(ec-qagri.tfm) = %{tl_version}, tex(ec-qbkb-sc.tfm) = %{tl_version}
Provides:       tex(ec-qbkb.tfm) = %{tl_version}, tex(ec-qbkbi-sc.tfm) = %{tl_version}
Provides:       tex(ec-qbkbi.tfm) = %{tl_version}, tex(ec-qbkr-sc.tfm) = %{tl_version}
Provides:       tex(ec-qbkr.tfm) = %{tl_version}, tex(ec-qbkri-sc.tfm) = %{tl_version}
Provides:       tex(ec-qbkri.tfm) = %{tl_version}, tex(ec-qcrb-sc.tfm) = %{tl_version}
Provides:       tex(ec-qcrb.tfm) = %{tl_version}, tex(ec-qcrbi-sc.tfm) = %{tl_version}
Provides:       tex(ec-qcrbi.tfm) = %{tl_version}, tex(ec-qcrr-sc.tfm) = %{tl_version}
Provides:       tex(ec-qcrr.tfm) = %{tl_version}, tex(ec-qcrri-sc.tfm) = %{tl_version}
Provides:       tex(ec-qcrri.tfm) = %{tl_version}, tex(ec-qcsb-sc.tfm) = %{tl_version}
Provides:       tex(ec-qcsb.tfm) = %{tl_version}, tex(ec-qcsbi-sc.tfm) = %{tl_version}
Provides:       tex(ec-qcsbi.tfm) = %{tl_version}, tex(ec-qcsr-sc.tfm) = %{tl_version}
Provides:       tex(ec-qcsr.tfm) = %{tl_version}, tex(ec-qcsri-sc.tfm) = %{tl_version}
Provides:       tex(ec-qcsri.tfm) = %{tl_version}, tex(ec-qhvb-sc.tfm) = %{tl_version}
Provides:       tex(ec-qhvb.tfm) = %{tl_version}, tex(ec-qhvbi-sc.tfm) = %{tl_version}
Provides:       tex(ec-qhvbi.tfm) = %{tl_version}, tex(ec-qhvcb-sc.tfm) = %{tl_version}
Provides:       tex(ec-qhvcb.tfm) = %{tl_version}, tex(ec-qhvcbi-sc.tfm) = %{tl_version}
Provides:       tex(ec-qhvcbi.tfm) = %{tl_version}, tex(ec-qhvcr-sc.tfm) = %{tl_version}
Provides:       tex(ec-qhvcr.tfm) = %{tl_version}, tex(ec-qhvcri-sc.tfm) = %{tl_version}
Provides:       tex(ec-qhvcri.tfm) = %{tl_version}, tex(ec-qhvr-sc.tfm) = %{tl_version}
Provides:       tex(ec-qhvr.tfm) = %{tl_version}, tex(ec-qhvri-sc.tfm) = %{tl_version}
Provides:       tex(ec-qhvri.tfm) = %{tl_version}, tex(ec-qplb-sc.tfm) = %{tl_version}
Provides:       tex(ec-qplb.tfm) = %{tl_version}, tex(ec-qplbi-sc.tfm) = %{tl_version}
Provides:       tex(ec-qplbi.tfm) = %{tl_version}, tex(ec-qplr-sc.tfm) = %{tl_version}
Provides:       tex(ec-qplr.tfm) = %{tl_version}, tex(ec-qplri-sc.tfm) = %{tl_version}
Provides:       tex(ec-qplri.tfm) = %{tl_version}, tex(ec-qtmb-sc.tfm) = %{tl_version}
Provides:       tex(ec-qtmb.tfm) = %{tl_version}, tex(ec-qtmbi-sc.tfm) = %{tl_version}
Provides:       tex(ec-qtmbi.tfm) = %{tl_version}, tex(ec-qtmr-sc.tfm) = %{tl_version}
Provides:       tex(ec-qtmr.tfm) = %{tl_version}, tex(ec-qtmri-sc.tfm) = %{tl_version}
Provides:       tex(ec-qtmri.tfm) = %{tl_version}, tex(ec-qzcmi.tfm) = %{tl_version}
Provides:       tex(l7x-qagb-sc.tfm) = %{tl_version}, tex(l7x-qagb.tfm) = %{tl_version}
Provides:       tex(l7x-qagbi-sc.tfm) = %{tl_version}, tex(l7x-qagbi.tfm) = %{tl_version}
Provides:       tex(l7x-qagr-sc.tfm) = %{tl_version}, tex(l7x-qagr.tfm) = %{tl_version}
Provides:       tex(l7x-qagri-sc.tfm) = %{tl_version}, tex(l7x-qagri.tfm) = %{tl_version}
Provides:       tex(l7x-qbkb-sc.tfm) = %{tl_version}, tex(l7x-qbkb.tfm) = %{tl_version}
Provides:       tex(l7x-qbkbi-sc.tfm) = %{tl_version}, tex(l7x-qbkbi.tfm) = %{tl_version}
Provides:       tex(l7x-qbkr-sc.tfm) = %{tl_version}, tex(l7x-qbkr.tfm) = %{tl_version}
Provides:       tex(l7x-qbkri-sc.tfm) = %{tl_version}, tex(l7x-qbkri.tfm) = %{tl_version}
Provides:       tex(l7x-qcrb-sc.tfm) = %{tl_version}, tex(l7x-qcrb.tfm) = %{tl_version}
Provides:       tex(l7x-qcrbi-sc.tfm) = %{tl_version}, tex(l7x-qcrbi.tfm) = %{tl_version}
Provides:       tex(l7x-qcrr-sc.tfm) = %{tl_version}, tex(l7x-qcrr.tfm) = %{tl_version}
Provides:       tex(l7x-qcrri-sc.tfm) = %{tl_version}, tex(l7x-qcrri.tfm) = %{tl_version}
Provides:       tex(l7x-qcsb-sc.tfm) = %{tl_version}, tex(l7x-qcsb.tfm) = %{tl_version}
Provides:       tex(l7x-qcsbi-sc.tfm) = %{tl_version}, tex(l7x-qcsbi.tfm) = %{tl_version}
Provides:       tex(l7x-qcsr-sc.tfm) = %{tl_version}, tex(l7x-qcsr.tfm) = %{tl_version}
Provides:       tex(l7x-qcsri-sc.tfm) = %{tl_version}, tex(l7x-qcsri.tfm) = %{tl_version}
Provides:       tex(l7x-qhvb-sc.tfm) = %{tl_version}, tex(l7x-qhvb.tfm) = %{tl_version}
Provides:       tex(l7x-qhvbi-sc.tfm) = %{tl_version}, tex(l7x-qhvbi.tfm) = %{tl_version}
Provides:       tex(l7x-qhvcb-sc.tfm) = %{tl_version}, tex(l7x-qhvcb.tfm) = %{tl_version}
Provides:       tex(l7x-qhvcbi-sc.tfm) = %{tl_version}, tex(l7x-qhvcbi.tfm) = %{tl_version}
Provides:       tex(l7x-qhvcr-sc.tfm) = %{tl_version}, tex(l7x-qhvcr.tfm) = %{tl_version}
Provides:       tex(l7x-qhvcri-sc.tfm) = %{tl_version}, tex(l7x-qhvcri.tfm) = %{tl_version}
Provides:       tex(l7x-qhvr-sc.tfm) = %{tl_version}, tex(l7x-qhvr.tfm) = %{tl_version}
Provides:       tex(l7x-qhvri-sc.tfm) = %{tl_version}, tex(l7x-qhvri.tfm) = %{tl_version}
Provides:       tex(l7x-qplb-sc.tfm) = %{tl_version}, tex(l7x-qplb.tfm) = %{tl_version}
Provides:       tex(l7x-qplbi-sc.tfm) = %{tl_version}, tex(l7x-qplbi.tfm) = %{tl_version}
Provides:       tex(l7x-qplr-sc.tfm) = %{tl_version}, tex(l7x-qplr.tfm) = %{tl_version}
Provides:       tex(l7x-qplri-sc.tfm) = %{tl_version}, tex(l7x-qplri.tfm) = %{tl_version}
Provides:       tex(l7x-qtmb-sc.tfm) = %{tl_version}, tex(l7x-qtmb.tfm) = %{tl_version}
Provides:       tex(l7x-qtmbi-sc.tfm) = %{tl_version}, tex(l7x-qtmbi.tfm) = %{tl_version}
Provides:       tex(l7x-qtmr-sc.tfm) = %{tl_version}, tex(l7x-qtmr.tfm) = %{tl_version}
Provides:       tex(l7x-qtmri-sc.tfm) = %{tl_version}, tex(l7x-qtmri.tfm) = %{tl_version}
Provides:       tex(l7x-qzcmi.tfm) = %{tl_version}, tex(qx-qagb-sc.tfm) = %{tl_version}
Provides:       tex(qx-qagb.tfm) = %{tl_version}, tex(qx-qagbi-sc.tfm) = %{tl_version}
Provides:       tex(qx-qagbi.tfm) = %{tl_version}, tex(qx-qagr-sc.tfm) = %{tl_version}
Provides:       tex(qx-qagr.tfm) = %{tl_version}, tex(qx-qagri-sc.tfm) = %{tl_version}
Provides:       tex(qx-qagri.tfm) = %{tl_version}, tex(qx-qbkb-sc.tfm) = %{tl_version}
Provides:       tex(qx-qbkb.tfm) = %{tl_version}, tex(qx-qbkbi-sc.tfm) = %{tl_version}
Provides:       tex(qx-qbkbi.tfm) = %{tl_version}, tex(qx-qbkr-sc.tfm) = %{tl_version}
Provides:       tex(qx-qbkr.tfm) = %{tl_version}, tex(qx-qbkri-sc.tfm) = %{tl_version}
Provides:       tex(qx-qbkri.tfm) = %{tl_version}, tex(qx-qcrb-sc.tfm) = %{tl_version}
Provides:       tex(qx-qcrb.tfm) = %{tl_version}, tex(qx-qcrbi-sc.tfm) = %{tl_version}
Provides:       tex(qx-qcrbi.tfm) = %{tl_version}, tex(qx-qcrr-sc.tfm) = %{tl_version}
Provides:       tex(qx-qcrr.tfm) = %{tl_version}, tex(qx-qcrri-sc.tfm) = %{tl_version}
Provides:       tex(qx-qcrri.tfm) = %{tl_version}, tex(qx-qcsb-sc.tfm) = %{tl_version}
Provides:       tex(qx-qcsb.tfm) = %{tl_version}, tex(qx-qcsbi-sc.tfm) = %{tl_version}
Provides:       tex(qx-qcsbi.tfm) = %{tl_version}, tex(qx-qcsr-sc.tfm) = %{tl_version}
Provides:       tex(qx-qcsr.tfm) = %{tl_version}, tex(qx-qcsri-sc.tfm) = %{tl_version}
Provides:       tex(qx-qcsri.tfm) = %{tl_version}, tex(qx-qhvb-sc.tfm) = %{tl_version}
Provides:       tex(qx-qhvb.tfm) = %{tl_version}, tex(qx-qhvbi-sc.tfm) = %{tl_version}
Provides:       tex(qx-qhvbi.tfm) = %{tl_version}, tex(qx-qhvcb-sc.tfm) = %{tl_version}
Provides:       tex(qx-qhvcb.tfm) = %{tl_version}, tex(qx-qhvcbi-sc.tfm) = %{tl_version}
Provides:       tex(qx-qhvcbi.tfm) = %{tl_version}, tex(qx-qhvcr-sc.tfm) = %{tl_version}
Provides:       tex(qx-qhvcr.tfm) = %{tl_version}, tex(qx-qhvcri-sc.tfm) = %{tl_version}
Provides:       tex(qx-qhvcri.tfm) = %{tl_version}, tex(qx-qhvr-sc.tfm) = %{tl_version}
Provides:       tex(qx-qhvr.tfm) = %{tl_version}, tex(qx-qhvri-sc.tfm) = %{tl_version}
Provides:       tex(qx-qhvri.tfm) = %{tl_version}, tex(qx-qplb-sc.tfm) = %{tl_version}
Provides:       tex(qx-qplb.tfm) = %{tl_version}, tex(qx-qplbi-sc.tfm) = %{tl_version}
Provides:       tex(qx-qplbi.tfm) = %{tl_version}, tex(qx-qplr-sc.tfm) = %{tl_version}
Provides:       tex(qx-qplr.tfm) = %{tl_version}, tex(qx-qplri-sc.tfm) = %{tl_version}
Provides:       tex(qx-qplri.tfm) = %{tl_version}, tex(qx-qtmb-sc.tfm) = %{tl_version}
Provides:       tex(qx-qtmb.tfm) = %{tl_version}, tex(qx-qtmbi-sc.tfm) = %{tl_version}
Provides:       tex(qx-qtmbi.tfm) = %{tl_version}, tex(qx-qtmr-sc.tfm) = %{tl_version}
Provides:       tex(qx-qtmr.tfm) = %{tl_version}, tex(qx-qtmri-sc.tfm) = %{tl_version}
Provides:       tex(qx-qtmri.tfm) = %{tl_version}, tex(qx-qzcmi.tfm) = %{tl_version}
Provides:       tex(rm-qagb-sc.tfm) = %{tl_version}, tex(rm-qagb.tfm) = %{tl_version}
Provides:       tex(rm-qagbi-sc.tfm) = %{tl_version}, tex(rm-qagbi.tfm) = %{tl_version}
Provides:       tex(rm-qagr-sc.tfm) = %{tl_version}, tex(rm-qagr.tfm) = %{tl_version}
Provides:       tex(rm-qagri-sc.tfm) = %{tl_version}, tex(rm-qagri.tfm) = %{tl_version}
Provides:       tex(rm-qbkb-sc.tfm) = %{tl_version}, tex(rm-qbkb.tfm) = %{tl_version}
Provides:       tex(rm-qbkbi-sc.tfm) = %{tl_version}, tex(rm-qbkbi.tfm) = %{tl_version}
Provides:       tex(rm-qbkr-sc.tfm) = %{tl_version}, tex(rm-qbkr.tfm) = %{tl_version}
Provides:       tex(rm-qbkri-sc.tfm) = %{tl_version}, tex(rm-qbkri.tfm) = %{tl_version}
Provides:       tex(rm-qcrb-sc.tfm) = %{tl_version}, tex(rm-qcrb.tfm) = %{tl_version}
Provides:       tex(rm-qcrbi-sc.tfm) = %{tl_version}, tex(rm-qcrbi.tfm) = %{tl_version}
Provides:       tex(rm-qcrr-sc.tfm) = %{tl_version}, tex(rm-qcrr.tfm) = %{tl_version}
Provides:       tex(rm-qcrri-sc.tfm) = %{tl_version}, tex(rm-qcrri.tfm) = %{tl_version}
Provides:       tex(rm-qcsb-sc.tfm) = %{tl_version}, tex(rm-qcsb.tfm) = %{tl_version}
Provides:       tex(rm-qcsbi-sc.tfm) = %{tl_version}, tex(rm-qcsbi.tfm) = %{tl_version}
Provides:       tex(rm-qcsr-sc.tfm) = %{tl_version}, tex(rm-qcsr.tfm) = %{tl_version}
Provides:       tex(rm-qcsri-sc.tfm) = %{tl_version}, tex(rm-qcsri.tfm) = %{tl_version}
Provides:       tex(rm-qhvb-sc.tfm) = %{tl_version}, tex(rm-qhvb.tfm) = %{tl_version}
Provides:       tex(rm-qhvbi-sc.tfm) = %{tl_version}, tex(rm-qhvbi.tfm) = %{tl_version}
Provides:       tex(rm-qhvcb-sc.tfm) = %{tl_version}, tex(rm-qhvcb.tfm) = %{tl_version}
Provides:       tex(rm-qhvcbi-sc.tfm) = %{tl_version}, tex(rm-qhvcbi.tfm) = %{tl_version}
Provides:       tex(rm-qhvcr-sc.tfm) = %{tl_version}, tex(rm-qhvcr.tfm) = %{tl_version}
Provides:       tex(rm-qhvcri-sc.tfm) = %{tl_version}, tex(rm-qhvcri.tfm) = %{tl_version}
Provides:       tex(rm-qhvr-sc.tfm) = %{tl_version}, tex(rm-qhvr.tfm) = %{tl_version}
Provides:       tex(rm-qhvri-sc.tfm) = %{tl_version}, tex(rm-qhvri.tfm) = %{tl_version}
Provides:       tex(rm-qplb-sc.tfm) = %{tl_version}, tex(rm-qplb.tfm) = %{tl_version}
Provides:       tex(rm-qplbi-sc.tfm) = %{tl_version}, tex(rm-qplbi.tfm) = %{tl_version}
Provides:       tex(rm-qplr-sc.tfm) = %{tl_version}, tex(rm-qplr.tfm) = %{tl_version}
Provides:       tex(rm-qplri-sc.tfm) = %{tl_version}, tex(rm-qplri.tfm) = %{tl_version}
Provides:       tex(rm-qtmb-sc.tfm) = %{tl_version}, tex(rm-qtmb.tfm) = %{tl_version}
Provides:       tex(rm-qtmbi-sc.tfm) = %{tl_version}, tex(rm-qtmbi.tfm) = %{tl_version}
Provides:       tex(rm-qtmr-sc.tfm) = %{tl_version}, tex(rm-qtmr.tfm) = %{tl_version}
Provides:       tex(rm-qtmri-sc.tfm) = %{tl_version}, tex(rm-qtmri.tfm) = %{tl_version}
Provides:       tex(rm-qzcmi.tfm) = %{tl_version}, tex(t5-qagb-sc.tfm) = %{tl_version}
Provides:       tex(t5-qagb.tfm) = %{tl_version}, tex(t5-qagbi-sc.tfm) = %{tl_version}
Provides:       tex(t5-qagbi.tfm) = %{tl_version}, tex(t5-qagr-sc.tfm) = %{tl_version}
Provides:       tex(t5-qagr.tfm) = %{tl_version}, tex(t5-qagri-sc.tfm) = %{tl_version}
Provides:       tex(t5-qagri.tfm) = %{tl_version}, tex(t5-qbkb-sc.tfm) = %{tl_version}
Provides:       tex(t5-qbkb.tfm) = %{tl_version}, tex(t5-qbkbi-sc.tfm) = %{tl_version}
Provides:       tex(t5-qbkbi.tfm) = %{tl_version}, tex(t5-qbkr-sc.tfm) = %{tl_version}
Provides:       tex(t5-qbkr.tfm) = %{tl_version}, tex(t5-qbkri-sc.tfm) = %{tl_version}
Provides:       tex(t5-qbkri.tfm) = %{tl_version}, tex(t5-qcrb-sc.tfm) = %{tl_version}
Provides:       tex(t5-qcrb.tfm) = %{tl_version}, tex(t5-qcrbi-sc.tfm) = %{tl_version}
Provides:       tex(t5-qcrbi.tfm) = %{tl_version}, tex(t5-qcrr-sc.tfm) = %{tl_version}
Provides:       tex(t5-qcrr.tfm) = %{tl_version}, tex(t5-qcrri-sc.tfm) = %{tl_version}
Provides:       tex(t5-qcrri.tfm) = %{tl_version}, tex(t5-qcsb-sc.tfm) = %{tl_version}
Provides:       tex(t5-qcsb.tfm) = %{tl_version}, tex(t5-qcsbi-sc.tfm) = %{tl_version}
Provides:       tex(t5-qcsbi.tfm) = %{tl_version}, tex(t5-qcsr-sc.tfm) = %{tl_version}
Provides:       tex(t5-qcsr.tfm) = %{tl_version}, tex(t5-qcsri-sc.tfm) = %{tl_version}
Provides:       tex(t5-qcsri.tfm) = %{tl_version}, tex(t5-qhvb-sc.tfm) = %{tl_version}
Provides:       tex(t5-qhvb.tfm) = %{tl_version}, tex(t5-qhvbi-sc.tfm) = %{tl_version}
Provides:       tex(t5-qhvbi.tfm) = %{tl_version}, tex(t5-qhvcb-sc.tfm) = %{tl_version}
Provides:       tex(t5-qhvcb.tfm) = %{tl_version}, tex(t5-qhvcbi-sc.tfm) = %{tl_version}
Provides:       tex(t5-qhvcbi.tfm) = %{tl_version}, tex(t5-qhvcr-sc.tfm) = %{tl_version}
Provides:       tex(t5-qhvcr.tfm) = %{tl_version}, tex(t5-qhvcri-sc.tfm) = %{tl_version}
Provides:       tex(t5-qhvcri.tfm) = %{tl_version}, tex(t5-qhvr-sc.tfm) = %{tl_version}
Provides:       tex(t5-qhvr.tfm) = %{tl_version}, tex(t5-qhvri-sc.tfm) = %{tl_version}
Provides:       tex(t5-qhvri.tfm) = %{tl_version}, tex(t5-qplb-sc.tfm) = %{tl_version}
Provides:       tex(t5-qplb.tfm) = %{tl_version}, tex(t5-qplbi-sc.tfm) = %{tl_version}
Provides:       tex(t5-qplbi.tfm) = %{tl_version}, tex(t5-qplr-sc.tfm) = %{tl_version}
Provides:       tex(t5-qplr.tfm) = %{tl_version}, tex(t5-qplri-sc.tfm) = %{tl_version}
Provides:       tex(t5-qplri.tfm) = %{tl_version}, tex(t5-qtmb-sc.tfm) = %{tl_version}
Provides:       tex(t5-qtmb.tfm) = %{tl_version}, tex(t5-qtmbi-sc.tfm) = %{tl_version}
Provides:       tex(t5-qtmbi.tfm) = %{tl_version}, tex(t5-qtmr-sc.tfm) = %{tl_version}
Provides:       tex(t5-qtmr.tfm) = %{tl_version}, tex(t5-qtmri-sc.tfm) = %{tl_version}
Provides:       tex(t5-qtmri.tfm) = %{tl_version}, tex(t5-qzcmi.tfm) = %{tl_version}
Provides:       tex(texnansi-qagb-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qagb.tfm) = %{tl_version}, tex(texnansi-qagbi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qagbi.tfm) = %{tl_version}, tex(texnansi-qagr-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qagr.tfm) = %{tl_version}, tex(texnansi-qagri-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qagri.tfm) = %{tl_version}, tex(texnansi-qbkb-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qbkb.tfm) = %{tl_version}, tex(texnansi-qbkbi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qbkbi.tfm) = %{tl_version}, tex(texnansi-qbkr-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qbkr.tfm) = %{tl_version}, tex(texnansi-qbkri-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qbkri.tfm) = %{tl_version}, tex(texnansi-qcrb-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qcrb.tfm) = %{tl_version}, tex(texnansi-qcrbi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qcrbi.tfm) = %{tl_version}, tex(texnansi-qcrr-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qcrr.tfm) = %{tl_version}, tex(texnansi-qcrri-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qcrri.tfm) = %{tl_version}, tex(texnansi-qcsb-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qcsb.tfm) = %{tl_version}, tex(texnansi-qcsbi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qcsbi.tfm) = %{tl_version}, tex(texnansi-qcsr-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qcsr.tfm) = %{tl_version}, tex(texnansi-qcsri-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qcsri.tfm) = %{tl_version}, tex(texnansi-qhvb-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qhvb.tfm) = %{tl_version}, tex(texnansi-qhvbi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qhvbi.tfm) = %{tl_version}, tex(texnansi-qhvcb-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qhvcb.tfm) = %{tl_version}, tex(texnansi-qhvcbi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qhvcbi.tfm) = %{tl_version}
Provides:       tex(texnansi-qhvcr-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qhvcr.tfm) = %{tl_version}, tex(texnansi-qhvcri-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qhvcri.tfm) = %{tl_version}
Provides:       tex(texnansi-qhvr-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qhvr.tfm) = %{tl_version}, tex(texnansi-qhvri-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qhvri.tfm) = %{tl_version}, tex(texnansi-qplb-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qplb.tfm) = %{tl_version}, tex(texnansi-qplbi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qplbi.tfm) = %{tl_version}, tex(texnansi-qplr-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qplr.tfm) = %{tl_version}, tex(texnansi-qplri-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qplri.tfm) = %{tl_version}, tex(texnansi-qtmb-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qtmb.tfm) = %{tl_version}, tex(texnansi-qtmbi-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qtmbi.tfm) = %{tl_version}, tex(texnansi-qtmr-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qtmr.tfm) = %{tl_version}, tex(texnansi-qtmri-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-qtmri.tfm) = %{tl_version}, tex(texnansi-qzcmi.tfm) = %{tl_version}
Provides:       tex(ts1-qagb.tfm) = %{tl_version}, tex(ts1-qagbi.tfm) = %{tl_version}
Provides:       tex(ts1-qagr.tfm) = %{tl_version}, tex(ts1-qagri.tfm) = %{tl_version}
Provides:       tex(ts1-qbkb.tfm) = %{tl_version}, tex(ts1-qbkbi.tfm) = %{tl_version}
Provides:       tex(ts1-qbkr.tfm) = %{tl_version}, tex(ts1-qbkri.tfm) = %{tl_version}
Provides:       tex(ts1-qcrb.tfm) = %{tl_version}, tex(ts1-qcrbi.tfm) = %{tl_version}
Provides:       tex(ts1-qcrr.tfm) = %{tl_version}, tex(ts1-qcrri.tfm) = %{tl_version}
Provides:       tex(ts1-qcsb.tfm) = %{tl_version}, tex(ts1-qcsbi.tfm) = %{tl_version}
Provides:       tex(ts1-qcsr.tfm) = %{tl_version}, tex(ts1-qcsri.tfm) = %{tl_version}
Provides:       tex(ts1-qhvb.tfm) = %{tl_version}, tex(ts1-qhvbi.tfm) = %{tl_version}
Provides:       tex(ts1-qhvcb.tfm) = %{tl_version}, tex(ts1-qhvcbi.tfm) = %{tl_version}
Provides:       tex(ts1-qhvcr.tfm) = %{tl_version}, tex(ts1-qhvcri.tfm) = %{tl_version}
Provides:       tex(ts1-qhvr.tfm) = %{tl_version}, tex(ts1-qhvri.tfm) = %{tl_version}
Provides:       tex(ts1-qplb.tfm) = %{tl_version}, tex(ts1-qplbi.tfm) = %{tl_version}
Provides:       tex(ts1-qplr.tfm) = %{tl_version}, tex(ts1-qplri.tfm) = %{tl_version}
Provides:       tex(ts1-qtmb.tfm) = %{tl_version}, tex(ts1-qtmbi.tfm) = %{tl_version}
Provides:       tex(ts1-qtmr.tfm) = %{tl_version}, tex(ts1-qtmri.tfm) = %{tl_version}
Provides:       tex(ts1-qzcmi.tfm) = %{tl_version}, tex(qagb.pfb) = %{tl_version}
Provides:       tex(qagbi.pfb) = %{tl_version}, tex(qagr.pfb) = %{tl_version}
Provides:       tex(qagri.pfb) = %{tl_version}, tex(qbkb.pfb) = %{tl_version}
Provides:       tex(qbkbi.pfb) = %{tl_version}, tex(qbkr.pfb) = %{tl_version}
Provides:       tex(qbkri.pfb) = %{tl_version}, tex(qcrb.pfb) = %{tl_version}
Provides:       tex(qcrbi.pfb) = %{tl_version}, tex(qcrr.pfb) = %{tl_version}
Provides:       tex(qcrri.pfb) = %{tl_version}, tex(qcsb.pfb) = %{tl_version}
Provides:       tex(qcsbi.pfb) = %{tl_version}, tex(qcsr.pfb) = %{tl_version}
Provides:       tex(qcsri.pfb) = %{tl_version}, tex(qhvb.pfb) = %{tl_version}
Provides:       tex(qhvbi.pfb) = %{tl_version}, tex(qhvcb.pfb) = %{tl_version}
Provides:       tex(qhvcbi.pfb) = %{tl_version}, tex(qhvcr.pfb) = %{tl_version}
Provides:       tex(qhvcri.pfb) = %{tl_version}, tex(qhvr.pfb) = %{tl_version}
Provides:       tex(qhvri.pfb) = %{tl_version}, tex(qplb.pfb) = %{tl_version}
Provides:       tex(qplbi.pfb) = %{tl_version}, tex(qplr.pfb) = %{tl_version}
Provides:       tex(qplri.pfb) = %{tl_version}, tex(qtmb.pfb) = %{tl_version}
Provides:       tex(qtmbi.pfb) = %{tl_version}, tex(qtmr.pfb) = %{tl_version}
Provides:       tex(qtmri.pfb) = %{tl_version}, tex(qzcmi.pfb) = %{tl_version}
Provides:       tex(il2qag.fd) = %{tl_version}, tex(il2qbk.fd) = %{tl_version}
Provides:       tex(il2qcr.fd) = %{tl_version}, tex(il2qcs.fd) = %{tl_version}
Provides:       tex(il2qhv.fd) = %{tl_version}, tex(il2qhvc.fd) = %{tl_version}
Provides:       tex(il2qpl.fd) = %{tl_version}, tex(il2qtm.fd) = %{tl_version}
Provides:       tex(il2qzc.fd) = %{tl_version}, tex(l7xqag.fd) = %{tl_version}
Provides:       tex(l7xqbk.fd) = %{tl_version}, tex(l7xqcr.fd) = %{tl_version}
Provides:       tex(l7xqcs.fd) = %{tl_version}, tex(l7xqhv.fd) = %{tl_version}
Provides:       tex(l7xqhvc.fd) = %{tl_version}, tex(l7xqpl.fd) = %{tl_version}
Provides:       tex(l7xqtm.fd) = %{tl_version}, tex(l7xqzc.fd) = %{tl_version}
Provides:       tex(ly1qag.fd) = %{tl_version}, tex(ly1qbk.fd) = %{tl_version}
Provides:       tex(ly1qcr.fd) = %{tl_version}, tex(ly1qcs.fd) = %{tl_version}
Provides:       tex(ly1qhv.fd) = %{tl_version}, tex(ly1qhvc.fd) = %{tl_version}
Provides:       tex(ly1qpl.fd) = %{tl_version}, tex(ly1qtm.fd) = %{tl_version}
Provides:       tex(ly1qzc.fd) = %{tl_version}, tex(ot1qag.fd) = %{tl_version}
Provides:       tex(ot1qbk.fd) = %{tl_version}, tex(ot1qcr.fd) = %{tl_version}
Provides:       tex(ot1qcs.fd) = %{tl_version}, tex(ot1qhv.fd) = %{tl_version}
Provides:       tex(ot1qhvc.fd) = %{tl_version}, tex(ot1qpl.fd) = %{tl_version}
Provides:       tex(ot1qtm.fd) = %{tl_version}, tex(ot1qzc.fd) = %{tl_version}
Provides:       tex(ot4qag.fd) = %{tl_version}, tex(ot4qbk.fd) = %{tl_version}
Provides:       tex(ot4qcr.fd) = %{tl_version}, tex(ot4qcs.fd) = %{tl_version}
Provides:       tex(ot4qhv.fd) = %{tl_version}, tex(ot4qhvc.fd) = %{tl_version}
Provides:       tex(ot4qpl.fd) = %{tl_version}, tex(ot4qtm.fd) = %{tl_version}
Provides:       tex(ot4qzc.fd) = %{tl_version}, tex(qbookman.sty) = %{tl_version}
Provides:       tex(qcourier.sty) = %{tl_version}, tex(qpalatin.sty) = %{tl_version}
Provides:       tex(qswiss.sty) = %{tl_version}, tex(qtimes.sty) = %{tl_version}
Provides:       tex(qxqag.fd) = %{tl_version}, tex(qxqbk.fd) = %{tl_version}
Provides:       tex(qxqcr.fd) = %{tl_version}, tex(qxqcs.fd) = %{tl_version}
Provides:       tex(qxqhv.fd) = %{tl_version}, tex(qxqhvc.fd) = %{tl_version}
Provides:       tex(qxqpl.fd) = %{tl_version}, tex(qxqtm.fd) = %{tl_version}
Provides:       tex(qxqzc.fd) = %{tl_version}, tex(qzapfcha.sty) = %{tl_version}
Provides:       tex(t1qag.fd) = %{tl_version}, tex(t1qbk.fd) = %{tl_version}
Provides:       tex(t1qcr.fd) = %{tl_version}, tex(t1qcs.fd) = %{tl_version}
Provides:       tex(t1qhv.fd) = %{tl_version}, tex(t1qhvc.fd) = %{tl_version}
Provides:       tex(t1qpl.fd) = %{tl_version}, tex(t1qtm.fd) = %{tl_version}
Provides:       tex(t1qzc.fd) = %{tl_version}, tex(t5qag.fd) = %{tl_version}
Provides:       tex(t5qbk.fd) = %{tl_version}, tex(t5qcr.fd) = %{tl_version}
Provides:       tex(t5qcs.fd) = %{tl_version}, tex(t5qhv.fd) = %{tl_version}
Provides:       tex(t5qhvc.fd) = %{tl_version}, tex(t5qpl.fd) = %{tl_version}
Provides:       tex(t5qtm.fd) = %{tl_version}, tex(t5qzc.fd) = %{tl_version}
Provides:       tex(tgadventor.sty) = %{tl_version}, tex(tgbonum.sty) = %{tl_version}
Provides:       tex(tgchorus.sty) = %{tl_version}, tex(tgcursor.sty) = %{tl_version}
Provides:       tex(tgheros.sty) = %{tl_version}, tex(tgpagella.sty) = %{tl_version}
Provides:       tex(tgschola.sty) = %{tl_version}, tex(tgtermes.sty) = %{tl_version}
Provides:       tex(ts1qag.fd) = %{tl_version}, tex(ts1qbk.fd) = %{tl_version}
Provides:       tex(ts1qcr.fd) = %{tl_version}, tex(ts1qcs.fd) = %{tl_version}
Provides:       tex(ts1qhv.fd) = %{tl_version}, tex(ts1qhvc.fd) = %{tl_version}
Provides:       tex(ts1qpl.fd) = %{tl_version}, tex(ts1qtm.fd) = %{tl_version}
Provides:       tex(ts1qzc.fd) = %{tl_version}

%description -n texlive-tex-gyre
The TeX-GYRE bundle consists of six font families: TeX Gyre
Adventor is based on the URW Gothic L family of fonts (which is
derived from ITC Avant Garde Gothic, designed by Herb Lubalin
and Tom Carnase). TeX Gyre Bonum is based on the URW Bookman L
family (from Bookman Old Style, designed by Alexander
Phemister). TeX Gyre Chorus is based on URW Chancery L Medium
Italic (from ITC Zapf Chancery, designed by Hermann Zapf in
1979). TeX-Gyre Cursor is based on URW Nimbus Mono L (based on
Courier, designed by Howard G. Kettler in 1955, for IBM). TeX
Gyre Heros is based on URW Nimbus Sans L (from Helvetica,
prepared by Max Miedinger, with Eduard Hoffmann in 1957). TeX
Gyre Pagella is based on URW Palladio L (from Palatino,
designed by Hermann Zapf in the 1940s). TeX Gyre Schola is
based on the URW Century Schoolbook L family (which was
designed by Morris Fuller Benton for the American Type
Founders). TeX Gyre Termes is based on the URW Nimbus Roman No9
L family of fonts (whose original, Times, was designed by
Stanley Morison together with Starling Burgess and Victor
Lardent and first offered by Monotype). The constituent
standard faces of each family have been greatly extended, and
contain nearly 1100 glyphs each (though Chorus omits Greek
support, has no small-caps family and has approximately 800
glyphs). Each family is available in Adobe Type 1 and Open Type
formats, and LaTeX support (for use with a variety of
encodings) is provided. Vietnamese characters were added by Han
The Thanh.

%package -n texlive-tex-gyre-doc
Summary:        Documentation for tex-gyre
Version:        svn48058
Provides:       tex-tex-gyre-doc
AutoReqProv:    No

%description -n texlive-tex-gyre-doc
Documentation for tex-gyre

%package -n texlive-tex-gyre-math
Provides:       tex-tex-gyre-math = %{tl_version}
License:        LPPL
Summary:        Maths fonts to match tex-gyre text fonts
Version:        svn41264

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(texgyrebonum-math.otf) = %{tl_version}
Provides:       tex(texgyrepagella-math.otf) = %{tl_version}
Provides:       tex(texgyreschola-math.otf) = %{tl_version}
Provides:       tex(texgyretermes-math.otf) = %{tl_version}

%description -n texlive-tex-gyre-math
TeX-Gyre-Math is a collection of maths fonts to match the text
fonts of the TeX-Gyre collection. The collection is available
in OpenType format, only; fonts conform to the developing
standards for OpenType maths fonts. TeX-Gyre-Math-Bonum (to
match TeX-Gyre-Bonum), TeX-Gyre-Math-Pagella (to match TeX-Gyre-
Pagella), TeX-Gyre-Math-Schola (to match TeX-Gyre-Schola) and
TeX-Gyre-Math-Termes (to match TeX-Gyre-Termes) fonts are
provided.

%package -n texlive-tex-gyre-math-doc
Summary:        Documentation for tex-gyre-math
Version:        svn41264

Provides:       tex-tex-gyre-math-doc
AutoReqProv:    No

%description -n texlive-tex-gyre-math-doc
Documentation for tex-gyre-math

%package -n texlive-tex-ps
Provides:       tex-tex-ps = %{tl_version}
License:        Public Domain
Summary:        TeX to PostScript generic macros and add-ons
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cmyk-hax.tex) = %{tl_version}, tex(epsfx.tex) = %{tl_version}
Provides:       tex(poligraf.sty) = %{tl_version}, tex(trans.tex) = %{tl_version}

%description -n texlive-tex-ps
TeX to PostScript generic macros and add-ons: transformations
of EPS files, prepress preparation, color separation, mirror,
etc.

%package -n texlive-tex-ps-doc
Summary:        Documentation for tex-ps
Version:        svn15878.0

Provides:       tex-tex-ps-doc
AutoReqProv:    No

%description -n texlive-tex-ps-doc
Documentation for tex-ps

%package -n texlive-textglos
Provides:       tex-textglos = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset and index linguistic gloss abbreviations
Version:        svn30788.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty)
Provides:       tex(textglos.sty) = %{tl_version}

%description -n texlive-textglos
The package provides a set of macros for in-line linguistic
examples (as opposed to interlinear glossing, set apart from
the main text). It prevents hyphenated examples from breaking
across lines and consistently formats phonemic examples,
orthographic examples, and more.

%package -n texlive-textglos-doc
Summary:        Documentation for textglos
Version:        svn30788.1.0

Provides:       tex-textglos-doc
AutoReqProv:    No

%description -n texlive-textglos-doc
Documentation for textglos

%package -n texlive-texlive-zh-cn-doc
Summary:        Documentation for texlive-zh-cn
Version:        svn44333
Provides:       tex-texlive-zh-cn-doc
AutoReqProv:    No

%description -n texlive-texlive-zh-cn-doc
Documentation for texlive-zh-cn

%package -n texlive-t2
Provides:       tex-t2 = %{tl_version}
License:        LPPL
Summary:        Support for using T2 encoding
Version:        svn47870
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex(amssymb.sty), tex(enumerate.sty)
Provides:       tex(t2a-mod1.enc) = %{tl_version}, tex(t2a-mod2.enc) = %{tl_version}
Provides:       tex(t2a.enc) = %{tl_version}, tex(t2b.enc) = %{tl_version}
Provides:       tex(t2c.enc) = %{tl_version}, tex(x2.enc) = %{tl_version}
Provides:       tex(alias-cmc.tex) = %{tl_version}, tex(alias-wncy.tex) = %{tl_version}
Provides:       tex(cyralias.tex) = %{tl_version}, tex(fnstcorr.tex) = %{tl_version}
Provides:       tex(citehack.sty) = %{tl_version}, tex(mathtext.sty) = %{tl_version}
Provides:       tex(misccorr.sty) = %{tl_version}

%description -n texlive-t2
The T2 bundle provides a variety of separate support functions,
for using Cyrillic characters in LaTeX: - the mathtext package,
for using Cyrillic letters 'transparently' in formulae - the
citehack package, for using Cyrillic (or indeed any non-ascii)
characters in citation keys; - support for Cyrillic in BibTeX; -
support for Cyrillic in Makeindex; and - various items of font
support.

%post -n texlive-t2
if [ $1 -gt 0 ] ; then
sed -i 's/^\#\!\ cyramstex.*$/cyramstex pdftex language.dat -translate-file=cp227.tcx *cyramstx.ini/' %{_texdir}/texmf-dist/web2c/fmtutil.cnf
sed -i 's/^\#\!\ cyrtex.*$/cyrtex pdftex language.dat -translate-file=cp227.tcx *cyrtex.ini/' %{_texdir}/texmf-dist/web2c/fmtutil.cnf
sed -i 's/^\#\!\ cyrtexinfo.*$/cyrtexinfo pdftex language.dat -translate-file=cp227.tcx *cyrtxinf.ini/' %{_texdir}/texmf-dist/web2c/fmtutil.cnf
fi
:

%postun -n texlive-t2
if [ $1 == 0 ] ; then
sed -i 's/^cyramstex.*$/\#\!\ cyramstex pdftex language.dat -translate-file=cp227.tcx *cyramstx.ini/' %{_texdir}/texmf-dist/web2c/fmtutil.cnf > /dev/null 2>&1
sed -i 's/^cyrtex.*$/\#\!\ cyrtex pdftex language.dat -translate-file=cp227.tcx *cyrtex.ini/' %{_texdir}/texmf-dist/web2c/fmtutil.cnf > /dev/null 2>&1
sed -i 's/^cyrtexinfo.*$/\#\!\ cyrtexinfo pdftex language.dat -translate-file=cp227.tcx *cyrtxinf.ini/' %{_texdir}/texmf-dist/web2c/fmtutil.cnf > /dev/null 2>&1
fi
:

%package -n texlive-t2-doc
Summary:        Documentation for t2
Version:        svn47870
Provides:       tex-t2-doc
AutoReqProv:    No

%description -n texlive-t2-doc
Documentation for t2

%package -n texlive-texlive-ru-doc
Summary:        Documentation for texlive-ru
Version:        svn44444
Provides:       tex-texlive-ru-doc
AutoReqProv:    No

%description -n texlive-texlive-ru-doc
Documentation for texlive-ru

%package -n texlive-texlive-sr-doc
Summary:        Documentation for texlive-sr
Version:        svn44341
Provides:       tex-texlive-sr-doc
AutoReqProv:    No

%description -n texlive-texlive-sr-doc
Documentation for texlive-sr

%package -n texlive-texlive-cz-doc
Summary:        Documentation for texlive-cz
Version:        svn44347
Provides:       tex-texlive-cz-doc
AutoReqProv:    No

%description -n texlive-texlive-cz-doc
Documentation for texlive-cz

%package -n texlive-tabulars-e-doc
Summary:        Documentation for tabulars-e
Version:        svn21191.1.0

Provides:       tex-tabulars-e-doc
AutoReqProv:    No

%description -n texlive-tabulars-e-doc
Documentation for tabulars-e

%package -n texlive-tamethebeast-doc
Summary:        Documentation for tamethebeast
Version:        svn15878.1.4

Provides:       tex-tamethebeast-doc
AutoReqProv:    No

%description -n texlive-tamethebeast-doc
Documentation for tamethebeast

%package -n texlive-tds-doc
Summary:        Documentation for tds
Version:        svn15878.1.1

Provides:       tex-tds-doc
AutoReqProv:    No

%description -n texlive-tds-doc
Documentation for tds

%package -n texlive-teubner
Provides:       tex-teubner = %{tl_version}
License:        LPPL 1.3
Summary:        Philological typesetting of classical Greek
Version:        svn40197

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(iftex.sty), tex(type1ec.sty), tex(graphicx.sty), tex(ifthen.sty)
Requires:       tex(exscale.sty), tex(textalpha.sty), tex(trace.sty)
Provides:       tex(teubner.sty) = %{tl_version}, tex(teubnertx.sty) = %{tl_version}

%description -n texlive-teubner
An extension to babel greek option for typesetting classical
Greek with a philological approach. The package works with the
author's greek fonts using the 'Lispiakos' font shape derived
from that of the fonts used in printers' shops in Lispia. The
package name honours the publisher B.G. Teubner
Verlaggesellschaft whose Greek text publications are of high
quality.

%package -n texlive-teubner-doc
Summary:        Documentation for teubner
Version:        svn40197

Provides:       tex-teubner-doc
AutoReqProv:    No

%description -n texlive-teubner-doc
Documentation for teubner

%package -n texlive-texlive-it-doc
Summary:        Documentation for texlive-it
Version:        svn44357
Provides:       tex-texlive-it-doc
AutoReqProv:    No

%description -n texlive-texlive-it-doc
Documentation for texlive-it

%package -n texlive-tex-font-errors-cheatsheet-doc
Summary:        Documentation for tex-font-errors-cheatsheet
Version:        svn18314.0.1

Provides:       tex-tex-font-errors-cheatsheet-doc
AutoReqProv:    No

%description -n texlive-tex-font-errors-cheatsheet-doc
Documentation for tex-font-errors-cheatsheet

%package -n texlive-tex-overview-doc
Summary:        Documentation for tex-overview
Version:        svn41403

Provides:       tex-tex-overview-doc
AutoReqProv:    No

%description -n texlive-tex-overview-doc
Documentation for tex-overview

%package -n texlive-tex-refs-doc
Summary:        Documentation for tex-refs
Version:        svn44131
Provides:       tex-tex-refs-doc
AutoReqProv:    No

%description -n texlive-tex-refs-doc
Documentation for tex-refs

%package -n texlive-texbytopic-doc
Summary:        Documentation for texbytopic
Version:        svn15878.0

Provides:       tex-texbytopic-doc
AutoReqProv:    No

%description -n texlive-texbytopic-doc
Documentation for texbytopic

%package -n texlive-titlepages-doc
Summary:        Documentation for titlepages
Version:        svn19457.0

Provides:       tex-titlepages-doc
AutoReqProv:    No

%description -n texlive-titlepages-doc
Documentation for titlepages

%package -n texlive-tlc2-doc
Summary:        Documentation for tlc2
Version:        svn26096.0

Provides:       tex-tlc2-doc
AutoReqProv:    No

%description -n texlive-tlc2-doc
Documentation for tlc2

%package -n texlive-tabvar
Provides:       tex-tabvar = %{tl_version}
License:        LPPL 1.3
Summary:        Typesetting tables showing variations of functions
Version:        svn28908.1.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(array.sty), tex(colortbl.sty), tex(varwidth.sty), tex(ifthen.sty)
Requires:       tex(graphicx.sty), tex(ifpdf.sty)
Provides:       tex(tabvar.map) = %{tl_version}, tex(tabvar.tfm) = %{tl_version}
Provides:       tex(tabvar.pfb) = %{tl_version}, tex(tabvar.cfg) = %{tl_version}
Provides:       tex(tabvar.sty) = %{tl_version}

%description -n texlive-tabvar
This LaTeX package is meant to ease the typesetting of tables
showing variations of functions as they are used in France.

%package -n texlive-tabvar-doc
Summary:        Documentation for tabvar
Version:        svn28908.1.7

Provides:       tex-tabvar-doc
AutoReqProv:    No

%description -n texlive-tabvar-doc
Documentation for tabvar

%package -n texlive-tap
Provides:       tex-tap = %{tl_version}
License:        Public Domain
Summary:        TeX macros for typesetting complex tables
Version:        svn31731.0.77

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tap.tex) = %{tl_version}

%description -n texlive-tap
The package offers a simple notation for pretty complex tables
(to Michael J. Ferguson's credit). With PostScript, the package
allows shaded/coloured tables, diagonal rules, etc. The package
is supposed to work with both Plain and LaTeX. An AWK converter
from ASCII semigraphic tables to TAP notation is included.

%package -n texlive-tap-doc
Summary:        Documentation for tap
Version:        svn31731.0.77

Provides:       tex-tap-doc
AutoReqProv:    No

%description -n texlive-tap-doc
Documentation for tap

%package -n texlive-texdraw
Provides:       tex-texdraw = %{tl_version}
License:        CC-BY
Summary:        Graphical macros, using embedded PostScript
Version:        svn31894.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty)
Provides:       tex(blockdiagram.tex) = %{tl_version}, tex(texdraw.sty) = %{tl_version}
Provides:       tex(texdraw.tex) = %{tl_version}, tex(txdexamp.tex) = %{tl_version}
Provides:       tex(txdps.tex) = %{tl_version}, tex(txdtools.tex) = %{tl_version}

%description -n texlive-texdraw
TeXdraw is a set of macro definitions for TeX, which allow the
user to produce PostScript drawings from within TeX and LaTeX.
TeXdraw has been designed to be extensible. Drawing 'segments'
are relocatable, self-contained units. Using a combination of
the TeX's grouping mechanism and the gsave/grestore mechanism
in PostScript, drawing segments allow for local changes to the
scaling and line parameters. Using TeX's macro definition
capability, new drawing commands can be constructed from
drawing segments.

%package -n texlive-texdraw-doc
Summary:        Documentation for texdraw
Version:        svn31894.0

Provides:       tex-texdraw-doc
AutoReqProv:    No

%description -n texlive-texdraw-doc
Documentation for texdraw

%package -n texlive-tex-virtual-academy-pl-doc
Summary:        Documentation for tex-virtual-academy-pl
Version:        svn34177.0

Provides:       tex-tex-virtual-academy-pl-doc
AutoReqProv:    No

%description -n texlive-tex-virtual-academy-pl-doc
Documentation for tex-virtual-academy-pl

%package -n texlive-texlive-pl-doc
Summary:        Documentation for texlive-pl
Version:        svn44343
Provides:       tex-texlive-pl-doc
AutoReqProv:    No

%description -n texlive-texlive-pl-doc
Documentation for texlive-pl

%package -n texlive-tdsfrmath
Provides:       tex-tdsfrmath = %{tl_version}
License:        LPPL
Summary:        Macros for French teachers of mathematics
Version:        svn15878.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(xkeyval.sty), tex(xstring.sty), tex(amsmath.sty)
Requires:       tex(amssymb.sty), tex(xspace.sty), tex(xargs.sty), tex(suffix.sty)
Requires:       tex(stmaryrd.sty)
Provides:       tex(tdsfrmath.sty) = %{tl_version}

%description -n texlive-tdsfrmath
A collection of macros for French maths teachers in colleges
and lycees (and perhaps elsewhere). It is hoped that the
package will facilitate the everyday use of LaTeX by
mathematics teachers.

%package -n texlive-tdsfrmath-doc
Summary:        Documentation for tdsfrmath
Version:        svn15878.1.3

Provides:       tex-tdsfrmath-doc
AutoReqProv:    No

%description -n texlive-tdsfrmath-doc
Documentation for tdsfrmath

%package -n texlive-texlive-fr-doc
Summary:        Documentation for texlive-fr
Version:        svn44342
Provides:       tex-texlive-fr-doc
AutoReqProv:    No

%description -n texlive-texlive-fr-doc
Documentation for texlive-fr

%package -n texlive-tabto-generic
Provides:       tex-tabto-generic = %{tl_version}
License:        Public Domain
Summary:        "Tab" to a measured position in the line
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tabto.tex) = %{tl_version}

%description -n texlive-tabto-generic
\tabto{<length>} moves the typesetting position to <length>
from the left margin of the paragraph. If the typesetting
position is already further along, \tabto starts a new line.

%package -n texlive-tablor
Provides:       tex-tablor = %{tl_version}
License:        LPPL
Summary:        Create tables of signs and of variations
Version:        svn31855.4.07_g

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(filecontents.sty), tex(ifthen.sty), tex(fancyvrb.sty), tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Provides:       tex(tablor-xetex.sty) = %{tl_version}, tex(tablor.cfg) = %{tl_version}
Provides:       tex(tablor.sty) = %{tl_version}

%description -n texlive-tablor
The package allows the user to use the computer algebra system
XCAS to generate tables of signs and of variations (the actual
plotting of the tables uses the MetaPost macro package
tableauVariations). Tables with forbidden regions may be
developed using the package. A configuration file permits some
configuration of the language to be used in the diagrams. The
tablor package requires that shell escape be enabled.

%package -n texlive-tablor-doc
Summary:        Documentation for tablor
Version:        svn31855.4.07_g

Provides:       tex-tablor-doc
AutoReqProv:    No

%description -n texlive-tablor-doc
Documentation for tablor

%package -n texlive-tensor
Provides:       tex-tensor = %{tl_version}
License:        LPPL
Summary:        Typeset tensors
Version:        svn15878.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tensor.sty) = %{tl_version}

%description -n texlive-tensor
A package which allows the user to set tensor-style super- and
subscripts with offsets between successive indices. It supports
the typesetting of tensors with mixed upper and lower indices
with spacing, also typset preposed indices. This is a complete
revision and extension of the original 'tensor' package by Mike
Piff.

%package -n texlive-tensor-doc
Summary:        Documentation for tensor
Version:        svn15878.2.1

Provides:       tex-tensor-doc
AutoReqProv:    No

%description -n texlive-tensor-doc
Documentation for tensor

%package -n texlive-tex-ewd
Provides:       tex-tex-ewd = %{tl_version}
License:        BSD
Summary:        Macros to typeset calculational proofs and programs in Dijkstra's style
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dotnot.tex) = %{tl_version}

%description -n texlive-tex-ewd
Edsger W. Dijkstra and others suggest a unique style to present
mathematical proofs and to construct programs. This package
provides macros that support calculational proofs and
Dijkstra's "guarded command language".

%package -n texlive-tex-ewd-doc
Summary:        Documentation for tex-ewd
Version:        svn15878.0

Provides:       tex-tex-ewd-doc
AutoReqProv:    No

%description -n texlive-tex-ewd-doc
Documentation for tex-ewd

%package -n texlive-textpath
Provides:       tex-textpath = %{tl_version}
License:        LPPL
Summary:        Setting text along a path with MetaPost
Version:        svn15878.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(soul.sty)
Provides:       tex(textpathmp.sty) = %{tl_version}

%description -n texlive-textpath
This MetaPost package provides macros to typeset text along a
free path with the help of LaTeX, thereby preserving kerning
and allowing for 8-bit input (accented characters).

%package -n texlive-textpath-doc
Summary:        Documentation for textpath
Version:        svn15878.1.6

Provides:       tex-textpath-doc
AutoReqProv:    No

%description -n texlive-textpath-doc
Documentation for textpath

%if %{with_texinfo}
%package -n texlive-texinfo
Provides:       tex-texinfo = %{tl_version}
License:        GPL+
Summary:        Texinfo documentation system
Version:        svn45305
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(texinfo.tex) = %{tl_version}, tex(txi-cs.tex) = %{tl_version}
Provides:       tex(txi-de.tex) = %{tl_version}, tex(txi-en.tex) = %{tl_version}
Provides:       tex(txi-es.tex) = %{tl_version}, tex(txi-fr.tex) = %{tl_version}
Provides:       tex(txi-it.tex) = %{tl_version}, tex(txi-nb.tex) = %{tl_version}
Provides:       tex(txi-nl.tex) = %{tl_version}, tex(txi-nn.tex) = %{tl_version}
Provides:       tex(txi-pl.tex) = %{tl_version}, tex(txi-pt.tex) = %{tl_version}
Provides:       tex(txi-ru.tex) = %{tl_version}, tex(txi-sr.tex) = %{tl_version}
Provides:       tex(txi-tr.tex) = %{tl_version}, tex(txi-uk.tex) = %{tl_version}

%description -n texlive-texinfo
Texinfo is the preferred format for documentation in the GNU
project; the format may be used to produce online or printed
output from a single source. The Texinfo macros may be used to
produce printable output using TeX; other programs in the
distribution offer online interactive use (with hypertext
linkages in some cases). Note that a developers' snapshot of
the latest release of the Texinfo macros may be found in the
Texinfo 'latest' package.
%endif

%package -n texlive-templates-fenn-doc
Summary:        Documentation for templates-fenn
Version:        svn15878.0

Provides:       tex-templates-fenn-doc
AutoReqProv:    No

%description -n texlive-templates-fenn-doc
Documentation for templates-fenn

%package -n texlive-templates-sommer-doc
Summary:        Documentation for templates-sommer
Version:        svn15878.0

Provides:       tex-templates-sommer-doc
AutoReqProv:    No

%description -n texlive-templates-sommer-doc
Documentation for templates-sommer

%package -n texlive-texlive-de-doc
Summary:        Documentation for texlive-de
Version:        svn44366
Provides:       tex-texlive-de-doc
AutoReqProv:    No

%description -n texlive-texlive-de-doc
Documentation for texlive-de

%package -n texlive-termmenu
Provides:       tex-termmenu = %{tl_version}
License:        LPPL 1.3
Summary:        The package provides support for terminal-based menus using expl3
Version:        svn37700.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(termmenu.tex) = %{tl_version}

%description -n texlive-termmenu
When writing programs, it's often required to present the user
with a list of options/actions. The user is then expected to
select one of these options for the program to process.
termmenu provides this mechanism for TeX. It requires only
expl3 support, thus the l3kernel and l3packages are both
required.

%package -n texlive-termmenu-doc
Summary:        Documentation for termmenu
Version:        svn37700.0

Provides:       tex-termmenu-doc
AutoReqProv:    No

%description -n texlive-termmenu-doc
Documentation for termmenu

%package -n texlive-texapi
Provides:       tex-texapi = %{tl_version}
License:        LPPL
Summary:        Macros to write format-independent packages
Version:        svn24237.1.04

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(texapi.tex) = %{tl_version}

%description -n texlive-texapi
Texapi provides utility macros to write format-independent (and
-aware) packages. It is similar in spirit to the etoolbox,
except that it isn't tied to LaTeX. Tools include: engine and
format detection, expansion control, command definition and
manipulation, various testing macros, string operations, and
highly customizable while and for loops. The package requires e-
TeX (and, should you want to compile its documentation, the
pitex package is also needed).

%package -n texlive-texapi-doc
Summary:        Documentation for texapi
Version:        svn24237.1.04

Provides:       tex-texapi-doc
AutoReqProv:    No

%description -n texlive-texapi-doc
Documentation for texapi

%package -n texlive-textcase
Provides:       tex-textcase = %{tl_version}
License:        LPPL
Summary:        Case conversion ignoring mathematics, etc
Version:        svn15878.0
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(textcase.sty) = %{tl_version}

%description -n texlive-textcase
The textcase package offers commands \MakeTextUppercase and
\MakeTextLowercase are similar to the standard \MakeUppercase
and \MakeLowercase, but they do not change the case of any
sections of mathematics, or the arguments of \cite, \label and
\ref commands within the argument. A further command
\NoCaseChange does nothing but suppress case change within its
argument, so to force uppercase of a section including an
environment, one might say:
\MakeTextUppercase{...\NoCaseChange{\begin{foo}}
...\NoCaseChange{\end{foo}}...}

%package -n texlive-textcase-doc
Summary:        Documentation for textcase
Version:        svn15878.0

Provides:       tex-textcase-doc
AutoReqProv:    No

%description -n texlive-textcase-doc
Documentation for textcase

%package -n texlive-tabfigures
Provides:       tex-tabfigures = %{tl_version}
License:        LPPL 1.3
Summary:        Maintain vertical alignment of figures
Version:        svn25202.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(xcolor.sty)
Provides:       tex(tabfigures.sty) = %{tl_version}

%description -n texlive-tabfigures
Knuth designed his original fonts with tabular figures (figures
whose width is uniform); this makes some layout problems rather
simple. In more recent times, fonts (such as Minion Pro), which
offer proportionally spaced figures, are increasingly being
used. The package provides mechanisms whereby such proportional
figures may still be aligned in tabular style (for example, in
the table of contents).

%package -n texlive-tabfigures-doc
Summary:        Documentation for tabfigures
Version:        svn25202.1.1

Provides:       tex-tabfigures-doc
AutoReqProv:    No

%description -n texlive-tabfigures-doc
Documentation for tabfigures

%package -n texlive-table-fct
Summary:        Draw a variations table of functions and a convexity table of its graph.
Version:        svn41849
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(table-fct.sty) = %{tl_version}

%description -n texlive-table-fct
Draw a variations table of functions and a convexity table of
its graph This version offers two environnements, to draw
variations table of a function and a convexity table of its
graph.

%package -n texlive-termcal-de
Summary:        German localization for termcal
Version:        svn47111
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(termcal-de.sty) = %{tl_version}

%description -n texlive-termcal-de
This package provides a German localization to the termcal
package written by Bill Mitchell, which is intended to print a
term calendar for use in planning a class.

%package -n texlive-testidx
Summary:        Dummy text for testing index styles and indexing applications
Version:        svn45021
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(testidx-glossaries.sty) = %{tl_version}
Provides:       tex(testidx.sty) = %{tl_version}

%description -n texlive-testidx
This is a LaTeX package that provides a command to produce
dummy text interspersed with \index commands to test an index
style or indexing application. The dummy text is mostly in
English, but includes extended Latin characters provided either
through LaTeX accent commands or directly with UTF-8
characters, depending on the setup, to allow for testing
extended Latin alphabets. The supplementary package
testidx-glossaries.sty uses the indexing interface provided by
the glossaries package.

%package -n texlive-texproposal-doc
Summary:        Materials for proposals to offer TeX courses
Version:        svn43151
License:        CC-BY and MIT

%description -n texlive-texproposal-doc
Materials for the "Proposal for Offering TeX Courses and Relevant 
Resources in Chongqing University"


%package -n texlive-tableaux
Provides:       tex-tableaux = %{tl_version}
License:        LPPL
Summary:        Construct tables of signs and variations
Version:        svn42413
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(inputenc.sty), tex(fontenc.sty), tex(babel.sty), tex(amsmath.sty)
Requires:       tex(amssymb.sty), tex(array.sty), tex(hhline.sty), tex(graphicx.sty)
Requires:       tex(pstcol.sty), tex(pst-fill.sty), tex(pst-plot.sty), tex(pst-tree.sty)
Provides:       tex(minimum.sty) = %{tl_version}, tex(tableau.sty) = %{tl_version}

%description -n texlive-tableaux
The package uses PStricks; the user may define the width of the
table, the number of lines and the height of each line.
Placement of labels within the boxes may be absolute, or as a
percentage of the width; various other controls are available.

%package -n texlive-tableaux-doc
Summary:        Documentation for tableaux
Version:        svn42413
Provides:       tex-tableaux-doc
AutoReqProv:    No

%description -n texlive-tableaux-doc
Documentation for tableaux

%package -n texlive-tablefootnote
Provides:       tex-tablefootnote = %{tl_version}
License:        LPPL 1.3
Summary:        Permit footnotes in tables
Version:        svn32804.1.1c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ltxcmds.sty), tex(letltxmacro.sty), tex(xifthen.sty), tex(etoolbox.sty)
Provides:       tex(tablefootnote.sty) = %{tl_version}

%description -n texlive-tablefootnote
The package provides the command \tablefootnote to be used in a
table or sidewaystable environment, where \footnote will not
work (and when using \footnotemark and \footnotetext, and
adjusting the counter as necessary, is too much work).

%package -n texlive-tablefootnote-doc
Summary:        Documentation for tablefootnote
Version:        svn32804.1.1c

Provides:       tex-tablefootnote-doc
AutoReqProv:    No

%description -n texlive-tablefootnote-doc
Documentation for tablefootnote

%package -n texlive-tableof
Provides:       tex-tableof = %{tl_version}
License:        LPPL 1.3
Summary:        Tagging tables of contents
Version:        svn36489.1.4a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tableof.sty) = %{tl_version}

%description -n texlive-tableof
The package provides the commands to flag chapters or sections
(or anything else destined to become a TOC line). The command
\nexttocwithtags{req1,req2,...}{excl1,excl2,...} specifies
which tags are to be required and which ones are to be excluded
by the next \tableofcontents (or equivalent) command. In a
document that uses a class where \tableofcontents may only be
used once, the command
\tableoftaggedcontents{req1,req2,...}{excl1,excl2,...} may be
used to provide several tables.

%package -n texlive-tableof-doc
Summary:        Documentation for tableof
Version:        svn36489.1.4a

Provides:       tex-tableof-doc
AutoReqProv:    No

%description -n texlive-tableof-doc
Documentation for tableof

%package -n texlive-tablestyles
Provides:       tex-tablestyles = %{tl_version}
License:        LPPL
Summary:        tablestyles package
Version:        svn34495.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty), tex(etoolbox.sty), tex(xcolor.sty), tex(ragged2e.sty)
Provides:       tex(tablestyles.sty) = %{tl_version}

%description -n texlive-tablestyles
tablestyles package

%package -n texlive-tablestyles-doc
Summary:        Documentation for tablestyles
Version:        svn34495.0

Provides:       tex-tablestyles-doc
AutoReqProv:    No

%description -n texlive-tablestyles-doc
Documentation for tablestyles

%package -n texlive-tablists
Provides:       tex-tablists = %{tl_version}
License:        LPPL
Summary:        Tabulated lists of short items
Version:        svn15878.0.0e

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(makecell.sty)
Provides:       tex(tablists.sty) = %{tl_version}

%description -n texlive-tablists
This package offers environments and commands for one-level and
two-level lists of short items (e.g., exercises in textbooks).
The environments support optional arguments of item numbering
similar to the enumerate or paralist packages.

%package -n texlive-tablists-doc
Summary:        Documentation for tablists
Version:        svn15878.0.0e

Provides:       tex-tablists-doc
AutoReqProv:    No

%description -n texlive-tablists-doc
Documentation for tablists

%package -n texlive-tabls
Provides:       tex-tabls = %{tl_version}
License:        Dotseqn
Summary:        Better vertical spacing in tables and arrays
Version:        svn17255.3.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tabls.sty) = %{tl_version}

%description -n texlive-tabls
Modifies LaTeX's array and tabular environments to keep text
from touching other text or hlines above or below. Several new
parameters are defined and some standard macros are re-defined.
The package slows down compilation of tables, since each entry
is boxed twice.

%package -n texlive-tabls-doc
Summary:        Documentation for tabls
Version:        svn17255.3.5

Provides:       tex-tabls-doc
AutoReqProv:    No

%description -n texlive-tabls-doc
Documentation for tabls

%package -n texlive-tabstackengine
Provides:       tex-tabstackengine = %{tl_version}
License:        LPPL
Summary:        "Tabbing" front-end to stackengine
Version:        svn46848
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(stackengine.sty), tex(calc.sty)
Provides:       tex(tabstackengine.sty) = %{tl_version}

%description -n texlive-tabstackengine
The package provides a front end to the stackengine package, to
allow tabbed stacking. In most cases, an existing stackengine
command may be prepended with the word "tabbed", "align" or
"tabular" to create a new tabbed version of a stacking macro.
In addition, hooks in the package's parser, that tabbed strings
of data may be parsed, extracted and reconstituted (not
requiring use of any stacking constructions).

%package -n texlive-tabstackengine-doc
Summary:        Documentation for tabstackengine
Version:        svn46848
Provides:       tex-tabstackengine-doc
AutoReqProv:    No

%description -n texlive-tabstackengine-doc
Documentation for tabstackengine

%package -n texlive-tabto-ltx
Provides:       tex-tabto-ltx = %{tl_version}
License:        LPPL
Summary:        "Tab" to a measured position in the line
Version:        svn30710.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tabto.sty) = %{tl_version}

%description -n texlive-tabto-ltx
\tabto{<length>} moves the typesetting position to <length>
from the left margin of the paragraph. If the typesetting
position is already further along, \tabto starts a new line;
the command \tabto* will move position backwards if necessary,
so that previous text may be overwritten. The command
\TabPositions may be used to define a set of tabbing positions,
after which the command \tab advances typesetting position to
the next defined 'tab stop'.

%package -n texlive-tabto-ltx-doc
Summary:        Documentation for tabto-ltx
Version:        svn30710.1.3

Provides:       tex-tabto-ltx-doc
AutoReqProv:    No

%description -n texlive-tabto-ltx-doc
Documentation for tabto-ltx

%package -n texlive-tabu
Provides:       tex-tabu = %{tl_version}
License:        LPPL 1.3
Summary:        Flexible LaTeX tabulars
Version:        svn21534.2.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty), tex(varwidth.sty), tex(delarray.sty), tex(linegoal.sty)
Provides:       tex(tabu.sty) = %{tl_version}

%description -n texlive-tabu
The package provides an environment, tabu, which will make any
sort of tabular (that doesn't need to split across pages), and
an environment longtabu which provides the facilities of tabu
in a modified longtable environment. (Note that this latter
offers an enhancement of ltxtable.) The package requires the
array package, and needs e-TeX to run (since array.sty is
present in every conforming distribution of LaTeX, and since
every publicly available LaTeX format is built using e-TeX, the
requirements are provided by default on any reasonable system).
The package also requires xcolor for coloured rules in tables,
and colortbl for coloured cells. The longtabu environment
further requires that longtable be loaded. The package itself
does not load any of these packages for the user. The tabu
environment may be used in place of tabular, tabular* and
tabularx environments, as well as the array environment in
maths mode. It overloads tabularx's X-column specification,
allowing a width specification, alignment (l, r, c and j) and
column type indication (p, m and b). \begin{tabu} to <dimen>
specifies a target width, and \begin{tabu} spread <dimen>
enlarges the environment's "natural" width.

%package -n texlive-tabu-doc
Summary:        Documentation for tabu
Version:        svn21534.2.8

Provides:       tex-tabu-doc
AutoReqProv:    No

%description -n texlive-tabu-doc
Documentation for tabu

%package -n texlive-tabularborder
Provides:       tex-tabularborder = %{tl_version}
License:        LPPL 1.2
Summary:        Remove excess space at left and right of tabular
Version:        svn17885.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(booktabs.sty), tex(array.sty)
Provides:       tex(tabularborder.sty) = %{tl_version}

%description -n texlive-tabularborder
The tabular environment is changed so that the outer
\tabcolseps are compensated and a \hline has the same length as
the text. No @{} is needed.

%package -n texlive-tabularborder-doc
Summary:        Documentation for tabularborder
Version:        svn17885.1.0a

Provides:       tex-tabularborder-doc
AutoReqProv:    No

%description -n texlive-tabularborder-doc
Documentation for tabularborder

%package -n texlive-tabularcalc
Provides:       tex-tabularcalc = %{tl_version}
License:        LPPL
Summary:        Calculate formulas in a tabular environment
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fp.sty), tex(xstring.sty), tex(numprint.sty)
Provides:       tex(tabularcalc.sty) = %{tl_version}

%description -n texlive-tabularcalc
Given a list of numbers and one (or more) formulas, the package
offers an easy syntax to build a table of values, i.e., a
tabular in which the first row contains the list of numbers,
and the other rows contain the calculated values of the
formulas for each number of the list. The table may be built
either horizontally or vertically and is fully customizable.

%package -n texlive-tabularcalc-doc
Summary:        Documentation for tabularcalc
Version:        svn15878.0.2

Provides:       tex-tabularcalc-doc
AutoReqProv:    No

%description -n texlive-tabularcalc-doc
Documentation for tabularcalc

%package -n texlive-tabularew
Provides:       tex-tabularew = %{tl_version}
License:        LPPL
Summary:        A variation on the tabular environment
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty)
Provides:       tex(tabularew.sty) = %{tl_version}

%description -n texlive-tabularew
The package offers a modification of the tabular environment,
which deals with the problem of column heads that are
significantly wider than the body of the column.

%package -n texlive-tabularew-doc
Summary:        Documentation for tabularew
Version:        svn15878.0.1

Provides:       tex-tabularew-doc
AutoReqProv:    No

%description -n texlive-tabularew-doc
Documentation for tabularew

%package -n texlive-tabulary
Provides:       tex-tabulary = %{tl_version}
License:        LPPL
Summary:        Tabular with variable width columns balanced
Version:        svn34368.0.10

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty)
Provides:       tex(tabulary.sty) = %{tl_version}

%description -n texlive-tabulary
The package defines a tabular*-like environment, tabulary,
taking a 'total width' argument as well as the column
specifications. The environment uses column types L, C, R and J
for variable width columns (\raggedright', \centering,
\raggedleft, and normally justified). In contrast to tabularx's
X columns, the width of each column is weighted according to
the natural width of the widest cell in the column.

%package -n texlive-tabulary-doc
Summary:        Documentation for tabulary
Version:        svn34368.0.10

Provides:       tex-tabulary-doc
AutoReqProv:    No

%description -n texlive-tabulary-doc
Documentation for tabulary

%package -n texlive-tagging
Provides:       tex-tagging = %{tl_version}
License:        LPPL 1.3
Summary:        Document configuration with tags
Version:        svn23761.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(verbatim.sty)
Provides:       tex(tagging.sty) = %{tl_version}

%description -n texlive-tagging
The package allows the user to generate multiple documents from
a single source, by marking pieces of the document with tags
and specifying which marked pieces to include or exclude.

%package -n texlive-tagging-doc
Summary:        Documentation for tagging
Version:        svn23761.0

Provides:       tex-tagging-doc
AutoReqProv:    No

%description -n texlive-tagging-doc
Documentation for tagging

%package -n texlive-tagpair
Provides:       tex-tagpair = %{tl_version}
License:        LPPL 1.3
Summary:        Word-by-word glosses, translations, and bibliographic attributions
Version:        svn42138
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(varwidth.sty)
Provides:       tex(tagpair.sty) = %{tl_version}

%description -n texlive-tagpair
This package provides environments and commands for pairing
lines, bottom lines, and tagged lines, intended to be used in
particular for word-by-word glosses, translations, and
bibliographic attributions, respectively. This LaTeX package is
inspired by Marcel R. van der Goot's classic Plain TeX macros
in gloss.tex.

%package -n texlive-tagpair-doc
Summary:        Documentation for tagpair
Version:        svn42138
Provides:       tex-tagpair-doc
AutoReqProv:    No

%description -n texlive-tagpair-doc
Documentation for tagpair

%package -n texlive-talk
Provides:       tex-talk = %{tl_version}
License:        LPPL
Summary:        A LaTeX class for presentations
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(multido.sty), tex(amsmath.sty), tex(graphicx.sty), tex(pgf.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(sidebars.sty) = %{tl_version}, tex(talk.cls) = %{tl_version}

%description -n texlive-talk
The talk document class allows you to create slides for screen
presentations or printing on transparencies. It also allows you
to print personal notes for your talk. You can create overlays
and display structure information (current section /
subsection, table of contents) on your slides. The main feature
that distinguishes talk from other presentation classes like
beamer or prosper is that it allows the user to define an
arbitrary number of slide styles and switch between these
styles from slide to slide. This way the slide layout can be
adapted to the slide content. For example, the title or
contents page of a talk can be given a slightly different
layout than the other slides. The talk class makes no
restrictions on the slide design whatsoever. The entire look
and feel of the presentation can be defined by the user. The
style definitions should be put in a separate sty file.
Currently the package comes with only one set of pre-defined
slide styles (greybars.sty). Contributions from people who are
artistically more gifted than the author are more than welcome!

%package -n texlive-talk-doc
Summary:        Documentation for talk
Version:        svn42428
Provides:       tex-talk-doc
AutoReqProv:    No

%description -n texlive-talk-doc
Documentation for talk

%package -n texlive-tamefloats
Provides:       tex-tamefloats = %{tl_version}
License:        LPPL 1.3
Summary:        Experimentally use \holdinginserts with LaTeX floats
Version:        svn27345.v0.42

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tameflts.sty) = %{tl_version}

%description -n texlive-tamefloats
LaTeX's figures, tables, and \marginpars are dangerous for
footnotes (and probably also \enlargethispage). Here is a
proposal (a 'patch' package) to help, by using \holdinginserts
in a simple way. It replaces the original problem with a new
one -- it is an experiment to find out whether the new problem
is less bad (or it is just a contribution to the discussion,
maybe just a summary of previous work). The files provide
further information.

%package -n texlive-tamefloats-doc
Summary:        Documentation for tamefloats
Version:        svn27345.v0.42

Provides:       tex-tamefloats-doc
AutoReqProv:    No

%description -n texlive-tamefloats-doc
Documentation for tamefloats

%package -n texlive-tasks
Provides:       tex-tasks = %{tl_version}
License:        LPPL 1.3
Summary:        Horizontally columned lists
Version:        svn41851
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty), tex(epic.sty)
Requires:       tex(cntformats.sty), tex(xtemplate.sty), tex(environ.sty)
Provides:       tex(tasks.cfg) = %{tl_version}, tex(tasks.sty) = %{tl_version}

%description -n texlive-tasks
The reason for the creation of the tasks environment was an
unwritten agreement in German maths textbooks (exspecially
(junior) high school textbooks) to organize exercises in
columns counting horizontally rather than vertically. This is
what the tasks package helps to achieve.

%package -n texlive-tasks-doc
Summary:        Documentation for tasks
Version:        svn41851
Provides:       tex-tasks-doc
AutoReqProv:    No

%description -n texlive-tasks-doc
Documentation for tasks

%package -n texlive-tcldoc
Provides:       tex-tcldoc = %{tl_version}
License:        LPPL
Summary:        Doc/docstrip for tcl
Version:        svn22018.2.40

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(rtkinenc.sty), tex(xdoc2.sty), tex(docidx2e.sty)
Provides:       tex(tcldoc.cls) = %{tl_version}, tex(tcldoc.sty) = %{tl_version}
Provides:       tex(tclldoc.cls) = %{tl_version}, tex(tclldoc.sty) = %{tl_version}

%description -n texlive-tcldoc
The tclldoc package and class simplify the application of the
doc/docstrip style of literate programming with Dr. John
Ousterhout's Tool Command Language (Tcl, pronounced "tickle",
a.k.a. The Cool Language). The tclldoc package is a bit like
the doc package is for LaTeX, whereas the tclldoc class more
parallels the ltxdoc class.

%package -n texlive-tcldoc-doc
Summary:        Documentation for tcldoc
Version:        svn22018.2.40

Provides:       tex-tcldoc-doc
AutoReqProv:    No

%description -n texlive-tcldoc-doc
Documentation for tcldoc

%package -n texlive-tcolorbox
Provides:       tex-tcolorbox = %{tl_version}
License:        LPPL 1.3
Summary:        Coloured boxes, for LaTeX examples and theorems, etc
Version:        svn48282
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pgf.sty), tex(verbatim.sty), tex(environ.sty), tex(etoolbox.sty)
Provides:       tex(tcbbreakable.code.tex) = %{tl_version}
Provides:       tex(tcbdocumentation.code.tex) = %{tl_version}
Provides:       tex(tcbexternal.code.tex) = %{tl_version}
Provides:       tex(tcbfitting.code.tex) = %{tl_version}
Provides:       tex(tcbhooks.code.tex) = %{tl_version}, tex(tcblistings.code.tex) = %{tl_version}
Provides:       tex(tcblistingscore.code.tex) = %{tl_version}
Provides:       tex(tcblistingsutf8.code.tex) = %{tl_version}
Provides:       tex(tcbmagazine.code.tex) = %{tl_version}
Provides:       tex(tcbminted.code.tex) = %{tl_version}, tex(tcbraster.code.tex) = %{tl_version}
Provides:       tex(tcbskins.code.tex) = %{tl_version}, tex(tcbskinsjigsaw.code.tex) = %{tl_version}
Provides:       tex(tcbtheorems.code.tex) = %{tl_version}
Provides:       tex(tcbxparse.code.tex) = %{tl_version}, tex(tcolorbox.sty) = %{tl_version}

%description -n texlive-tcolorbox
The package provides an environment for coloured and framed
text boxes with a heading line. Optionally, such a box may be
split in an upper and a lower part; thus the package may be
used for the setting of LaTeX examples where one part of the
box displays the source code and the other part shows the
output. Another common use case is the setting of theorems. The
package supports saving and reuse of source code and text
parts.

%package -n texlive-tcolorbox-doc
Summary:        Documentation for tcolorbox
Version:        svn48282
Provides:       tex-tcolorbox-doc
AutoReqProv:    No

%description -n texlive-tcolorbox-doc
Documentation for tcolorbox

%package -n texlive-tdclock
Provides:       tex-tdclock = %{tl_version}
License:        GPLv2+
Summary:        A ticking digital clock package for PDF output
Version:        svn33043.v2.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(hyperref.sty), tex(xcolor.sty), tex(xkeyval.sty)
Provides:       tex(tdclock.sty) = %{tl_version}

%description -n texlive-tdclock
A ticking digital clock package to be used in Pdf-LaTeX
documents, for example in presentations.

%package -n texlive-tdclock-doc
Summary:        Documentation for tdclock
Version:        svn33043.v2.5

Provides:       tex-tdclock-doc
AutoReqProv:    No

%description -n texlive-tdclock-doc
Documentation for tdclock

%package -n texlive-technics
Provides:       tex-technics = %{tl_version}
License:        LPPL
Summary:        A package to format technical documents
Version:        svn29349.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(technics.sty) = %{tl_version}

%description -n texlive-technics
The package provides a very simple LaTeX document template, in
the hope that this use of LaTeX will become attractive to
typical word processor users. (Presentation is as if it were a
class; users are expected to start from a template document.)

%package -n texlive-technics-doc
Summary:        Documentation for technics
Version:        svn29349.1.0

Provides:       tex-technics-doc
AutoReqProv:    No

%description -n texlive-technics-doc
Documentation for technics

%package -n texlive-ted
Provides:       tex-ted = %{tl_version}
License:        LPPL
Summary:        A (primitive) token list editor
Version:        svn15878.1.06

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ted.sty) = %{tl_version}

%description -n texlive-ted
Just like sed is a stream editor, ted is a token list editor.
Actually, it is not as powerfull as sed, but its main feature
is that it really works with tokens, not only characters. The
ted package provides two user macros: \Substitute and
\ShowTokens. The first is maybe the most useful: it performs
substitutions in token lists (even inside braces). The second
displays each token of the list (one per line) with its catcode
(in the list, not just the current one), and can be useful for
debugging or for TeX learners. Ted is designed to work well
even if strange tokens (that is, unusual {charcode, catcode}
pairs or tokens with a confusing meaning) occur in the list.

%package -n texlive-ted-doc
Summary:        Documentation for ted
Version:        svn15878.1.06

Provides:       tex-ted-doc
AutoReqProv:    No

%description -n texlive-ted-doc
Documentation for ted

%package -n texlive-templatetools
Provides:       tex-templatetools = %{tl_version}
License:        LPPL 1.3
Summary:        Commands useful in LaTeX templates
Version:        svn34495.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(etoolbox.sty), tex(ltxcmds.sty), tex(array.sty)
Requires:       tex(ifdraft.sty), tex(scrlfile.sty)
Provides:       tex(templatetools.sty) = %{tl_version}

%description -n texlive-templatetools
The package provides a collection of tools, which are helpful
for the creation of a LaTeX template if conditional paths for
code execution are required. All the commands work both in the
preamble and in the document.

%package -n texlive-templatetools-doc
Summary:        Documentation for templatetools
Version:        svn34495.0

Provides:       tex-templatetools-doc
AutoReqProv:    No

%description -n texlive-templatetools-doc
Documentation for templatetools

%package -n texlive-termcal
Provides:       tex-termcal = %{tl_version}
License:        LPPL
Summary:        Print a class calendar
Version:        svn22514.1.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(longtable.sty), tex(ifthen.sty)
Provides:       tex(termcal.sty) = %{tl_version}

%description -n texlive-termcal
This package is intended to print a term calendar for use in
planning a class. It has a flexible mechanism for specifying
which days of the week are to be included and for inserting
text either regularly on the same day each week, or on selected
days, or for a series of consecutive days. It also has a
flexible mechanism for specifing class and nonclass days. Text
may be inserted into consecutive days so that it automatically
flows around nonclass days.

%package -n texlive-termcal-doc
Summary:        Documentation for termcal
Version:        svn22514.1.8

Provides:       tex-termcal-doc
AutoReqProv:    No

%description -n texlive-termcal-doc
Documentation for termcal

%package -n texlive-termlist
Provides:       tex-termlist = %{tl_version}
License:        LPPL
Summary:        Label any kind of term with a continuous counter
Version:        svn18923.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(termlist.sty) = %{tl_version}

%description -n texlive-termlist
The termlist package provides environments to indent and label
any kind of terms with a continuous number. Candidate terms may
appear inside an equation or eqnarray environment.

%package -n texlive-termlist-doc
Summary:        Documentation for termlist
Version:        svn18923.1.1

Provides:       tex-termlist-doc
AutoReqProv:    No

%description -n texlive-termlist-doc
Documentation for termlist

%package -n texlive-testhyphens
Provides:       tex-testhyphens = %{tl_version}
License:        LPPL 1.3
Summary:        Testing hyphenation patterns
Version:        svn38928

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(testhyphens.sty) = %{tl_version}

%description -n texlive-testhyphens
The package may be used for testing hyphenation patterns or for
controlling that specific words are hyphenated as expected.
This package implements some old TUGboat code to adapt it to
LaTeX with some enhancements. It differs form \showhyphens,
because it typesets its output on the document's output file.
It also works with xelatex, where \showhyphens requires a
workaround.

%package -n texlive-testhyphens-doc
Summary:        Documentation for testhyphens
Version:        svn35162.0.6

Provides:       tex-testhyphens-doc
AutoReqProv:    No

%description -n texlive-testhyphens-doc
Documentation for testhyphens

%package -n texlive-tex-label
Provides:       tex-tex-label = %{tl_version}
License:        LPPL 1.3
Summary:        Place a classification on each page of a document
Version:        svn16372.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(fancyhdr.sty)
Provides:       tex(tex-label.sty) = %{tl_version}

%description -n texlive-tex-label
Enables the user to place a 'classification' label on each
page, at the bottom to the right of the page number

%package -n texlive-tex-label-doc
Summary:        Documentation for tex-label
Version:        svn16372.0

Provides:       tex-tex-label-doc
AutoReqProv:    No

%description -n texlive-tex-label-doc
Documentation for tex-label

%package -n texlive-texlogos
Provides:       tex-texlogos = %{tl_version}
License:        LPPL
Summary:        Ready-to-use LaTeX logos
Version:        svn19083.1.3.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(graphics.sty), tex(ifthen.sty)
Provides:       tex(texlogos.sty) = %{tl_version}

%description -n texlive-texlogos
TeXlogos defines an assortment of frequently used logos not
contained in base LaTeX itself. The Metafont, MetapostAMS,
BibTeX and SliTeX logos are defined, as long as you have the
appropriate CM/Logo/AMS fonts. Currency symbols Euro, Cent,
Yen, Won and Naira are defined so as not to need TS1-encoded
fonts. Also defined are the C++ logo, with the '+' signs
properly positioned, and the logo of the Vienna University
Business Administration Center (BWZ).

%package -n texlive-texmate
Provides:       tex-texmate = %{tl_version}
License:        LPPL
Summary:        Comprehensive chess annotation in LaTeX
Version:        svn15878.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amssymb.sty), tex(chessfss.sty), tex(skak.sty)
Provides:       tex(texmate.sty) = %{tl_version}

%description -n texlive-texmate
TeXmate formats chess games from very simple ascii input. The
clean "1. e4 e5; 2. Nf3 Nc6; 3. Bb5 a6" will produce the same
results as the sloppier "1 e4 e5; Nf3 Nc6 3.. Bb5 a6". The
resulting format is fully customizable. There are 4 levels of
commentary: 1 is the main game, 2-3 are commentaries. Each has
its fonts, punctuation marks, etc., and these are also
customizable. The package includes a tool for the creation of
diagrams. The package works in conjunction with skak to produce
diagrams of the current position automatically. For chess
fonts, the package uses the chessfss system.

%package -n texlive-texmate-doc
Summary:        Documentation for texmate
Version:        svn15878.2

Provides:       tex-texmate-doc
AutoReqProv:    No

%description -n texlive-texmate-doc
Documentation for texmate

%package -n texlive-texments
Provides:       tex-texments = %{tl_version}
License:        LPPL
Summary:        Using the Pygments highlighter in LaTeX
Version:        svn15878.0.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fancyvrb.sty), tex(color.sty), tex(ifthen.sty)
Provides:       tex(texments.sty) = %{tl_version}

%description -n texlive-texments
A package which allows to use the Pygments highlighter inside
LaTeX documents. Pygments supports syntax colouring of over 50
types of files, and ships with multiple colour schemes.

%package -n texlive-texments-doc
Summary:        Documentation for texments
Version:        svn15878.0.2.0

Provides:       tex-texments-doc
AutoReqProv:    No

%description -n texlive-texments-doc
Documentation for texments

%package -n texlive-texpower
Provides:       tex-texpower = %{tl_version}
License:        GPL+
Summary:        Create dynamic online presentations with LaTeX
Version:        svn29349.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex-tpslifonts, tex(ifthen.sty), tex(relsize.sty), tex(tppstcol.sty)
Requires:       tex(ifpdf.sty), tex(graphics.sty), tex(seminar.bug), tex(seminar.bg2)
Requires:       tex(calc.sty), tex(keyval.sty), tex(color.sty), tex(pstricks.sty)
Requires:       tex(sem-page.sty)
Provides:       tex(automata.sty) = %{tl_version}, tex(fixseminar.sty) = %{tl_version}
Provides:       tex(powersem.cls) = %{tl_version}, tex(texpower.sty) = %{tl_version}
Provides:       tex(tpcolors.cfg) = %{tl_version}, tex(tplists.sty) = %{tl_version}
Provides:       tex(tpoptions.cfg) = %{tl_version}, tex(tppstcol.sty) = %{tl_version}
Provides:       tex(tpsem-a4.sty) = %{tl_version}, tex(tpsettings.cfg) = %{tl_version}

%description -n texlive-texpower
TeXPower is a bundle of packages intended to provide an all-
inclusive environment for designing pdf screen presentations to
be viewed in full-screen mode, especially for projecting
`online' with a video beamer. For some of its core functions,
it uses code derived from ppower4 packages. It is, however, not
a complete environment in itself: it relies on an existing
class for preparing slides (such as foiltex or seminar) or
another package such as pdfslide.

%package -n texlive-texpower-doc
Summary:        Documentation for texpower
Version:        svn29349.0.2

Provides:       tex-texpower-doc
AutoReqProv:    No
Requires:       tex-tpslifonts-doc

%description -n texlive-texpower-doc
Documentation for texpower

%package -n texlive-texshade
Provides:       tex-texshade = %{tl_version}
License:        GPLv2+
Summary:        Package for setting nucleotide and peptide alignments
Version:        svn46559
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(color.sty), tex(graphics.sty), tex(amssymb.sty)
Provides:       tex(texshade.def) = %{tl_version}, tex(texshade.sty) = %{tl_version}

%description -n texlive-texshade
TeXshade is alignment shading software completely written in
TeX/LaTeX; it can process multiple sequence alignments in the
.MSF and the .ALN file formats. In addition to common shading
algorithms, it provides special shading modes showing
functional aspects, e.g. charge or hydropathy, and a wide range
of commands for handling shading colours, text styles, labels,
legends; it even allows the user to define completely new
shading modes. TeXshade combines highest flexibility with TeX
output quality -- all in a bundle that does not demand
excessive development time of the user.

%package -n texlive-texshade-doc
Summary:        Documentation for texshade
Version:        svn46559
Provides:       tex-texshade-doc
AutoReqProv:    No

%description -n texlive-texshade-doc
Documentation for texshade

%package -n texlive-textfit
Provides:       tex-textfit = %{tl_version}
License:        LPPL 1.3
Summary:        Fit text to a desired size
Version:        svn20591.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(textfit.sty) = %{tl_version}

%description -n texlive-textfit
Package to fit text to a given width or height by scaling the
font. For example: \scaletowidth{3in}{This}. (The job is done
by calculating a magstep and applying it to the current font;
thus "This" will be very tall, as well as very wide; to scale
in just one dimension, use the facilities of the graphicx
package.)

%package -n texlive-textfit-doc
Summary:        Documentation for textfit
Version:        svn20591.5

Provides:       tex-textfit-doc
AutoReqProv:    No

%description -n texlive-textfit-doc
Documentation for textfit

%package -n texlive-textgreek
Provides:       tex-textgreek = %{tl_version}
License:        LPPL
Summary:        Upright greek letters in text
Version:        svn44192
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(textgreek.sty) = %{tl_version}
Requires:       texlive-greek-fontenc, texlive-cbfonts-fd

%description -n texlive-textgreek
Use upright greek letters as text symbols, e.g. \textbeta.

%package -n texlive-textgreek-doc
Summary:        Documentation for textgreek
Version:        svn44192
Provides:       tex-textgreek-doc
AutoReqProv:    No

%description -n texlive-textgreek-doc
Documentation for textgreek

%package -n texlive-textmerg
Provides:       tex-textmerg = %{tl_version}
License:        Public Domain
Summary:        Merge text in TeX and LaTeX
Version:        svn20677.2.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(textmerg.sty) = %{tl_version}

%description -n texlive-textmerg
Repetetively produce documents from a fixed part and a variable
part. Such an operation is commonly used as "mail merge" to
produce mail shots.

%package -n texlive-textmerg-doc
Summary:        Documentation for textmerg
Version:        svn20677.2.01

Provides:       tex-textmerg-doc
AutoReqProv:    No

%description -n texlive-textmerg-doc
Documentation for textmerg

%package -n texlive-textpos
Provides:       tex-textpos = %{tl_version}
License:        GPL+
Summary:        Place boxes at arbitrary positions on the LaTeX page
Version:        svn41331

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(everyshi.sty)
Provides:       tex(textpos.sty) = %{tl_version}

%description -n texlive-textpos
A package to facilitate placement of boxes at absolute
positions on the LaTeX page. There are several reasons why this
might be useful, an important one being to help the creation of
large-format conference posters.

%package -n texlive-textpos-doc
Summary:        Documentation for textpos
Version:        svn41331

Provides:       tex-textpos-doc
AutoReqProv:    No

%description -n texlive-textpos-doc
Documentation for textpos

%package -n texlive-tabriz-thesis
Provides:       tex-tabriz-thesis = %{tl_version}
License:        LPPL 1.3
Summary:        A template for the University of Tabriz
Version:        svn29421.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsthm.sty), tex(amssymb.sty), tex(amsmath.sty), tex(geometry.sty)
Requires:       tex(graphicx.sty), tex(framed.sty), tex(lastpage.sty), tex(fancyhdr.sty)
Requires:       tex(tocbibind.sty), tex(makeidx.sty), tex(hyperref.sty)
Provides:       tex(tabriz-thesis.cls) = %{tl_version}

%description -n texlive-tabriz-thesis
The package offers a document class for typesetting theses and
dissertations at the University of Tabriz. The class requires
use of XeLaTeX.

%package -n texlive-tabriz-thesis-doc
Summary:        Documentation for tabriz-thesis
Version:        svn29421.1.1

Provides:       tex-tabriz-thesis-doc
AutoReqProv:    No

%description -n texlive-tabriz-thesis-doc
Documentation for tabriz-thesis

%package -n texlive-texilikechaps
Provides:       tex-texilikechaps = %{tl_version}
License:        LPPL
Summary:        Format chapters with a texi-like format
Version:        svn28553.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(texilikechaps.sty) = %{tl_version}

%description -n texlive-texilikechaps
The package enables the user to reduce the size of the rather
large chapter headings in standard classes into a texi-like
smaller format. Details of the format may be controlled with
internal commands.

%package -n texlive-texilikecover
Provides:       tex-texilikecover = %{tl_version}
License:        LPPL
Summary:        A cover-page package, like TeXinfo
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(texilikecover.sty) = %{tl_version}

%description -n texlive-texilikecover
The package creates document cover pages, like those that
TeXinfo produces.

%package -n texlive-textopo
Provides:       tex-textopo = %{tl_version}
License:        GPL+
Summary:        Annotated membrane protein topology plots
Version:        svn23796.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(texshade.sty), tex(color.sty), tex(graphics.sty)
Provides:       tex(biotex.sty) = %{tl_version}, tex(textopo.def) = %{tl_version}
Provides:       tex(textopo.sty) = %{tl_version}

%description -n texlive-textopo
A LaTeX package for setting shaded and annotated membrane
protein topology plots and helical wheels.

%package -n texlive-textopo-doc
Summary:        Documentation for textopo
Version:        svn23796.1.5

Provides:       tex-textopo-doc
AutoReqProv:    No

%description -n texlive-textopo-doc
Documentation for textopo

%package -n texlive-texlive-docindex
Provides:       tex-texlive-docindex = %{tl_version}
License:        LPPL
Summary:        top-level TeX Live doc.html, etc
Version:        svn45575
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-texlive-docindex
These files are regenerated as needed, which is often, so we
make them a separate package.  See the tl-update-auto script
for the process.

%package -n texlive-texlive-docindex-doc
Summary:        Documentation for texlive-docindex
Version:        svn45575
Provides:       tex-texlive-docindex-doc
AutoReqProv:    No

%description -n texlive-texlive-docindex-doc
Documentation for texlive-docindex

%package -n texlive-tempora-doc
Provides:       tex-tempora-doc = %{tl_version}
License:        GPLv2+ with exceptions and LPPL
Summary:        doc files of tempora
Version:        svn39596

AutoReqProv:    No

%description -n texlive-tempora-doc
Documentation for tempora

%package -n texlive-tempora
Provides:       tex-tempora = %{tl_version}
License:        GPLv2+ and LPPL
Summary:        Greek and Cyrillic to accompany Times
Version:        svn39596

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tempora.sty) = %{tl_version}, tex(tempora.map) = %{tl_version}
Provides:       tex(ot2tempora-tlf.fd) = %{tl_version}, tex(TS1Tempora-TOsF.fd) = %{tl_version}
Provides:       tex(T1Tempora-TLF.fd) = %{tl_version}, tex(T1Tempora-Sup.fd) = %{tl_version}
Provides:       tex(t2atempora-tlf.fd) = %{tl_version}, tex(OT1Tempora-TOsF.fd) = %{tl_version}
Provides:       tex(TS1Tempora-TLF.fd) = %{tl_version}, tex(OT1Tempora-TLF.fd) = %{tl_version}
Provides:       tex(t2btempora-tosf.fd) = %{tl_version}, tex(t2ctempora-tosf.fd) = %{tl_version}
Provides:       tex(OT1Tempora-Sup.fd) = %{tl_version}, tex(t2btempora-tlf.fd) = %{tl_version}
Provides:       tex(t2atempora-tosf.fd) = %{tl_version}, tex(ot2tempora-tosf.fd) = %{tl_version}
Provides:       tex(lgrtempora-tlf.fd) = %{tl_version}, tex(lgrtempora-tosf.fd) = %{tl_version}
Provides:       tex(t2ctempora-tlf.fd) = %{tl_version}, tex(T1Tempora-TOsF.fd) = %{tl_version}
Provides:       tex(Tempora-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Tempora-Bold.pfb) = %{tl_version}, tex(Tempora-Italic.pfb) = %{tl_version}
Provides:       tex(Tempora-Regular.pfb) = %{tl_version}
Provides:       tex(tmp_xvqxbr.enc) = %{tl_version}, tex(tmp_jglahm.enc) = %{tl_version}
Provides:       tex(ot2-tempora.enc) = %{tl_version}, tex(t2b-tempora.enc) = %{tl_version}
Provides:       tex(t2c-temporaosf.enc) = %{tl_version}, tex(ot2-temporaosf.enc) = %{tl_version}
Provides:       tex(t2a-tempora.enc) = %{tl_version}, tex(t2b-temporaosf.enc) = %{tl_version}
Provides:       tex(tmp_yz5x6b.enc) = %{tl_version}, tex(t2a-temporaosf.enc) = %{tl_version}
Provides:       tex(tmp_6rqc3d.enc) = %{tl_version}, tex(tmp_q3dzgc.enc) = %{tl_version}
Provides:       tex(tmp_y4r4km.enc) = %{tl_version}, tex(lgr-temporaosf.enc) = %{tl_version}
Provides:       tex(tmp_arnbc6.enc) = %{tl_version}, tex(tmp_v6f3ze.enc) = %{tl_version}
Provides:       tex(tmp_aq2g6w.enc) = %{tl_version}, tex(tmp_m6t7eu.enc) = %{tl_version}
Provides:       tex(t2c-tempora.enc) = %{tl_version}, tex(tmp_mdnuug.enc) = %{tl_version}
Provides:       tex(tmp_ac5xuc.enc) = %{tl_version}, tex(lgr-tempora.enc) = %{tl_version}
Provides:       tex(Tempora-Regular.otf) = %{tl_version}
Provides:       tex(Tempora-BoldItalic.otf) = %{tl_version}
Provides:       tex(Tempora-Bold.otf) = %{tl_version}, tex(Tempora-Italic.otf) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tosf-ot1.vf) = %{tl_version}
Provides:       tex(Tempora-Regular-tlf-ot1.vf) = %{tl_version}
Provides:       tex(Tempora-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(Tempora-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Tempora-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Tempora-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Tempora-Regular-tosf-ot1.vf) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Tempora-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(Tempora-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Tempora-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(Tempora-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Tempora-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Tempora-Bold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(Tempora-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(Tempora-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Tempora-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(Tempora-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(Tempora-Bold-tosf-ot1.vf) = %{tl_version}
Provides:       tex(Tempora-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Tempora-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-TLF-ot2.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-TOsF-t2b.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-TLF-ot2.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-TOsF-t2b.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-TOsF-ot2.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-TLF-ot2.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-TLF-t2c.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-TOsF-lgr.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-TOsF-lgr.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-TLF-t2b.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-TLF-t2b.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-TLF-ot2.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-TOsF-ot2.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-TLF-t2b.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-TOsF-t2a.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-TOsF-lgr.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-TOsF-t2c.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-TLF-t2a.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-TLF-t2c.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-TLF-t2a.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-TLF-t2c.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-TLF-lgr.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-TOsF-t2a.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-TOsF-t2a.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-TLF-t2c.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-TLF-t2a.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-TOsF-t2b.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-TLF-t2a.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-TOsF-ot2.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-TOsF-ot2.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-TLF-t2b.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-TOsF-t2a.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-TLF-lgr.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-TOsF-t2c.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-TOsF-t2b.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-TLF-lgr.tfm) = %{tl_version}
Provides:       tex(Tempora-Bold-TOsF-t2c.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-Regular-TOsF-t2c.tfm) = %{tl_version}
Provides:       tex(Tempora-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-TLF-lgr.tfm) = %{tl_version}
Provides:       tex(Tempora-BoldItalic-TOsF-lgr.tfm) = %{tl_version}

%description -n texlive-tempora
This package, derived from TemporaLGCUni by Alexej Kryukov, is
meant as a companion to Times text font packages, providing
Greek and Cyrillic in matching weights and styles. OpenType and
Type1 fonts are provided, with LaTeX support files giving
essentially complete LGR coverage of monotonic, polytonic and
ancient Greek, and almost full T2A coverage of Cyrillic.

%package -n texlive-tex-ini-files-doc
Provides:       tex-tex-ini-files-doc = %{tl_version}
License:        Public Domain
Summary:        doc files of tex-ini-files
Version:        svn40533

AutoReqProv:    No

%description -n texlive-tex-ini-files-doc
Documentation for tex-ini-files

%package -n texlive-tex-ini-files
Provides:       tex-tex-ini-files = %{tl_version}
License:        Public Domain
Summary:        Model TeX format creation files
Version:        svn40533

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pdftexconfig.tex) = %{tl_version}, tex(luatexconfig.tex) = %{tl_version}

%description -n texlive-tex-ini-files
This bundle provides a collection of model .ini files for
creating TeX formats. These files are commonly used to
introduced distribution-dependent variations in formats. They
are also used to allow existing format source files to be used
with newer engines, for example to adapt the plain e-TeX source
file to work with XeTeX and LuaTeX.

%package -n texlive-texlive-es-doc
Provides:       tex-texlive-es-doc = %{tl_version}
License:        LPPL
Summary:        doc files of texlive-es
Version:        svn44356
AutoReqProv:    No

%description -n texlive-texlive-es-doc
Documentation for texlive-es

%package -n texlive-texvc-doc
Provides:       tex-texvc-doc = %{tl_version}
License:        ASL 2.0
Summary:        doc files of texvc
Version:        svn46844
AutoReqProv:    No

%description -n texlive-texvc-doc
Documentation for texvc

%package -n texlive-texvc
Provides:       tex-texvc = %{tl_version}
License:        ASL 2.0 and LPPL
Summary:        Use MediaWiki LaTeX commands
Version:        svn46844
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(texvc.sty) = %{tl_version}

%description -n texlive-texvc
User MediaWiki LaTeX commands to copy and past formulae from
MediaWiki to LaTeX documents.

%package -n texlive-texworks-doc
Provides:       tex-texworks-doc = %{tl_version}
License:        Public Domain
Summary:        doc files of texworks
Version:        svn43291
AutoReqProv:    No

%description -n texlive-texworks-doc
Documentation for texworks

%package -n texlive-tagpdf
Summary:        Tools for experimenting with tagging using pdfLaTeX and LuaLaTeX
Version:        svn48366
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tagpdf-checks-code.sty) = %{tl_version}
Provides:       tex(tagpdf-luatex.def) = %{tl_version}, tex(tagpdf-mc-code-generic.sty) = %{tl_version}
Provides:       tex(tagpdf-mc-code-lua.sty) = %{tl_version}
Provides:       tex(tagpdf-mc-code-shared.sty) = %{tl_version}
Provides:       tex(tagpdf-pdftex.def) = %{tl_version}, tex(tagpdf-roles-code.sty) = %{tl_version}
Provides:       tex(tagpdf-struct-code.sty) = %{tl_version}
Provides:       tex(tagpdf-tree-code.sty) = %{tl_version}
Provides:       tex(tagpdf-user.sty) = %{tl_version}, tex(tagpdf.lua) = %{tl_version}
Provides:       tex(tagpdf.sty) = %{tl_version}

%description -n texlive-tagpdf
The package offers tools to experiment with tagging and
accessibility using pdfLaTeX and LuaTeX. It isn't meant for
production but allows the user to try out how difficult it is
to tag some structures; to try out how much tagging is really
needed; to test what else is needed so that a pdf works e.g.
with a screen reader. Its goal is to get a feeling for what has
to be done, which kernel changes are needed, how packages
should be adapted.

%package -n texlive-texdate
Summary:        Date printing, formatting, and manipulation in TeX
Version:        svn47878
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(texdate.sty) = %{tl_version}

%description -n texlive-texdate
TeX and LaTeX provide few facilities for dates by default,
though many packages have filled this gap. This package fills
it, as well, with a pure TeX-primitive implementation. It can
print dates, advance them by numbers of days, weeks, or months,
determine the weekday automatically (with an algorithm cribbed
from the dayofweek.tex file written by Martin Minow), and print
them in (mostly) arbitrary format. It can also print calendars
(monthly and yearly) automatically, and can be easily localized
for non-English languages.

%package -n texlive-textualicomma
Summary:        Use the textual comma character as decimal separator in math mode
Version:        svn48474
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(textualicomma.sty) = %{tl_version}

%description -n texlive-textualicomma
The package is based on the icomma package, and intended as a
solution for situations where the text comma character discerns
from the math comma character, e. g. when fonts whithout math
support are involved. Escaping to text mode every time a comma
is used in math mode may slow down the compilation process.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/tex-gyre public/tex-gyre-math"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
mv %{buildroot}/%{_texdir}/texmf-dist/doc/info/* %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-texlive-common-doc
%{_texdir}/texmf-dist/doc/texlive/index.html
%{_texdir}/texmf-dist/doc/texlive/texlive-common/examples/ex5.tex
%{_texdir}/texmf-dist/doc/texlive/texlive-common/examples/ex6.tex
%{_texdir}/texmf-dist/doc/texlive/texlive-common/examples/ex6a.tex
%{_texdir}/texmf-dist/doc/texlive/texlive-common/examples/ex6b.tex
%{_texdir}/texmf-dist/doc/texlive/texlive-common/examples/ex6c.tex
%{_texdir}/texmf-dist/doc/texlive/texlive-common/install-lnx-main.png
%{_texdir}/texmf-dist/doc/texlive/texlive-common/nsis_installer.png
%{_texdir}/texmf-dist/doc/texlive/texlive-common/psview.png
%{_texdir}/texmf-dist/doc/texlive/texlive-common/stdcoll.png
%{_texdir}/texmf-dist/doc/texlive/texlive-common/tray-menu.png
%{_texdir}/texmf-dist/doc/texlive/texlive-common/wizard-w32.png
%exclude %{_texdir}/texmf-dist/doc/texlive/texlive-common/tlmgr*

%files -n texlive-texlive-msg-translations
%{_texdir}/tlpkg/translations/
%exclude %{_texdir}/tlpkg/tlpobj/
%exclude %{_texdir}/texmf-dist/tlpkg/tlpobj/

%files -n texlive-tapir
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/tapir/
%{_texdir}/texmf-dist/fonts/type1/public/tapir/

%files -n texlive-tapir-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/tapir/

%files -n texlive-tengwarscript
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/tengwarscript/
%{_texdir}/texmf-dist/fonts/map/dvips/tengwarscript/
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/
%{_texdir}/texmf-dist/fonts/vf/public/tengwarscript/
%{_texdir}/texmf-dist/tex/latex/tengwarscript/

%files -n texlive-tengwarscript-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tengwarscript/

%files -n texlive-tfrupee
%license gpl3.txt
%{_texdir}/texmf-dist/fonts/afm/public/tfrupee/
%{_texdir}/texmf-dist/fonts/map/dvips/tfrupee/
%{_texdir}/texmf-dist/fonts/tfm/public/tfrupee/
%{_texdir}/texmf-dist/fonts/type1/public/tfrupee/
%{_texdir}/texmf-dist/tex/latex/tfrupee/

%files -n texlive-tfrupee-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/fonts/tfrupee/

%files -n texlive-tex-gyre
%license gfsl.txt
%{_datadir}/fonts/tex-gyre
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/
%{_texdir}/texmf-dist/tex/latex/tex-gyre/

%files -n texlive-tex-gyre-doc
%license gfsl.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/

%files -n texlive-tex-gyre-math
%license gfl.txt
%{_datadir}/fonts/tex-gyre-math
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre-math/

%files -n texlive-tex-gyre-math-doc
%license gfl.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre-math/

%files -n texlive-tabto-generic
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/tabto-generic/

%files -n texlive-termmenu
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/termmenu/

%files -n texlive-termmenu-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/termmenu/

%files -n texlive-texapi
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/texapi/

%files -n texlive-texapi-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/texapi/

%files -n texlive-tex-ps
%license pd.txt
%{_texdir}/texmf-dist/dvips/tex-ps/
%{_texdir}/texmf-dist/tex/generic/tex-ps/

%files -n texlive-tex-ps-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/tex-ps/

%files -n texlive-textglos
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/textglos/

%files -n texlive-textglos-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/textglos/

%files -n texlive-texlive-zh-cn-doc
%{_texdir}/texmf-dist/doc/texlive/texlive-zh-cn/

%files -n texlive-t2
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/enc/t2/
%{_texdir}/texmf-dist/tex/generic/t2/
%{_texdir}/texmf-dist/tex/latex/t2/

%files -n texlive-t2-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/t2/

%files -n texlive-texlive-ru-doc
%{_texdir}/texmf-dist/doc/texlive/texlive-ru/

%files -n texlive-texlive-sr-doc
%{_texdir}/texmf-dist/doc/texlive/texlive-sr/

%files -n texlive-texlive-cz-doc
%{_texdir}/texmf-dist/doc/texlive/texlive-cz/

%files -n texlive-tabulars-e-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tabulars-e/

%files -n texlive-tamethebeast-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/bibtex/tamethebeast/

%files -n texlive-tds-doc
%{_texdir}/texmf-dist/doc/generic/tds/

%files -n texlive-tex-font-errors-cheatsheet-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tex-font-errors-cheatsheet/

%files -n texlive-tex-overview-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tex-overview/

%files -n texlive-tex-refs-doc
%{_texdir}/texmf-dist/doc/generic/tex-refs/

%files -n texlive-texbytopic-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/plain/texbytopic/

%files -n texlive-tabvar
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/afm/public/tabvar/
%{_texdir}/texmf-dist/fonts/map/dvips/tabvar/
%{_texdir}/texmf-dist/fonts/tfm/public/tabvar/
%{_texdir}/texmf-dist/fonts/type1/public/tabvar/
%{_texdir}/texmf-dist/metapost/tabvar/
%{_texdir}/texmf-dist/tex/latex/tabvar/

%files -n texlive-tabvar-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tabvar/

%files -n texlive-tdsfrmath
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tdsfrmath/

%files -n texlive-tdsfrmath-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tdsfrmath/

%files -n texlive-texlive-fr-doc
%{_texdir}/texmf-dist/doc/texlive/texlive-fr/

%files -n texlive-templates-fenn-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/templates-fenn/

%files -n texlive-templates-sommer-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/templates-sommer/

%files -n texlive-texlive-de-doc
%{_texdir}/texmf-dist/doc/texlive/texlive-de/

%files -n texlive-teubner
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/teubner/

%files -n texlive-teubner-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/teubner/

%files -n texlive-texlive-it-doc
%{_texdir}/texmf-dist/doc/texlive/texlive-it/

%files -n texlive-tap
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/tap/

%files -n texlive-tap-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/tap/

%files -n texlive-tex-virtual-academy-pl-doc
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/

%files -n texlive-texlive-pl-doc
%{_texdir}/texmf-dist/doc/texlive/texlive-pl/

%files -n texlive-textcase
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/textcase/

%files -n texlive-textcase-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/textcase/

%files -n texlive-texdraw
%{_infodir}/texdraw.info*
%{_texdir}/texmf-dist/tex/generic/texdraw/

%files -n texlive-texdraw-doc
%{_texdir}/texmf-dist/doc/support/texdraw/

%files -n texlive-tabfigures
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tabfigures/

%files -n texlive-tabfigures-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tabfigures/

%files -n texlive-tableaux
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tableaux/

%files -n texlive-tableaux-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tableaux/

%files -n texlive-tablefootnote
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tablefootnote/

%files -n texlive-tablefootnote-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tablefootnote/

%files -n texlive-tableof
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tableof/

%files -n texlive-tableof-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tableof/

%files -n texlive-tablestyles
%{_texdir}/texmf-dist/tex/latex/tablestyles/

%files -n texlive-tablestyles-doc
%{_texdir}/texmf-dist/doc/latex/tablestyles/

%files -n texlive-tablists
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tablists/

%files -n texlive-tablists-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tablists/

%files -n texlive-tabls
%{_texdir}/texmf-dist/tex/latex/tabls/

%files -n texlive-tabls-doc
%{_texdir}/texmf-dist/doc/latex/tabls/

%files -n texlive-tabstackengine
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tabstackengine/

%files -n texlive-tabstackengine-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tabstackengine/

%files -n texlive-tabto-ltx
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tabto-ltx/

%files -n texlive-tabto-ltx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tabto-ltx/

%files -n texlive-tabu
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tabu/

%files -n texlive-tabu-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tabu/

%files -n texlive-tabularborder
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/tabularborder/

%files -n texlive-tabularborder-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/tabularborder/

%files -n texlive-tabularcalc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tabularcalc/

%files -n texlive-tabularcalc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tabularcalc/

%files -n texlive-tabularew
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tabularew/

%files -n texlive-tabularew-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tabularew/

%files -n texlive-tabulary
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tabulary/

%files -n texlive-tabulary-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tabulary/

%files -n texlive-tagging
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tagging/

%files -n texlive-tagging-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tagging/

%files -n texlive-tagpair
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tagpair/

%files -n texlive-tagpair-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tagpair/

%files -n texlive-talk
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/talk/

%files -n texlive-talk-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/talk/

%files -n texlive-tamefloats
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tamefloats/

%files -n texlive-tamefloats-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tamefloats/

%files -n texlive-tasks
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tasks/

%files -n texlive-tasks-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tasks/

%files -n texlive-tcldoc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tcldoc/

%files -n texlive-tcldoc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tcldoc/

%files -n texlive-tcolorbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tcolorbox/

%files -n texlive-tcolorbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tcolorbox/

%files -n texlive-tdclock
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/tdclock/

%files -n texlive-tdclock-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/tdclock/

%files -n texlive-technics
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/technics/

%files -n texlive-technics-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/technics/

%files -n texlive-ted
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ted/

%files -n texlive-ted-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ted/

%files -n texlive-templatetools
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/templatetools/

%files -n texlive-templatetools-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/templatetools/

%files -n texlive-termcal
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/termcal/

%files -n texlive-termcal-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/termcal/

%files -n texlive-termlist
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/termlist/

%files -n texlive-termlist-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/termlist/

%files -n texlive-testhyphens
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/testhyphens/

%files -n texlive-testhyphens-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/testhyphens/

%files -n texlive-tex-label
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tex-label/

%files -n texlive-tex-label-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tex-label/

%files -n texlive-texlogos
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/texlogos/

%files -n texlive-texmate
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/texmate/

%files -n texlive-texmate-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/texmate/

%files -n texlive-texments
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/texments/

%files -n texlive-texments-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/texments/

%files -n texlive-texpower
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/texpower/

%files -n texlive-texpower-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/texpower/

%files -n texlive-texshade
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/texshade/

%files -n texlive-texshade-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/texshade/

%files -n texlive-textfit
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/textfit/

%files -n texlive-textfit-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/textfit/

%files -n texlive-textgreek
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/textgreek/

%files -n texlive-textgreek-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/textgreek/

%files -n texlive-textmerg
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/textmerg/

%files -n texlive-textmerg-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/textmerg/

%files -n texlive-textpos
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/textpos/

%files -n texlive-textpos-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/textpos/

%files -n texlive-tablor
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tablor/

%files -n texlive-tablor-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tablor/

%files -n texlive-tensor
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tensor/

%files -n texlive-tensor-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tensor/

%files -n texlive-tex-ewd
%license bsd.txt
%{_texdir}/texmf-dist/tex/generic/tex-ewd/

%files -n texlive-tex-ewd-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/generic/tex-ewd/

%files -n texlive-textpath
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/textpath/
%{_texdir}/texmf-dist/tex/latex/textpath/

%files -n texlive-textpath-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/textpath/

%if %{with_texinfo}
%files -n texlive-texinfo
%license gpl.txt
%{_texdir}/texmf-dist/tex/texinfo/
%endif

%files -n texlive-tabriz-thesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tabriz-thesis/

%files -n texlive-tabriz-thesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tabriz-thesis/

%files -n texlive-texilikechaps
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/texilikechaps/

%files -n texlive-texilikecover
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/texilikecover/

%files -n texlive-textopo
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/textopo/

%files -n texlive-textopo-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/textopo/

%files -n texlive-tempora-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/fonts/tempora/

%files -n texlive-tempora
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/tempora/
%{_texdir}/texmf-dist/fonts/opentype/public/tempora/
%{_texdir}/texmf-dist/fonts/map/dvips/tempora/
%{_texdir}/texmf-dist/fonts/tfm/public/tempora/
%{_texdir}/texmf-dist/fonts/vf/public/tempora/
%{_texdir}/texmf-dist/fonts/enc/dvips/tempora/
%{_texdir}/texmf-dist/fonts/afm/public/tempora/
%{_texdir}/texmf-dist/fonts/type1/public/tempora/

%files -n texlive-tex-ini-files-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/tex-ini-files/

%files -n texlive-tex-ini-files
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/tex-ini-files/

%files -n texlive-texlive-es-doc
%license lppl.txt
%{_texdir}/texmf-dist/doc/texlive/texlive-es/

%files -n texlive-texvc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/texvc/

%files -n texlive-texvc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/texvc/

%files -n texlive-texworks-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/texworks/

%files -n texlive-texlive-docindex
%{_texdir}/texmf-dist/scripts/texlive/var/texcatalogue.keywords

%files -n texlive-texlive-docindex-doc
%{_texdir}/doc.html

%files -n texlive-table-fct
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/table-fct/
%{_texdir}/texmf-dist/tex/latex/table-fct/

%files -n texlive-termcal-de
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/termcal-de/
%{_texdir}/texmf-dist/tex/latex/termcal-de/

%files -n texlive-testidx
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/testidx/
%{_texdir}/texmf-dist/tex/latex/testidx/

%files -n texlive-texproposal-doc
%doc %{_texdir}/texmf-dist/doc/latex/texproposal/

%files -n texlive-tagpdf
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/tagpdf/
%doc %{_texdir}/texmf-dist/doc/latex/tagpdf/

%files -n texlive-texdate
%license lppl.txt
%{_texdir}/texmf-dist/tex/generic/texdate/
%doc %{_texdir}/texmf-dist/doc/generic/texdate/

%files -n texlive-textualicomma
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/textualicomma/
%doc %{_texdir}/texmf-dist/doc/latex/textualicomma/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
