```json
{
  "id": "67023aa00f0649d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293989,
  "host_pid": "9e6742732c60:1",
  "hash": "8d30050aead2d86a30aee7ee7fc346edbb385374b80ea50661847256495db0f0",
  "cid": "QmV18d30050aead2d86a30aee7ee7fc346edbb385374",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293989,
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
      "evaluated_at": 1760293989
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
  "sig": "7b8497aec005352609bb998268edff7160f66fe07257e973584791531d400f89"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271527804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 112608460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285764, 'matching_hash': '5c006846cf6d606a'}}}