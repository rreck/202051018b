```json
{
  "id": "8c88a90d10211dda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289856,
  "host_pid": "9e6742732c60:1",
  "hash": "8afb174c904a8694901a1dffb6942dd6f6ba061bb2e5517bcd95922d9ba1379d",
  "cid": "QmV18afb174c904a8694901a1dffb6942dd6f6ba061b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289856,
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
      "evaluated_at": 1760289856
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
  "sig": "0c42ff2fe975fe81e004d363ef68b3107acc58db4409dbeb0f10ea07dba3c687"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154543608
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 10627740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285763, 'matching_hash': '3d9c367e54a48e12'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '013419643', 'validation_error': 'Invalid routing number checksum'}}}