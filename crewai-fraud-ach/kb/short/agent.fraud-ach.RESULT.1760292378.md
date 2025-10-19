```json
{
  "id": "907502581ee044fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292378,
  "host_pid": "9e6742732c60:1",
  "hash": "150af79d3bf6fcdf21bb3e18f1036a342b417e2004738f3bbacd38d5da6679eb",
  "cid": "QmV1150af79d3bf6fcdf21bb3e18f1036a342b417e20",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292378,
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
      "evaluated_at": 1760292378
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
  "sig": "ade0d14a963991a39d959282d3f94e46106e671cb40311ebf09fc8d576b55c4b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246112063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 27204408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': '58be5dc306b57ee9'}}}