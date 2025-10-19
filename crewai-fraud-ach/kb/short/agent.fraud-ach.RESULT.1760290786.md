```json
{
  "id": "91c13d95c278f8f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290786,
  "host_pid": "9e6742732c60:1",
  "hash": "e15146ccec81ba680f6c4a9dd685c313386de2b64bf36208861a61fe6a4c3d8d",
  "cid": "QmV1e15146ccec81ba680f6c4a9dd685c313386de2b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290786,
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
      "evaluated_at": 1760290786
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
  "sig": "606fb5e7561340ffd15477f3c4f71412af2101e9225337edcf91dd05ba24e2c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039343574
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 22588653, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285765, 'matching_hash': '13f5b4dcf27391fd'}}}}