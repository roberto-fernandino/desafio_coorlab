<script>
export default {
  data() {
    return {
      showOtherComponent: false,
    };
  },
  methods: {
    onCalcClick() {
      this.$emit("calcClicked");
    },
  },
};
</script>

<template>
  <div id="sidebarContainer">
    <div id="logo">
      <img src="../assets/logo.png" alt="Imagem Logo" />
    </div>
    <div id="optionsContainer">
      <div id="calc" @click="onCalcClick">
        <img
          id="calcIcon"
          src="../assets/calculator.svg"
          alt="Calculadora Icone"
        />
        <span id="calcText">Calculadora de viagens</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
#sidebarContainer {
  max-width: 20rem;
  padding: 0.5rem;
  height: 100vh;
  background-color: #2b2f42;
}
#logo {
  padding: 0.8rem;
  img {
    max-width: 100%;
  }
}
#calc {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: center;
  margin-top: 7rem;
  padding-left: 0.3rem;

  &:hover {
    cursor: pointer;
  }

  #calcText {
    font-size: 1.4rem;
    font-weight: bold;
    text-align: center;
    font-family: sans-serif;
    user-select: none;
    color: white;
    -webkit-touch-callout: none; /* iOS Safari */
    -webkit-user-select: none; /* Safari */
    -khtml-user-select: none; /* Konqueror HTML */
    -moz-user-select: none; /* Old versions of Firefox */
    -ms-user-select: none; /* Internet Explorer/Edge */
    user-select: none; /* Non-prefixed version, currently supported by Chrome, Edge, Opera and Firefox */
  }
}
</style>
