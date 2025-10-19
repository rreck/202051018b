```json
{
  "id": "e3f3f67b6040a8dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291070,
  "host_pid": "9e6742732c60:1",
  "hash": "373592e74e883e885597e6f6c6c227e21e81392112ae8aa3e26f86d9bf48f6dd",
  "cid": "QmV1373592e74e883e885597e6f6c6c227e21e813921",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291070,
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
      "evaluated_at": 1760291070
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
  "sig": "0c0341a3b2c5608359e052cbaf03164c508467e992c0d7cab49e79c31037a619"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598219019
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 18957698, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285765, 'matching_hash': '253a69ee76b5426a'}}}