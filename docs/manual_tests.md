# Pruebas manuales (sugeridas)

| Id  | Acción                                          | Esperado                                        | Resultado Obtenido                               | Fallo o Éxito |
|-----|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|---------------|
| T01 | Crear evento único                              | Aparece al listar                               | Aparece al listar                               | Éxito         |
| T02 | Crear duplicado (misma (nombre,fecha,categoría))| Rechazo con mensaje                             | Rechazo con mensaje                             | Éxito         |
| T03 | Editar cambiando a clave compuesta duplicada    | Rechazo                                         | Rechazo                                         | Éxito         |
| T04 | Filtro por nombre "charla"                      | Solo nombres que contengan "charla"             | Solo nombres que contengan "charla"             | Éxito         |
| T05 | Filtro por fecha 2025-02-20                     | Solo esa fecha                                  | Solo esa fecha                                  | Éxito         |
| T06 | Filtro por categoría "charlas"                  | Solo esa categoría                              | Solo esa categoría                              | Éxito         |
| T07 | Vender con cupos>0                              | Disminuye en 1                                  | Disminuye en 1                                  | Éxito         |
| T08 | Vender con cupos=0                              | Rechazo                                         | Rechazo                                         | Éxito         |
| T09 | Devolver con cupos<cupos_max                    | Aumenta en 1                                    | Aumenta en 1                                    | Éxito         |
| T10 | Devolver con cupos==cupos_max                   | Rechazo                                         | Rechazo                                         | Éxito         |
| T11 | Reporte                                         | Total, suma de cupos y agotados correctos       | Total, suma de cupos y agotados correctos       | Éxito         |