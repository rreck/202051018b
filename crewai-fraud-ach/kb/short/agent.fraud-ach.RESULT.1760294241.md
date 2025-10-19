```json
{
  "id": "651a18d89683b982",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294241,
  "host_pid": "9e6742732c60:1",
  "hash": "ff35e8ec246fb2503a1ec44b7cd9872c485fa8ded90fec7766a8778c1ddb1337",
  "cid": "QmV1ff35e8ec246fb2503a1ec44b7cd9872c485fa8de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294241,
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
      "evaluated_at": 1760294241
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
  "sig": "24b181c0183ee674b217d842a258889f45f70f523942213a54a1184f6c6a96d6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594239738
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 310, 'threshold': 50, 'total_amount': 65979160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 309, 'first_seen': 1760284979, 'matching_hash': '98c544a6e0691c0b'}}}