```json
{
  "id": "b12350f721e6e135",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293229,
  "host_pid": "9e6742732c60:1",
  "hash": "f69173b577afcc5ea534d78374c39b7460603ff70ea254ac93d762a7cd438217",
  "cid": "QmV1f69173b577afcc5ea534d78374c39b7460603ff7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293229,
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
      "evaluated_at": 1760293229
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
  "sig": "ddee5e34472900ded7e3dbd26c2e48e8ff959f8e5f895291c00db3ec26f1f624"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151773289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 105258468, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '7b1e6accdb666d6e'}}}