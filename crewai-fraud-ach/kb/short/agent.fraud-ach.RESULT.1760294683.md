```json
{
  "id": "aba69f901b9fde71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294683,
  "host_pid": "9e6742732c60:1",
  "hash": "7137b3f6d36e9a48accc2563f0473df2263908b29495c9be60fa8e33162927dd",
  "cid": "QmV17137b3f6d36e9a48accc2563f0473df2263908b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294683,
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
      "evaluated_at": 1760294683
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
  "sig": "689c12eb29f2eb926ad57394a19788796b6836d2765697032a7cb4e31186f37f"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 649338001689495
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 80574384, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285765, 'matching_hash': '47ca0a67ca137c75'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '649338005', 'validation_error': 'Invalid routing number checksum'}}}