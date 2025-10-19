```json
{
  "id": "8f6103b3c5998f1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288457,
  "host_pid": "9e6742732c60:1",
  "hash": "25a1f17e4361a7b1179b1a4d577becb3293b575d86d56083bdded247c325c7ba",
  "cid": "QmV125a1f17e4361a7b1179b1a4d577becb3293b575d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288457,
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
      "evaluated_at": 1760288457
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
  "sig": "9eb8ff9df1feaf22f10bb6f7fb3b20dae9c9c19bd592fb15a4c5695713d825f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021252160
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 44743812, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '942f41a705b17558'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '868351851', 'validation_error': 'Invalid routing number checksum'}}}