```json
{
  "id": "c5e97c0487fa1eaa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288870,
  "host_pid": "9e6742732c60:1",
  "hash": "7150da63e2dabbcd9255046942264c9a3aedd175f121e0e63d8d2697dff0e3cc",
  "cid": "QmV17150da63e2dabbcd9255046942264c9a3aedd175",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288870,
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
      "evaluated_at": 1760288870
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
  "sig": "1dca03e974a6a3b613e1e1c7e51f22c7ebb9fa9968d292c0215338fbfa7d3ca0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 33734288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}