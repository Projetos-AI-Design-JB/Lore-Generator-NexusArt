-- Habilita a extensão pgvector para buscas semânticas
CREATE EXTENSION IF NOT EXISTS vector;

-- Tabela para armazenar os personagens gerados
CREATE TABLE IF NOT EXISTS characters (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    lore TEXT NOT NULL,
    image_url TEXT,
    style TEXT,
    embedding VECTOR(768), -- Ajustado para Google text-embedding-004
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now())
);

-- Função para busca semântica via RPC
CREATE OR REPLACE FUNCTION match_characters (
  query_embedding VECTOR(768),
  match_threshold FLOAT,
  match_count INT
)
RETURNS TABLE (
  id UUID,
  name TEXT,
  lore TEXT,
  image_url TEXT,
  style TEXT,
  similarity FLOAT
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    characters.id,
    characters.name,
    characters.lore,
    characters.image_url,
    characters.style,
    1 - (characters.embedding <=> query_embedding) AS similarity
  FROM characters
  WHERE 1 - (characters.embedding <=> query_embedding) > match_threshold
  ORDER BY similarity DESC
  LIMIT match_count;
END;
$$;
