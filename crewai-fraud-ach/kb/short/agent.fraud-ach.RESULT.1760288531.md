```json
{
  "id": "4dec4891595f1f7c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288531,
  "host_pid": "9e6742732c60:1",
  "hash": "868c519fb901235de4b7ff167d54005c7bb6878e08619ab026cb7bcb44f524f7",
  "cid": "QmV1868c519fb901235de4b7ff167d54005c7bb6878e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288531,
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
      "evaluated_at": 1760288531
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
  "sig": "ece8576a54c00721621871c64705b184ab826f1db7b0611a7d22255283a43374"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 039274533993332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 15644448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285765, 'matching_hash': 'a2ad50f9b8d4dabc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '039274537', 'validation_error': 'Invalid routing number checksum'}}}