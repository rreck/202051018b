```json
{
  "id": "4b02373c700e7d05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288751,
  "host_pid": "9e6742732c60:1",
  "hash": "2a4927e35b05902587141e5e9ba7ecc648b554e016cb6dda9456fcc984e5b5a5",
  "cid": "QmV12a4927e35b05902587141e5e9ba7ecc648b554e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288751,
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
      "evaluated_at": 1760288751
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
  "sig": "229b6f58dc881302ad3500dd4c1234cfe14617ae1f7f717ed5d21b087d2a5c67"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038495907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 28016206, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285763, 'matching_hash': '3a0df0e30691ba23'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '013419643', 'validation_error': 'Invalid routing number checksum'}}}