```json
{
  "id": "8f31c0111a87c00c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288314,
  "host_pid": "9e6742732c60:1",
  "hash": "1c31262fff59fb2c037d8138170b88b3f4b80396371d9036dafc5b7050a10ee7",
  "cid": "QmV11c31262fff59fb2c037d8138170b88b3f4b80396",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288314,
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
      "evaluated_at": 1760288314
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
  "sig": "adcec390af21ee13a46110bf84746b184c0727d571b459621ffcfb464723b374"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028263855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 22250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285765, 'matching_hash': 'de539bef65b21552'}}}