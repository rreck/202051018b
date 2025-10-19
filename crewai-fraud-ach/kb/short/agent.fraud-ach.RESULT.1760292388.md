```json
{
  "id": "1af03fd3c848068c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292388,
  "host_pid": "9e6742732c60:1",
  "hash": "2d4382fc700b814ffb817f9d9b425ca9c1bc0df00c0476a0d12793ee64517ebe",
  "cid": "QmV12d4382fc700b814ffb817f9d9b425ca9c1bc0df0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292388,
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
      "evaluated_at": 1760292388
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
  "sig": "240db7abd9ae0e1bfc99fb7e77d227cbb6fb6b6ac3a15e5a2160c85bcfb39a7c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242521033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 13039684, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285765, 'matching_hash': 'cfb80109aa92585a'}}}