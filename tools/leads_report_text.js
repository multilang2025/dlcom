// Evaluates the report page script with a stub DOM and dumps the rendered ES/FR copy (with computed numbers) as JSON.
// Usage: node tools/leads_report_text.js data/leads/informe-leads.html > texts.json
const fs = require("fs");
const html = fs.readFileSync(process.argv[2], "utf8");
const js = html.match(/<script>([\s\S]*)<\/script>/)[1];
const stub = () => ({ setAttribute() {}, set innerHTML(v) {}, set onclick(v) {}, style: {} });
global.document = { getElementById: stub, documentElement: {}, title: "" };
global.location = { hash: "" };
global.localStorage = { getItem() { return null; }, setItem() {} };
const wrapped = js + "\n;globalThis.__R = { X, K, D, setLang: l => { lang = l; } };";
(0, eval)(wrapped);
const { X, K, D, setLang } = globalThis.__R;
const out = { K };
for (const l of ["es", "fr"]) {
  setLang(l);
  const t = X[l];
  out[l] = {
    title: t.title, eyebrow: t.eyebrow, lead: t.lead(), kpi: t.kpi.map(k => k[0]), find: t.find(),
    i_volumen: t.i_volumen(), i_tipo: t.i_tipo, i_origen: t.i_origen(), i_areas: t.i_areas(), i_idiomas: t.i_idiomas,
    cards: Object.fromEntries(Object.entries(t.cards).map(([k, v]) => [k, { h: v.h, p: v.p() }])),
    areaNotes: Object.fromEntries(Object.entries(t.areaNotes).map(([k, f]) => [k, f()])),
    i_arbol: t.i_arbol, i_combos: t.i_combos, i_form: t.i_form, steps: t.steps, ints: t.ints, i_blog: t.i_blog(),
    recs: t.recs, metodo: t.metodo(), pk: t.pk, natK: t.natK,
    h: { esencial: t.h_esencial, volumen: t.h_volumen, tipo: t.h_tipo, origen: t.h_origen, areas: t.h_areas, idiomas: t.h_idiomas, arbol: t.h_arbol, combos: t.h_combos, form: t.h_form, blog: t.h_blog, recom: t.h_recom, metodo: t.h_metodo },
    misc: { client: t.client, nature: t.nature, ctryT: t.ctryT, natT: t.natT, famNat: t.famNat, inSpain: t.inSpain, outSpain: t.outSpain, unknown: t.unknown, cNote: t.cNote,
            colDD: t.colDD, colTX: t.colTX, other: t.other, top: t.top, lift: t.lift, colLeaf: t.colLeaf, colN: t.colN, colPrim: t.colPrim, colLang: t.colLang, colSub: t.colSub,
            colPair: t.colPair, colPairN: t.colPairN, pkg: t.pkg, routesT: t.routesT, colShare: t.colShare, info: t.info, ask: t.ask, colSubB: t.colSubB, colLeads: t.colLeads, colPosts: t.colPosts,
            gap: t.gap, ok: t.ok, gapN: t.gapN, enNote: t.enNote, exists: t.exists, proposed: t.proposed, files: t.files, foot: t.foot, pTitle: t.pTitle, pNote: t.pNote,
            fP: t.fP, fA: t.fA, fU: t.fU, fI: t.fI, flagsT: t.flagsT, medLen: t.medLen, chars: t.chars, traffic: t.traffic() }
  };
}
process.stdout.write(JSON.stringify(out));
