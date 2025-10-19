```json
{
  "id": "b43c3b2fed83f4d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294485,
  "host_pid": "9e6742732c60:1",
  "hash": "844c54ec2ab3a87e583fdcde42356d6ef418ace589ef387a781058b951fc9753",
  "cid": "QmV1844c54ec2ab3a87e583fdcde42356d6ef418ace5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294485,
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
      "evaluated_at": 1760294485
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
  "sig": "eeab43661a286f7cc606fe322b215d99f00787ac9312a300403bfdbf89c9511b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022356059
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 40154151, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': 'fa8ad4fa6a79b6e4'}}}