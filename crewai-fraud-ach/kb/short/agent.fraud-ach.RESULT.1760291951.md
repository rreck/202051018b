```json
{
  "id": "5e4f1b5a5b18779e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291951,
  "host_pid": "9e6742732c60:1",
  "hash": "bcc73a1fd7210572528d3f8c387bc80db886e092c0951de16e6d5d6ff82f2abc",
  "cid": "QmV1bcc73a1fd7210572528d3f8c387bc80db886e092",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291951,
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
      "evaluated_at": 1760291951
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
  "sig": "b2613ac03eb6020520ce7b70a74d2294df5eba51650f14b9cccb2ac7173f0acf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271879965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 39662513, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '9c4837aa9a8e4a4a'}}}