```json
{
  "id": "03f6344c86550abb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293119,
  "host_pid": "9e6742732c60:1",
  "hash": "8987bd0ff3637f87dfcd3831798659037c480e3d8c782f80ee588990fc9551cb",
  "cid": "QmV18987bd0ff3637f87dfcd3831798659037c480e3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293119,
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
      "evaluated_at": 1760293119
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
  "sig": "dff4dc98c915175d3a45fc1da6506545fc5538cb49e7aa4de6ee16a6ef83b145"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026691588
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 85789404, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '1da0382cf03ec7d2'}}}