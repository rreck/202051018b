```json
{
  "id": "60c5aa74259a1972",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288572,
  "host_pid": "9e6742732c60:1",
  "hash": "9c6ebc05cc15372c2a30aab96f1dca8332b21c5d1916f00d96aabbc6db743cf2",
  "cid": "QmV19c6ebc05cc15372c2a30aab96f1dca8332b21c5d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288572,
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
      "evaluated_at": 1760288572
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
  "sig": "dc19dc9317076f0b3dccb3c2e7f5640e940cfab98be09b9aaf01e98c6e97dd09"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466004729
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 27669929, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285765, 'matching_hash': '1e26fed2c08b1370'}}}