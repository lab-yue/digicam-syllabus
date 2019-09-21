<template>
  <syllabus-layout>
    <v-card width="1500" class="mx-auto teacher-title">
      <v-card-title>
        All
        <span class="teacher-length">{{ teachers.length }}</span>
        Teachers
        <v-spacer />
        <v-text-field v-model="searchText" append-icon="search" label="名前検索"></v-text-field>
      </v-card-title>
      <syllabus-card :links="teachers" :card_col="4" />
    </v-card>
  </syllabus-layout>
  <!--
  <syllabus-layout class="teacher">
    <h1 class="syllabus-page-title">
      All
      <span class="syllabus-page-title-count">{{ teachers.length }}</span>Teachers
    </h1>

    <input class="syllabus-input" placeholder="名前検索" v-model="searchText" />

    <transition-group name="syllabus-tags" tag="nav">
      <syllabus-button :link="link" v-for="link in teachers" :key="link.name" />
    </transition-group>
  </syllabus-layout>
  -->
</template>

<script>
import SyllabusCard from "../components/SyllabusCard";

export default {
  metaInfo: {
    title: "Teachers"
  },
  data() {
    return {
      page_col: 4,
      searchText: ""
    };
  },
  computed: {
    teachers() {
      let teachers = this.$page.allTeacher.edges.map(edge => {
        const { name, id, subjects } = edge.node;
        return {
          extra: subjects.totalCount,
          name,
          url: `/teacher/${id}`
        };
      });

      if (this.searchText) {
        teachers = teachers.filter(teacher =>
          teacher.name.includes(this.searchText)
        );
      }
      return teachers;
    }
  },
  components: {
    SyllabusCard
  }
};
</script>

<page-query>
query {
  allTeacher {
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
.teacher {
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
