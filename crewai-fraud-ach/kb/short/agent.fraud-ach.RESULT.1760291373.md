```json
{
  "id": "4ddd261707560fca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291373,
  "host_pid": "9e6742732c60:1",
  "hash": "59d97b5e488e91dcd0eca8fa179243789b68aa89d5d00f019a2a37c0ac68cb8a",
  "cid": "QmV159d97b5e488e91dcd0eca8fa179243789b68aa89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291373,
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
      "evaluated_at": 1760291373
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
  "sig": "107326303d400b25547273b7804c3e446f57e43ce0031159bd8263fec0b342d1"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 264316140004295
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 67328659, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285765, 'matching_hash': 'f346c773c62e50ad'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '264316140', 'validation_error': 'Invalid routing number checksum'}}}