```json
{
  "id": "777532ef85620975",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293773,
  "host_pid": "9e6742732c60:1",
  "hash": "bd1a8473c0a177706f29033c2425448e0188ae7c12bdf37bf6466ceefcad4292",
  "cid": "QmV1bd1a8473c0a177706f29033c2425448e0188ae7c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293773,
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
      "evaluated_at": 1760293773
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "791e2fe310963a0a6d270c3f1720462b5312a2e5855b3908a8fcdf060adf3656"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 818309298369568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 105999750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285765, 'matching_hash': '9e3984c977816ea5'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}