```json
{
  "id": "646b218a9d15beb3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292699,
  "host_pid": "9e6742732c60:1",
  "hash": "86c8ce113c55f96cd824abef9b3e983aa572770d68c7a4c754386732256cc916",
  "cid": "QmV186c8ce113c55f96cd824abef9b3e983aa572770d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292699,
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
      "evaluated_at": 1760292699
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
  "sig": "5a0c540f11b3f95c8eb9f238e9cc22891d6a13d93a4c78ca557bd8647f2a126a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037120396
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 22944075, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '29cd45017b863efa'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '650095545', 'validation_error': 'Invalid routing number checksum'}}}