```json
{
  "id": "e32f0f1f331960b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286617,
  "host_pid": "9e6742732c60:1",
  "hash": "96cb0c74d2bbf5ed458a6adbdb3e682948d95eaf08945fdbf23afd1aa55d5433",
  "cid": "QmV196cb0c74d2bbf5ed458a6adbdb3e682948d95eaf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286617,
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
      "evaluated_at": 1760286617
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "3c192fd38f1d20ad62d2ff509accaa5cfa64a8c38253f66a8515aacb5da37089"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000021011137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10326875, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285764, 'matching_hash': '3868aeea45d72d6f'}}}