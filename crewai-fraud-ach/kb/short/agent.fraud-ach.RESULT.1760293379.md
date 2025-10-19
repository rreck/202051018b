```json
{
  "id": "3a3e958480d38933",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293379,
  "host_pid": "9e6742732c60:1",
  "hash": "0e88fc9737f12ede762fc4da2cb6d5eeec48bca718351fb1cb743e79e4dd6c52",
  "cid": "QmV10e88fc9737f12ede762fc4da2cb6d5eeec48bca7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293379,
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
      "evaluated_at": 1760293379
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
  "sig": "7d1b608c0e9c7631e2e9d1bf4d35a91cf9cb5e69f7824e6fb12c2f8581d4b48d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272952668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 38417463, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': 'e2aecc84b992b480'}}}