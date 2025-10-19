```json
{
  "id": "ef607435b443aa19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294391,
  "host_pid": "9e6742732c60:1",
  "hash": "be1c3bb1c43741d95a586b2eafbfb91416c1ee768f613cd862830b718a930c54",
  "cid": "QmV1be1c3bb1c43741d95a586b2eafbfb91416c1ee76",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294391,
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
      "evaluated_at": 1760294391
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
  "sig": "695ed8570e79bf9f1a08f521519a5d0f72a29800d823268bc9af1ceaa8e3c5c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277234112
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 89350896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285765, 'matching_hash': '11106d4d9e5d055e'}}}}