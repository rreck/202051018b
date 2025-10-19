```json
{
  "id": "b159abbf8e7c033c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289197,
  "host_pid": "9e6742732c60:1",
  "hash": "10a7e74e44fbb1b95b659990723f9c92e7228b3d65a26f41e935234e938d6d07",
  "cid": "QmV110a7e74e44fbb1b95b659990723f9c92e7228b3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289197,
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
      "evaluated_at": 1760289197
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
  "sig": "e8c40895ac4d36519361c431578146d39f655d8567f5d98433058740b246ffce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029285635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 40394564, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': '952b5fd24342145c'}}}