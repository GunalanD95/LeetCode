<h2><a href="https://leetcode.com/problems/subarrays-with-k-different-integers/">992. Subarrays with K Different Integers</a></h2><h3>Hard</h3><hr><div element-id="473"><p element-id="472">Given an integer array <code element-id="471">nums</code> and an integer <code element-id="470">k</code>, return <em element-id="469">the number of <strong element-id="468">good subarrays</strong> of </em><code element-id="467">nums</code>.</p>

<p element-id="466">A <strong element-id="465">good array</strong> is an array where the number of different integers in that array is exactly <code element-id="464">k</code>.</p>

<ul element-id="463">
	<li element-id="462">For example, <code element-id="461">[1,2,3,1,2]</code> has <code element-id="460">3</code> different integers: <code element-id="459">1</code>, <code element-id="458">2</code>, and <code element-id="457">3</code>.</li>
</ul>

<p element-id="456">A <strong element-id="455">subarray</strong> is a <strong element-id="454">contiguous</strong> part of an array.</p>

<p element-id="453">&nbsp;</p>
<p element-id="452"><strong class="example" element-id="451">Example 1:</strong></p>

<pre element-id="450"><strong element-id="449">Input:</strong> nums = [1,2,1,2,3], k = 2
<strong element-id="448">Output:</strong> 7
<strong element-id="447">Explanation:</strong> Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
</pre>

<p element-id="446"><strong class="example" element-id="445">Example 2:</strong></p>

<pre element-id="444"><strong element-id="443">Input:</strong> nums = [1,2,1,3,4], k = 3
<strong element-id="442">Output:</strong> 3
<strong element-id="441">Explanation:</strong> Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
</pre>

<p element-id="440">&nbsp;</p>
<p element-id="439"><strong element-id="438">Constraints:</strong></p>

<ul element-id="437">
	<li element-id="436"><code element-id="435">1 &lt;= nums.length &lt;= 2 * 10<sup element-id="434">4</sup></code></li>
	<li element-id="433"><code element-id="432">1 &lt;= nums[i], k &lt;= nums.length</code></li>
</ul>
</div>