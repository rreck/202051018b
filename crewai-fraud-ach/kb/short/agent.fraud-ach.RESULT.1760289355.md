```json
{
  "id": "a9e9ae939f415d09",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289355,
  "host_pid": "9e6742732c60:1",
  "hash": "bd58e89c2e023c5a73ad3a1d4d80ccc8d5c3cf588004d4f7acd57fd127649019",
  "cid": "QmV1bd58e89c2e023c5a73ad3a1d4d80ccc8d5c3cf58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289355,
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
      "evaluated_at": 1760289355
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
  "sig": "99c66a5ce4e7c353e88a99dffeffb94e639c8cb47fdad6f59012be7940af6595"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 864091464204372
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 28630899, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285763, 'matching_hash': '74f25dd839f89a8f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '864091464', 'validation_error': 'Invalid routing number checksum'}}}