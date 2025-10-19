```json
{
  "id": "154e5617c2e974e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292088,
  "host_pid": "9e6742732c60:1",
  "hash": "613cc692c44b4e9be3cc4602332921973422d4ea366b76350d1c0822db055579",
  "cid": "QmV1613cc692c44b4e9be3cc4602332921973422d4ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292088,
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
      "evaluated_at": 1760292088
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
  "sig": "a24e317aaee1d9a4823961b5dedd122be3efc55e9a1bd5c72d1b2fd2297f5db1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027419247
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 89265990, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': 'f49fdb64c00c5aec'}}}