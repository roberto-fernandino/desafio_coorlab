<script>
export default {
  methods: {
    emitCleanSignal() {
      this.$emit("clean-error");
    },
  },
};
</script>

<template>
  <div id="container">
    <img src="../assets/warning.svg" alt="Error icone" />
    <span id="text">Escolha as opções pra começar a cotação</span>
    <button id="button" @click="emitCleanSignal">Fechar</button>
  </div>
</template>

<style scoped>
#container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: white;
  padding: 5rem;
  border-radius: 2rem;
  #text {
    font-size: 2rem;
    font-family: sans-serif;
    align-items: center;
  }
  #button {
    background-color: #04a8b5;
    padding: 1rem;
    font-family: sans-serif;
    border: none;
    border-radius: 1rem;
    margin-top: 3rem;
  }
}
</style>
