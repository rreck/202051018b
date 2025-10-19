```json
{
  "id": "4903c386f4f93c34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291842,
  "host_pid": "9e6742732c60:1",
  "hash": "e7674c74a7373dabb3c1c5aa8ec4eea421db6f93fcf5c1519ad63ce79d5892fe",
  "cid": "QmV1e7674c74a7373dabb3c1c5aa8ec4eea421db6f93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291842,
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
      "evaluated_at": 1760291842
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
  "sig": "3588c31e4c36c88a0d25e41409adb0fed8ab8d70e614c2f276288805fababe31"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 54608440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}