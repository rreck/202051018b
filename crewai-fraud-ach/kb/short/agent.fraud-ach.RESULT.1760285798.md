```json
{
  "id": "0356fce461051bba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285798,
  "host_pid": "9e6742732c60:1",
  "hash": "2b3b3b2ae422be08d1f5cf7388dab602867274e8521fd8c6085944d7e9d2cbb8",
  "cid": "QmV12b3b3b2ae422be08d1f5cf7388dab602867274e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285798,
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
      "evaluated_at": 1760285798
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
  "sig": "8db99f386294e161028ca7faab65f409f7495b19c460c62242bf28d2a0afcb47"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105151540950
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285763, 'matching_hash': '9c022c6e80e7fcd3'}}}