```json
{
  "id": "9f2259f116d5bd6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289408,
  "host_pid": "9e6742732c60:1",
  "hash": "e85feba85d40b91a4ff604c2aff44c22ecc282ed32677a31fbc9afc02bbae79e",
  "cid": "QmV1e85feba85d40b91a4ff604c2aff44c22ecc282ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289408,
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
      "evaluated_at": 1760289408
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
  "sig": "3fb1c5ed7b999e4c51ba82d8c315c1d4f8f899074294c7938ed87485a78567c9"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 264316140004295
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 47480326, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285765, 'matching_hash': 'f346c773c62e50ad'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '264316140', 'validation_error': 'Invalid routing number checksum'}}}