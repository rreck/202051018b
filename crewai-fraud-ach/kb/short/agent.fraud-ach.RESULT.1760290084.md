```json
{
  "id": "dfcdbd8f1b619eed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290084,
  "host_pid": "9e6742732c60:1",
  "hash": "503aac1fe9aaffdf7da20d01f3d858cefe95e3772d945cbe061e0a90b625ef36",
  "cid": "QmV1503aac1fe9aaffdf7da20d01f3d858cefe95e377",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290084,
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
      "evaluated_at": 1760290084
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
  "sig": "57ed911545cb65a589f662ff0049f9a8575f51b003159cad35c908179b1bf743"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248536916
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 20780439, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285764, 'matching_hash': '45170da297af1bde'}}}