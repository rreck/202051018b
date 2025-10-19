```json
{
  "id": "e7f621161e028d71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291747,
  "host_pid": "9e6742732c60:1",
  "hash": "ce05bde94ce35c06b880ae5a056f9a94e841d26fa3cdc8d333ee5e3fc0e66936",
  "cid": "QmV1ce05bde94ce35c06b880ae5a056f9a94e841d26f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291747,
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
      "evaluated_at": 1760291747
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
  "sig": "0067161c839ac0c96fd350aa2e26026fe133c3d99434cb05afb90afe8c4f81ba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248887344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 10757838, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285764, 'matching_hash': '5acb0608ecf9576e'}}}