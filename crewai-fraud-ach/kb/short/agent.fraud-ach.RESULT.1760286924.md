```json
{
  "id": "ba065211993c5558",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286924,
  "host_pid": "9e6742732c60:1",
  "hash": "35c4b985ee21c234543d5f75977cdc388c31ad420e62d2ca82e2225e2c5b5b78",
  "cid": "QmV135c4b985ee21c234543d5f75977cdc388c31ad42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286924,
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
      "evaluated_at": 1760286924
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
  "sig": "b087cd1c40bc16440a684ac483de1384d3a8cfb9abe4bd56b05ceac234b2d191"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201462755939
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285764, 'matching_hash': '0ef039381f9434ef'}}}