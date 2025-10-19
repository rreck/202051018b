```json
{
  "id": "66a0b2dee463f862",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286046,
  "host_pid": "9e6742732c60:1",
  "hash": "da9b87eb85839f13a8377d9340d872b21007eff4470b31d3c86a91ab25d2e232",
  "cid": "QmV1da9b87eb85839f13a8377d9340d872b21007eff4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286046,
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
      "evaluated_at": 1760286046
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
  "sig": "da6849b0ff8f1135dba5c1f1d1b6bad8c01de7a0acff20985b4fba771a082bd0"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}