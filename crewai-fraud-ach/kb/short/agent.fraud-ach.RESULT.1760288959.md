```json
{
  "id": "0f4d1b98dbd131fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288959,
  "host_pid": "9e6742732c60:1",
  "hash": "93ea27e7d96d059de5d1b5898627858d012f0c3aac9867dd1f9ba1d4471ca9ae",
  "cid": "QmV193ea27e7d96d059de5d1b5898627858d012f0c3a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288959,
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
      "evaluated_at": 1760288959
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
  "sig": "87f7f9c707b4e94138b4ea9700c43522e02182c1e6fd1b6a8f5ab65d753e03ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038959082
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285765, 'matching_hash': '98ae9ae4174799d3'}}}een': 1760285763, 'matching_hash': '17d6d8b38d025182'}}}