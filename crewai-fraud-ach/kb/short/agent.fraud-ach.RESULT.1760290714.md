```json
{
  "id": "25dea067149d5ac0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290714,
  "host_pid": "9e6742732c60:1",
  "hash": "525de029633a50a7d2c9513dbf9763941961d2227e78eb675a34168aff70e01a",
  "cid": "QmV1525de029633a50a7d2c9513dbf9763941961d222",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290714,
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
      "evaluated_at": 1760290714
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
  "sig": "9222b6ec845dedce3d4798f4aa2d5ec8d7872efb96be8aab8303835c78d79b3c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462505262
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 61470838, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285764, 'matching_hash': 'e15f6eb56271d036'}}}