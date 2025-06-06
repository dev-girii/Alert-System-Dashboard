<template>
    <section class="searchSection">
        <div class="tabSection">
            <div class="criticalTab">
                <i class="fas fa-exclamation-triangle" style="color:crimson"></i>
                <h4>Critical</h4>
            </div>
            <div class="moderateTab">
                <i class="fas fa-exclamation-circle" style="color:orange"></i>
                <h4>Moderate</h4>
            </div>
            <div class="safeTab">
                <i class="fas fa-check-circle" style="color:green"></i>
                <h4>Safe</h4>
            </div>
        </div>
        <div class="search-container">
            <input type="text" placeholder="Search hosts..." />
            <i class="fas fa-search"></i>
        </div>
    </section>
</template>

<style scoped>
.tabSection{
    display: flex;
    justify-content: space-evenly;
}
.tabSection div{
    padding: 10px;
    background-color: #f0f2fa;
    outline: 1px solid #00000057;
    display: flex;
    cursor: pointer;
    gap: 8px;
}

.tabSection div.active{
    background: #becbff;
}
.tabSection div h4{
    font-weight: 400;
}
.searchSection{
    width: 100%;
    display: flex;
    align-content: center;
    justify-content: space-between;
    align-items: center;
    padding: 1.3rem 1rem 1rem 1rem;
}
.search-container {
  display: flex;
  align-items: center;
  background-color: #f0f2fa; /* soft gray background */
  padding: 10px;
  border: 1px solid #00000057; /* light border */
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  transition: box-shadow 0.2s ease-in-out;
  flex: 1 1 250px;
  max-width: 35%;
}

.search-container:hover {
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.search-container i {
  color: #484c54; /* gray-600 */
  margin-right: 0.5rem;
  font-size: 1rem;
}

.search-container input {
  border: none;
  background: transparent;
  color: #111827; /* gray-900 */
  font-size: 0.95rem;
  outline: none;
  width: 100%;
}

.search-container input::placeholder {
  color: #484c54; /* gray-400 */
}

@media (max-width: 600px) {
  /* .search-container {
    width: 100%;
  } */
   .searchSection{
    flex-direction: column;
   }
   .search-container{
    flex: 1 1;
    margin: 2rem;
    max-width: 100%;
   }
}

</style>