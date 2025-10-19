```json
{
  "id": "350140776f1a1048",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292085,
  "host_pid": "9e6742732c60:1",
  "hash": "45ebe2243cb28b4110b2fea80401237dc089e3c0dc22a66b008db0f25a85dc6c",
  "cid": "QmV145ebe2243cb28b4110b2fea80401237dc089e3c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292085,
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
      "evaluated_at": 1760292085
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
  "sig": "4bc4279f7dd3555d5d030b0a5d2137144a76bcb4848150903fede78979120b08"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025810032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 93054210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': '4a1b4df87be22a11'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '568426909', 'validation_error': 'Invalid routing number checksum'}}}