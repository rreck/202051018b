```json
{
  "id": "d9e397f6205e0ebb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294445,
  "host_pid": "9e6742732c60:1",
  "hash": "e1800f2bb271f4dadacc6a898803f6e412adb6390951e2d76afbda467b974565",
  "cid": "QmV1e1800f2bb271f4dadacc6a898803f6e412adb639",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294445,
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
      "evaluated_at": 1760294445
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
  "sig": "252256510c79fa9d200528269a0128f138af74e203cbd020a9fd38a8b6cb06a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027737863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 112021364, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285764, 'matching_hash': '0d7de9a99f2e5847'}}}