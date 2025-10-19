```json
{
  "id": "5cc68cc101815de4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286727,
  "host_pid": "9e6742732c60:1",
  "hash": "503d5336aafaed692a31aa9ff199d56379214fee7caf9a7dca79dbf34993d880",
  "cid": "QmV1503d5336aafaed692a31aa9ff199d56379214fee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286727,
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
      "evaluated_at": 1760286727
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
  "sig": "2034e15832f278779442affc853aca78438a7bdfedbd240e5841eb5517e9439b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027783214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 53855091, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760284979, 'matching_hash': '00d004b11e9e3015'}}}