<script>
export default {
  props: {
    cheaper: Boolean,
    faster: Boolean,
    trip: Object,
  },
  computed: {
    isCheaperAndFaster() {
      return this.cheaper && this.faster;
    },
  },
};
</script>

<template>
  <div id="container">
    <div v-if="isCheaperAndFaster" class="tripContainer">
      <!--content if cheapest and fastest-->
      <div id="twoIcons">
        <img
          src="../assets/hand-coins-white.svg"
          alt="cheaper icon"
          id="icon1"
        />
        <div id="divider"></div>
        <img
          src="../assets/clock-clockwise.svg"
          alt="cheaper icon"
          id="icon2"
        />
      </div>
      <div class="tripInfo">
        <span class="tripCompanion">
          {{ trip.name }}
        </span>
        <div class="tripDuration">Tempo estimado: {{ trip.duration }}h</div>
      </div>
      <div class="tripPrice">
        Convencional R${{ trip.price_econ }} <br />
        Leito: R${{ trip.price_confort }}
      </div>
    </div>

    <div v-else-if="cheaper" class="tripContainer">
      <!-- content if cheapest -->
      <div class="icon">
        <img src="../assets/hand-coins-white.svg" alt="cheaper icon" />
        +barato
      </div>
      <div class="tripInfo">
        <span class="tripCompanion">
          {{ trip.name }}
        </span>
        <div class="tripDuration">Tempo estimado: {{ trip.duration }}h</div>
      </div>
      <div class="tripPrice">
        Convencional R${{ trip.price_econ }} <br />
        Leito: R${{ trip.price_confort }}
      </div>
    </div>

    <div v-else-if="faster" class="tripContainer">
      <!-- content if faster -->
      <div class="icon">
        <img src="../assets/clock-clockwise.svg" alt="faster icon" />
        +rapido
      </div>
      <div class="tripInfo">
        <span class="tripCompanion">
          {{ trip.name }}
        </span>
        <div class="tripDuration">Tempo estimado: {{ trip.duration }}h</div>
      </div>
      <div class="tripPrice">
        Convencional R${{ trip.price_econ }} <br />
        Leito: R${{ trip.price_confort }}
      </div>
    </div>
  </div>
</template>

<style scoped>
#container {
  display: flex;
  flex-direction: row;
  background-color: #e3e2e3;
  width: 100%;
  border-radius: 1rem;
  margin-left: 1rem;
  margin-top: 1rem;
}

.tripContainer {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  align-items: center;
  width: 100%;
  #twoIcons {
    border-top-left-radius: 1rem;
    border-bottom-left-radius: 1rem;
    position: relative;
    width: 70px;
    height: 70px;
    margin-left: 0;
    background-color: #04a8b5;
  }
  .icon {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-top-left-radius: 1rem;
    border-bottom-left-radius: 1rem;
    width: 70px;
    height: 70px;
    margin-left: 0;
    background-color: #04a8b5;
    color: white;
  }
  .tripInfo {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 0.5rem;
    .tripCompanion {
      font-family: sans-serif;
      font-weight: 700;
      font-size: 1rem;
    }
  }
  .tripPrice {
    margin-right: 1rem;
  }
}
#icon1 {
  position: absolute;
  top: 5;
  padding: 0.3rem;
  left: 1;
}

#icon2 {
  position: absolute;
  padding: 0.3rem;
  bottom: 0;
  right: 0;
}
#divider {
  position: absolute;
  height: 2px;
  width: 80%;
  top: 50%;
  left: 15%;
  background: #fff;
  transform: rotate(-45deg);
}
@media (max-width: 1039px) {
  #container {
    flex-direction: column;
  }
  .tripContainer {
    flex-direction: column;
  }
  #twoIcons {
    border-radius: 1rem;
  }
  * {
    text-align: center;
  }
}
</style>
