<template>
  <div>
    <v-navigation-drawer v-model="drawer" app temporary>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="nav-title">DHU Syllabus</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list>
        <g-link v-for="item in items" :key="item.title" :to="item.link">
          <v-list-item link>
            <v-list-item-icon class="nav-icon">
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </g-link>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar elevate-on-scroll app color="#fafafa">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Syllabus</v-toolbar-title>
      <v-spacer></v-spacer>
      <syllabus-search />
    </v-app-bar>
  </div>
  <!--
  <header class="header">
    <nav>
      <g-link class="header-link" to="/">Syllabus</g-link>
      <g-link class="header-link" to="/subject">Subject</g-link>
      <g-link class="header-link" to="/teacher">Teacher</g-link>
      <g-link class="header-link" to="/category">Category</g-link>
      <g-link class="header-link" to="/field">Field</g-link>
      <g-link class="header-link" to="/email">Email</g-link>
    </nav>
    <syllabus-search />
  </header>
  -->
</template>

<script>
import SyllabusMenu from "./SyllabusMenu";
import SyllabusSearch from "./SyllabusSearch";
export default {
  props: [],
  data() {
    return {
      drawer: false,
      items: [
        { title: "Syllabus", link: "/", icon: "home" },
        { title: "Subject", link: "/subject", icon: "subject" },
        { title: "Teacher", link: "/teacher", icon: "emoji_people" },
        { title: "Category", link: "/category", icon: "category" },
        { title: "Field", link: "/field", icon: "border_all" },
        { title: "Email", link: "/email", icon: "email" }
      ]
    };
  },
  components: {
    SyllabusSearch,
    SyllabusMenu
  }
};
</script>

<style lang="scss" scoped>
.nav {
  &-icon {
    margin-right: 30px;
  }
  &-title {
    margin-top: 50px;
    font-size: 1.5em;
  }
}
/*
.header {
  margin-top: 1rem;
  display: flex;
  justify-content: space-between;
  &-link {
    color: $theme-green;
    font-size: 1.2rem;
    &:not(:last-child):after {
      content: " / ";
      color: $theme-light-green;
    }
  }
}
*/
</style>
