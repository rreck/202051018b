```json
{
  "id": "26449233cce7ccdf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286040,
  "host_pid": "9e6742732c60:1",
  "hash": "07e509029cc0fe93d77db21a010df8441b1303b7afeb654ebbb12a0a3b82d56b",
  "cid": "QmV107e509029cc0fe93d77db21a010df8441b1303b7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286040,
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
      "evaluated_at": 1760286040
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
  "sig": "c4a1230eb5742d040c3b88af7251374aef1a97da258cdebc0274afee63c2d87c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000025883497
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285765, 'matching_hash': '8c29ee71720a2634'}}}