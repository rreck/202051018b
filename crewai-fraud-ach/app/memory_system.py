#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Copyright (c) RRECKTEK LLC
# Project: CrewAI Fraud Detection Agent - Biomimicry Memory System
# Version: 1.0.0
#
# Purpose:
#   Biomimicry-driven persistent memory system with:
#   - Strict filename patterns: <scope>.<KEY>.<EPOCH>.md
#   - JSON headers with cryptographic provenance (hash, cid, AICP)
#   - Bidirectional edges with weights
#   - Co-occurrence tracking within τ=7d window
#   - Weight decay λ=0.01/day
#   - Consolidation: CLUSTER, SYNTHESIS, META, ECHO, CONSENSUS
#   - kb/short for atomic notes (≤64KB)
#   - kb/long for rollups (≤512KB)
# -----------------------------------------------------------------------------

import hashlib
import json
import os
import socket
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set
from enum import Enum
import hmac


class MemoryScope(str, Enum):
    """Memory artifact scope"""
    AGENT = 'agent'
    CREW = 'crew'


class MemoryKey(str, Enum):
    """Memory artifact key types"""
    IDEA = 'IDEA'
    TASK = 'TASK'
    PROBLEM = 'PROBLEM'
    ACTION = 'ACTION'
    RESULT = 'RESULT'
    LESSON = 'LESSON'
    CLUSTER = 'CLUSTER'
    SYNTHESIS = 'SYNTHESIS'
    META = 'META'
    ECHO = 'ECHO'
    CONSENSUS = 'CONSENSUS'


class AICPComponent:
    """AICP (AI Compliance Protocol) components"""

    @staticmethod
    def create_prov(issuer: str, created_at: int, method: str) -> Dict:
        """Create AICP-PROV (Provenance) component"""
        return {
            'issuer': issuer,
            'created_at': created_at,
            'method': method,
            'vc_type': 'VerifiableCredential'
        }

    @staticmethod
    def create_ucon(usage_constraints: List[str], purpose: str) -> Dict:
        """Create AICP-UCON (Usage Control) component"""
        return {
            'usage_constraints': usage_constraints,
            'purpose': purpose,
            'enforcement': 'mandatory'
        }

    @staticmethod
    def create_eval(confidence: float, evidence_count: int, review_status: str) -> Dict:
        """Create AICP-EVAL (Evaluation) component"""
        return {
            'confidence': confidence,
            'evidence_count': evidence_count,
            'review_status': review_status,
            'evaluated_at': int(time.time())
        }


class MemoryArtifact:
    """Base class for memory artifacts"""

    def __init__(self,
                 scope: MemoryScope,
                 key: MemoryKey,
                 agent_name: str = 'fraud-ach',
                 content: str = '',
                 sources: Optional[List[str]] = None,
                 edges: Optional[List[Dict]] = None,
                 tags: Optional[List[str]] = None):
        self.scope = scope
        self.key = key
        self.agent_name = agent_name
        self.epoch = int(time.time())
        self.content = content
        self.sources = sources or []
        self.edges = edges or []
        self.tags = tags or []

        # Generate unique ID
        self.id = self._generate_id()

        # Compute hash and CID
        self.hash = self._compute_hash()
        self.cid = self._compute_cid()

        # Host and PID
        self.host_pid = f"{socket.gethostname()}:{os.getpid()}"

        # AICP components
        self.aicp = {
            'prov': AICPComponent.create_prov(
                issuer=self.host_pid,
                created_at=self.epoch,
                method='automated_fraud_detection'
            ),
            'ucon': AICPComponent.create_ucon(
                usage_constraints=['no_pii_export', 'audit_required'],
                purpose='fraud_detection_analysis'
            ),
            'eval': AICPComponent.create_eval(
                confidence=1.0,
                evidence_count=len(self.sources),
                review_status='pending'
            )
        }

        # Metrics and thresholds
        self.metrics = {}
        self.thresholds = {}

        # Signature (HMAC-SHA256)
        self.sig = self._compute_signature()

    def _generate_id(self) -> str:
        """Generate unique artifact ID"""
        components = [
            self.scope.value,
            self.agent_name,
            self.key.value,
            str(self.epoch)
        ]
        id_str = '.'.join(components)
        return hashlib.sha256(id_str.encode('utf-8')).hexdigest()[:16]

    def _compute_hash(self) -> str:
        """Compute SHA256 hash of content"""
        return hashlib.sha256(self.content.encode('utf-8')).hexdigest()

    def _compute_cid(self) -> str:
        """Compute Content Identifier (simplified IPFS-like CID)"""
        # In production, use actual IPFS CID computation
        prefix = 'QmV1'  # Simplified prefix
        return prefix + self.hash[:40]

    def _compute_signature(self) -> str:
        """Compute HMAC signature for integrity"""
        # In production, use proper key management
        secret_key = f"fraud-ach-{self.epoch}".encode('utf-8')
        message = f"{self.id}:{self.hash}:{self.cid}".encode('utf-8')
        return hmac.new(secret_key, message, hashlib.sha256).hexdigest()

    def get_filename(self) -> str:
        """Generate filename following pattern: <scope>.<agent>.<KEY>.<EPOCH>.md"""
        return f"{self.scope.value}.{self.agent_name}.{self.key.value}.{self.epoch}.md"

    def to_json_header(self) -> str:
        """Generate JSON header block"""
        header = {
            'id': self.id,
            'scope': self.scope.value,
            'key': self.key.value,
            'epoch': self.epoch,
            'host_pid': self.host_pid,
            'hash': self.hash,
            'cid': self.cid,
            'aicp': self.aicp,
            'sources': self.sources,
            'edges': self.edges,
            'metrics': self.metrics,
            'thresholds': self.thresholds,
            'tags': self.tags,
            'sig': self.sig
        }
        return json.dumps(header, indent=2)

    def to_markdown(self) -> str:
        """Generate complete markdown file with JSON header"""
        parts = [
            '```json',
            self.to_json_header(),
            '```',
            '',
            self.content
        ]
        return '\n'.join(parts)

    def size_bytes(self) -> int:
        """Get size in bytes"""
        return len(self.to_markdown().encode('utf-8'))

    def validate_size(self, max_bytes: int) -> bool:
        """Validate artifact size against limit"""
        return self.size_bytes() <= max_bytes


