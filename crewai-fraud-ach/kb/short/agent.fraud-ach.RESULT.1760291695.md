```json
{
  "id": "25b3b2507b60af20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291695,
  "host_pid": "9e6742732c60:1",
  "hash": "53b6724e5919c6458be74354e446fa1624bd828e003df3295095ac6146ea0e4a",
  "cid": "QmV153b6724e5919c6458be74354e446fa1624bd828e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291695,
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
      "evaluated_at": 1760291695
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
  "sig": "eb1bccefe44310f5e3165678fa44ed727cec9f7207aac4583e0d52c886dc1ca1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024174154
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 77054415, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '443a0c3eda74d322'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '372851336', 'validation_error': 'Invalid routing number checksum'}}}