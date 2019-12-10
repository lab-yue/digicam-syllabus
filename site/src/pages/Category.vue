<template>
  <syllabus-layout>
    <v-card width="1500" class="mx-auto category-title">
      <v-card-title>
        All
        <span class="category-length">{{ categories.length }}</span>
        Categories
        <v-spacer />
        <v-text-field v-model="searchText" append-icon="search" label="カテゴリ検索"></v-text-field>
      </v-card-title>
      <syllabus-card :links="categories" :card_col="4" />
    </v-card>
  </syllabus-layout>
  <!--
  <syllabus-layout>
    <h2 class="syllabus-page-title">
      All
      <span class="syllabus-page-title-count">{{ categories.length }}</span>
      Categories
    </h2>

    <input
      class="syllabus-input"
      placeholder="カテゴリ検索"
      v-model="searchText"
    />

    <transition-group name="syllabus-tags" tag="nav">
      <syllabus-button :link="link" v-for="link in categories" :key="link.id" />
    </transition-group>
  </syllabus-layout>
  -->
</template>

<script>
import SyllabusCard from "../components/SyllabusCard";

export default {
  metaInfo: {
    title: "Categories"
  },
  data() {
    return {
      page_col: 3,
      searchText: ""
    };
  },
  computed: {
    categories() {
      let items = this.$page.allCategory.edges.map(edge => {
        const { name, id, subjects } = edge.node;
        return {
          id,
          name,
          extra: subjects.totalCount,
          url: `/category/${id}`
        };
      });

      if (this.searchText) {
        items = items.filter(item => item.name.includes(this.searchText));
      }
      return items;
    }
  },
  components: {
    SyllabusCard
  }
};
</script>

<page-query>
query {
  allCategory {
    edges {
      node {
        id
        name
        subjects {
          totalCount
        }
      }
    }
  }
}
</page-query>

<style lang="scss" scoped>
.category {
  &-title {
    padding: 30px 40px;
  }
  &-length {
    margin: 5px;
    font-size: 1.2em;
    color: rgb(0, 147, 226);
  }
}
</style>
