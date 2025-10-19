```json
{
  "id": "c820d8da1a4cdcb7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294190,
  "host_pid": "9e6742732c60:1",
  "hash": "fed5fbbce09daccfd18fcc0b9e013e8c26d81fd893d1dcc3dd334d2fa017bfb6",
  "cid": "QmV1fed5fbbce09daccfd18fcc0b9e013e8c26d81fd8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294190,
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
      "evaluated_at": 1760294190
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
  "sig": "86e02486e73b1802c7c3719344686efbfbb4dc441fafcfb1cb17ad03095b46cc"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 906924177607497
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 60111903, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285765, 'matching_hash': 'a0bedab775ea6194'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '906924178', 'validation_error': 'Invalid routing number checksum'}}}