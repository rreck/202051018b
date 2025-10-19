```json
{
  "id": "9aae17e37377951a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292192,
  "host_pid": "9e6742732c60:1",
  "hash": "3d34dde1675717032430978dd64b4a3626761c561e84cf3c1df7d47423ef4207",
  "cid": "QmV13d34dde1675717032430978dd64b4a3626761c56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292192,
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
      "evaluated_at": 1760292192
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
  "sig": "e7ee4b95c87a4b4c3d49ca486f6ad641c5cce3632a3f74ab884461faa13c0915"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274458495
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 87592128, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285764, 'matching_hash': '191d9163e8e6657e'}}}