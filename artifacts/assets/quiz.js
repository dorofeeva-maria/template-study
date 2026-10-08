/* Self-check quiz for theory artifacts. Marks the learner's choice right or wrong — nothing else:
   it never reveals the right option and never explains. Options are shuffled on every load, so
   their position carries no clue.

   Markup (options of equal length and form; exactly one has data-correct):
     <div class="quiz">
       <div class="qq">
         <p class="qq-text">Question?</p>
         <ul class="opts">
           <li data-correct>Option text</li>
           <li>Option text</li>
         </ul>
       </div>
     </div>
*/
(function () {
  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function build(quiz) {
    var originals = quiz.__originals || (quiz.__originals = Array.prototype.map.call(
      quiz.querySelectorAll(".qq"), function (q) { return q.cloneNode(true); }));
    quiz.innerHTML = "";
    var answered = 0, right = 0, total = originals.length;
    var bar = document.createElement("div");
    bar.className = "bar";
    var score = document.createElement("span");
    var again = document.createElement("button");
    again.type = "button";
    again.textContent = "↻";
    again.title = "Start over (reshuffles)";
    again.onclick = function () { build(quiz); };
    bar.appendChild(score); bar.appendChild(again);

    function update() { score.textContent = answered + " / " + total + " answered · " + right + " right"; }

    originals.forEach(function (orig) {
      var q = orig.cloneNode(true);
      var list = q.querySelector(".opts");
      var items = shuffle(Array.prototype.slice.call(list.children));
      list.innerHTML = "";
      var verdict = document.createElement("div");
      verdict.className = "verdict";
      var buttons = [];
      items.forEach(function (li) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "opt";
        b.innerHTML = li.innerHTML;
        var correct = li.hasAttribute("data-correct");
        b.onclick = function () {
          buttons.forEach(function (x) { x.disabled = true; });
          b.classList.add(correct ? "right" : "wrong");
          verdict.textContent = correct ? "✓ right" : "✗ wrong";
          answered++; if (correct) right++;
          update();
        };
        buttons.push(b);
        var wrapLi = document.createElement("li");
        wrapLi.appendChild(b);
        list.appendChild(wrapLi);
      });
      q.appendChild(verdict);
      quiz.appendChild(q);
    });
    quiz.appendChild(bar);
    update();
  }

  document.addEventListener("DOMContentLoaded", function () {
    Array.prototype.forEach.call(document.querySelectorAll(".quiz"), build);
  });
})();
