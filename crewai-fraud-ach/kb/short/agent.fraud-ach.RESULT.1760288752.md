```json
{
  "id": "519acfe01825099e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288752,
  "host_pid": "9e6742732c60:1",
  "hash": "9e75b5b876efdd308c62499f4e4247932407d72d7c5fe86440d4a22201b8294f",
  "cid": "QmV19e75b5b876efdd308c62499f4e4247932407d72d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288752,
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
      "evaluated_at": 1760288752
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
  "sig": "74fcbc45d5918fbb2810faeab49d1a6c2a405fd5d6400e7b5507bab745f992c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598152937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 25750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285763, 'matching_hash': '12ca21f72ace6b8c'}}}