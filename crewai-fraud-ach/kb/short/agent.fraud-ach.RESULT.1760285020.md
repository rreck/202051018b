```json
{
  "id": "fd602df8c8c12e4f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285020,
  "host_pid": "9e6742732c60:1",
  "hash": "672a112f19666a6cbdea27752a46be071aa8d81946f7f5217c81b7405be6aa80",
  "cid": "QmV1672a112f19666a6cbdea27752a46be071aa8d819",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285020,
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
      "evaluated_at": 1760285020
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
  "sig": "1301f15659c56a31246876dbdffa8b249dfdf422785d52cb4a9cc165c95990fb"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}