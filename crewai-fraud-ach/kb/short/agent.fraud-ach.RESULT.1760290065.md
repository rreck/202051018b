```json
{
  "id": "45a6623739711189",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290065,
  "host_pid": "9e6742732c60:1",
  "hash": "6df955149d9df357c9d8de7166058769b011f92808ecf59821c91270f00ea02d",
  "cid": "QmV16df955149d9df357c9d8de7166058769b011f928",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290065,
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
      "evaluated_at": 1760290065
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
  "sig": "d97207a717005d5bab1b3f63f10ff6976d70689dde58dbf9cab9d001c22e0f2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 44554720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}