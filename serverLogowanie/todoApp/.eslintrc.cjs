/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution')

module.exports = {
  root: true,
  extends: [
    'plugin:vue/vue3-recommended',
    'eslint:recommended',
    '@vue/eslint-config-prettier/skip-formatting',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/eslint-recommended'
  ],
  env: {
    browser: true,
    node: true,
    es6: true
  },
  parserOptions: {
    ecmaVersion: 'latest',
    vueFeatures: {
      filter: true,
      interpolationAsNonHTML: false
    },
    parser: '@typescript-eslint/parser',
    sourceType: 'module'
  },
  plugins: ['@typescript-eslint'],

  parser: 'vue-eslint-parser',

  rules: {
    '@typescript-eslint/no-explicit-any': 'error',
    '@typescript-eslint/no-empty-function': 'error',
    '@typescript-eslint/no-non-null-assertion': 'error',
    'no-useless-escape': 'error',
    'no-use-before-define': 'error',
    '@typescript-eslint/no-use-before-define': 'error',
    '@typescript-eslint/ban-types': 'error',
    '@typescript-eslint/no-unused-vars': [
      'error',
      {
        argsIgnorePattern: '^_',
        varsIgnorePattern: '^_'
      }
    ],
    'no-unused-vars': [
      'error',
      {
        argsIgnorePattern: '^_',
        varsIgnorePattern: '^_'
      }
    ],
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',

    'vue/array-bracket-newline': 'error',
    'vue/array-bracket-spacing': 'error',
    'vue/arrow-spacing': 'error',
    'vue/block-spacing': 'error',
    'vue/brace-style': 'error',
    'vue/camelcase': 'error',
    'vue/comma-dangle': 'error',
    'vue/comma-spacing': 'error',
    'vue/comma-style': 'error',
    'vue/dot-location': 'error',
    'vue/dot-notation': 'error',
    'vue/eqeqeq': 'error',
    'vue/func-call-spacing': 'error',
    'vue/key-spacing': 'error',
    'vue/keyword-spacing': 'error',
    'vue/no-constant-condition': 'error',
    'vue/no-empty-pattern': 'error',
    'vue/no-irregular-whitespace': 'error',
    'vue/no-loss-of-precision': 'error',
    'vue/no-restricted-syntax': 'error',
    'vue/no-sparse-arrays': 'error',
    'vue/no-useless-concat': 'error',
    'vue/object-curly-newline': 'error',
    'vue/object-property-newline': 'error',
    'vue/object-shorthand': 'error',
    'vue/operator-linebreak': 'error',
    'vue/prefer-template': 'error',
    'vue/space-in-parens': 'error',
    'vue/space-infix-ops': 'error',
    'vue/space-unary-ops': 'error',
    'vue/template-curly-spacing': 'error',
    'vue/block-tag-newline': 'error',
    'vue/component-api-style': 'error',
    'vue/component-name-in-template-casing': 'error',
    'vue/component-options-name-casing': 'error',
    'vue/custom-event-name-casing': 'error',
    'vue/define-emits-declaration': 'error',
    'vue/define-macros-order': 'error',
    'vue/define-props-declaration': 'error',
    'vue/html-button-has-type': 'error',
    'vue/html-comment-content-newline': 'error',
    'vue/html-comment-content-spacing': 'error',
    'vue/html-comment-indent': 'error',
    'vue/match-component-file-name': 'error',
    'vue/match-component-import-name': 'error',
    'vue/new-line-between-multi-line-property': 'error',
    'vue/next-tick-style': 'error',
    'vue/no-boolean-default': 'error',
    'vue/no-duplicate-attr-inheritance': 'error',
    'vue/no-empty-component-block': 'error',
    'vue/no-multiple-objects-in-class': 'error',
    'vue/no-potential-component-option-typo': 'error',
    'vue/no-ref-object-destructure': 'error',
    'vue/no-required-prop-with-default': 'error',
    'vue/no-restricted-block': 'error',
    'vue/no-restricted-call-after-await': 'error',
    'vue/no-restricted-class': 'error',
    'vue/no-restricted-component-options': 'error',
    'vue/no-restricted-custom-event': 'error',
    'vue/no-restricted-html-elements': 'error',
    'vue/no-restricted-props': 'error',
    'vue/no-restricted-static-attribute': 'error',
    'vue/no-restricted-v-bind': 'error',
    'vue/no-this-in-before-route-enter': 'error',
    'vue/no-undef-properties': 'error',
    'vue/no-unsupported-features': 'error',
    'vue/no-unused-properties': 'error',
    'vue/no-unused-refs': 'error',
    'vue/no-useless-mustaches': 'error',
    'vue/no-useless-v-bind': 'error',
    'vue/no-v-text': 'error',
    'vue/padding-line-between-blocks': 'error',
    'vue/padding-line-between-tags': 'error',
    'vue/padding-lines-in-component-definition': 'error',
    'vue/prefer-prop-type-boolean-first': 'error',
    'vue/prefer-separate-static-class': 'error',
    'vue/prefer-true-attribute-shorthand': 'error',
    'vue/require-direct-export': 'error',
    'vue/require-emit-validator': 'error',
    'vue/require-expose': 'error',
    'vue/require-name-property': 'error',
    'vue/static-class-names-order': 'error',
    'vue/v-for-delimiter-style': 'error'
  },
  overrides: [
    {
      files: ['**/__tests__/*.{j,t}s?(x)', '**/tests/unit/**/*.spec.{j,t}s?(x)'],
      env: {
        jest: true
      }
    }
  ]
}
