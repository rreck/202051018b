```json
{
  "id": "d0c98bf3c38762dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294588,
  "host_pid": "9e6742732c60:1",
  "hash": "b463048e4689f432ced64c6f8fa7ec2e4c9091904e1b96ed7081a5486338ad82",
  "cid": "QmV1b463048e4689f432ced64c6f8fa7ec2e4c909190",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294588,
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
      "evaluated_at": 1760294588
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
  "sig": "5dbb78adac95169043327461b620c0c90d246ad651290c80ecf8c4018b8a9a99"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468983209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 68790317, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'c1a39c32a70f5fe9'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}