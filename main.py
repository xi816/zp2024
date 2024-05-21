import sys;
import pygame as pg;

pg.init();

W = 800;
H = 512;

Display = pg.display.set_mode((W, H));
pg.display.set_caption("Знатоки прогаммирования 2024");

clock = pg.time.Clock();
font = pg.font.SysFont("ubuntumono", 30);

WHITE = (0xFF, 0xFF, 0xFF);
BLACK = (0x00, 0x00, 0x00);

kp = set();
kp_keys = ["left shift", "right shift", "right alt", "left meta", "right meta", "caps lock"];

text = [f"{chr(0xA0)}#000000", "Хорошо написанная программа –\nэто программа, написанная нами."];
spec_kbs_ra_EN = {
  "1": "!",
  "2": "@",
  "3": "#",
  "4": "$",
  "5": "%",
  "6": "^",
  "7": "&",
  "8": "*",
  "9": "(",
  "0": ")"
};

spec_kbs_ra_RU = {
  "1": "!",
  "2": "\"",
  "3": "№",
  "4": ";",
  "5": "%",
  "6": ":",
  "7": "?",
  "8": "*",
  "9": "{",
  "0": "}"
};

spec_kbs_ex_TA = {
  "f": "ә",
  ";": "җ",
  "[": "һ",
  "y": "ң",
  "j": "ө",
  "e": "ү",
};

spec_kbs_ex_NB = {
  "q": "ѕ",
  "w": "і",
  "e": "ѵ",
  "r": "ξ",
  "t": "ω",
  "y": "ψ",
  "u": "ѳ",
  "i": "",
  "o": "",
  "p": "`"
};

layout_names = ["EN", "RU", "TA", "NB"];
lay_c = 0;
lay_cur = layout_names[0];

layout_RU = {
  "q": "й", "w": "ц", "e": "у", "r": "к", "t": "е", "y": "н", "u": "г", "i": "ш", "o": "щ", "p": "з",
  "a": "ф", "s": "ы", "d": "в", "f": "а", "g": "п", "h": "р", "j": "о", "k": "л", "l": "д",
  "z": "я", "x": "ч", "c": "с", "v": "м", "b": "и", "n": "т", "m": "ь",
  "[": "х", "]": "ъ",
  ";": "ж", "'": "э",
  ",": "б", ".": "ю", "/": "."
}

layout_NB = {
  "q": "й", "w": "ц", "e": "у", "r": "к", "t": "є", "y": "н", "u": "г", "i": "ћ", "o": "ш", "p": "з",
  "a": "ф", "s": "ї", "d": "в", "f": "а", "g": "п", "h": "р", "j": "о", "k": "л", "l": "д",
  "z": "ѧ", "x": "ч", "c": "с", "v": "м", "b": "и", "n": "т", "m": "ь",
  "[": "х", "]": "ъ",
  ";": "ж", "'": "ѣ",
  ",": "б", ".": "ѫ", "/": "."
}

def format_write(Display, font, text: str):
  x = 10;
  y = 10;
  for i in text:
    if (i == ""):
      continue;
    elif (i[0] == chr(0xA0)):
      ccl = (int(i[2:4], base=16), int(i[4:6], base=16), int(i[6:8], base=16));
    else:
      for j in i:
        if (j == "\n"):
          x = 10;
          y += 40;
        else:
          Display.blit(font.render(j, True, ccl), (x, y));
          x += 16;

while True:
  for ev in pg.event.get():
    if (ev.type == pg.QUIT):
      sys.exit(2);
    elif ((ev.type == pg.KEYDOWN)):
      ckey = pg.key.name(ev.key);
      if (ckey in kp_keys):
        kp.add(ckey);
      if (ckey == "backspace"):
        if (text[-1]):
          text[-1] = text[-1][:-1];
        else:
          text = text[:-2];
          if (not text):
            text = [f"{chr(0xA0)}#000000", ""];
      elif (ckey == "return"):
        text[-1] += "\n";
      elif (len(ckey) == 1):
        if (lay_cur == "EN"):
          if ((ckey == "1") and ("right shift" in kp)):
            text = [f"{chr(0xA0)}#000000", ""];
          elif ((ckey == "a") and ("right shift" in kp)):
            text += [f"{chr(0xA0)}#FF0000", ""];
          elif ((ckey == "s") and ("right shift" in kp)):
            text += [f"{chr(0xA0)}#00FF00", ""];
          elif ((ckey == "d") and ("right shift" in kp)):
            text += [f"{chr(0xA0)}#0000FF", ""];
          elif ((ckey == "f") and ("right shift" in kp)):
            text += [f"{chr(0xA0)}#000000", ""];
          elif ((ckey == "g") and ("right shift" in kp)):
            text += [f"{chr(0xA0)}#{input('Введите цвет (без `#`): ')}", ""];
        if ((ckey in spec_kbs_ra_EN) and ("left shift" in kp)):
          text[-1] += spec_kbs_ra_EN[ckey];
        elif ((ckey in spec_kbs_ex_TA) and ("right shift" in kp) and (lay_cur == "TA")):
          text[-1] += spec_kbs_ex_TA[ckey];
        elif ((ckey in spec_kbs_ex_NB) and ("right shift" in kp) and (lay_cur == "NB")):
          text[-1] += spec_kbs_ex_NB[ckey];
        else:
          if (lay_cur == "EN"):
            if ("caps lock" in kp):
              if (ckey.isalpha()):
                text[-1] += ckey.upper();
            else:
              text[-1] += ckey;
          elif (lay_cur == "RU"):
            if ("caps lock" in kp):
              text[-1] += layout_RU.get(ckey.upper());
            else:
              text[-1] += layout_RU.get(ckey);
          elif (lay_cur == "TA"):
            if ("caps lock" in kp):
              text[-1] += layout_RU.get(ckey.upper());
            else:
              text[-1] += layout_RU.get(ckey);
          elif (lay_cur == "NB"):
            if ("caps lock" in kp):
              text[-1] += layout_NB.get(ckey.upper());
            else:
              text[-1] += layout_NB.get(ckey);
      elif (ckey == "space"):
        if ("right shift" in kp):
          lay_c += 1;
          lay_c = (lay_c % len(layout_names));
          lay_cur = layout_names[lay_c];
        else:
          text[-1] += " ";
      print(ckey);
    elif ((ev.type == pg.KEYUP) and (pg.key.name(ev.key) in kp_keys)):
      kp.remove(pg.key.name(ev.key));

  Display.fill(WHITE);
  format_write(Display, font, text); Display.blit(font.render(lay_cur, True, BLACK), (W-38, H-35));
  pg.display.update();
  clock.tick(60);

