# character-personality-catcher
<h3>Testing IBM BlueMix NLP Service on a Fictional First-Person Novel Character</h3>

This is support code for a medium article publication:
https://medium.com/@shahamfarooq/who-is-holden-caulfield-aa5ef13005bc#.ek8o9mjq3

<p>The code supports analysis by retrieving a personality tree from IBM BlueMix NLP service and charting it on plots using the Big Five Model.</p>

<h3>To use this code:</h3>
<ol>
  <li>Replace username, password strings with your credentials in retrieve_personality.py</li>
  <li>The text_edit.py is very specific to separating chapters for The Catcher in the Rye, you will have to replace that with a function of your own that can separate your choice of input text by chapters.</li>
  <li>Once your novel is separated by chapters, run retrieve_personality.py to save personality tree in bin.dat (sample has been provided)</li>
  <li>Run chart_personality.py to create the charts (samples provided in plot/ directory)</li>
</ol>
