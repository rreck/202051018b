```json
{
  "id": "d84fcf9860f1b184",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294483,
  "host_pid": "9e6742732c60:1",
  "hash": "7df45c6af2771503f8507c673f2a04bb09bb974bf7e3927a915c868f8e5be47c",
  "cid": "QmV17df45c6af2771503f8507c673f2a04bb09bb974b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294483,
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
      "evaluated_at": 1760294483
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
  "sig": "1478de495ea397e7bbb40d919b20a5edc0ddfd747eed9956ba45d0c180024882"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025759024
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 91472709, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': 'fa026da4c6071776'}}}