```json
{
  "id": "f39df676e77edbdf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292508,
  "host_pid": "9e6742732c60:1",
  "hash": "75aa14300e2bd3a9dd8dfd3a0b62a693e10ce4238451dc2f236bd85172e8fd97",
  "cid": "QmV175aa14300e2bd3a9dd8dfd3a0b62a693e10ce423",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292508,
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
      "evaluated_at": 1760292508
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
  "sig": "bf1c798a1be8f5edfbad7da874b0bb57fe843bb46b1458dade0365411c4485b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277305476
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 81202945, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': 'e8a0d4fc67d0b61c'}}}