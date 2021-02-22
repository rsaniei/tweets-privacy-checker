import React from 'react';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';


const useStyles = makeStyles({
  root: {
    width: '100%',
    maxWidth: '100%',
  },
  text: {
    textAlign: "justify"
  },
  title: {
    backgroundColor: "#275eb047",
    padding: "12px",
    paddingBottom: "3px",
    borderRadius: "5px",
    color: "#043465",
    fontWeight: "600"

  },
  box: {
    border: "1px solid transparent",
    borderColor: "#b7b7bb;",
    marginBottom: "20px",
    backgroundColor: "#fff",
    border: "1px solid transparent",
    borderRadius: "4px",
    padding: "20px"
  }
});

export default function Types() {
  const classes = useStyles();

  return (
    <Container style={{ padding: '50px', paddingLeft: '70px', paddingRight: '70px' }}>
      <div className={classes.root}>
        <Typography style={{ fontWeight: "600" }} variant="h4" gutterBottom>
          PHDD Corpus: Corpus of Physical Health Data Disclosure on Twitter During COVID-19 Pandemic
        </Typography>
        <div style={{ paddingBottom: "9px", margin: "14px 0 20px", borderBottom: "1px solid #eee" }}>
        </div>
        <div className={classes.box}>
          <Typography className={classes.title} style={{ paddingBottom: "10px" }} variant="h6" gutterBottom>
            Corpus Description
        </Typography>
          <Typography className={classes.text} variant="body1" gutterBottom>
            The PHDD corpus contains a set of manually tagged tweets in English for privacy purposes. Each Twitter post is tagged in 3 dimensions represented below:
          <ul>
              <li><b> Health Sensitivity Status:</b> Specifies whether the tweet contains any physical health information of an identifiable/identified individual (Health Sensitive/Not Health Sensitive).</li>
              <li><b> Health Information Category</b>: For Health Sensitive tweets, determines type(s) of the provided physical health information (Test Result, Symptom, Disease, Other information). All health-sensitive tweets are also tagged as "Physical Health".</li>
              <li><b> Health History Subject</b>: For Health Sensitive tweets, specifies the position of a tweet author with respect to the disclosed information; whether it is a "self-disclosure" of the author's health history (Individual Health History), a disclosure about the author's family members health history (Family Health History), or a disclosure about other identified/identifiable people (Others Health History).
          <br />
                <br />To publish this corpus in a machine-readable format, we used a lightweight ontology called <b>"Privacy Tags for Health Information (PTHI)"</b>, created specifically for this goal. Supplementary information about PTHI can be found <a href="https://protect.oeg.fi.upm.es/def/pthi/widoco/index-en.html">here</a>.
          A typical record in the corpus contains an identifier and a set of associated tags. You can see below the diagram of a sample example record, and its associated RDF code:</li>
            </ul>
            <div style={{ marginBottom: "25px", textAlign: "justify" }}>
              <img style={{ display: "block", margin: "0 auto", maxWidth: '60%' }} src="https://protect.oeg.fi.upm.es/def/pthi/resources/CorpusExampleDigram.png" width="800" />
            </div>

            <div style={{ fontSize: "13px", backgroundColor: "#f9f9f9", border: "1px solid #adadad", borderRadius: "5px", padding: "15px", marginTop: "0px" }} >
              <pre><code>@prefix pthi: https://protect.oeg.fi.upm.es/def/pthi#/> .
              <br />@prefix rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
              <br />@prefix dpv: http://www.w3.org/ns/dpv#> .
              <br />@prefix sioc: http://rdfs.org/sioc/ns#> .
              <br />@prefix owl: http://www.w3.org/2002/07/owl#> .
              <br />
                <br />pthi:1298037841700638726 a sioc:Post ;<div style={{ marginLeft: '30px' }}>sioc:id"1298037841700638726";
              <br />sioc:created "Mon Aug 24 23:21:52 +0000 2020" ;
              <br />sioc:content "@RexChapman My mom has dementia and shes in quarantine because of
              <br />COVID. Im afraid shes not going to remember who I am."@en;
              <br />pthi:hasHealthSensitiveStatus pthi:healthSensitive ;
              <br />pthi:hasHealthInformationCategory pthi: PhysicalHealth, pthi:Disease ;
              <br />pthi:hasHealthHistorySubjectTag pthi:FamilyHealthHistory .
              </div>
                <br />
                <br />pthi: PhysicalHealth owl:sameAs dpv:PhysicalHealth .
              <br />pthi: FamilyHealthHistory owl:sameAs dpv:FamilyHealthHistory .
            </code></pre>
            </div>
          </Typography>
        </div>
        <div className={classes.box}>
          <Typography className={classes.title} style={{ paddingTop: '5px' }} variant="h6" gutterBottom>
            Corpus Download
        </Typography>
          <Typography className={classes.text} variant="body1" gutterBottom>
            The corpus contains tags in the the dimensions as mentioned above, using this <a href="https://protect.oeg.fi.upm.es/def/pthi/resources/criteria.pdf">criteria document</a>. You can download the final corpus in <a href="https://protect.oeg.fi.upm.es/def/pthi/resources/corpus.nt.zip">RDF</a> or <a href="https://protect.oeg.fi.upm.es/def/pthi/resources/final-corpus.xlsx.zip">XLSX</a> format.
        </Typography>
        </div>
        <div className={classes.box}>
          <Typography className={classes.title} style={{ paddingTop: '5px' }} variant="h6" gutterBottom>
            Authorship
        </Typography>
          <Typography className={classes.text} variant="body1" gutterBottom>
            For copyright reasons, the text is not available for download (but requests at
          <span style={{ display: "inline", color: "white", backgroundColor: "black", borderRadius: "2px", padding: "1px", fontSize: "13px", margin: "3px" }}>rsaniei.AT.delicias.dia.fi.upm.es</span>
          will be considered). The annotations are work of Rana Saniei, Delaram Golpaygani, Beatriz Gonçalves Crisóstomo Esteves, and Karen Vázquez Flores. They are freely downloadable under the <a href="https://creativecommons.org/licenses/by/4.0/">CC-BY 4.0</a> license.
          <img style={{ display: "inline" }} src="https://protect.oeg.fi.upm.es/def/pthi/resources/ccby.png" width="50" />
          </Typography>
        </div>
      </div >
    </Container >
  );
}
