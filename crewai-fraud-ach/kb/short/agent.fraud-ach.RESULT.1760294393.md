```json
{
  "id": "54357847e3215913",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294393,
  "host_pid": "9e6742732c60:1",
  "hash": "0b5cfbd5d6ea2eca8ab83e534df9e084ddceab42bfd912b888b87c9b4cd0a050",
  "cid": "QmV10b5cfbd5d6ea2eca8ab83e534df9e084ddceab42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294393,
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
      "evaluated_at": 1760294393
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
  "sig": "8d69a3cfd67ead8759b4af706862224304fa86e093a018fcd52e0e46ab5965ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022887585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 83174913, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '812b0d5784c9619b'}}}