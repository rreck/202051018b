```json
{
  "id": "075e6fb66ccb144d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291843,
  "host_pid": "9e6742732c60:1",
  "hash": "100bb88a479e77bc0cc40a6d81097005155eeaaa7439dfb4c8256ecbb0a61ba7",
  "cid": "QmV1100bb88a479e77bc0cc40a6d81097005155eeaaa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291843,
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
      "evaluated_at": 1760291843
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
  "sig": "6614eb027104dc9e0fd0caac7cc285f14845cf8a6d96ec783af229fac80a34c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468284841
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 34463752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285764, 'matching_hash': 'af26bab6e9f38d2a'}}}