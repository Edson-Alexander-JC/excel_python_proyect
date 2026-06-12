import streamlit as st
class ColumnSetter:
    def set_column(self,dim):
        return st.columns(dim)
    
    def put_column(self,poss,columnas,elemento):
        with columnas[poss]:
            elemento()
            
    def mk_col(self,elements:list):
        colmuna = self.set_column(len(elements))
        
        for i, element in enumerate(elements):
            self.put_column(i,colmuna,element)
        