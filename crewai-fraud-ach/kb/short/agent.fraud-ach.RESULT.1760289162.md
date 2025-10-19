```json
{
  "id": "230c5dc67f0e8102",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289162,
  "host_pid": "9e6742732c60:1",
  "hash": "9ea0d4c0c8801707e016cc225ee4b3dbee73c86ababdeb7c8c8dc44d4962fae8",
  "cid": "QmV19ea0d4c0c8801707e016cc225ee4b3dbee73c86a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289162,
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
      "evaluated_at": 1760289162
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
  "sig": "86885ceaa8393aae637e135f2216737fd63a941da1b2c9b51e2c388feb6d242d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599017181
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 20377770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285763, 'matching_hash': '7f94592234367703'}}}