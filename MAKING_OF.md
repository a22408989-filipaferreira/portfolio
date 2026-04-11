# Making Of — Modelação do Portfólio

## V1 — Modelo inicial (DER em papel)

![V1 - DER inicial](images/v1.jpg)

### O que fiz
Comecei por um DER completo em papel onde tentei representar todo o contexto académico:

- Licenciatura  
- Unidade Curricular  
- Docente  
- Projeto  
- Tecnologia  
- Competência  
- Instituição  
- TFC  

### Decisões
- Separei **Projeto** de **TFC**  
- Criei entidades próprias para:
  - Tecnologia  
  - Competência  
- Incluí **Instituição** para contextualizar a licenciatura  

### Problemas encontrados
- Modelo demasiado complexo  
- Muitas relações N:N  
- Difícil de passar diretamente para Django  
- Algumas redundâncias (Projeto vs TFC)  

---

## V2 — Refinamento e reorganização

![V2 - Modelo refinado](images/v2.jpg)

### O que alterei
Na V2 reorganizei o modelo e introduzi o **Profile** como entidade central.

Passei a ter:
- Profile  
- Course  
- Subject  
- Project  
- Tech  
- Skill  
- CapstoneProject  
- Certification  
- WorkExperience  

### Decisões
- `Profile` como centro do sistema  
- Separação entre:
  - percurso académico  
  - percurso profissional  

- Relações principais:
  - Project ↔ Tech (N:N)  
  - Project ↔ Skill (N:N)  
  - Subject ↔ Teacher (N:N)  

### Problemas encontrados
- Modelo ainda complexo  
- Muitas relações N:N  
- Difícil implementação no Django  

---

## V3 — Modelo final (implementação em Django)

![V3 - Modelo final](images/v3.jpg)

### O que fiz
Na V3 simplifiquei o modelo para implementação prática em Django.

### Entidades finais
- `Profile`
- `Course`
- `Subject`
- `Teacher`
- `Tech`
- `Skill`
- `Project`
- `CapstoneProject`
- `Certification`
- `WorkExperience`
- `MakingOf`

### Decisões
- Tradução das entidades:
  - Licenciatura → `Course`
  - UC → `Subject`
  - Docente → `Teacher`

- Separação clara:
  - `Project` → projetos de UC  
  - `CapstoneProject` → TFC  

- Redução de complexidade:
  - uso de `ForeignKey` sempre que possível  
  - manter apenas relações N:N essenciais  

- `MakingOf` associado a:
  - Project  
  - Subject  

### Problemas encontrados

#### 1. Dados inconsistentes
Exemplo:
- `"Semestral"` em vez de número  

Resolvido com parsing para inteiro  

#### 2. Foreign key error
- Uso de `profile_id=1`  

Corrigido para `profile.id`  

#### 3. Dados sujos (nomes de docentes)
Exemplo:
- `"Pedro AlvesEm parceria com..."`

---

## Inserção de dados

### Automático
Os seguintes dados foram carregados automaticamente através de scripts:

- **Courses** e **Subjects** → obtidos através de API  
- **CapstoneProjects** → carregados a partir de ficheiros JSON  
- **Teachers** → extraídos automaticamente a partir dos dados dos projetos  

### Manual (Django Admin)
Os seguintes dados foram inseridos manualmente:

- Skills  
- Certifications  
- WorkExperience  
- Projects  

### Justificação
A inserção manual foi utilizada para estes dados porque:

- São dados pessoais e específicos do utilizador  
- Não existem APIs públicas consistentes para este tipo de informação  
- Permitem maior controlo e personalização do portfólio  

---

## Justificação das entidades

### Profile
- Centraliza toda a informação do utilizador  
- Permite organizar o portfólio de forma estruturada  

### Course
- Representa a licenciatura do utilizador  
- Permite agrupar unidades curriculares e projetos  

### Subject
- Representa unidades curriculares  
- Permite associar projetos, docentes e tecnologias  

### Project
- Representa trabalhos académicos realizados nas UCs  
- Permite associação a tecnologias e competências  

### CapstoneProject
- Representa o trabalho final de curso (TFC)  
- Contém informação detalhada como resumo, autores e ano  

### Teacher
- Evita repetição de nomes de docentes  
- Permite reutilização entre várias unidades curriculares  

### Tech
- Representa tecnologias utilizadas  
- Evita redundância e permite reutilização  

### Skill
- Representa competências adquiridas pelo utilizador  
- Pode ser associada a projetos e experiência  

### Certification
- Representa formações adicionais  
- Complementa o percurso académico  

### WorkExperience
- Representa experiência profissional  
- Permite distinguir o percurso académico do profissional  

### MakingOf
- Documenta o processo de desenvolvimento dos projetos  
- Facilita a explicação e avaliação do trabalho realizado  

Resolvido com:
```python
name.split("Em parceria com")
