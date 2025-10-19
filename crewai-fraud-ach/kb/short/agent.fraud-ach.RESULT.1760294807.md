```json
{
  "id": "997e490c1d6bdc58",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294807,
  "host_pid": "9e6742732c60:1",
  "hash": "92ef1b3a6755a00fcf125fbbf59b185b0752dd0947b584ea2bde0ac63a662153",
  "cid": "QmV192ef1b3a6755a00fcf125fbbf59b185b0752dd09",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294807,
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
      "evaluated_at": 1760294807
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
  "sig": "020820ae2a7eafacc3a1ec20a337f9f2778b489ca8717f071c10c80c281152d7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029518652
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 18632250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': 'e772ab4f6c2a0903'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '730896563', 'validation_error': 'Invalid routing number checksum'}}}