```json
{
  "id": "66fb0f083bddf6c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291672,
  "host_pid": "9e6742732c60:1",
  "hash": "4006f2802a22e44eac307513847bc5b76248edc48078ec3bbe3b31028282ded0",
  "cid": "QmV14006f2802a22e44eac307513847bc5b76248edc4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291672,
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
      "evaluated_at": 1760291672
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
  "sig": "a37fa0235441da0f014e8b75bcf671265a11f506d1ef9e412fd12671a0665e2c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 264316140004295
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 70052940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285765, 'matching_hash': 'f346c773c62e50ad'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '264316140', 'validation_error': 'Invalid routing number checksum'}}}