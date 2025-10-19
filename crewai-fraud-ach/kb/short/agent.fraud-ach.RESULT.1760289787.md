```json
{
  "id": "9a77fdaf67cf405c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289787,
  "host_pid": "9e6742732c60:1",
  "hash": "3d52225ad24504a89c02eea2a9668340e943ede440fe37791809aec9fa9ff850",
  "cid": "QmV13d52225ad24504a89c02eea2a9668340e943ede4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289787,
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
      "evaluated_at": 1760289787
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
  "sig": "1fce3dcdf813f1e22b6f4bc48a9da54167b843d9925a3c0fcd20222b09404003"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241012804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 36727950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': 'ba9ba43773b08e05'}}}