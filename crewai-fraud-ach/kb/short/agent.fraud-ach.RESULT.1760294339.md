```json
{
  "id": "06b8be2b78f9398d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294339,
  "host_pid": "9e6742732c60:1",
  "hash": "45f5c4ae14a1d24977eac84e7c619e76dba7bb8694f4de22d48606eceb0ab6b5",
  "cid": "QmV145f5c4ae14a1d24977eac84e7c619e76dba7bb86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294339,
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
      "evaluated_at": 1760294339
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
  "sig": "2d9433db6b05f6656b7c8f29a3d4e4c82d2e13a5c782a780ff334d1cd5b8d09a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032539256
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 116595800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '34ea678ce834982a'}}}