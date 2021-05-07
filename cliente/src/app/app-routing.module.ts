import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FuncionalidadComponent } from './Componentes/funcionalidad/funcionalidad.component';
import { PrincipalComponent } from './Componentes/principal/principal.component';

const routes: Routes = [
  {
    path: "",
    component: PrincipalComponent
  },
  {
    path: "funcionalidad",
    component: FuncionalidadComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
