```json
{
  "id": "1e12f6430c17adff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287790,
  "host_pid": "9e6742732c60:1",
  "hash": "15316ea9a902efe6ffac94a2ced514e4bf9e81d3b38dd08d167d6751eea568ab",
  "cid": "QmV115316ea9a902efe6ffac94a2ced514e4bf9e81d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287790,
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
      "evaluated_at": 1760287790
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
  "sig": "f057831bfca2704e8a9fea2efa6d1d7f6fd2fa4bf1bce4bfcc09876a175311e2"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 044000035733360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 23635152, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285765, 'matching_hash': '19d9911872be19af'}}}