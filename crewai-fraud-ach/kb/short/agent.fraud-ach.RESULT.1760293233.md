```json
{
  "id": "eebfe32ec6dce50e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293233,
  "host_pid": "9e6742732c60:1",
  "hash": "2c3596597a856c7cb8a21cee14d963a405a3bd924ce3c7a88e9362e30f174c48",
  "cid": "QmV12c3596597a856c7cb8a21cee14d963a405a3bd92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293233,
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
      "evaluated_at": 1760293233
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
  "sig": "d3f415ff73eba5b53bee7db7dc9c33d1d349465eec99ee834e403659472c17e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020012424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 49229202, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '53913ea58eda97e4'}}}