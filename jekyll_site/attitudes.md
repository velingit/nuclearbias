---
layout: default
title: Attitudes towards renewable energy
permalink: /attitudes/
---
# Cosmopolitan attitudes towards renewable energy in Europe

In this short project I have looked at the [European Social Survey Round 8]() and specifically at the energy panel. I had the idea to compare cosmopolitanism with renewable support after reading [Bechtel et al. (2014)](https://onlinelibrary.wiley.com/doi/full/10.1111/ajps.12079) wherein they relate the concepts of altruism and cosmopolitanism with support for Eurozone bailouts in Germany. Their findings indicate that a strong predictor for said support is exactly the social disposition of voters. 

To find out, I looked at two different types of climate policies:  
*Soft Solidarity:* Subsidising renewable energy (feels like a win-win, "free" money). Operationalized through the support for subsidies question.  
*Hard Solidarity:* Increasing taxes on fossil fuels. Operationalized through the taxes on fossil fuels question. 

Besides that, I collected variables motivated by the general literature on identity politics and energy specific findings: age, rile, gender, years of education, feelings about household income, urban/rural divide, trust in politicians; worries about energy affordability. 

I decided to look at those two because they seemed interesting and because it aligned with identity literature that I had read before. 
Theoretical frameworks also suggest that people can hold nested identities: meaning they can be deeply attached to both their nation and to Europe at the same time without these feelings competing [(Medrano & Gutiérrez, 2001)](https://www.tandfonline.com/doi/abs/10.1080/01419870120063963). In that regard I was interested in what happens when one looks at feelings of European and national belonging, thus I included the first two variables, namely national and European attachment. 

---

<b> Results: </b> 
European citizens are generally highly supportive of public subsidies for renewable energy, viewing it as a matter of technological efficiency that serves the general good. My models confirm that being attached to Europe predicts support for green subsidies. Being attached to your country also independently predicts support but the interaction of the two is not significant. 
When policies don't demand direct personal sacrifice, national identity and European identity work together in harmony. There is no clash here.

For a nested identifier, a citizen who loves both their country and Europe, their national identity acts as a brake on their willingness to pay for the climate through support of stronger fossil fuel taxes. When asked to make a  sacrifice perceived as personal, national identity mobilises in a protectionist direction, dampening the cosmopolitan, pro-climate effects of their European identity.

  
My models reveal two roadblocks green solidarity that go beyond identity and have been identified in [literature](https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS8_pawcer_climate_change.pdf):  

People struggling to make ends meet, or those who are highly anxious that energy will become too expensive, are intensely opposed to fossil fuel taxes (more so than people with strong national attitudes).

Urban and rural divide is very strong, as previously identified by [Balta-Ozkan & Gallo (2018)](https://www.sciencedirect.com/science/article/pii/S1364032117309620#bib41)

<html>
<head>
<meta http-equiv="Content-type" content="text/html;charset=UTF-8">
<style>
html, body { background-color: black; }
table { border-collapse:collapse; border:none; }
caption { font-weight: bold; text-align:left; }
td {  }
.thead { border-top: double; text-align:center; font-style:normal; font-weight:bold; padding:0.2cm; }
.tdata { padding:0.2cm; text-align:left; vertical-align:top; }
.arc { background-color:#f2f2f2; }
.summary { padding-top:0.1cm; padding-bottom:0.1cm; }
.summarydata { text-align:left; }
.fixedparts { font-weight:bold; text-align:left; }
.randomparts { font-weight:bold; text-align:left; padding-top:.8em; }
.zeroparts { font-weight:bold; text-align:left; padding-top:.8em; }
.simplexparts { font-weight:bold; text-align:left; padding-top:.8em; }
.lasttablerow { border-bottom: double; }
.firsttablerow {  }
.firstsumrow { border-top:1px solid; }
.labelcellborder { border-bottom:1px solid; }
.depvarhead { text-align:center; border-bottom:1px solid; font-style:italic; font-weight:normal; }
.depvarheadnodv { border-top: double; text-align:center; border-bottom:1px solid; font-style:italic; font-weight:normal; }
.leftalign { text-align:left; }
.centeralign { text-align:center; }
.firsttablecol { text-align:left; }
.footnote { font-style:italic; border-top:double black; text-align:right; }
.subtitle { font-weight: normal; }
.modelcolumn1 {  }
.modelcolumn2 {  }
.modelcolumn3 {  }
.modelcolumn4 {  }
.modelcolumn5 {  }
.modelcolumn6 {  }
.modelcolumn7 {  }
.col1 {  }
.col2 {  }
.col3 {  }
.col4 {  }
.col5 {  }
.col6 {  }
</style>
</head>
<body>
<table>
  <tr>
    <th class="thead firsttablerow firsttablecol col1">&nbsp;</th>
    <th colspan="3" class="thead firsttablerow">Support for fossil fuel<br>taxes</th>
    <th colspan="3" class="thead firsttablerow">Support for renewable<br>energy subsidies</th>
  </tr>
  <tr>
    <td class="depvarhead firsttablerow firsttablecol col1">Predictors</td>
    <td class="depvarhead firsttablerow col2">Estimates</td>
    <td class="depvarhead firsttablerow col3">CI</td>
    <td class="depvarhead firsttablerow col4">p</td>
    <td class="depvarhead firsttablerow col5">Estimates</td>
    <td class="depvarhead firsttablerow col6">CI</td>
    <td class="depvarhead firsttablerow col7">p</td>
  </tr>
  <tr>
    <td class="tdata firsttablecol col1">(Intercept)</td>
    <td class="tdata centeralign modelcolumn1 col2">3.16</td>
    <td class="tdata centeralign modelcolumn1 col3">3.03&nbsp;&ndash;&nbsp;3.29</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">4.00</td>
    <td class="tdata centeralign modelcolumn2 col6">3.87&nbsp;&ndash;&nbsp;4.14</td>
    <td class="tdata centeralign modelcolumn2 col7"><strong>&lt;0.001</strong></td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">National Attachment<br>(Mean-Centered)</td>
    <td class="tdata centeralign modelcolumn1 col2">&#45;0.05</td>
    <td class="tdata centeralign modelcolumn1 col3">&#45;0.05&nbsp;&ndash;&nbsp;-0.04</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">0.01</td>
    <td class="tdata centeralign modelcolumn2 col6">0.01&nbsp;&ndash;&nbsp;0.02</td>
    <td class="tdata centeralign modelcolumn2 col7"><strong>&lt;0.001</strong></td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">European Attachment<br>(Mean-Centered)</td>
    <td class="tdata centeralign modelcolumn1 col2">0.05</td>
    <td class="tdata centeralign modelcolumn1 col3">0.04&nbsp;&ndash;&nbsp;0.05</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">0.03</td>
    <td class="tdata centeralign modelcolumn2 col6">0.03&nbsp;&ndash;&nbsp;0.04</td>
    <td class="tdata centeralign modelcolumn2 col7"><strong>&lt;0.001</strong></td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">left-right scale</td>
    <td class="tdata centeralign modelcolumn1 col2">&#45;0.04</td>
    <td class="tdata centeralign modelcolumn1 col3">&#45;0.04&nbsp;&ndash;&nbsp;-0.03</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">&#45;0.03</td>
    <td class="tdata centeralign modelcolumn2 col6">&#45;0.03&nbsp;&ndash;&nbsp;-0.02</td>
    <td class="tdata centeralign modelcolumn2 col7"><strong>&lt;0.001</strong></td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">Age</td>
    <td class="tdata centeralign modelcolumn1 col2">&#45;0.00</td>
    <td class="tdata centeralign modelcolumn1 col3">&#45;0.00&nbsp;&ndash;&nbsp;-0.00</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">&#45;0.00</td>
    <td class="tdata centeralign modelcolumn2 col6">&#45;0.00&nbsp;&ndash;&nbsp;-0.00</td>
    <td class="tdata centeralign modelcolumn2 col7"><strong>&lt;0.001</strong></td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">Gender: gndr2</td>
    <td class="tdata centeralign modelcolumn1 col2">0.07</td>
    <td class="tdata centeralign modelcolumn1 col3">0.04&nbsp;&ndash;&nbsp;0.09</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">&#45;0.03</td>
    <td class="tdata centeralign modelcolumn2 col6">&#45;0.05&nbsp;&ndash;&nbsp;-0.01</td>
    <td class="tdata centeralign modelcolumn2 col7"><strong>0.009</strong></td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">Years of education</td>
    <td class="tdata centeralign modelcolumn1 col2">0.02</td>
    <td class="tdata centeralign modelcolumn1 col3">0.02&nbsp;&ndash;&nbsp;0.03</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">0.02</td>
    <td class="tdata centeralign modelcolumn2 col6">0.02&nbsp;&ndash;&nbsp;0.02</td>
    <td class="tdata centeralign modelcolumn2 col7"><strong>&lt;0.001</strong></td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">Feeling about household's<br>income</td>
    <td class="tdata centeralign modelcolumn1 col2">&#45;0.09</td>
    <td class="tdata centeralign modelcolumn1 col3">&#45;0.11&nbsp;&ndash;&nbsp;-0.08</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">&#45;0.03</td>
    <td class="tdata centeralign modelcolumn2 col6">&#45;0.05&nbsp;&ndash;&nbsp;-0.02</td>
    <td class="tdata centeralign modelcolumn2 col7"><strong>&lt;0.001</strong></td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">Urban/rural living space:<br>domicil2</td>
    <td class="tdata centeralign modelcolumn1 col2">&#45;0.08</td>
    <td class="tdata centeralign modelcolumn1 col3">&#45;0.13&nbsp;&ndash;&nbsp;-0.04</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">0.08</td>
    <td class="tdata centeralign modelcolumn2 col6">0.03&nbsp;&ndash;&nbsp;0.12</td>
    <td class="tdata centeralign modelcolumn2 col7"><strong>&lt;0.001</strong></td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">Urban/rural living space:<br>domicil3</td>
    <td class="tdata centeralign modelcolumn1 col2">&#45;0.16</td>
    <td class="tdata centeralign modelcolumn1 col3">&#45;0.19&nbsp;&ndash;&nbsp;-0.13</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">&#45;0.02</td>
    <td class="tdata centeralign modelcolumn2 col6">&#45;0.05&nbsp;&ndash;&nbsp;0.01</td>
    <td class="tdata centeralign modelcolumn2 col7">0.231</td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">Urban/rural living space:<br>domicil4</td>
    <td class="tdata centeralign modelcolumn1 col2">&#45;0.21</td>
    <td class="tdata centeralign modelcolumn1 col3">&#45;0.25&nbsp;&ndash;&nbsp;-0.18</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">&#45;0.03</td>
    <td class="tdata centeralign modelcolumn2 col6">&#45;0.06&nbsp;&ndash;&nbsp;0.00</td>
    <td class="tdata centeralign modelcolumn2 col7">0.078</td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">Urban/rural living space:<br>domicil5</td>
    <td class="tdata centeralign modelcolumn1 col2">&#45;0.33</td>
    <td class="tdata centeralign modelcolumn1 col3">&#45;0.39&nbsp;&ndash;&nbsp;-0.26</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">0.02</td>
    <td class="tdata centeralign modelcolumn2 col6">&#45;0.04&nbsp;&ndash;&nbsp;0.08</td>
    <td class="tdata centeralign modelcolumn2 col7">0.488</td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">Trust in politicians</td>
    <td class="tdata centeralign modelcolumn1 col2">0.05</td>
    <td class="tdata centeralign modelcolumn1 col3">0.05&nbsp;&ndash;&nbsp;0.06</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">0.00</td>
    <td class="tdata centeralign modelcolumn2 col6">&#45;0.00&nbsp;&ndash;&nbsp;0.01</td>
    <td class="tdata centeralign modelcolumn2 col7">0.701</td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">Energy affordability<br>worries</td>
    <td class="tdata centeralign modelcolumn1 col2">&#45;0.06</td>
    <td class="tdata centeralign modelcolumn1 col3">&#45;0.08&nbsp;&ndash;&nbsp;-0.05</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">0.05</td>
    <td class="tdata centeralign modelcolumn2 col6">0.04&nbsp;&ndash;&nbsp;0.06</td>
    <td class="tdata centeralign modelcolumn2 col7"><strong>&lt;0.001</strong></td>
</tr>
  <tr>
    <td class="tdata firsttablecol col1">atchctr_c:atcherp_c</td>
    <td class="tdata centeralign modelcolumn1 col2">&#45;0.01</td>
    <td class="tdata centeralign modelcolumn1 col3">&#45;0.01&nbsp;&ndash;&nbsp;-0.00</td>
    <td class="tdata centeralign modelcolumn1 col4"><strong>&lt;0.001</strong></td>
    <td class="tdata centeralign modelcolumn2 col5">&#45;0.00</td>
    <td class="tdata centeralign modelcolumn2 col6">&#45;0.00&nbsp;&ndash;&nbsp;0.00</td>
    <td class="tdata centeralign modelcolumn2 col7">0.544</td>
</tr>
  <tr>
    <td colspan="7" class="randomparts">Random Effects</td>
  </tr>

  <tr>
    <td class="tdata leftalign summary">&sigma;<sup>2</sup></td>
    <td class="tdata summary summarydata" colspan="3">1.39</td>
    <td class="tdata summary summarydata" colspan="3">1.09</td>
  </tr>

  <tr>
    <td class="tdata leftalign summary">&tau;<sub>00</sub></td>
    <td class="tdata summary summarydata" colspan="3">0.05 <sub>cntry</sub></td>
    <td class="tdata summary summarydata" colspan="3">0.06 <sub>cntry</sub></td>

  <tr>
    <td class="tdata leftalign summary">ICC</td>
    <td class="tdata summary summarydata" colspan="3">0.03</td>
    <td class="tdata summary summarydata" colspan="3">0.06</td>

  <tr>
    <td class="tdata leftalign summary">N</td>
    <td class="tdata summary summarydata" colspan="3">23 <sub>cntry</sub></td>
    <td class="tdata summary summarydata" colspan="3">23 <sub>cntry</sub></td>
  <tr>
    <td class="tdata leftalign summary firstsumrow">Observations</td>
    <td class="tdata summary summarydata firstsumrow" colspan="3">35949</td>
    <td class="tdata summary summarydata firstsumrow" colspan="3">35949</td>
  </tr>
  <tr>
    <td class="tdata leftalign summary">Marginal R<sup>2</sup> / Conditional R<sup>2</sup></td>
    <td class="tdata summary summarydata" colspan="3">0.069 / 0.100</td>
    <td class="tdata summary summarydata" colspan="3">0.028 / 0.082</td>
  </tr>

