```json
{
  "id": "298888438560706b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287207,
  "host_pid": "9e6742732c60:1",
  "hash": "fc2629643f8c0a9a7ef94df151939505888c8c68779224169b8db164ec45dac1",
  "cid": "QmV1fc2629643f8c0a9a7ef94df151939505888c8c68",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287207,
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
      "evaluated_at": 1760287207
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "8a67d310bd32ffed043cc2307788ebc4b1544a403f81648014ba4a520dbad2d9"
}
```

Fraud detected: duplicate_transaction (score: 69)
Transaction: 044000037116719
Details: {'velocity': {'fraud_detected': True, 'risk_score': 54, 'details': {'transaction_count': 52, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285763, 'matching_hash': 'c24831f619c6556e'}}}