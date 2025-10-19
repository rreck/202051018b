```json
{
  "id": "3d3bab22f9d9047e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291388,
  "host_pid": "9e6742732c60:1",
  "hash": "877042aa064fd17b6c894f1742c5aa4c974d5027db2ee9d95b9efe68eb32a896",
  "cid": "QmV1877042aa064fd17b6c894f1742c5aa4c974d5027",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291388,
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
      "evaluated_at": 1760291389
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
  "sig": "2da9bc2d63d29d6c59856be257887ef65695b01017ef204e12efa0a21d11a12a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595856880
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 54408582, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': '3e252270c9e333bc'}}}