class MemoryEdge:
    """Bidirectional edge between memory artifacts"""

    def __init__(self,
                 source_id: str,
                 target_id: str,
                 weight: float = 0.5,
                 created_at: Optional[int] = None,
                 edge_type: str = 'reference'):
        self.source_id = source_id
        self.target_id = target_id
        self.weight = max(0.0, min(1.0, weight))  # Clip to [0,1]
        self.created_at = created_at or int(time.time())
        self.edge_type = edge_type
        self.last_updated = self.created_at

    def decay(self, days_elapsed: float, lambda_per_day: float = 0.01):
        """Apply weight decay: w_new = w_old * (1 - λ * days)"""
        decay_factor = 1.0 - (lambda_per_day * days_elapsed)
        self.weight = max(0.0, min(1.0, self.weight * decay_factor))
        self.last_updated = int(time.time())

    def reinforce(self, boost: float = 0.1):
        """Reinforce edge weight"""
        self.weight = min(1.0, self.weight + boost)
        self.last_updated = int(time.time())

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'source_id': self.source_id,
            'target_id': self.target_id,
            'weight': round(self.weight, 4),
            'created_at': self.created_at,
            'last_updated': self.last_updated,
            'edge_type': self.edge_type
        }


class MemoryStore:
    """Memory storage and retrieval system"""

    def __init__(self, base_dir: str = './kb'):
        self.base_dir = base_dir
        self.short_dir = os.path.join(base_dir, 'short')
        self.long_dir = os.path.join(base_dir, 'long')

        # Ensure directories exist
        os.makedirs(self.short_dir, exist_ok=True)
        os.makedirs(self.long_dir, exist_ok=True)

        # Size limits
        self.MAX_SHORT_BYTES = 64 * 1024  # 64 KB
        self.MAX_LONG_BYTES = 512 * 1024  # 512 KB

        # Edge tracking
        self.edges: Dict[str, MemoryEdge] = {}

        # Consolidation parameters
        self.TAU_WINDOW_DAYS = 7
        self.LAMBDA_DECAY_PER_DAY = 0.01
        self.CLUSTER_MIN_SOURCES = 5
        self.CLUSTER_MIN_WEIGHT = 0.6
        self.SYNTHESIS_MIN_CLUSTERS = 2
        self.CONSENSUS_QUORUM = 0.67

    def save_artifact(self, artifact: MemoryArtifact, force_long: bool = False) -> str:
        """Save memory artifact to appropriate directory"""
        # Determine directory based on key and size
        if force_long or artifact.key in [MemoryKey.CLUSTER, MemoryKey.SYNTHESIS,
                                           MemoryKey.META, MemoryKey.CONSENSUS]:
            target_dir = self.long_dir
            max_size = self.MAX_LONG_BYTES
        else:
            target_dir = self.short_dir
            max_size = self.MAX_SHORT_BYTES

        # Validate size
        if not artifact.validate_size(max_size):
            raise ValueError(f"Artifact exceeds size limit: {artifact.size_bytes()} > {max_size}")

        # Write file
        file_path = os.path.join(target_dir, artifact.get_filename())
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(artifact.to_markdown())

        return file_path

    def load_artifact(self, filename: str) -> Optional[MemoryArtifact]:
        """Load memory artifact from file"""
        # Try both directories
        for directory in [self.short_dir, self.long_dir]:
            file_path = os.path.join(directory, filename)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract JSON header
                if content.startswith('```json\n'):
                    json_end = content.find('\n```\n')
                    if json_end != -1:
                        json_str = content[8:json_end]
                        header = json.loads(json_str)
                        body = content[json_end + 5:]

                        # Reconstruct artifact
                        artifact = MemoryArtifact(
                            scope=MemoryScope(header['scope']),
                            key=MemoryKey(header['key']),
                            agent_name='fraud-ach',
                            content=body,
                            sources=header.get('sources', []),
                            edges=header.get('edges', []),
                            tags=header.get('tags', [])
                        )
                        return artifact

        return None

    def add_edge(self, source_id: str, target_id: str, weight: float = 0.5, edge_type: str = 'reference'):
        """Add or update edge between artifacts"""
        edge_key = f"{source_id}:{target_id}"
        if edge_key in self.edges:
            self.edges[edge_key].reinforce()
        else:
            self.edges[edge_key] = MemoryEdge(source_id, target_id, weight, edge_type=edge_type)

    def decay_edges(self):
        """Apply time-based decay to all edges"""
        current_time = int(time.time())
        for edge in self.edges.values():
            days_elapsed = (current_time - edge.last_updated) / (24 * 3600)
            edge.decay(days_elapsed, self.LAMBDA_DECAY_PER_DAY)

    def get_recent_artifacts(self, key: Optional[MemoryKey] = None, days: int = 7) -> List[str]:
        """Get recent artifacts within time window"""
        cutoff_time = int(time.time()) - (days * 24 * 3600)
        artifacts = []

        for directory in [self.short_dir, self.long_dir]:
            for filename in os.listdir(directory):
                if filename.endswith('.md'):
                    # Parse epoch from filename
                    parts = filename.split('.')
                    if len(parts) >= 4:
                        try:
                            epoch = int(parts[-2])
                            if epoch >= cutoff_time:
                                if key is None or parts[-3] == key.value:
                                    artifacts.append(filename)
                        except ValueError:
                            continue

        return sorted(artifacts, key=lambda x: int(x.split('.')[-2]), reverse=True)

    def create_cluster(self, source_ids: List[str], pattern: str, summary: str) -> Optional[MemoryArtifact]:
        """Create CLUSTER artifact from multiple sources"""
        if len(source_ids) < self.CLUSTER_MIN_SOURCES:
            return None

        # Calculate average edge weight
        total_weight = 0.0
        edge_count = 0
        for i, src1 in enumerate(source_ids):
            for src2 in source_ids[i+1:]:
                edge_key = f"{src1}:{src2}"
                if edge_key in self.edges:
                    total_weight += self.edges[edge_key].weight
                    edge_count += 1

        avg_weight = total_weight / edge_count if edge_count > 0 else 0.0

        if avg_weight < self.CLUSTER_MIN_WEIGHT:
            return None

        # Create cluster content
        content_parts = [
            f"## CLUSTER: {pattern}",
            "",
            f"**Summary**: {summary}",
            "",
            f"**Members**: {len(source_ids)} artifacts",
            f"**Average Weight**: {avg_weight:.3f}",
            "",
            "**Pattern Analysis**:",
            f"- Detected pattern: {pattern}",
            f"- Co-occurrence within {self.TAU_WINDOW_DAYS} day window",
            "",
            "**Next Actions**:",
            "- Monitor for similar patterns",
            "- Update fraud detection rules if validated",
            "- Consider synthesis with related clusters"
        ]

        artifact = MemoryArtifact(
            scope=MemoryScope.AGENT,
            key=MemoryKey.CLUSTER,
            agent_name='fraud-ach',
            content='\n'.join(content_parts),
            sources=source_ids,
            tags=['cluster', pattern]
        )

        artifact.metrics = {
            'source_count': len(source_ids),
            'average_weight': avg_weight,
            'pattern': pattern
        }

        return artifact

    def list_artifacts(self, directory: Optional[str] = None) -> List[str]:
        """List all artifacts in store"""
        dirs = [directory] if directory else [self.short_dir, self.long_dir]
        artifacts = []
        for d in dirs:
            if os.path.exists(d):
                artifacts.extend([f for f in os.listdir(d) if f.endswith('.md')])
        return sorted(artifacts)

    def get_statistics(self) -> Dict:
        """Get memory store statistics"""
        short_files = len([f for f in os.listdir(self.short_dir) if f.endswith('.md')])
        long_files = len([f for f in os.listdir(self.long_dir) if f.endswith('.md')])

        return {
            'short_artifacts': short_files,
            'long_artifacts': long_files,
            'total_edges': len(self.edges),
            'active_edges': sum(1 for e in self.edges.values() if e.weight > 0.1),
            'tau_window_days': self.TAU_WINDOW_DAYS,
            'lambda_decay': self.LAMBDA_DECAY_PER_DAY
        }
