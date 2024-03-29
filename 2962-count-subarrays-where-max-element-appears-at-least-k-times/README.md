<h2><a href="https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/">2962. Count Subarrays Where Max Element Appears at Least K Times</a></h2><h3>Medium</h3><hr><div element-id="830"><p element-id="829">You are given an integer array <code element-id="828">nums</code> and a <strong element-id="827">positive</strong> integer <code element-id="826">k</code>.</p>

<p element-id="825">Return <em element-id="824">the number of subarrays where the <strong element-id="823">maximum</strong> element of </em><code element-id="822">nums</code><em element-id="821"> appears <strong element-id="820">at least</strong> </em><code element-id="819">k</code><em element-id="818"> times in that subarray.</em></p>

<p element-id="817">A <strong element-id="816">subarray</strong> is a contiguous sequence of elements within an array.</p>

<p element-id="815">&nbsp;</p>
<p element-id="814"><strong class="example" element-id="813">Example 1:</strong></p>

<pre element-id="812"><strong element-id="811">Input:</strong> nums = [1,3,2,3,3], k = 2
<strong element-id="810">Output:</strong> 6
<strong element-id="809">Explanation:</strong> The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
</pre>

<p element-id="808"><strong class="example" element-id="807">Example 2:</strong></p>

<pre element-id="806"><strong element-id="805">Input:</strong> nums = [1,4,2,1], k = 3
<strong element-id="804">Output:</strong> 0
<strong element-id="803">Explanation:</strong> No subarray contains the element 4 at least 3 times.
</pre>

<p element-id="802">&nbsp;</p>
<p element-id="801"><strong element-id="800">Constraints:</strong></p>

<ul element-id="799">
	<li element-id="798"><code element-id="797">1 &lt;= nums.length &lt;= 10<sup element-id="796">5</sup></code></li>
	<li element-id="795"><code element-id="794">1 &lt;= nums[i] &lt;= 10<sup element-id="793">6</sup></code></li>
	<li element-id="792"><code element-id="791">1 &lt;= k &lt;= 10<sup element-id="790">5</sup></code></li>
</ul>
</div>