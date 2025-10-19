```json
{
  "id": "be658c4615781f7b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291284,
  "host_pid": "9e6742732c60:1",
  "hash": "febbddb66e5a6745ef137631c506fdafa0b967dfaf95e3607e04dc9dccd2bbce",
  "cid": "QmV1febbddb66e5a6745ef137631c506fdafa0b967df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291284,
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
      "evaluated_at": 1760291284
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
  "sig": "9d55309d8e12fcc252c8c13ec5f734b76793404fdaa5d85e07e94bc913190a6f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467134805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 46519695, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': 'bc3c56d4b0e7489d'}}}