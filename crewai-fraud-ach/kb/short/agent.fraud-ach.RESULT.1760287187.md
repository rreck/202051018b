```json
{
  "id": "cdc037a1c3849e37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287187,
  "host_pid": "9e6742732c60:1",
  "hash": "0de69ee05272fc375d9fe36ccbf5ae3331314fddc67cee48dfb2cf8fa9ac84f7",
  "cid": "QmV10de69ee05272fc375d9fe36ccbf5ae3331314fdd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287187,
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
      "evaluated_at": 1760287187
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
  "sig": "3241c03532534ba28118045e6b3f727dad82e47368f1b61937331275d1b740da"
}
```

Fraud detected: duplicate_transaction (score: 68)
Transaction: 111000021748494
Details: {'velocity': {'fraud_detected': True, 'risk_score': 52, 'details': {'transaction_count': 51, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285765, 'matching_hash': '2adbcd1f80c0d3e0'}}}een': 1760285763, 'matching_hash': 'bc3c56d4b0e7489d'}}}