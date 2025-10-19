```json
{
  "id": "db66a022cce441c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294656,
  "host_pid": "9e6742732c60:1",
  "hash": "07fa054cdbe339d343b2c2833d0aa917b4f4e548e335691d9063bf89d1cdd0da",
  "cid": "QmV107fa054cdbe339d343b2c2833d0aa917b4f4e548",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294656,
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
      "evaluated_at": 1760294656
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
  "sig": "39af82cc39f3589b285513ab063baeca90698c96ee8ae3ea339ac7dc7e19a808"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154787030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 106404980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285764, 'matching_hash': '945ae0d1ce138c7f'}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}