<h2><a href="https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/">1985. Find the Kth Largest Integer in the Array</a></h2><h3>Medium</h3><hr><div element-id="484"><p element-id="483">You are given an array of strings <code element-id="482">nums</code> and an integer <code element-id="481">k</code>. Each string in <code element-id="480">nums</code> represents an integer without leading zeros.</p>

<p element-id="479">Return <em element-id="478">the string that represents the </em><code element-id="477">k<sup element-id="476">th</sup></code><em element-id="475"><strong element-id="474"> largest integer</strong> in </em><code element-id="473">nums</code>.</p>

<p element-id="472"><strong element-id="471">Note</strong>: Duplicate numbers should be counted distinctly. For example, if <code element-id="470">nums</code> is <code element-id="469">["1","2","2"]</code>, <code element-id="468">"2"</code> is the first largest integer, <code element-id="467">"2"</code> is the second-largest integer, and <code element-id="466">"1"</code> is the third-largest integer.</p>

<p element-id="465">&nbsp;</p>
<p element-id="464"><strong class="example" element-id="463">Example 1:</strong></p>

<pre element-id="462"><strong element-id="461">Input:</strong> nums = ["3","6","7","10"], k = 4
<strong element-id="460">Output:</strong> "3"
<strong element-id="459">Explanation:</strong>
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4<sup element-id="458">th</sup> largest integer in nums is "3".
</pre>

<p element-id="457"><strong class="example" element-id="456">Example 2:</strong></p>

<pre element-id="455"><strong element-id="454">Input:</strong> nums = ["2","21","12","1"], k = 3
<strong element-id="453">Output:</strong> "2"
<strong element-id="452">Explanation:</strong>
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3<sup element-id="451">rd</sup> largest integer in nums is "2".
</pre>

<p element-id="450"><strong class="example" element-id="449">Example 3:</strong></p>

<pre element-id="448"><strong element-id="447">Input:</strong> nums = ["0","0"], k = 2
<strong element-id="446">Output:</strong> "0"
<strong element-id="445">Explanation:</strong>
The numbers in nums sorted in non-decreasing order are ["0","0"].
The 2<sup element-id="444">nd</sup> largest integer in nums is "0".
</pre>

<p element-id="443">&nbsp;</p>
<p element-id="442"><strong element-id="441">Constraints:</strong></p>

<ul element-id="440">
	<li element-id="439"><code element-id="438">1 &lt;= k &lt;= nums.length &lt;= 10<sup element-id="437">4</sup></code></li>
	<li element-id="436"><code element-id="435">1 &lt;= nums[i].length &lt;= 100</code></li>
	<li element-id="434"><code element-id="433">nums[i]</code> consists of only digits.</li>
	<li element-id="432"><code element-id="431">nums[i]</code> will not have any leading zeros.</li>
</ul>
</div>