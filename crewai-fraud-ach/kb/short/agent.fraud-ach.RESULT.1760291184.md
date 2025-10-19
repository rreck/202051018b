```json
{
  "id": "151bd1fa99fcae51",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291184,
  "host_pid": "9e6742732c60:1",
  "hash": "a19ddd186fd77f46b6f669bb07442934f6e401cba0aef9543b27393b0d60d6d5",
  "cid": "QmV1a19ddd186fd77f46b6f669bb07442934f6e401cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291184,
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
      "evaluated_at": 1760291184
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
  "sig": "63770cbe624a5c3955b9673539ce8901137c01a8858063325800e28684da877a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241906665
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 43804462, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285764, 'matching_hash': '6ca698820fae5f27'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '586667919', 'validation_error': 'Invalid routing number checksum'}}}