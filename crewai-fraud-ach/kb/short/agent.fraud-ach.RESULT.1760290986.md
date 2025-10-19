```json
{
  "id": "9d0f8c2e58fc4c32",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290986,
  "host_pid": "9e6742732c60:1",
  "hash": "2957e4870e8dcc23a0deeb122ae5015254e0feb5aabb22faa1c7d5caec3b38e1",
  "cid": "QmV12957e4870e8dcc23a0deeb122ae5015254e0feb5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290986,
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
      "evaluated_at": 1760290986
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
  "sig": "e9ec6e2db690ee7f68f0d5ee3dec6345715c4015332bb87df03cb9d8d5598a75"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037507630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 59162016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': '9b4ed9a2b11bf5fa'}}}