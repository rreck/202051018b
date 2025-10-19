```json
{
  "id": "3a1ad50a5bb0d54c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290043,
  "host_pid": "9e6742732c60:1",
  "hash": "f0f21df68bb733f554733b1569ed3e554a832e6ff2e9cb55162caa69c90259ee",
  "cid": "QmV1f0f21df68bb733f554733b1569ed3e554a832e6f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290043,
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
      "evaluated_at": 1760290043
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
  "sig": "783c04ffda0fdd92ff3257612f564371546491e78bb6927b7f3de25ca38f149c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 182683956982385
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 20950580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285764, 'matching_hash': '0eeac2a2909779e4'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '182683957', 'validation_error': 'Invalid routing number checksum'}}}