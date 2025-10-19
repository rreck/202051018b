```json
{
  "id": "96e41a1cfbb97d88",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291982,
  "host_pid": "9e6742732c60:1",
  "hash": "d3198f478be6bc564cc740801dc7b397154e799b978f5928b2cf50dd4d04f0ea",
  "cid": "QmV1d3198f478be6bc564cc740801dc7b397154e799b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291982,
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
      "evaluated_at": 1760291982
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
  "sig": "c00ca5bc62cf1411d40a6ba367e9a4e71d0f81d928668920f35c643008d01b26"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150171825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 35150203, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285765, 'matching_hash': 'da3473f59eec3040'}}}