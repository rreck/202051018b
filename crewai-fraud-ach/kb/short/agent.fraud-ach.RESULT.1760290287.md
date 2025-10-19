```json
{
  "id": "7376a76dd697aafb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290287,
  "host_pid": "9e6742732c60:1",
  "hash": "897138a4d3b0645c2d82da22cb072854d86ef80fb762f4c84c9437f957c47c16",
  "cid": "QmV1897138a4d3b0645c2d82da22cb072854d86ef80f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290287,
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
      "evaluated_at": 1760290287
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
  "sig": "317117ebf0d623de4a4dc440faaeb33a2ad3f09a0654fb2d6abb6536df7cbf18"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464250877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 54454934, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285765, 'matching_hash': '9a278d14d50dbff1'}}}