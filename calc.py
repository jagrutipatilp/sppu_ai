<apex: page controller="TrignometricController">

<apex: form >

<apex: pageBlock >

<apex: pageBlockSection >

<apex: inputText label="Angle" value="{!angle}" />

</apex: pageBlockSection>

<apex: pageBlockButtons >

<apex: commandButton value="Calculate" action="{!calculate}" rerender="results" />

</apex: pageBlockButtons>

<apex: pageBlockSection title="Results" id="results">

<apex:outputText value="Sin: {!sinResult}" /><br/> <apex: outputText value="Cos: {!cosResult}" /><br/>

<apex: outputText value="Tan: (!tanResult}" /><br/>

<apex: outputText value="Cosec: {!cosecResult}" /><br/>

<apex: output Text value="Sec {!secResult)" /><br/>

<apex: outputText value="Cot: {!cotResult}" />

</apex: pageBlockSection>

</apex: pageBlock>

</apex:form>

</apex: page>

trignometric.vfp
public class TrignometricController {

public Double angle { get; set; }

public Double sinResult { get; set; }

public Double 'cosResult { get; set; }

public Double tanResult { get; set; }

public Double cosecResult {get; set;}

public Double secResult { get; set;)

public Double cotResult { get; set;)

public void calculate() {

sinResult Math.sin(angle);

cosResult Math.cos(angle);

tanßesult = Math.tan(angle);

cosecResult = 1/ Math.sin(angle);

secResult =1/ Math.cos(angle);

cotResult -1/ Math.tan(angle);

)

)