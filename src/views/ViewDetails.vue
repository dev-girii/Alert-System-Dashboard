<template>
  <div>
    <h2>Viewing Details for: {{ tender }}</h2>
    <!-- You can now load content based on this -->
  </div>
</template>

<script>
export default {
  props: ['tender'], // tender will be "tntenders" or "aptenders"

  mounted() {
    // You can fetch data based on this.tender
    console.log("Viewing:", this.tender);
  }
}
</script>
