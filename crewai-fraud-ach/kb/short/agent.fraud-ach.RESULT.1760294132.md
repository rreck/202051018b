```json
{
  "id": "03b79599dee550b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294132,
  "host_pid": "9e6742732c60:1",
  "hash": "6e0a7e0da0096885cbde6ff58b89d3168545f9b21ccb287409425427bb2ce885",
  "cid": "QmV16e0a7e0da0096885cbde6ff58b89d3168545f9b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294132,
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
      "evaluated_at": 1760294132
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
  "sig": "429d2fd191d7c0b7b0b32eadc9bae2aad54d0714e24208fe617b7820f91110cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244291071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 29366792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '1f8fb3dc368ee7c3'}}}maly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5513113}}}