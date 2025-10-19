```json
{
  "id": "d5633aed3082dee4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288624,
  "host_pid": "9e6742732c60:1",
  "hash": "9e42dc39606424ddc3bab7184713f8d7d6e1279677ce292a4e8bd0fbfc6854e4",
  "cid": "QmV19e42dc39606424ddc3bab7184713f8d7d6e12796",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288624,
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
      "evaluated_at": 1760288624
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
  "sig": "66a125fb786c5efacb7a1ca25b4c7c693d94d082e8ab24f64b81a9cf465f29c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150369382
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 35422992, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': '1d04175be49b6deb'}}}