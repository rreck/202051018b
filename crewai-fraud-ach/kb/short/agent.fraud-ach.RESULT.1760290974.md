```json
{
  "id": "10d1ab485947d304",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290974,
  "host_pid": "9e6742732c60:1",
  "hash": "dfc3cd21737e770fe8ec077f7347d7a0bd41ca5200e75c1c6db30a44009a9907",
  "cid": "QmV1dfc3cd21737e770fe8ec077f7347d7a0bd41ca52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290974,
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
      "evaluated_at": 1760290974
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
  "sig": "4ea6be9700118824ea640aad3d33b0d9f3ec1affb0083c71bfb26f017fe5d1c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463831807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 29565100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': 'ac2384e4a351cc1b'}}}