/* Self-check quiz for theory artifacts. Marks the learner's choice right or wrong — nothing else:
   it never reveals the right option and never explains. Options are shuffled on every load, so
   their position carries no clue. The key (data-correct) is visible in the page source: this is
   a self-check, not an exam — accepted on purpose.

   Markup (options of equal length and form; exactly one has data-correct, placed at a varying
   position in the source):
     <div class="quiz">
       <div class="qq">
         <p class="qq-text">Question?</p>
         <ul class="opts">
           <li>Option text</li>
           <li data-correct>Option text</li>
           <li>Option text</li>
         </ul>
       </div>
     </div>
   Only .qq blocks inside .quiz are used; anything else there is kept above the questions.
   Labels follow the page's language (<html lang="…">): en and ru built in, English otherwise.
*/
(function () {
  var counter = 0;
  var STRINGS = {
    en: { again: "↻ again", againLabel: "Start the quiz over (options reshuffled)",
          score: function (a, t, r) { return a + " / " + t + " answered · " + r + " right"; },
          right: "✓ right", wrong: "✗ wrong" },
    ru: { again: "↻ заново", againLabel: "Пройти квиз заново (варианты перемешаются)",
          score: function (a, t, r) { return "отвечено " + a + " из " + t + " · верно " + r; },
          right: "✓ верно", wrong: "✗ неверно" }
  };
  var lang = (document.documentElement.lang || "en").toLowerCase().split("-")[0];
  var L = STRINGS[lang] || STRINGS.en;

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function build(quiz) {
    if (!quiz.__originals) {
      quiz.__originals = Array.prototype.map.call(quiz.querySelectorAll(".qq"), function (q) {
        var copy = q.cloneNode(true);
        q.parentNode.removeChild(q);
        return copy;
      });
      quiz.__body = document.createElement("div");
      quiz.appendChild(quiz.__body);
    }
    var body = quiz.__body;
    body.innerHTML = "";
    var originals = quiz.__originals, answered = 0, right = 0, total = originals.length;

    var bar = document.createElement("div");
    bar.className = "bar";
    var score = document.createElement("span");
    score.setAttribute("role", "status");
    score.setAttribute("aria-live", "polite");
    var again = document.createElement("button");
    again.type = "button";
    again.textContent = L.again;
    again.setAttribute("aria-label", L.againLabel);
    again.onclick = function () { build(quiz); };
    bar.appendChild(score); bar.appendChild(again);

    function update() { score.textContent = L.score(answered, total, right); }

    originals.forEach(function (orig) {
      var q = orig.cloneNode(true);
      var id = "qq-" + (++counter);
      var text = q.querySelector(".qq-text");
      if (text) { text.id = id; }
      q.setAttribute("role", "group");
      if (text) { q.setAttribute("aria-labelledby", id); }
      var list = q.querySelector(".opts");
      var items = shuffle(Array.prototype.slice.call(list.children));
      list.innerHTML = "";
      var verdict = document.createElement("div");
      verdict.className = "verdict";
      verdict.setAttribute("role", "status");
      verdict.setAttribute("aria-live", "polite");
      verdict.tabIndex = -1;
      var buttons = [];
      items.forEach(function (li) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "opt";
        b.innerHTML = li.innerHTML;
        b.setAttribute("aria-pressed", "false");
        var correct = li.hasAttribute("data-correct");
        b.onclick = function () {
          buttons.forEach(function (x) { x.disabled = true; });
          b.classList.add(correct ? "right" : "wrong");
          b.setAttribute("aria-pressed", "true");
          verdict.textContent = correct ? L.right : L.wrong;
          answered++; if (correct) { right++; }
          update();
          verdict.focus();
        };
        buttons.push(b);
        var wrapLi = document.createElement("li");
        wrapLi.appendChild(b);
        list.appendChild(wrapLi);
      });
      q.appendChild(verdict);
      body.appendChild(q);
    });
    body.appendChild(bar);
    update();
  }

  function init() { Array.prototype.forEach.call(document.querySelectorAll(".quiz"), build); }
  if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", init); }
  else { init(); }
})();
