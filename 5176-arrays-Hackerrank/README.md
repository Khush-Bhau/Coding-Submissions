# [Arrays](https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true)
## Easy
<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The <em>NumPy</em> (Numeric Python) package helps us manipulate large arrays and matrices of numeric data. </p>

<p>To use the <em>NumPy</em> module, we need to import it using:</p>

<pre><code>import numpy
</code></pre>

<p><a href="http://docs.scipy.org/doc/numpy/reference/arrays.html"><strong>Arrays</strong></a>  </p>

<p>A <em>NumPy</em> array is a grid of values. They are similar to lists, except that every element of an array must be the same type. </p>

<pre><code>import numpy

a = numpy.array([1,2,3,4,5])
print a[1]          #2

b = numpy.array([1,2,3,4,5],float)
print b[1]          #2.0
</code></pre>

<p>In the above example, <code>numpy.array()</code> is used to convert a list into a <em>NumPy</em> array. The second argument (float) can be used to set the type of array elements.</p>

<hr>

<p><strong>Task</strong>  </p>

<p>You are given a space separated list of numbers. <br>
Your task is to print a reversed <em>NumPy</em> array with the element type <code>float</code>.</p></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>A single line of input containing space separated numbers.</p></div></div></div><div class="challenge_output_format"><div class="msB challenge_output_format_title"><p><strong>Output Format</strong></p></div><div class="msB challenge_output_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>Print the reverse <em>NumPy</em> array with type float.</p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>1 2 3 4 -8 -10
</code></pre></div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>[-10.  -8.   4.   3.   2.   1.]
</code></pre></div></div></div></div>