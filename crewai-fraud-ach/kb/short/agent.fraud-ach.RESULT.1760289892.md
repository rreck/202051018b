```json
{
  "id": "79a36201a9f0dc89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289892,
  "host_pid": "9e6742732c60:1",
  "hash": "9c52d9fc092574c143666f790a69548e678d67c8bc455ca423a92636262887bc",
  "cid": "QmV19c52d9fc092574c143666f790a69548e678d67c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289892,
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
      "evaluated_at": 1760289892
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
  "sig": "e06168e1f5b9d6662dc2dd101d49b90c3fcece92f5121ecb152526c900988f52"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244516225
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 19941000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': '305c81c4ba1c9c62'}}}