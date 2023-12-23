module.exports = {
  root: true,
  env: {
    node: true,
    browser: true,
  },
  extends: [
    "eslint:recommended",
    "plugin:vue/recommended",
    "plugin:import/recommended",
    "plugin:prettier-vue/recommended",
  ],
  plugins: ["html"],
  parserOptions: {
    parser: "@typescript-eslint/parser",
  },
  rules: {
    "import/order": [
      "error",
      {
        groups: ["builtin", "external", "internal", ["parent", "sibling"]],
        pathGroups: [
          {
            pattern: "vue+(|-router|x)",
            group: "external",
            position: "before",
          },
          {
            pattern: "**/models/**",
            group: "internal",
            position: "before",
          },
          {
            pattern: "**/stores/**",
            group: "internal",
            position: "before",
          },
          {
            pattern: "**/services/**",
            group: "internal",
            position: "before",
          },
          {
            pattern: "**/mixins/**",
            group: "internal",
            position: "before",
          },
          {
            pattern: "**/views/**",
            group: "internal",
            position: "before",
          },
          {
            pattern: "**/components/**",
            group: "internal",
            position: "before",
          },
          {
            pattern: "**/composables/**",
            group: "internal",
            position: "before",
          },
          {
            pattern: "**/utils/**",
            group: "internal",
            position: "before",
          },
          {
            pattern: "**/assets/**",
            group: "internal",
            position: "after",
          },
        ],
        pathGroupsExcludedImportTypes: ["vue+(|x|tify)"],
        "newlines-between": "always",
        alphabetize: {
          order: "asc",
          caseInsensitive: true,
        },
      },
    ],
    "no-unused-vars": "warn",
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "error" : "off",
    "vue/component-definition-name-casing": ["error", "PascalCase"],
    "vue/component-name-in-template-casing": ["error", "PascalCase"],
    "vue/component-tags-order": [
      "error",
      {
        order: ["template", "script", "style"],
      },
    ],
    "vue/custom-event-name-casing": "error",
    "vue/match-component-file-name": [
      "error",
      {
        extensions: ["vue"],
        shouldMatchCase: true,
      },
    ],
    "vue/max-attributes-per-line": "off",
    "vue/no-deprecated-scope-attribute": "error",
    "vue/no-deprecated-slot-attribute": [
      "error",
      {
        ignore: ["ion-tab-bar"],
      },
    ],
    "vue/no-deprecated-slot-scope-attribute": "error",
    "vue/no-reserved-component-names": "error",
    "vue/no-static-inline-styles": "error",
    "vue/padding-line-between-blocks": "error",
    "vue/require-name-property": "error",
    "vue/valid-v-bind-sync": "error",
    "vue/no-unused-components": "warn",
    "vue/valid-v-slot": "error",
  },
};
