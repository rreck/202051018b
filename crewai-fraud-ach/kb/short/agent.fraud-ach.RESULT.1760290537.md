```json
{
  "id": "0991a50922c2ef0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290537,
  "host_pid": "9e6742732c60:1",
  "hash": "c3319e9336dd5b9822861f2c39f7dfa6bc928c3303e9024fdd29a32c0ba52151",
  "cid": "QmV1c3319e9336dd5b9822861f2c39f7dfa6bc928c33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290537,
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
      "evaluated_at": 1760290537
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
  "sig": "9894ad452f2d24516f53433f2d992508e736204a65fec2e828b4a30965eb5366"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027419247
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 71882613, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': 'f49fdb64c00c5aec'}}}