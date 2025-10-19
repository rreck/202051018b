```json
{
  "id": "16ea306a45712a0f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289091,
  "host_pid": "9e6742732c60:1",
  "hash": "5971a1a11c2fcc429491f8ff42978729293181250f5e6b2eb3d865edcc875b0a",
  "cid": "QmV15971a1a11c2fcc429491f8ff4297872929318125",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289091,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760289091
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "422d4dc22984e0e0140391fe386011770bdcf27128812e7d02170487148a66a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024300942
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285763, 'matching_hash': '95903848ba405d51'}}}een': 1760285764, 'matching_hash': 'd3845a7ded8f78ea'}}}