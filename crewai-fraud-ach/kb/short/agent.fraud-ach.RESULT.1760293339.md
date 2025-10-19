```json
{
  "id": "a16c19ea17785dc1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293339,
  "host_pid": "9e6742732c60:1",
  "hash": "405e99842a1a4c397d2e04c3a336486c8202e37f912500b3dba6aa01932286ad",
  "cid": "QmV1405e99842a1a4c397d2e04c3a336486c8202e37f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293339,
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
      "evaluated_at": 1760293339
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
  "sig": "43ed6c4ea202c3901c74d82a074be5d4cf5955003c36ccc3a910e68cf1dad8b0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247533282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 32399568, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285765, 'matching_hash': '15ae64209d1fefcb'}}}