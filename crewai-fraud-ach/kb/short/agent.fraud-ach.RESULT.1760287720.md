```json
{
  "id": "67e8b8691491e360",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287720,
  "host_pid": "9e6742732c60:1",
  "hash": "cf140177933d47006bf06f79fe3d29c7712067b2e484baff6fbb05c4b160f24c",
  "cid": "QmV1cf140177933d47006bf06f79fe3d29c7712067b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287720,
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
      "evaluated_at": 1760287720
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
  "sig": "441a16b6e7b3b1b20d8b1ad148cbe43f5511dde7d1df7682c2b92eb5184c1f06"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 111000026472141
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 14420840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285764, 'matching_hash': 'c34da1cfbf75ff05'}}}