```json
{
  "id": "7aa83786d3331d19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287077,
  "host_pid": "9e6742732c60:1",
  "hash": "87241b3428ca6a87860b6686227f715d992140e4c97914350aa096a4a506ef64",
  "cid": "QmV187241b3428ca6a87860b6686227f715d992140e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287077,
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
      "evaluated_at": 1760287077
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
  "sig": "00d13298bb00551d640da71e34d355d3f307892d7f891892b8def940cc6d90a4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243684464
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285765, 'matching_hash': '4ae1f96c7cecc03b'}}}