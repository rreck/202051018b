```json
{
  "id": "241c7bcf005a9a2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290559,
  "host_pid": "9e6742732c60:1",
  "hash": "fdaf1f76da2a166434fcc5b057a3e4459c4f8110d59f7530e03d1fedc868e778",
  "cid": "QmV1fdaf1f76da2a166434fcc5b057a3e4459c4f8110",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290559,
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
      "evaluated_at": 1760290559
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
  "sig": "da27da9258f87f4125a2f3bb70cd2782996f2c99fc12332cd3e8a0555ae6102c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273742232
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 32256531, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285765, 'matching_hash': '98264f1e6b5ab805'}}}