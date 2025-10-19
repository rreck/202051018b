```json
{
  "id": "9c3740b8df3cbfa8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293534,
  "host_pid": "9e6742732c60:1",
  "hash": "d146b66e603217929bd9c2dabf76f2f9c6e1137d7178fd21e84bb7adbfc6c675",
  "cid": "QmV1d146b66e603217929bd9c2dabf76f2f9c6e1137d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293534,
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
      "evaluated_at": 1760293534
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
  "sig": "60d4ef524cefb251c0621f931cfa4c8fa4445fe729ac2fb7373fbad12f128fdd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025883497
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 69960880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285765, 'matching_hash': '8c29ee71720a2634'}}}