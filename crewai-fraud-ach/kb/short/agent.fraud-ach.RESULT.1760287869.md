```json
{
  "id": "222f88799caa41a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287869,
  "host_pid": "9e6742732c60:1",
  "hash": "2c94dd239bac496855f8371a1a527cdeb249e94d3a804d71dacdc563f5c265f1",
  "cid": "QmV12c94dd239bac496855f8371a1a527cdeb249e94d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287869,
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
      "evaluated_at": 1760287869
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
  "sig": "93daf55311240111600c54b401b8a8e537c9a8d638b02dd62433f7c5fadf9db6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273941483
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 23487000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285763, 'matching_hash': '33ec4b85754ad38a'}}}