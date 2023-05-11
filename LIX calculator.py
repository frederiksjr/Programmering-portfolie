#LIX calculator

a = calcA(t);
if (a == 0) {
    putLIX("The text must contain at least one word.");
    putRead("");
    return null;
}

b = calcB(t);
if (b == 0) {
    PutLIX("The text must contain at least one period or other sentence separator.");
    putRead("");
    return null;
}

c = calcC(t);

lix = a / b + c * 100 / a;
lix = floor(lix + 0.5);
putLIX("The LIX score of the text is " + lix + ".");


if (lix >= 55) {
    putRead("Difficulty: Very hard.");
    return null;
  }
  
if (lix >= 45) {
    putRead("Difficulty: Hard.");
    return null;
  }
  
if (lix >= 35) {
    putRead("Difficulty: Average.");
    return null;
  }
  
if (lix >= 25) {
    putRead("Difficulty: Easy.");
    return null;
  }
  
putRead("Difficulty: Very easy.");


function calcA(t) {
 m = t.match(/[æøå\w]+/g);
  if (m === null) {
    return 0;
  } else {
    return m.length;
  }
}

function calcB(t) {
  m = t.match(/[.:;!?]+/g);
  if (m === null) {
    return 0;
  } else {
    return m.length;
  }
}

function calcC(t) {
  m = t.match(/[æøå\w]{6}[æøå\w]*\b/g);
  if (m === null) {
    return 0;
  } else {
    return m.length;
  }
}

function putLIX(message) {
  lix = select('#LIX');
  lix.html(message);
}

function putRead(message) {
  readability = select('#readability');
  readability.html(message);
}

calculate(jeg plukker frugt med en brugt frugt plukker.)