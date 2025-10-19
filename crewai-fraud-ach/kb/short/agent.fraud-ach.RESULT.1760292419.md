```json
{
  "id": "f55a8010683af76c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292419,
  "host_pid": "9e6742732c60:1",
  "hash": "5257c171f87257cf4bd79d0688784414f694684f86089a9ff5f51dc010590614",
  "cid": "QmV15257c171f87257cf4bd79d0688784414f694684f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292419,
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
      "evaluated_at": 1760292419
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
  "sig": "4b7cc039f4d11ebdfe1e545c7ad025fd57bb3337ebae35e08d172e2b772c81a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274458495
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 89873173, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285764, 'matching_hash': '191d9163e8e6657e'}}}