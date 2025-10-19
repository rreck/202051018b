```json
{
  "id": "1cc57932715cf372",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291239,
  "host_pid": "9e6742732c60:1",
  "hash": "1ae32c1aa270455d3d86f7044337a277dd69dbfcb635e25cecf9560564b428d1",
  "cid": "QmV11ae32c1aa270455d3d86f7044337a277dd69dbfc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291239,
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
      "evaluated_at": 1760291239
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
  "sig": "a82493d53bc71a423277005a81c9046b8038177ccfa23ef500cc22e72a074208"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595235556
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 29676220, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285765, 'matching_hash': 'e45b9dbcffb11ba0'}}}