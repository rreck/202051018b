```json
{
  "id": "c6dbb0e47c4d2780",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294167,
  "host_pid": "9e6742732c60:1",
  "hash": "1bb744d9150f8277fb0553f714d93304767060fa04e5454aa02dae9708308d0d",
  "cid": "QmV11bb744d9150f8277fb0553f714d93304767060fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294167,
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
      "evaluated_at": 1760294167
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
  "sig": "85cc3f1be1df1e35bbd5fdca172905bfc052c22b94701e66b87a9e4262940365"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 085520768954692
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 113149227, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '4f8cdcee5609bbf1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '085520764', 'validation_error': 'Invalid routing number checksum'}}}