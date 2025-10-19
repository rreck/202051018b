```json
{
  "id": "6e5e65319ee7ca6c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294394,
  "host_pid": "9e6742732c60:1",
  "hash": "4f7b4e0875c28b1208f0e9e73544e8db11232d6a330c271928bd4a610626c775",
  "cid": "QmV14f7b4e0875c28b1208f0e9e73544e8db11232d6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294394,
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
      "evaluated_at": 1760294394
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
  "sig": "6d0f952246a48ff206b3c50db07f1c870bb34859716e33ea73ae09bb8ffa180a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029233033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 98410458, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': 'f6bf3c76ea3935d9'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '834096558', 'validation_error': 'Invalid routing number checksum'}}}