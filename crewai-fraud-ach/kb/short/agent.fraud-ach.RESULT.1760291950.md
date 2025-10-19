```json
{
  "id": "01989d4a6d720866",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291950,
  "host_pid": "9e6742732c60:1",
  "hash": "12ba7936dc8f36f90a58f44141dfc1c84ec40645701f1e6208a19af694d61418",
  "cid": "QmV112ba7936dc8f36f90a58f44141dfc1c84ec40645",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291950,
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
      "evaluated_at": 1760291950
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
  "sig": "c7045d9c43c1aa2364c46c4ff1b8a18714df7eaa325ff853beeae8bd0c7f0a1d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248845664
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 43873379, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': 'd68dab2741390ae3'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}