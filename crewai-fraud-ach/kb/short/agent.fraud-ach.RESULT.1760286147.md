```json
{
  "id": "4d321ee288998eda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286147,
  "host_pid": "9e6742732c60:1",
  "hash": "c429f25ebf457f56cfcd88db658c2b446251474cc7edc5e73431f514db0d293f",
  "cid": "QmV1c429f25ebf457f56cfcd88db658c2b446251474c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286147,
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
      "evaluated_at": 1760286147
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
  "sig": "f15b61b1584a0c140e91e5a810fc89a4863a816df4dd6f945de1ad92d3594a17"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000020009015
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285763, 'matching_hash': 'f404409c8af40265'}}}