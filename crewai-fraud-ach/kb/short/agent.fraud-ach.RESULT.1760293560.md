```json
{
  "id": "5622293c7ebd161e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293560,
  "host_pid": "9e6742732c60:1",
  "hash": "d862dcdeabb5ccae27d0eb910457ee513298166a51dfb5f6c102feff86228abe",
  "cid": "QmV1d862dcdeabb5ccae27d0eb910457ee513298166a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293560,
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
      "evaluated_at": 1760293560
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
  "sig": "f5a2e141981256f1ccbde7e4b2c2b6c8c0d10769f52189768e86053fb3c74ee6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021151885
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 54118701, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285764, 'matching_hash': '925ef0ca9f93e495'}}}