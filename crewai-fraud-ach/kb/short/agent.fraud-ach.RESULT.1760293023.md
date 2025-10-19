```json
{
  "id": "6c4616cb2f202edb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293023,
  "host_pid": "9e6742732c60:1",
  "hash": "ab2455ddb5eb7d477bfe8adfe31b977402f74e120b4a783eb34eb73f505c0d41",
  "cid": "QmV1ab2455ddb5eb7d477bfe8adfe31b977402f74e12",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293023,
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
      "evaluated_at": 1760293023
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
  "sig": "33488561b5b1e6e60fd764474485ba82e09e0bb3a2e30aadaaca1a03719ac26d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022248507
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 82385100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': '9ba0ba747d27e727'}}}