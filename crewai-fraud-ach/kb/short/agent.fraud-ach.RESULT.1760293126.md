```json
{
  "id": "8dc8c3e02e1afc56",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293126,
  "host_pid": "9e6742732c60:1",
  "hash": "8f4529e1f78f11e878252de6311e443b326c855b90fb38d3e08ebf52b888b2d0",
  "cid": "QmV18f4529e1f78f11e878252de6311e443b326c855b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293126,
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
      "evaluated_at": 1760293126
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
  "sig": "ba1dcb432ffc1d1d514b730dae65adb992d812405ba2f487c7f9caad6d12ba49"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592967123
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 37369664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': 'c09be009c43e6bc8'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '728187403', 'validation_error': 'Invalid routing number checksum'}}}