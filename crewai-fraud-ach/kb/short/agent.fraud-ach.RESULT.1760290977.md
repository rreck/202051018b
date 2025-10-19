```json
{
  "id": "adb51c3df3fc4f1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290977,
  "host_pid": "9e6742732c60:1",
  "hash": "0903acaaf8b13fe550674b541e1bb1d79df2af33f6db05ca63f892d727142b8c",
  "cid": "QmV10903acaaf8b13fe550674b541e1bb1d79df2af33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290977,
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
      "evaluated_at": 1760290977
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
  "sig": "47415c51365748eff5fbf9da1d14ee9c3d1a9baca5b5e3752a56e13b3b4c0e8b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466383232
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 32758836, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': '37ada470abbef201'}}}