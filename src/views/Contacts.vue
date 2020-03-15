<template>
  <div>
  	<div class="title"><h1>Контакты</h1></div>
    <div class="contacts_block">
      <div class="maps"><iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A208a152bbbb7a3fb3a88349e68ea2f24fbb5207d6fc947d1e293a412c799e7c0&amp;source=constructor" width="686" height="500" frameborder="0"></iframe></div>
      <div class="description">
          <div class="description__text">Вы всегда можете получить  <br> полную информацию по нашим работам</div>
          <div class="description__name">Советский р-н, Новосибирск, <br> Новосибирская обл., 630055</div>
          <div class="description__works"> <span>Режим работы:</span> <br> Пн- Пт с 10:00 до 19:00 <br> Сб 11-16:00, Вс - выходной</div>
          <div class="descrption__tell"><span>Контакты</span> <br> <a href="tel:+78182208010">+7 (8182) 20-80-10</a> <br><a href="tel:+7(960)0028010">+7 (960) 002 80 10</a> </div>
          <div class="description__help">Если возникли вопросы, вы можете  <br> написать нам на электронную почту  <br> <br> <a href="mailto:7knt@mail.ru">7knt@mail.ru</a></div>
      </div> 
    </div>
  </div>
</template>
<style lang="css">
a{
  color: black;
  text-decoration: none;
}
.contacts_block{
  margin-top: 80px;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
.maps{
  flex-basis: 50%;
}
.description{
  flex-basis: 50%;
}
.description__text{
  font-size: 25px;
  margin-bottom: 50px;
}
.description__name{
  font-size: 16px;
  margin-bottom: 50px;
}
.description__works{
  font-size: 20px;
  margin-bottom: 50px;
}
.descrption__tell{
  font-size: 20px;
  margin-bottom: 30px;
}
.description__help{
  font-size: 18px;
}
</style>

<script>

export default {
  data(){
    return {
      
    }

  }
}
</script>