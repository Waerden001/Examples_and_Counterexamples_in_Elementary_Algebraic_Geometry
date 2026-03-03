window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true,
    packages: {'[+]': ['ams', 'mathtools', 'amscd']},
    macros: {
      // Standard operator names used in the project
      Spec: "\\operatorname{Spec}\\,",
      Proj: "\\operatorname{Proj}\\,",
      Hom: "\\operatorname{Hom}",
      Ext: "\\operatorname{Ext}",
      Pic: "\\operatorname{Pic}",
      Aut: "\\operatorname{Aut}",
      GL: "\\operatorname{GL}",
      SL: "\\operatorname{SL}",
      Cl: "\\operatorname{Cl}",
      Gal: "\\operatorname{Gal}",
      Div: "\\operatorname{Div}",
      End: "\\operatorname{End}",
      Jac: "\\operatorname{Jac}",
      Hilb: "\\operatorname{Hilb}",
      Gr: "\\operatorname{Gr}",
      codim: "\\operatorname{codim}",
      coker: "\\operatorname{coker}",
      rank: "\\operatorname{rank}",
      Frac: "\\operatorname{Frac}",
      Tor: "\\operatorname{Tor}",
    }
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  loader: {
    load: ['[tex]/ams', '[tex]/mathtools', '[tex]/amscd']
  }
};

document$.subscribe(() => {
  MathJax.typesetPromise().then(() => {
    // Also typeset math in TOC sidebar and page header
    const tocElements = document.querySelectorAll(
      '.md-nav__link, .md-header__topic, .md-tabs__link, h1, h2, h3, h4'
    );
    if (tocElements.length > 0) {
      MathJax.typesetPromise(Array.from(tocElements));
    }
  });
})
