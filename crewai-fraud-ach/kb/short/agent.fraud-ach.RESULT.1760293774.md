```json
{
  "id": "966e14f6d3b893b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293774,
  "host_pid": "9e6742732c60:1",
  "hash": "d2b406af0c25b2ccdd42eac46c7b1435e9fcdb8c3ea57cdf2d66ea1f90f160c4",
  "cid": "QmV1d2b406af0c25b2ccdd42eac46c7b1435e9fcdb8c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293774,
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
      "evaluated_at": 1760293774
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
  "sig": "880f9e0cb47fdbd0c82eb02de84c051243319122df21a6b7553309984ddbf0f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154102308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 301, 'threshold': 50, 'total_amount': 110896527, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 300, 'first_seen': 1760284979, 'matching_hash': '687d8a253912c530'}}}