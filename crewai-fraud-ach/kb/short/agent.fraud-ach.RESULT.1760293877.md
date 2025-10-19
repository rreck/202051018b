```json
{
  "id": "58d5ebf4e4bf3469",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293877,
  "host_pid": "9e6742732c60:1",
  "hash": "8810827273d11ea15a98d445dd7333cec18f4550572b9d1c9228221b3e251ad3",
  "cid": "QmV18810827273d11ea15a98d445dd7333cec18f4550",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293877,
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
      "evaluated_at": 1760293877
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
  "sig": "c98b80bbbbfdad74e295a408b6619c730f7b2bd5ae1e1c7a98596f8c4675e3ff"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153716353
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 303, 'threshold': 50, 'total_amount': 48029439, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 302, 'first_seen': 1760284979, 'matching_hash': '4e18e54a79e9d8ab'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}