```json
{
  "id": "544bc2fe99fbc11e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294879,
  "host_pid": "9e6742732c60:1",
  "hash": "35493054f580ea4f808f1f6b1bb611ad2bf35fda42bbc435901ce21f14472afd",
  "cid": "QmV135493054f580ea4f808f1f6b1bb611ad2bf35fda",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294879,
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
      "evaluated_at": 1760294879
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
  "sig": "7c368f06a2a43a08d639218c323038f98479eaa78f0b7598c96f1e3b61392617"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244430877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 24600000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': 'c92664da58a26885'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '291093507', 'validation_error': 'Invalid routing number checksum'}}}