```json
{
  "id": "d282cf0d0ab95621",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287331,
  "host_pid": "9e6742732c60:1",
  "hash": "067830aabdc6b3874f50361f343bc12260deeddcaa4eeaf1d5e47171580014ee",
  "cid": "QmV1067830aabdc6b3874f50361f343bc12260deeddc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287331,
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
      "evaluated_at": 1760287331
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "d6b315f378ee7edcad824231aca275afc05a2285bd230710dab7b3f339feed3d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201464250877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 20886824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285765, 'matching_hash': '9a278d14d50dbff1'}}}