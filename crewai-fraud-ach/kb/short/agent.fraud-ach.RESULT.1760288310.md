```json
{
  "id": "5baa1eed133b2a70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288310,
  "host_pid": "9e6742732c60:1",
  "hash": "73b0aa91b2a18bde8473df5f3d57a7d6af9d3af0ec368cbc058207b8006e5daa",
  "cid": "QmV173b0aa91b2a18bde8473df5f3d57a7d6af9d3af0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288310,
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
      "evaluated_at": 1760288310
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
  "sig": "5ded0e71a786d4c3d75c24a5f3fea6e3cc6269bb7951c8463efbd096a340ee56"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 009592678117470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 10779146, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285764, 'matching_hash': 'f5249213623024b2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '009592679', 'validation_error': 'Invalid routing number checksum'}}}