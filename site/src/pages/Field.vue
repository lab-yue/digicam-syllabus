<template>
  <syllabus-layout>
    <v-card width="1500" class="mx-auto field-title">
      <v-card-title>
        All
        <span class="field-length">{{ fields.length }}</span>
        Fields
        <v-spacer />
        <v-text-field v-model="searchText" append-icon="search" label="分野名検索"></v-text-field>
      </v-card-title>
      <syllabus-card :links="fields" :card_col="4" />
    </v-card>
  </syllabus-layout>
  <!--
  <syllabus-layout>
    <h2 class="syllabus-page-title">
      All
      <span class="syllabus-page-title-count">{{ fields.length }}</span> Fields
    </h2>

    <input
      class="syllabus-input"
      placeholder="分野名検索"
      v-model="searchText"
    />

    <transition-group name="syllabus-tags" tag="nav">
      <syllabus-button :link="link" v-for="link in fields" :key="link.id" />
    </transition-group>
  </syllabus-layout>
  -->
</template>

<script>
import SyllabusCard from "../components/SyllabusCard";

export default {
  metaInfo: {
    title: "Fields"
  },
  data() {
    return {
      searchText: ""
    };
  },
  computed: {
    fields() {
      let items = this.$page.allField.edges.map(edge => {
        const { name, id, subjects } = edge.node;
        return {
          id,
          name: name,
          extra: subjects.totalCount,
          url: `/field/${id}`
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
  allField {
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
.field {
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
