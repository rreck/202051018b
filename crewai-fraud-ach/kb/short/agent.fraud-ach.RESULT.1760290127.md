```json
{
  "id": "c4819bfa83c5e969",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290127,
  "host_pid": "9e6742732c60:1",
  "hash": "50a3f14cb06841aed220a33f1f2d2dd50c6aca95a9fccfb1e47d3cd2d17d7643",
  "cid": "QmV150a3f14cb06841aed220a33f1f2d2dd50c6aca95",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290127,
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
      "evaluated_at": 1760290127
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
  "sig": "eaaa0c2b6646454d410ee1a6fa968c65b99d3ae553a01266f002996e2b8ee5e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026466423
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 67056092, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285764, 'matching_hash': '1fcdc28f16166b10'}}}