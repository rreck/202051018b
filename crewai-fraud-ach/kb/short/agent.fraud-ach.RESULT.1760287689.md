```json
{
  "id": "bd47de84a71b6770",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287689,
  "host_pid": "9e6742732c60:1",
  "hash": "217edd1e1f2300e299a6ad3b463a3387361447943c330de1e9b36ec9e2e455e6",
  "cid": "QmV1217edd1e1f2300e299a6ad3b463a338736144794",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287689,
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
      "evaluated_at": 1760287689
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
  "sig": "619d52bd52caf7b127c3539573faecc9ab6e6e4d95a0c56d1510e2241859622e"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 031201466524554
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 26387808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285763, 'matching_hash': 'c9a1c21cbf3363ae'}}}: {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8052182}}}