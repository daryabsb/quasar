/** @type {import('tailwindcss').Config} */
const plugin = require("tailwindcss/plugin");
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  mode: "jit",
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        night: "rgba(51,51,51,255)",
        midnight: "rgba(37,37,37,255)",
        milk: "rgba(255,255,255,255)",
        divide: "rgba(89,94,87,255)",
        sky: "rgba(27,161,226,255)",
        stroke: "rgba(82,85,80,255)",
        backdrop: "rgba(71,71,71,255)",
        garden: "rgba(82,212,104,255)",
        sun: "rgba(255,235,59,255)",
      },
      gridTemplateRows: {
        // Simple 12 row grid
        "12": "repeat(12, minmax(0, 1fr))",
        "11": "repeat(11, minmax(0, 1fr))",
        "10": "repeat(10, minmax(0, 1fr))",
        "9": "repeat(9, minmax(0, 1fr))",
        "8": "repeat(8, minmax(0, 1fr))",
        "7": "repeat(7, minmax(0, 1fr))",

        // Complex site-specific row configuration
        // 'layout': '200px minmax(900px, 1fr) 100px',
      },
      gridRow: {
        "span-7": "span 7 / span 7",
        "span-8": "span 8 / span 8",
        "span-9": "span 9 / span 9",
        "span-10": "span 10 / span 10",
        "span-11": "span 11 / span 11",
        "span-12": "span 12 / span 12",
      },
      gridRowStart: {
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "10",
        "11": "11",
        "12": "12",
      },
      fontFamily: {
        bakersville: ["Baskerville", "serif"],
        montserrat: ["Montserrat", "sans-serif"],
        // bakersvilleItalic: ["Baskerville italic", "serif"],
        //         font-family: 'Baskervville', serif;
        // font-family: 'Montserrat', sans-serif;
      },
    },
  },
  variants: {
    extend: {
      backGroundColor: ["blue"],
    },
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/line-clamp"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/aspect-ratio"),
    plugin(function ({ addVariant }) {
      // addVariant("blue", "&:blue");
      addVariant("blue", ".blue &");
      addVariant("pink", ".pink &");
      addVariant("green", ".green &");
      addVariant("yellow", ".yellow &");
    }),
  ],
};

/**
 * Used for animation when the element is displayed
 * @param maxOutput The larger the maxOutput output, the larger the generated css volume
 */
function createEnterPlugin(maxOutput = 6) {
  const createCss = (index, d = "x") => {
    const upd = d.toUpperCase();
    return {
      [`*> .enter-${d}:nth-child(${index})`]: {
        transform: `translate${upd}(50px)`,
      },
      [`*> .-enter-${d}:nth-child(${index})`]: {
        transform: `translate${upd}(-50px)`,
      },
      [`* > .enter-${d}:nth-child(${index}),* > .-enter-${d}:nth-child(${index})`]: {
        "z-index": `${10 - index}`,
        opacity: "0",
        animation: `enter-${d}-animation 0.4s ease-in-out 0.3s`,
        "animation-fill-mode": "forwards",
        "animation-delay": `${(index * 1) / 10}s`,
      },
    };
  };
  const handler = ({ addBase }) => {
    const addRawCss = {};
    for (let index = 1; index < maxOutput; index++) {
      Object.assign(addRawCss, {
        ...createCss(index, "x"),
        ...createCss(index, "y"),
      });
    }
    addBase({
      ...addRawCss,
      ["@keyframes enter-x-animation"]: {
        to: {
          opacity: "1",
          transform: "translateX(0)",
        },
      },
      ["@keyframes enter-y-animation"]: {
        to: {
          opacity: "1",
          transform: "translateY(0)",
        },
      },
    });
  };
  return { handler };
}
