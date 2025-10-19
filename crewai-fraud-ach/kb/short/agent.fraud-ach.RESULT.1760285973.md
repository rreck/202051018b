```json
{
  "id": "874a7aee31f8783a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285973,
  "host_pid": "9e6742732c60:1",
  "hash": "d53f7445323f64e2071f2aefb4368223cba5457ceb7296a6231bc8d9acff4ded",
  "cid": "QmV1d53f7445323f64e2071f2aefb4368223cba5457c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285973,
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
      "evaluated_at": 1760285973
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
  "sig": "9938c85ce69ed21e21b38e62203b29e816c885b12c601d1048a078fbfbf46785"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245017605
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285763, 'matching_hash': '04117a7715fe8402'}}}