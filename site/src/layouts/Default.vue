<template>
  <div class="layout">
    <header class="header">
      <g-link class="header-link" to="/">Syllabus</g-link>
      <g-link class="header-link" to="/subject">Subject</g-link>
      <g-link class="header-link" to="/teacher">Teacher</g-link>
      <g-link class="header-link" to="/category">Category</g-link>
      <g-link class="header-link" to="/field">Field</g-link>
    </header>
    <transition name="fade" appear>
      <main>
        <slot />
      </main>
    </transition>
  </div>
</template>

<static-query>
query {
  metaData {
    siteName
  }
}
</static-query>

<style lang="scss">
body {
  font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, sans-serif;
  margin: 0;
  padding: 0;
  line-height: 1.5;
}
ul {
  padding: 0;
  list-style: none;
}
a {
  text-decoration: none;
  color: inherit;
}
.layout {
  margin: 0 auto;
  padding-left: 20px;
  padding-right: 20px;
}
.header {
  margin-top: 1rem;
  &-link {
    color: $theme-green;
    font-size: 1.2rem;
    &:not(:last-child):after {
      content: " / ";
      color: $theme-light-green;
    }
  }
}
.fade-enter-active {
  transition: opacity 0.5s;
}

.fade-enter {
  opacity: 0;
}
</style>
