```json
{
  "id": "bd459a78d4e9ad24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287667,
  "host_pid": "9e6742732c60:1",
  "hash": "1d1ba662bfec34d70a5d399ed25cdcaa041377a7393b04a99486655c470e4de7",
  "cid": "QmV11d1ba662bfec34d70a5d399ed25cdcaa041377a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287667,
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
      "evaluated_at": 1760287667
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
  "sig": "1c80f37fe811de48d3d4245ce0f6713bff1029551de538bca829d1a4c5659611"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000021748494
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285765, 'matching_hash': '2adbcd1f80c0d3e0'}}}