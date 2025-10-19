```json
{
  "id": "868da65c0076fa0a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294494,
  "host_pid": "9e6742732c60:1",
  "hash": "3cb3e9ba70d472db2e576f2401c578fc6a32e37600845231471ad345ef4b1985",
  "cid": "QmV13cb3e9ba70d472db2e576f2401c578fc6a32e376",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294494,
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
      "evaluated_at": 1760294494
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
  "sig": "ba89d9822b20f849f7f80060bb432a896ff2006c1ece31807aaa975ff56603fb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153776491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 21149827, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '94746339473c09ed'}}}