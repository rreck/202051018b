```json
{
  "id": "6953747f40df237b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293957,
  "host_pid": "9e6742732c60:1",
  "hash": "1ff044ff11a485023708444e4e9c195f3d04de67e5827cb4b829e1c3a43bae0a",
  "cid": "QmV11ff044ff11a485023708444e4e9c195f3d04de67",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293957,
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
      "evaluated_at": 1760293957
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
  "sig": "9cbb9528f68086f9934b0d7d459c535c3690a231b1355ec8955474ac7ef6c812"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036798243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 101239068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': '9f3869b775bbb8aa'}}}