```json
{
  "id": "643d647228ee73d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291835,
  "host_pid": "9e6742732c60:1",
  "hash": "39f931059aaa7e7941eed55cddbab10621b894d205f68d10301c1c11fab54b15",
  "cid": "QmV139f931059aaa7e7941eed55cddbab10621b894d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291835,
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
      "evaluated_at": 1760291835
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
  "sig": "a52c3041c2328839f06b801161feb8a4a402df307c6a76f41416a1a9ffca0ce8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461577963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 80015712, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285764, 'matching_hash': '6bf1d905269d1dd3'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}