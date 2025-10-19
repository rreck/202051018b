```json
{
  "id": "6a4ecc08c31ccf21",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288900,
  "host_pid": "9e6742732c60:1",
  "hash": "6d763ce4d8f813e7017f266f9102b8525ed2a8a07571a8b2bbd1810124c5b9f2",
  "cid": "QmV16d763ce4d8f813e7017f266f9102b8525ed2a8a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288900,
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
      "evaluated_at": 1760288900
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
  "sig": "0403684938e20f3b85a6191be45aaee4951b5af8a5e0060fa559391bda5b95f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597421131
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 24969627, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285765, 'matching_hash': 'ee859bd02c19b1f0'}}}