```json
{
  "id": "de112abd3382e7f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286441,
  "host_pid": "9e6742732c60:1",
  "hash": "c71c13e880a794798de9372e79d7b5d32cbc9fffbf31d0ad489688feb4f04411",
  "cid": "QmV1c71c13e880a794798de9372e79d7b5d32cbc9fff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286441,
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
      "evaluated_at": 1760286441
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
  "sig": "931c5c2a88162dfc9110317d5dce958a071f985de60d0d5b7d24a473f7cad0a3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201466322331
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285765, 'matching_hash': '8006c6780242cc6a'}}}