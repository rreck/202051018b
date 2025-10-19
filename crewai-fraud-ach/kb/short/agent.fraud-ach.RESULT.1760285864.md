```json
{
  "id": "068fb7d8207666bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285864,
  "host_pid": "9e6742732c60:1",
  "hash": "c7d74f97e6acdf0aaa0481d37f9fa93f4562902ff98b609bdab0a86e04193db9",
  "cid": "QmV1c7d74f97e6acdf0aaa0481d37f9fa93f4562902f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285864,
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
      "evaluated_at": 1760285864
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
  "sig": "9a0eb5be8b201a9a265f3e21d4a3d19b639bb17429ba191fa44e141da6fc36e5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100278947252
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285763, 'matching_hash': 'c008d048aedbdb99'}}}