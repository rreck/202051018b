```json
{
  "id": "9c3faa136ecba0fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292459,
  "host_pid": "9e6742732c60:1",
  "hash": "a32bbc7f063fac5c5dba10c29c3a6fb35d8c27c19a4512ed28f70cf260144d63",
  "cid": "QmV1a32bbc7f063fac5c5dba10c29c3a6fb35d8c27c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292459,
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
      "evaluated_at": 1760292459
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
  "sig": "6ce6dd1293e23d85800aa77eedf7d0a61c9c81bb392a394911119473024cbf8c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461197823
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 35718210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': 'c7e6425f6e43a399'}}}