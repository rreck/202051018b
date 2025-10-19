```json
{
  "id": "7815915aa2e10281",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292523,
  "host_pid": "9e6742732c60:1",
  "hash": "06428239e57975a974fd4b5e64c8307cce53724bc2b10ebfdfed0fd58673587b",
  "cid": "QmV106428239e57975a974fd4b5e64c8307cce53724b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292523,
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
      "evaluated_at": 1760292523
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
  "sig": "6495f559e8064cb2e05dd3c54c7d54016eb5158bc39cf816a5c948b12349621a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020807792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 41541449, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285764, 'matching_hash': '8390351bce6e669b'}}}