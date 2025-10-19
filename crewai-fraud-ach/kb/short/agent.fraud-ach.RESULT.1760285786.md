```json
{
  "id": "067442d7e1a8524e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285786,
  "host_pid": "9e6742732c60:1",
  "hash": "88f458dda7a0965caf08a93273121b7edcbe651994b5ee084bce07346da68682",
  "cid": "QmV188f458dda7a0965caf08a93273121b7edcbe6519",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285786,
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
      "evaluated_at": 1760285786
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
  "sig": "fdb50d3a2811ed70cee67a04129c6a4bf910d8b5e5a61589ab47116b26e1a6e4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}