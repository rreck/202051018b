```json
{
  "id": "37b1689c03bafa7b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293520,
  "host_pid": "9e6742732c60:1",
  "hash": "b25d28f205d0b9fb568ff2c3e87bd545ae9de949a1a35af5b9e0292dd7bfcb45",
  "cid": "QmV1b25d28f205d0b9fb568ff2c3e87bd545ae9de949",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293520,
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
      "evaluated_at": 1760293520
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
  "sig": "a117435edf6aa226e308388b03b44b873f7bbb05729436eb16ba28b3bd58ddb8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039436848
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 99226380, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '703cb1be49d2cf8f'}}}