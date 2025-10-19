```json
{
  "id": "406a05e50217e85f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291483,
  "host_pid": "9e6742732c60:1",
  "hash": "1bb8b81b0f148e8582897fc14f4803b34aea0bc666fa19a5570ddbced6060ccf",
  "cid": "QmV11bb8b81b0f148e8582897fc14f4803b34aea0bc6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291483,
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
      "evaluated_at": 1760291484
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
  "sig": "6cdc9d8193791e08d9c3da5277fd2900cfd23e60bcba1f0a47269135522cc9db"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151550703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 67346400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285764, 'matching_hash': '1af10bcd1b5a60d5'}}}